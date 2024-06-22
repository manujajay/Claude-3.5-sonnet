# Claude 3.5 Sonnet AI Chatbot

This is a simple AI chatbot using the Claude 3.5 Sonnet model from Anthropic.

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/claude-chatbot.git
    cd claude-chatbot
    ```

2. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Create a `.env` file and add your Claude API key:**
    ```plaintext
    CLAUDE_KEY=your_claude_api_key
    ```

## Running the Chatbot

Run the chatbot using:
```bash
python app.py
```

Type your messages and the bot will respond. To quit, type `quit`.

## Notes

- This basic version does not maintain conversation context.
- For production use, ensure your API keys are kept secure.
    
