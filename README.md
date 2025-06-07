# FRIDAY - Personal AI Assistant

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

FRIDAY is your sophisticated AI assistant, inspired by the AI from Iron Man/Avengers. Built with Flask and powered by the Gemma-4B language model, FRIDAY offers a modern, responsive chat interface with persistent conversation history.

## Features

- 🤖 Modern, responsive chat interface
- 💾 Persistent chat history (SQLite database)
- 🔄 Real-time conversation with Gemma-4B
- 📝 Clear chat functionality
- 📱 Mobile-friendly design
- 💅 Clean, cyberpunk-themed UI with purple and cyan accents
- 📝 Natural conversation flow without repetitive self-identification

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/friday-ai-assistant.git
cd friday-ai-assistant
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run LM Studio with Gemma-4B model on port 1234

4. Start the Flask application:
```bash
python app.py
```

5. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Type your message in the input field
2. Press Enter or click Send to send the message
3. FRIDAY will respond with her sophisticated personality
4. Use the Clear Chat button to reset the conversation
5. Messages are automatically saved in the database

## Configuration

The application uses the following environment variables:

- `LM_API_URL`: URL of the LM Studio API (default: http://localhost:1234/v1/chat/completions)
- `MODEL_NAME`: Language model name (default: gemma:4b)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Project Structure

- `app.py`: Main Flask application with chat functionality
- `templates/`: HTML templates for the chat interface
- `static/`: Static assets (CSS, JavaScript)
- `database.py`: Database operations for chat history
- `requirements.txt`: Python dependencies
- `README.md`: Project documentation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Created by ALAN CYRIL SUNNY
- Powered by Gemma-4B language model
- Inspired by FRIDAY from Iron Man/Avengers universe

## Support

For support, please contact ALAN CYRIL SUNNY or open an issue in the GitHub repository.

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting a pull request.

## Technical Details

- **Backend**: Flask web framework
- **Frontend**: HTML5, CSS3, JavaScript
- **Language Model**: Gemma-4B
- **Database**: SQLite
- **UI Theme**: Cyberpunk-inspired with purple and cyan accents
