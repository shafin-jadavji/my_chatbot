# Chatbot Project

This project implements a simple chatbot using the `facebook/blenderbot-400M-distill` model from the Hugging Face Transformers library.

## Requirements

- Python 3.6+
- `transformers` library
- `torch` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/shafin-jadavji/chatbot.git
    cd chatbot
    ```

2. Install the required dependencies:
    ```sh
    pip install transformers torch
    ```

## Usage

Run the chatbot:
```sh
python chatbot.py
```

## How It Works

1. The script loads the `facebook/blenderbot-400M-distill` model and tokenizer.
2. It initializes an empty conversation history.
3. In a loop, it:
    - Prompts the user for input.
    - Tokenizes the input.
    - Generates a response using the model.
    - Decodes and prints the response.
    - Updates the conversation history.

## File Structure

- `chatbot.py`: Main script to run the chatbot.

## License

This project is licensed under the MIT License.