#!/usr/bin/env python3
"""
Interactive demo of the Automated Marketing Bot.
Shows the bot's capabilities without running a full automation cycle.
"""

import time
import json
from marketing_bot import MarketingBot

def print_header():
    """Print demo header."""
    print("\n" + "="*60)
    print("🤖 AUTOMATED MARKETING BOT - INTERACTIVE DEMO")
    print("="*60)
    print("This demo shows the bot's capabilities without sending real emails")
    print("or making external API calls. Perfect for testing and demonstration!")
    print("="*60)

def demo_survey_automation(bot):
    """Demo survey automation features."""
    print("\n📋 SURVEY AUTOMATION DEMO")
    print("-" * 30)
    
    print("🔍 Finding surveys on platforms...")
    surveys = bot.survey_automator.find_surveys_on_site("swagbucks.com")
    
    print(f"✅ Found {len(surveys)} available surveys:")
    for i, survey in enumerate(surveys[:2], 1):
        print(f"   {i}. {survey['title']} - {survey['reward']} ({survey['duration']})")
    
    print("\n💰 Simulating survey completion...")
    time.sleep(1)
    earnings = bot.survey_automator.get_earnings_summary()
    print(f"📊 Survey Summary:")
    print(f"   • Total surveys: {earnings['total_surveys']}")
    print(f"   • Total earnings: ${earnings['total_earnings']:.2f}")
    print(f"   • Completed today: {earnings['completed_today']}")

def demo_social_media(bot):
    """Demo social media automation."""
    print("\n📱 SOCIAL MEDIA AUTOMATION DEMO")
    print("-" * 35)
    
    platforms = ["twitter", "linkedin", "facebook", "instagram"]
    
    for platform in platforms:
        print(f"\n🎯 Generating content for {platform.title()}...")
        content = bot.social_media_manager.generate_platform_content(platform)
        print(f"✍️  Content: {content['text'][:80]}...")
        
        # Simulate posting
        time.sleep(0.5)
        engagement = bot.social_media_manager.simulate_engagement_metrics(platform)
        print(f"📈 Simulated engagement: {engagement}")
    
    print("\n📊 Social Media Summary:")
    analysis = bot.social_media_manager.analyze_engagement()
    print(f"   • Total posts: {analysis['total_posts']}")
    print(f"   • Total engagement: {analysis['total_engagement']}")

def demo_form_subscription(bot):
    """Demo form subscription automation."""
    print("\n📧 WEBSITE SUBSCRIPTION DEMO")
    print("-" * 32)
    
    print("🌐 Generating subscription identities...")
    
    for i in range(3):
        email = bot.form_subscriber.generate_email()
        name = bot.form_subscriber.generate_name()
        interests = bot.form_subscriber.get_marketing_interests()
        
        print(f"\n👤 Identity {i+1}:")
        print(f"   • Name: {name}")
        print(f"   • Email: {email}")
        print(f"   • Interests: {', '.join(interests[:3])}")
    
    print("\n📝 Subscription Summary:")
    summary = bot.form_subscriber.get_subscription_summary()
    print(f"   • Total subscriptions: {summary['total_subscriptions']}")
    print(f"   • Subscriptions today: {summary['subscriptions_today']}")

def demo_message_sending(bot):
    """Demo message sending to platforms."""
    print("\n💌 MARKETING MESSAGE DEMO")
    print("-" * 27)
    
    platforms = ["hootsuite.com", "buffer.com", "sproutsocial.com"]
    
    for platform in platforms:
        message = bot.message_sender.create_marketing_message(platform)
        print(f"\n📤 Message to {platform}:")
        print(f"   Subject: {message['subject']}")
        print(f"   Body: {message['body'][:60]}...")
    
    print(f"\n📊 Total messages prepared: {len(platforms)}")

def demo_email_marketing(bot):
    """Demo email marketing features."""
    print("\n📧 EMAIL MARKETING DEMO")
    print("-" * 25)
    
    print("👥 Target audience:")
    target_list = bot.get_target_email_list()
    for email in target_list:
        print(f"   • {email}")
    
    print("\n✍️  Marketing email content:")
    content = bot.generate_marketing_content()
    # Extract just the text content for demo
    import re
    text_content = re.sub('<[^<]+?>', '', content)
    lines = text_content.strip().split('\n')
    for line in lines[:5]:
        if line.strip():
            print(f"   {line.strip()}")
    
    print(f"\n📊 Campaign settings:")
    config = bot.config.get("marketing", {})
    print(f"   • Max emails per hour: {config.get('max_emails_per_hour', 50)}")
    print(f"   • Campaign interval: {config.get('campaign_interval', 3600)} seconds")

def interactive_menu(bot):
    """Show interactive menu."""
    while True:
        print("\n" + "="*50)
        print("🎛️  INTERACTIVE DEMO MENU")
        print("="*50)
        print("1. 📋 Survey Automation Demo")
        print("2. 📱 Social Media Demo")
        print("3. 📧 Website Subscription Demo")
        print("4. 💌 Message Sending Demo")
        print("5. 📧 Email Marketing Demo")
        print("6. 🏃 Run Full Demo")
        print("7. 📊 Generate Report")
        print("8. ❌ Exit")
        print("-" * 50)
        
        choice = input("Select an option (1-8): ").strip()
        
        if choice == "1":
            demo_survey_automation(bot)
        elif choice == "2":
            demo_social_media(bot)
        elif choice == "3":
            demo_form_subscription(bot)
        elif choice == "4":
            demo_message_sending(bot)
        elif choice == "5":
            demo_email_marketing(bot)
        elif choice == "6":
            run_full_demo(bot)
        elif choice == "7":
            bot.generate_daily_report()
        elif choice == "8":
            print("\n👋 Thank you for trying the Automated Marketing Bot!")
            print("✨ Configure config.json and run 'python marketing_bot.py' to start!")
            break
        else:
            print("❌ Invalid choice. Please select 1-8.")
        
        input("\nPress Enter to continue...")

def run_full_demo(bot):
    """Run complete demo of all features."""
    print("\n🎬 FULL AUTOMATION DEMO")
    print("="*40)
    print("Running complete marketing automation cycle...")
    
    demo_survey_automation(bot)
    demo_social_media(bot)
    demo_form_subscription(bot)
    demo_message_sending(bot)
    demo_email_marketing(bot)
    
    print("\n🎉 Full demo completed!")
    print("✅ The bot is ready to automate your marketing!")

def main():
    """Main demo function."""
    print_header()
    
    try:
        print("🚀 Initializing Marketing Bot...")
        bot = MarketingBot()
        print("✅ Bot initialized successfully!")
        
        interactive_menu(bot)
        
    except Exception as e:
        print(f"❌ Error initializing bot: {e}")
        print("💡 Make sure config.json exists and is properly formatted")

if __name__ == "__main__":
    main()