# FRIDAY - Cyberpunk AI Assistant

![Flask](https://img.shields.io/badge/Framework-Flask-blue)
![Python](https://img.shields.io/badge/Language-Python%203.10+-blue)
![Gemma-4B](https://img.shields.io/badge/Model-Gemma--4B-purple)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![MIT License](https://img.shields.io/badge/License-MIT-blue)

> **Developed by ALAN CYRIL SUNNY**  
> If you enjoy this project, please ⭐ [star the repository](https://github.com/yourusername/friday-ai-assistant)!

---

## 🤖 FRIDAY - Cyberpunk AI Assistant

A futuristic, cyberpunk-themed AI assistant inspired by FRIDAY from Iron Man/Avengers. FRIDAY features a modern chat interface, persistent conversation history, and is powered by the Gemma-4B language model.

---

## ✨ Features

- **Modern Chat UI**: Clean, responsive design with purple and cyan cyberpunk accents.
- **Persistent History**: All conversations are saved using SQLite.
- **Real-time AI**: Instant, natural responses via Gemma-4B.
- **Easy Controls**: Clear chat and manage messages effortlessly.
- **Mobile Ready**: Fully responsive for desktop and mobile.
- **Sophisticated Persona**: FRIDAY responds with a natural, engaging personality.

---

## 🛠️ Tech Stack

- [Flask](https://flask.palletsprojects.com/) – backend framework
- [Python 3.10+](https://www.python.org/downloads/) – language
- [Gemma-4B](https://lmstudio.ai/) – language model (via LM Studio)
- [SQLite](https://www.sqlite.org/) – database for chat history
- [HTML5, CSS3, JavaScript] – frontend
- **Cyberpunk UI**: Custom CSS with purple and cyan neon accents

---

## 💻 Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/friday-ai-assistant.git
   cd friday-ai-assistant
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure environment**
   - Set `LM_API_URL` (default: `http://localhost:1234/v1/chat/completions`)
   - Set `MODEL_NAME` (default: `gemma:4b`)
4. **Run LM Studio**
   - Start LM Studio with Gemma-4B model on port 1234
5. **Start the development server**
   ```bash
   python app.py
   ```
6. **Access FRIDAY**
   - Open [http://localhost:5000](http://localhost:5000) in your browser

---

## 📁 Project Structure

```
friday-ai-assistant/
├── app.py              # Main Flask application
├── database.py         # Database operations
├── requirements.txt    # Python dependencies
├── static/             # CSS, JavaScript, and assets
│   └── style.css
├── templates/          # HTML templates
│   └── index.html
└── README.md           # Project documentation
```

---

## 📝 Usage

1. **Type your message** in the chat input and send.
2. **Interact with FRIDAY** for instant, natural responses.
3. **Manage your chat** with clear/reset options. All messages are saved.

---

## 🤝 Contributing

Contributions are welcome!  
1. Fork the repository  
2. Create a new branch  
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. Make your changes and commit  
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. Push to your branch  
   ```bash
   git push origin feature/amazing-feature
   ```
5. Open a Pull Request

Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting a pull request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- Powered by Gemma-4B language model
- Inspired by FRIDAY from Iron Man/Avengers universe
- Created by ALAN CYRIL SUNNY

---

For more info, updates, and documentation, visit the  
👉 [GitHub Repository](https://github.com/yourusername/friday-ai-assistant)

Feel free to fork, star ⭐, and contribute!
