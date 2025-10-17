"""
Configuration switcher for production vs test API
Run this to switch between test and production Amadeus API
"""
from config import Config
import os
from pathlib import Path

def switch_to_production():
    """Switch to production Amadeus API for real-time prices"""
    print("🔄 Switching to Production API...")
    print("⚠️  Warning: Production API has rate limits and may charge for requests")
    print("💰 Make sure you have production Amadeus credentials")
    
    # Update config file
    config_file = Path("config.py")
    content = config_file.read_text()
    
    # Replace USE_TEST_API = True with False
    updated_content = content.replace("USE_TEST_API = True", "USE_TEST_API = False")
    config_file.write_text(updated_content)
    
    print("✅ Configuration updated to use Production API")
    print("🔍 This will provide real-time flight prices but with API limits")

def switch_to_test():
    """Switch back to test API"""
    print("🔄 Switching to Test API...")
    
    # Update config file
    config_file = Path("config.py")
    content = config_file.read_text()
    
    # Replace USE_TEST_API = False with True
    updated_content = content.replace("USE_TEST_API = False", "USE_TEST_API = True")
    config_file.write_text(updated_content)
    
    print("✅ Configuration updated to use Test API")
    print("📊 This provides demo data but with unlimited requests")

def main():
    print("🔧 City Break API Configuration")
    print("=" * 40)
    print("Current API mode:", "TEST" if Config.USE_TEST_API else "PRODUCTION")
    print()
    print("Options:")
    print("1. Switch to Production API (real prices, limited requests)")
    print("2. Switch to Test API (demo prices, unlimited requests)")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        switch_to_production()
    elif choice == "2":
        switch_to_test()
    elif choice == "3":
        print("👋 Configuration unchanged")
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()