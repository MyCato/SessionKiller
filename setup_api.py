#!/usr/bin/env python3
"""
Telegram API Credentials Generator
Automates the process of getting Telegram API credentials and configuring the bot.
"""

import json
import os
import re
import time
import asyncio
from telethon import TelegramClient
from telethon.errors import PhoneNumberInvalidError, PhoneCodeInvalidError, SessionPasswordNeededError

class TelegramAPISetup:
    def __init__(self):
        self.config_file = 'config.json'
        self.example_config_file = 'config.example.json'
        
    def print_banner(self):
        """Print welcome banner."""
        print("🤖" + "=" * 60)
        print("   TELEGRAM SESSION MONITOR BOT - API SETUP")
        print("=" * 62)
        print()
        print("This tool will help you:")
        print("✅ Get your Telegram API credentials automatically")
        print("✅ Configure your bot with proper credentials")
        print("✅ Test the connection to ensure everything works")
        print()
    
    def validate_phone(self, phone: str) -> str:
        """Validate and format phone number."""
        # Remove all non-digit characters except +
        phone = re.sub(r'[^\d+]', '', phone)
        
        # Add + if not present and starts with digit
        if phone and phone[0].isdigit():
            phone = '+' + phone
        
        # Basic validation
        if len(phone) < 8 or not phone.startswith('+'):
            raise ValueError("Invalid phone number format")
        
        return phone
    
    def get_user_input(self):
        """Get user input for API setup."""
        print("📱 STEP 1: Enter your phone number")
        print("   Format: +1234567890 (include country code)")
        
        while True:
            try:
                phone = input("📞 Phone number: ").strip()
                if not phone:
                    print("❌ Phone number cannot be empty!")
                    continue
                
                phone = self.validate_phone(phone)
                print(f"✅ Phone number validated: {phone}")
                break
                
            except ValueError as e:
                print(f"❌ {e}")
                print("   Example: +1234567890")
                continue
        
        return phone
    
    async def create_telegram_app(self, phone: str):
        """Create Telegram application and get API credentials."""
        print("\n🔑 STEP 2: Getting API credentials from Telegram")
        print("   This will create an API application for you automatically...")
        
        # Use official Telegram app credentials for initial connection
        # These are public and safe to use for this purpose
        api_id = 17349  # Official Telegram Desktop API ID
        api_hash = "344583e45741c457fe1862106095a5eb"  # Official hash
        
        client = TelegramClient('temp_session', api_id, api_hash)
        
        try:
            print("📡 Connecting to Telegram...")
            await client.connect()
            
            if not await client.is_user_authorized():
                print(f"📨 Sending verification code to {phone}...")
                await client.send_code_request(phone)
                
                while True:
                    try:
                        code = input("📲 Enter the verification code you received: ").strip()
                        if not code:
                            print("❌ Code cannot be empty!")
                            continue
                        
                        await client.sign_in(phone, code)
                        break
                        
                    except PhoneCodeInvalidError:
                        print("❌ Invalid code! Please try again.")
                        continue
                    except SessionPasswordNeededError:
                        password = input("🔒 Two-factor authentication enabled. Enter your password: ")
                        await client.sign_in(password=password)
                        break
            
            print("✅ Successfully authenticated with Telegram!")
            
            # Create API application
            print("\n🏗️  Creating API application...")
            
            app_title = "Session Monitor Bot"
            app_short_name = f"sessionbot_{int(time.time())}"
            app_url = ""
            app_platform = "desktop"
            app_desc = "Telegram session monitoring and security bot"
            
            # Use Telegram's API to create application
            from telethon.tl.functions.account import CreateApplicationRequest
            
            try:
                result = await client(CreateApplicationRequest(
                    title=app_title,
                    short_name=app_short_name,
                    url=app_url,
                    platform=app_platform,
                    description=app_desc
                ))
                
                new_api_id = result.api_id
                new_api_hash = result.api_hash
                
                print("🎉 API Application created successfully!")
                print(f"📋 API ID: {new_api_id}")
                print(f"🔑 API Hash: {new_api_hash}")
                
                return new_api_id, new_api_hash
                
            except Exception as e:
                print(f"⚠️  Could not create new API application: {e}")
                print("📝 Please create manually at https://my.telegram.org")
                print("\n🔧 Manual setup instructions:")
                print("1. Go to https://my.telegram.org")
                print("2. Enter your phone number and verify")
                print("3. Go to 'API Development Tools'")
                print("4. Create a new application with these details:")
                print(f"   - App title: {app_title}")
                print(f"   - Short name: {app_short_name}")
                print(f"   - Platform: {app_platform}")
                print(f"   - Description: {app_desc}")
                print("5. Copy the API ID and API Hash")
                
                api_id = input("\n📋 Enter your API ID: ").strip()
                api_hash = input("🔑 Enter your API Hash: ").strip()
                
                if not api_id or not api_hash:
                    raise ValueError("API ID and Hash are required!")
                
                return int(api_id), api_hash
                
        except PhoneNumberInvalidError:
            raise ValueError(f"Invalid phone number: {phone}")
        except Exception as e:
            raise ValueError(f"Authentication failed: {e}")
        finally:
            if client.is_connected():
                await client.disconnect()
            # Clean up temporary session
            if os.path.exists('temp_session.session'):
                os.remove('temp_session.session')
    
    def save_config(self, api_id: int, api_hash: str, phone: str):
        """Save configuration to config.json."""
        config = {
            "api_id": api_id,
            "api_hash": api_hash,
            "phone": phone
        }
        
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"\n💾 Configuration saved to {self.config_file}")
    
    async def test_connection(self, api_id: int, api_hash: str, phone: str):
        """Test the API credentials."""
        print("\n🧪 STEP 3: Testing API credentials...")
        
        client = TelegramClient('test_session', api_id, api_hash)
        
        try:
            await client.connect()
            
            if not await client.is_user_authorized():
                print("📨 Sending verification code...")
                await client.send_code_request(phone)
                
                code = input("📲 Enter verification code: ").strip()
                await client.sign_in(phone, code)
            
            # Test API functionality
            me = await client.get_me()
            print(f"✅ Connection successful! Logged in as: {me.first_name}")
            
            # Test session listing (main bot functionality)
            from telethon.tl.functions.account import GetAuthorizationsRequest
            result = await client(GetAuthorizationsRequest())
            session_count = len(getattr(result, 'authorizations', []))
            print(f"✅ Found {session_count} active sessions")
            
            return True
            
        except Exception as e:
            print(f"❌ Connection test failed: {e}")
            return False
        finally:
            if client.is_connected():
                await client.disconnect()
            # Clean up test session
            if os.path.exists('test_session.session'):
                os.remove('test_session.session')
    
    def print_success(self):
        """Print success message."""
        print("\n🎉" + "=" * 60)
        print("   SETUP COMPLETED SUCCESSFULLY!")
        print("=" * 62)
        print()
        print("✅ Your bot is now configured and ready to use!")
        print()
        print("🚀 Next steps:")
        print("1. Run your bot: python main.py")
        print("2. Send /start to yourself in Telegram")
        print("3. Use /sessions to see your current devices")
        print("4. Trust your current devices with /trust <hash>")
        print()
        print("🛡️  Your account will now be protected 24/7!")
        print("=" * 62)
    
    async def run_setup(self):
        """Run the complete setup process."""
        try:
            self.print_banner()
            
            # Get user input
            phone = self.get_user_input()
            
            # Get API credentials
            api_id, api_hash = await self.create_telegram_app(phone)
            
            # Save configuration
            self.save_config(api_id, api_hash, phone)
            
            # Test connection
            if await self.test_connection(api_id, api_hash, phone):
                self.print_success()
                return True
            else:
                print("\n❌ Setup failed! Please check your credentials and try again.")
                return False
                
        except KeyboardInterrupt:
            print("\n\n⏹️  Setup cancelled by user.")
            return False
        except Exception as e:
            print(f"\n❌ Setup failed: {e}")
            return False

async def main():
    """Main function."""
    print("Starting Telegram API Setup...")
    
    # Check if already configured
    if os.path.exists('config.json'):
        try:
            with open('config.json', 'r') as f:
                config = json.load(f)
            
            # Check if it's a template or real config
            if (config.get('api_id') not in ['YOUR_API_ID', 'YOUR_API_ID_HERE'] and
                config.get('api_hash') not in ['YOUR_API_HASH', 'YOUR_API_HASH_HERE']):
                
                print("⚠️  Configuration already exists!")
                choice = input("Do you want to reconfigure? (y/N): ").strip().lower()
                if choice != 'y':
                    print("Setup cancelled.")
                    return
        except:
            pass  # Continue with setup if config is invalid
    
    setup = TelegramAPISetup()
    success = await setup.run_setup()
    
    if success:
        print("\n🤖 You can now start your bot with: python main.py")
    else:
        print("\n📖 For manual setup instructions, see README.md")

if __name__ == "__main__":
    asyncio.run(main())
