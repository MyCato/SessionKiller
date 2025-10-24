# 🛡️ Telegram Session Monitor Bot

A powerful Python bot that monitors your Telegram login sessions in real-time and automatically logs out untrusted devices to protect your account from unauthorized access.

## ✨ Features

- 🔍 **Real-time Monitoring**: Scans for new login sessions every 0.5 seconds
- 🚨 **Automatic Protection**: Instantly logs out untrusted/unknown devices
- ✅ **Trusted Device Management**: Maintain a whitelist of your trusted devices
- 📱 **Session Information**: Detailed information about each active session
- 🔔 **Instant Notifications**: Get notified about all security events
- 📊 **Status Monitoring**: Track bot status and session statistics
- 🎮 **Interactive Commands**: Full control via Telegram commands

## 🚀 Quick Start

### One-Command Setup

```bash
git clone https://github.com/yourusername/TG_loginBOT.git
cd TG_loginBOT
chmod +x setup.sh
./setup.sh
```

That's it! The setup script will:
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Guide you through API credential setup
- ✅ Configure and test your bot
- ✅ Start protecting your account!

## 📋 Requirements

- Python 3.7 or higher
- A Telegram account
- Telegram API credentials (the bot will help you get these automatically)

## ⚙️ Manual Setup

If you prefer manual setup:

### 1. Clone and Install

```bash
git clone https://github.com/yourusername/TG_loginBOT.git
cd TG_loginBOT
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
```

### 2. Get API Credentials

Run the automated setup:
```bash
python setup_api.py
```

Or get them manually:
1. Go to [my.telegram.org](https://my.telegram.org)
2. Enter your phone number and verify
3. Go to "API Development Tools"
4. Create a new application
5. Copy your `api_id` and `api_hash`

### 3. Configure

Edit `config.json`:
```json
{
  "api_id": "your_api_id_here",
  "api_hash": "your_api_hash_here",
  "phone": "your_phone_number_here"
}
```

### 4. Run

```bash
python main.py
```

## 🎮 Bot Commands

Once your bot is running, message yourself on Telegram with these commands:

| Command | Description |
|---------|-------------|
| `/start` | Show welcome message and command list |
| `/status` | Display current monitoring status |
| `/sessions` | List all active login sessions |
| `/trust <hash>` | Add a device to trusted list |
| `/untrust <hash>` | Remove device from trusted list |
| `/trusted` | Show all trusted devices |
| `/stop` | Stop session monitoring |
| `/resume` | Resume session monitoring |

## 🔒 How It Works

1. **Continuous Monitoring**: The bot checks your active Telegram sessions every 0.5 seconds
2. **New Device Detection**: When a new login is detected, the bot immediately analyzes it
3. **Trust Verification**: If the device is in your trusted list, it's allowed
4. **Automatic Logout**: If the device is not trusted, it's immediately logged out
5. **Notifications**: You receive instant notifications about all activities

## 🛡️ Security Features

- **Zero-Tolerance Policy**: Any untrusted device is logged out instantly
- **Encrypted Storage**: All sensitive data is handled securely
- **Session Isolation**: Each session is tracked independently
- **Fail-Safe Design**: The bot continues monitoring even if individual operations fail
- **Privacy Protection**: No data is sent to external servers

## 📊 Session Information

For each session, the bot tracks:
- 📱 Device model and platform
- 🏢 App name and version
- 🌍 Location (country, region)
- 🌐 IP address
- 📅 Creation and last active timestamps
- 🆔 Unique session hash

## ⚠️ Important Security Notes

- **Initial Setup**: When you first run the bot, trust your current devices with `/trust <hash>`
- **New Devices**: Any new login will be logged out unless previously trusted
- **Regular Review**: Periodically review your trusted devices with `/trusted`
- **Emergency Access**: Keep the bot's session hash noted down for emergency access

## 🔧 Configuration

The bot stores configuration in:
- `config.json` - API credentials (keep this secure!)
- `trusted_devices.json` - Your trusted device list
- `session_monitor.session` - Bot's authentication session

## 📝 Logging

The bot logs all activities to:
- Console output (real-time)
- `bot.log` file (persistent)

Log levels include session changes, security events, and error details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This bot is for educational and personal security purposes. Users are responsible for complying with Telegram's Terms of Service and their local laws. The authors are not responsible for any misuse of this software.

## 🆘 Support

If you encounter any issues:

1. Check the `bot.log` file for error details
2. Ensure your API credentials are correct
3. Verify your network connection
4. Make sure you're using a supported Python version (3.7+)

For additional help, please open an issue on GitHub.

## 🎯 Use Cases

- **Personal Security**: Protect your personal Telegram account
- **Business Accounts**: Secure business communications
- **Shared Devices**: Monitor family or team account access
- **Travel Security**: Automatic protection when traveling
- **Privacy Monitoring**: Track who has access to your account

---

**⭐ If this bot helped secure your Telegram account, please consider giving it a star!**
