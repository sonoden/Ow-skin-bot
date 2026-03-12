# Overwatch Skin Bot

## Overview
The Overwatch Skin Bot is a utility that helps players keep track of skins for characters in Overwatch. It allows users to view, request, and be notified about new skins.

## Features
- **Skin Tracking**: Monitor available skins for each Overwatch character.
- **Notifications**: Receive updates when new skins are released.
- **Custom Commands**: Users can request information about specific skins or characters.

## Setup Instructions
1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/sonoden/Ow-skin-bot.git
   cd Ow-skin-bot
   ```
2. **Install Dependencies**:
   Make sure you have Node.js installed. Run the following command:
   ```bash
   npm install
   ```
3. **Configure the Bot**:
   - Create a `.env` file in the root directory and set your bot token:
     ```
     BOT_TOKEN=your_bot_token_here
     ```
4. **Run the Bot**:
   Once configured, you can start the bot with:
   ```bash
   node index.js
   ```

## Commands
- `!skins`: Lists available skins for all characters.
- `!skin <character>`: Provides information about skins for a specific character.
- `!notify <skin>`: Sets a notification for a specific skin when it becomes available.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.