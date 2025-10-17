class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.price = None
        self.currency = "EUR"  # Default to EUR for European flights
        self.origin_city = None
        self.origin_airport = None
        self.destination_city = None
        self.destination_airport = None
        self.out_date = None
        self.return_date = None
        self.stop_overs = 0
        self.via_city = None
        
    def find_cheapest_flight(self, flight_data):
        """Extract and structure flight data from the API response"""
        if not flight_data or "data" not in flight_data or not flight_data["data"]:
            print("No flight data available")
            return None
            
        try:
            cheapest_flight = flight_data["data"][0]
            
            # Basic flight information - handle Amadeus price format
            price_info = cheapest_flight.get("price")
            if isinstance(price_info, dict):
                # Amadeus returns price as {"currency": "EUR", "total": "200.84", ...}
                self.price = float(price_info.get("total", 0))
                self.currency = price_info.get("currency", "EUR")  # Keep EUR as default
            else:
                # Simple price format
                self.price = float(price_info) if price_info else 0
                self.currency = "EUR"  # Default to EUR for European flights
            
            # Handle different API formats - Amadeus vs others
            if "itineraries" in cheapest_flight:
                # Amadeus API format
                itinerary = cheapest_flight["itineraries"][0]
                segments = itinerary["segments"]
                
                if segments:
                    first_segment = segments[0]
                    last_segment = segments[-1]
                    
                    # Origin and destination info
                    self.origin_airport = first_segment["departure"]["iataCode"]
                    self.destination_airport = last_segment["arrival"]["iataCode"]
                    
                    # Dates
                    self.out_date = first_segment["departure"]["at"].split("T")[0]
                    
                    # Check for return flight (round trip)
                    if len(cheapest_flight["itineraries"]) > 1:
                        return_itinerary = cheapest_flight["itineraries"][1]
                        return_segments = return_itinerary["segments"]
                        if return_segments:
                            self.return_date = return_segments[0]["departure"]["at"].split("T")[0]
                    
                    # Calculate stopovers
                    self.stop_overs = len(segments) - 1
                    if self.stop_overs > 0:
                        self.via_city = segments[1]["arrival"]["iataCode"] if len(segments) > 1 else None
                        
            elif "route" in cheapest_flight:
                # Tequila/Kiwi API format (legacy)
                first_segment = cheapest_flight["route"][0]
                
                self.origin_city = first_segment.get("cityFrom")
                self.origin_airport = first_segment.get("flyFrom")
                self.destination_city = first_segment.get("cityTo")
                self.destination_airport = first_segment.get("flyTo")
                
                # Extract departure date
                if "local_departure" in first_segment:
                    self.out_date = first_segment["local_departure"].split("T")[0]
                
                # Handle return date - only if it's a round trip
                if len(cheapest_flight["route"]) > 1:
                    return_segment = cheapest_flight["route"][-1]  # Last segment for return
                    if "local_departure" in return_segment:
                        self.return_date = return_segment["local_departure"].split("T")[0]
                
                # Calculate stopovers and via cities
                route_length = len(cheapest_flight["route"])
                if route_length > 2:  # More than 2 segments means stopovers
                    self.stop_overs = route_length - 2
                    # Via city is the destination of the first segment (where you stopover)
                    if route_length > 1:
                        via_segment = cheapest_flight["route"][1]
                        self.via_city = via_segment.get("cityFrom")
                elif route_length == 2:
                    # Direct round trip, no stopovers
                    self.stop_overs = 0
                else:
                    # One way direct flight
                    self.stop_overs = 0
            
            return self
            
        except (KeyError, IndexError, TypeError) as e:
            print(f"Error parsing flight data: {e}")
            return None
    
    def __str__(self):
        """String representation of the flight data"""
        stopover_text = f" with {self.stop_overs} stopover(s)" if self.stop_overs > 0 else ""
        via_text = f" via {self.via_city}" if self.via_city else ""
        return_text = f" returning {self.return_date}" if self.return_date else ""
        
        return (f"Flight from {self.origin_airport} "
                f"to {self.destination_airport}: "
                f"{self.price:.2f} {self.currency}, departing {self.out_date}{return_text}"
                f"{stopover_text}{via_text}")
    
    