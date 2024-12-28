# OpenAI API Test Project

A simple project to test OpenAI API integration.

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the test script:
```bash
python test_openai.py
```

## Security Note
- Never commit your `.env` file
- Keep your API key secret
- Rotate your API key if it's ever exposed 