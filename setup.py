#!/usr/bin/env python3
"""
Setup script for the Automated Marketing Bot.
"""

import os
import sys
import json
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required!")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def install_requirements():
    """Install required packages."""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install packages: {e}")
        return False

def create_config_if_needed():
    """Create config file if it doesn't exist."""
    config_file = "config.json"
    if not os.path.exists(config_file):
        print("⚙️ Creating default configuration file...")
        default_config = {
            "email": {
                "smtp_server": "smtp.gmail.com",
                "smtp_port": 587,
                "username": "",
                "password": ""
            },
            "marketing": {
                "campaign_interval": 3600,
                "max_emails_per_hour": 50,
                "target_keywords": ["marketing", "sales", "business"]
            },
            "surveys": {
                "enabled": True,
                "platforms": ["surveymonkey", "google_forms"]
            },
            "social_media": {
                "platforms": ["twitter", "linkedin", "facebook"],
                "post_interval": 7200
            }
        }
        
        with open(config_file, 'w') as f:
            json.dump(default_config, f, indent=2)
        print(f"✅ Configuration file created: {config_file}")
    else:
        print(f"✅ Configuration file already exists: {config_file}")

def create_directories():
    """Create necessary directories."""
    directories = ["logs", "data", "temp"]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Directory created/verified: {directory}")

def verify_installation():
    """Verify the installation."""
    print("\n🔍 Verifying installation...")
    
    required_files = [
        "marketing_bot.py",
        "survey_automation.py",
        "social_media.py",
        "config.json",
        "requirements.txt"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing files: {', '.join(missing_files)}")
        return False
    
    print("✅ All required files present")
    return True

def display_usage_instructions():
    """Display usage instructions."""
    print("\n" + "="*60)
    print("🤖 AUTOMATED MARKETING BOT - SETUP COMPLETE!")
    print("="*60)
    print("\n📝 NEXT STEPS:")
    print("1. Edit config.json with your email credentials and preferences")
    print("2. Run the bot: python marketing_bot.py")
    print("\n⚙️ CONFIGURATION:")
    print("- Email settings: Configure SMTP settings for email marketing")
    print("- Marketing: Set campaign intervals and target keywords")
    print("- Surveys: Enable/disable survey automation")
    print("- Social Media: Configure platforms and posting intervals")
    print("\n🚀 FEATURES:")
    print("- ✅ Automated email marketing campaigns")
    print("- ✅ Survey completion and data collection")
    print("- ✅ Social media posting automation")
    print("- ✅ Website subscription management")
    print("- ✅ External site integration")
    print("- ✅ Marketing message automation")
    print("\n⚠️ IMPORTANT:")
    print("- Ensure you have proper permissions for automated activities")
    print("- Review and comply with platform terms of service")
    print("- Monitor bot activities and adjust settings as needed")
    print("- Use responsibly and ethically")
    print("\n📞 SUPPORT:")
    print("- Check the README.md for detailed documentation")
    print("- Review logs in the logs/ directory for troubleshooting")
    print("="*60)

def main():
    """Main setup function."""
    print("🚀 Setting up Automated Marketing Bot...")
    print("="*50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        print("❌ Setup failed during package installation")
        sys.exit(1)
    
    # Create config
    create_config_if_needed()
    
    # Create directories
    create_directories()
    
    # Verify installation
    if not verify_installation():
        print("❌ Setup verification failed")
        sys.exit(1)
    
    # Display usage instructions
    display_usage_instructions()
    
    print("\n🎉 Setup completed successfully!")

if __name__ == "__main__":
    main()