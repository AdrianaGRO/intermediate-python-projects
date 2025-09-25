#!/bin/bash

# Virtual Environment Management Script for the Instant Dictionary Webapp

PROJECT_ROOT="/Users/adricati/Personal Development/intermediate-python-projects"
VENV_PATH="$PROJECT_ROOT/.venv"
WEBAPP_DIR="$PROJECT_ROOT/17_ OOP_Object_Oriented_Programming/13_Instant_dictionary_webapp"

echo "🐍 Virtual Environment Manager for Instant Dictionary Webapp"
echo "============================================================"

# Function to activate virtual environment
activate_venv() {
    echo "📁 Navigating to project root..."
    cd "$PROJECT_ROOT"
    
    if [ -d "$VENV_PATH" ]; then
        echo "✅ Activating virtual environment..."
        source "$VENV_PATH/bin/activate"
        echo "🎉 Virtual environment activated!"
        echo "📍 Current Python: $(which python)"
        echo "📦 Python version: $(python --version)"
    else
        echo "❌ Virtual environment not found at $VENV_PATH"
        echo "💡 Run 'python3 -m venv .venv' to create one"
    fi
}

# Function to install requirements
install_requirements() {
    echo "📦 Installing requirements..."
    cd "$WEBAPP_DIR"
    pip install -r requirements.txt
    echo "✅ Requirements installed!"
}

# Function to run the webapp
run_webapp() {
    echo "🚀 Starting the webapp..."
    cd "$WEBAPP_DIR"
    python examples/main.py
}

# Function to show help
show_help() {
    echo "Usage: $0 [command]"
    echo ""
    echo "Commands:"
    echo "  activate    - Activate virtual environment"
    echo "  install     - Install requirements"
    echo "  run         - Run the webapp"
    echo "  help        - Show this help"
    echo ""
    echo "Example workflow:"
    echo "  $0 activate"
    echo "  $0 install"
    echo "  $0 run"
}

# Main script logic
case "$1" in
    "activate")
        activate_venv
        ;;
    "install")
        install_requirements
        ;;
    "run")
        run_webapp
        ;;
    "help"|*)
        show_help
        ;;
esac