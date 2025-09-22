# Flatmates Bill Calculator (Refactored)

A Flask web application for calculating and splitting bills between flatmates based on the number of days each person stayed in the house.

## Features

- Clean, modern web interface
- Form validation with error handling
- PDF report generation
- File sharing capability
- Responsive design
- Proper project structure

## Project Structure

```
09_flatmates_bill_web_refactored/
├── app.py                     # Main Flask application
├── requirements.txt           # Project dependencies
├── README.md                 # This file
├── models/                   # Data models and business logic
│   ├── __init__.py
│   ├── flat.py              # Bill and Flatmate classes
│   └── reports.py           # PDF generation and file sharing
├── templates/               # HTML templates
│   ├── bill_form_page.html  # Form page
│   └── results.html         # Results page
├── static/                  # Static assets
│   └── css/
│       └── main.css         # Styling
└── uploads/                 # Generated PDF files
```

## Installation

1. Navigate to the project directory:
```bash
cd 09_flatmates_bill_web_refactored
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Refactored Version (This Directory):
```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Original Course Version (For Learning):
If you want to follow the original course structure:

1. **Command-line version:**
```bash
cd ../09_flatmates_bill_web/flatmates_bill
python main.py
```

2. **Web version (simple Flask app):**
```bash
cd ../09_flatmates_bill_web
python app.py
```
Then visit `http://localhost:5000/bill_form_page`

> **Note**: The original course structure is messy but working. Use it to follow along with the lesson, then reference this refactored version to see best practices.

## Usage

1. Open the web application in your browser
2. Fill in the bill amount and period
3. Enter details for both flatmates (name and days in house)
4. Click "Calculate" to see the results
5. Download the generated PDF report

## Improvements Made

### From Original Structure:
- ❌ Mixed files in root directory
- ❌ Duplicate templates and CSS
- ❌ No actual Flask application
- ❌ Poor organization
- ❌ No form validation

### To Refactored Structure:
- ✅ Clean, organized directory structure
- ✅ Proper Flask application with routes
- ✅ Form validation with WTForms
- ✅ Modern, responsive CSS design
- ✅ Error handling and user feedback
- ✅ Proper file organization
- ✅ Updated dependencies for Python 3.12 compatibility

## Technical Improvements

1. **Proper MVC Architecture**: Separated models, views (templates), and controller (Flask app)
2. **Form Validation**: Using Flask-WTF for secure form handling
3. **Error Handling**: Graceful error handling for file operations
4. **Modern CSS**: Responsive design with CSS custom properties
5. **Security**: CSRF protection and input validation
6. **Dependencies**: Updated to compatible versions

This refactored version demonstrates proper Flask application structure and modern web development practices.