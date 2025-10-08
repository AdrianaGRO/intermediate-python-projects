# 🛰️ ISS Satellite Tracker

A Python application that tracks the International Space Station (ISS) and sends email notifications when it's visible overhead during nighttime.

## Features
- Checks if ISS is currently overhead your location
- Determines if it's nighttime using sunrise/sunset API
- Sends email notifications when ISS is visible
- Uses coordinates for Bucharest, Romania by default

## Files
- `satellite_main.py` - Main application logic
- `test_satellite.py` - Test file
- `.env` - Environment variables (email credentials)

## APIs Used
- ISS Current Location API
- Sunrise-Sunset API

## How to Run
1. Set up your `.env` file with email credentials
2. Run `python satellite_main.py`
3. Get notified when the ISS is visible overhead!