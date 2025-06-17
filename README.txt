# Multi AI Agents Light

## Requirements
- Python 3.13
- Ollama

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Make sure Ollama is running with the gemma3:4b model:
   ```bash
   ollama pull gemma3:4b
   ```

## Usage

### Command Line Usage
```bash
python main.py '{"task": "Your question here"}'
```