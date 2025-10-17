# Flight Deal Finder with Google Form

This application finds flight deals from a specified origin to various destinations, checking if there are direct or indirect flights available at prices below a set threshold. When a good deal is found, it sends notifications via SMS, WhatsApp, and personalized emails to users registered through a Google Form.

## Setup Instructions

1. **Create a .env file**:
   - Make a copy of `.env.example` and name it `.env`
   - Fill in your API credentials and other configuration values

2. **Required APIs**:
   - [Sheety](https://sheety.co/): Used to access and update Google Sheets data
   - [Amadeus](https://developers.amadeus.com/): Used for flight search
   - [Twilio](https://www.twilio.com/): Used for sending SMS or WhatsApp notifications

3. **Google Sheet Setup**:
   - Create a Google Sheet with two sheets:
     
     **Prices Sheet** with columns:
     - City
     - IATA Code (will be filled automatically)
     - Lowest Price (your price threshold)
     - id
     
     **Users Sheet** with columns (filled by Google Form responses):
     - firstName
     - lastName
     - email
     - id
     
4. **Google Form Setup**:
   - Create a Google Form to collect user information
   - Include fields for firstName, lastName, and email
   - Connect the form to your Google Sheet's Users tab

5. **Connect Google Sheet to Sheety**:
   - Follow Sheety instructions to connect your Google Sheet
   - Get your API endpoints and add them to `.env` as:
     - `SHEETY_PRICES_ENDPOINT` for the prices sheet
     - `SHEETY_USERS_ENDPOINT` for the users sheet

6. **Email Setup**:
   - Add your email credentials to `.env`:
     - `EMAIL_USER`: Your email address
     - `EMAIL_PASSWORD`: Your email app password
   - For Gmail, create an app password in your Google Account security settings

7. **Install Dependencies**:
   ```
   pip install python-dotenv==1.1.1 requests==2.32.5 twilio==9.8.4
   ```

## Running the Application

```
python main.py
```

The application will:
1. Check each destination in your Google Sheet
2. Search for direct flights first
3. If no direct flights are found, search for indirect flights
4. Send notifications (SMS, WhatsApp, and email) for any flights found below your price threshold
5. Send personalized emails to all registered users

## Features

- Direct and indirect flight search
- Information about number of stops in flights
- WhatsApp or SMS notifications for good deals
- Personalized email notifications to registered users
- Google Form integration for user registration
- Price tracking against your desired thresholds

## Testing Email Functionality

You can test if the email notification system is working correctly:

```
python test_email.py
```

This will prompt you to enter a test email address and will send a sample notification.

## Environment Variables

- `SHEETY_PRICES_ENDPOINT`: Your Sheety API endpoint for prices sheet
- `SHEETY_USERS_ENDPOINT`: Your Sheety API endpoint for users sheet
- `SHEETY_TOKEN`: Your Sheety API token
- `AMADEUS_API_KEY`: Your Amadeus API key
- `AMADEUS_API_SECRET`: Your Amadeus API secret
- `TWILIO_SID`: Your Twilio account SID
- `TWILIO_AUTH_TOKEN`: Your Twilio auth token
- `TWILIO_PHONE_NUMBER`: Your Twilio phone number
- `MY_PHONE_NUMBER`: Your verified phone number to receive notifications
- `EMAIL_USER`: Your email address for sending notifications
- `EMAIL_PASSWORD`: Your email app password (for Gmail, use an app-specific password)

## Project Structure

- **main.py**: Main application file that coordinates the workflow
- **data_manager.py**: Handles interactions with Google Sheets via Sheety API
- **flight_search.py**: Searches for flights using the Amadeus API
- **flight_data.py**: Contains the data model for flight information
- **notification_manager.py**: Handles sending notifications via SMS, WhatsApp, and email
- **test_email.py**: Test script for verifying email functionality