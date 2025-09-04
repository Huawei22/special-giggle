#!/usr/bin/env python3
"""
Test script for the Automated Marketing Bot.
Tests basic functionality without actually sending emails or making external requests.
"""

import json
import sys
import os

# Add current directory to path for imports
sys.path.insert(0, os.getcwd())

from marketing_bot import MarketingBot
from survey_automation import SurveyAutomator, FormSubscriber
from social_media import SocialMediaManager, MessageSender

def test_config_loading():
    """Test configuration loading."""
    print("🧪 Testing configuration loading...")
    
    try:
        bot = MarketingBot()
        assert bot.config is not None
        print("✅ Configuration loaded successfully")
        return True
    except Exception as e:
        print(f"❌ Configuration loading failed: {e}")
        return False

def test_survey_automation():
    """Test survey automation module."""
    print("🧪 Testing survey automation...")
    
    try:
        config = {"external_sites": {"survey_sites": ["example.com"]}}
        automator = SurveyAutomator(config)
        
        # Test survey finding
        surveys = automator.find_surveys_on_site("example.com")
        assert len(surveys) > 0
        
        # Test earnings summary
        summary = automator.get_earnings_summary()
        assert "total_surveys" in summary
        
        print("✅ Survey automation tests passed")
        return True
    except Exception as e:
        print(f"❌ Survey automation tests failed: {e}")
        return False

def test_social_media():
    """Test social media module."""
    print("🧪 Testing social media automation...")
    
    try:
        config = {
            "social_media": {
                "platforms": ["twitter", "linkedin"],
                "hashtags": ["#test", "#bot"]
            }
        }
        manager = SocialMediaManager(config)
        
        # Test content generation
        content = manager.generate_platform_content("twitter")
        assert "text" in content
        assert content["platform"] == "twitter"
        
        # Test engagement analysis
        analysis = manager.analyze_engagement()
        assert "total_posts" in analysis
        
        print("✅ Social media automation tests passed")
        return True
    except Exception as e:
        print(f"❌ Social media automation tests failed: {e}")
        return False

def test_form_subscriber():
    """Test form subscription module."""
    print("🧪 Testing form subscription...")
    
    try:
        config = {"website_integration": {"form_endpoints": ["https://example.com/signup"]}}
        subscriber = FormSubscriber(config)
        
        # Test email generation
        email = subscriber.generate_email()
        assert "@" in email
        
        # Test name generation
        name = subscriber.generate_name()
        assert " " in name
        
        # Test summary
        summary = subscriber.get_subscription_summary()
        assert "total_subscriptions" in summary
        
        print("✅ Form subscription tests passed")
        return True
    except Exception as e:
        print(f"❌ Form subscription tests failed: {e}")
        return False

def test_message_sender():
    """Test message sending module."""
    print("🧪 Testing message sender...")
    
    try:
        config = {"external_sites": {"marketing_platforms": ["platform1.com"]}}
        sender = MessageSender(config)
        
        # Test message creation
        message = sender.create_marketing_message("platform1.com")
        assert "subject" in message
        assert "body" in message
        
        print("✅ Message sender tests passed")
        return True
    except Exception as e:
        print(f"❌ Message sender tests failed: {e}")
        return False

def test_bot_initialization():
    """Test main bot initialization."""
    print("🧪 Testing bot initialization...")
    
    try:
        bot = MarketingBot()
        
        # Check if all modules are initialized
        assert hasattr(bot, 'survey_automator')
        assert hasattr(bot, 'form_subscriber')
        assert hasattr(bot, 'social_media_manager')
        assert hasattr(bot, 'message_sender')
        
        print("✅ Bot initialization tests passed")
        return True
    except Exception as e:
        print(f"❌ Bot initialization tests failed: {e}")
        return False

def run_demo():
    """Run a quick demo of bot functionality."""
    print("\n🎬 Running bot functionality demo...")
    
    try:
        # Create a test bot
        bot = MarketingBot()
        
        # Test survey automation
        print("📋 Testing survey completion...")
        survey_summary = bot.survey_automator.get_earnings_summary()
        print(f"   Survey stats: {survey_summary}")
        
        # Test social media
        print("📱 Testing social media content generation...")
        content = bot.social_media_manager.generate_platform_content("twitter")
        print(f"   Generated content: {content['text'][:50]}...")
        
        # Test form subscription
        print("📧 Testing form subscription...")
        email = bot.form_subscriber.generate_email()
        name = bot.form_subscriber.generate_name()
        print(f"   Generated identity: {name} <{email}>")
        
        print("✅ Demo completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🚀 AUTOMATED MARKETING BOT - TEST SUITE")
    print("=" * 50)
    
    tests = [
        test_config_loading,
        test_survey_automation,
        test_social_media,
        test_form_subscriber,
        test_message_sender,
        test_bot_initialization
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 TEST RESULTS: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Running demo...")
        run_demo()
        print("\n✅ Bot is ready for use!")
        return True
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)