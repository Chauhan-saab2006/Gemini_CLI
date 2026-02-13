# Gemini CLI

A simple command-line interface for chatting with Google's Gemini AI using the Generative AI API.

## Screenshot

![Gemini CLI Demo](screenshot.png)

> **Note:** To add a screenshot, run the application and take a screenshot of your terminal, then save it as `screenshot.png` in the project directory.

## Features

- 💬 Interactive chat with Gemini AI
- 🔐 Secure API key management using environment variables
- 🎨 Clean ASCII art banner
- ⚡ Real-time responses from Gemini 2.5 Flash model
- 🔄 Continuous conversation until you choose to exit

## Requirements

- Python 3.7+
- Google Gemini API key

## Installation

1. Clone or download this repository

2. Navigate to the project directory:

```bash
cd gemini_cli
```

3. Create a virtual environment (optional but recommended):

```bash
python -m venv env
```

4. Activate the virtual environment:
   - Windows:
     ```bash
     env\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source env/bin/activate
     ```

5. Install required packages:

```bash
pip install -r requirements.txt
```

## Setup

1. Create a `.env` file in the project root directory

2. Add your Gemini API key to the `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

3. Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## Usage

Run the CLI application:

```bash
python main.py
```

Once started:

- Type your message and press Enter to chat with Gemini
- Type `exit` to quit the application

### Example Session

```
===================================================
   ██████  ███████ ███    ███ ██ ███    ██ ██
  ██       ██      ████  ████ ██ ████   ██ ██
  ██   ███ █████   ██ ████ ██ ██ ██ ██  ██ ██
  ██    ██ ██      ██  ██  ██ ██ ██  ██ ██ ██
   ██████  ███████ ██      ██ ██ ██   ████ ██

                GEMINI_CLI
===================================================

you: Hello! How are you?
gemini: I'm doing well, thank you for asking! How can I help you today?

you: exit
```

## Project Structure

```
gemini_cli/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not tracked in git)
├── env/                 # Virtual environment (not tracked in git)
└── README.md           # This file
```

## Dependencies

- `google-generativeai` - Google's Generative AI Python SDK
- `python-dotenv` - Load environment variables from .env file

## Troubleshooting

### API Key Not Found

If you see `⚠️ GEMINI_API_KEY not found in .env file`:

- Make sure you created a `.env` file in the project root
- Check that the API key is correctly formatted: `GEMINI_API_KEY=your_key`
- Ensure there are no extra spaces around the `=` sign

### Model Not Found Error

If you get a model not found error, the model name may have changed. Try updating the model name in `main.py`:

```python
model = genai.GenerativeModel("gemini-1.5-flash")
```

## Security Note

⚠️ Never commit your `.env` file or expose your API key publicly. Add `.env` to your `.gitignore` file.

## License

This project is open source and available for personal and educational use.

## Contributing

Feel free to fork this project and submit pull requests for any improvements.
