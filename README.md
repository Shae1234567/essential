# Essential AI Assistant Core

A clean, modular Python template for building and running a local AI assistant core.

## Project Structure

```
essential/
├── src/
│   ├── essential/
│   │   ├── __init__.py
│   │   ├── config.py     # Environment & settings loader
│   │   ├── tools.py      # Extensible tool registry framework
│   │   └── core.py       # Main interactive loop / assistant runner
├── requirements.txt      # Project dependencies
└── .gitignore            # Excludes sensitive files & local state
```

## Quickstart

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Shae1234567/essential.git
   cd essential
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Create a `.env` file in the root directory:
   ```env
   ASSISTANT_NAME=EssentialCore
   API_KEY=your_api_key_here
   ```

5. **Run the local assistant**:
   ```bash
   python -m src.essential.core
   ```
