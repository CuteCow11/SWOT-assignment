# SWOT Software AI Assignment: LLM Assistant

A lightweight, command-line AI assistant built using Python and LangChain. It takes user input, queries the `nemotron-3-super-120b-a12b` model via the OpenRouter API, and streams the parsed response directly to the terminal.

## Prerequisites
- Python 3.8 or higher
- A free OpenRouter API key (Obtain one at [OpenRouter](https://openrouter.ai/))

## Setup & Installation

1. **Download the script:** Ensure the main Python script is in your working directory.

2. **Install dependencies:**
   Open your terminal and install the required Python packages:
   ```bash
   pip install langchain-openai langchain-core python-dotenv
