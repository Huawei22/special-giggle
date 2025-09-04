#!/usr/bin/env python3
"""
Simple launcher for the Automated Marketing Bot.
Provides easy access to different bot functions.
"""

import sys
import os

def show_banner():
    """Show the bot banner."""
    print("""
╔══════════════════════════════════════════════════════════╗
║                🤖 AUTOMATED MARKETING BOT 🤖              ║
║                                                          ║
║  Boost your business with intelligent marketing          ║
║  automation, survey completion, and social media        ║
║  management - all running automatically 24/7!           ║
╚══════════════════════════════════════════════════════════╝
    """)

def show_menu():
    """Show the main menu."""
    print("🎯 What would you like to do?")
    print("-" * 40)
    print("1. 🚀 Start Full Marketing Bot")
    print("2. 🎬 Run Interactive Demo")
    print("3. 🧪 Test Bot Components")
    print("4. ⚙️  Setup/Install Dependencies")
    print("5. 📖 View Documentation")
    print("6. ❌ Exit")
    print("-" * 40)

def start_marketing_bot():
    """Start the full marketing bot."""
    print("🚀 Starting Automated Marketing Bot...")
    print("⚠️  Note: This will run continuous automation!")
    confirm = input("Continue? (y/N): ").lower().strip()
    
    if confirm == 'y':
        try:
            from marketing_bot import main
            main()
        except KeyboardInterrupt:
            print("\n⏹️  Bot stopped by user")
        except Exception as e:
            print(f"❌ Error: {e}")
    else:
        print("✅ Cancelled")

def run_demo():
    """Run the interactive demo."""
    try:
        from demo import main
        main()
    except Exception as e:
        print(f"❌ Demo error: {e}")

def run_tests():
    """Run the test suite."""
    try:
        from test_bot import main
        main()
    except Exception as e:
        print(f"❌ Test error: {e}")

def run_setup():
    """Run the setup script."""
    try:
        from setup import main
        main()
    except Exception as e:
        print(f"❌ Setup error: {e}")

def show_docs():
    """Show basic documentation."""
    print("\n📖 QUICK START GUIDE")
    print("=" * 50)
    print("1. Configuration:")
    print("   • Edit config.json with your email and API settings")
    print("   • Customize marketing intervals and targets")
    print()
    print("2. Features:")
    print("   • ✅ Automated email marketing campaigns")
    print("   • ✅ Survey completion for rewards")
    print("   • ✅ Social media posting automation")
    print("   • ✅ Website subscription management")
    print("   • ✅ Marketing platform integration")
    print()
    print("3. Safety:")
    print("   • Always comply with platform terms of service")
    print("   • Use reasonable delays and limits")
    print("   • Monitor bot activities regularly")
    print()
    print("4. Files:")
    print("   • marketing_bot.py - Main bot application")
    print("   • config.json - Configuration settings")
    print("   • demo.py - Interactive demonstration")
    print("   • test_bot.py - Test suite")
    print("   • README.md - Full documentation")
    print("=" * 50)

def main():
    """Main launcher function."""
    show_banner()
    
    while True:
        show_menu()
        choice = input("\nSelect option (1-6): ").strip()
        
        if choice == "1":
            start_marketing_bot()
        elif choice == "2":
            run_demo()
        elif choice == "3":
            run_tests()
        elif choice == "4":
            run_setup()
        elif choice == "5":
            show_docs()
        elif choice == "6":
            print("\n👋 Goodbye! Happy marketing automation!")
            break
        else:
            print("❌ Invalid choice. Please select 1-6.")
        
        if choice != "6":
            input("\nPress Enter to return to menu...")
            print("\n" * 2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Launcher error: {e}")
        print("💡 Try running the components directly if needed")