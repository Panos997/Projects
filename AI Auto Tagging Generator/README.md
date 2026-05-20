# AI Auto Tagging Generator

## Overview

AI Auto Tagging Generator is a lightweight AI-powered application that automatically generates relevant tags from text content using Google Gemini models.

The purpose of the project is to simplify content organization by automatically identifying the main topics and keywords inside an article or paragraph.

Instead of manually reading a text and assigning tags, the user can simply paste the content into the application and let the AI generate meaningful tags automatically.

---

# What the Application Does

The application takes text as input and returns a list of semantic tags that describe the main topics of the content.

Example:

### Input

```text
Artificial intelligence is transforming healthcare systems through automation and predictive analytics.
```

### Output

```text
artificial intelligence
healthcare
automation
predictive analytics
technology
```

The AI analyzes the meaning of the text and generates tags based on semantic understanding instead of simple keyword matching.

---

# How It Works

The workflow of the application is simple:

```text
User enters text
        ↓
Text is sent to Gemini AI
        ↓
Gemini analyzes the content
        ↓
Structured JSON tags are generated
        ↓
Tags are cleaned and displayed
```

The application sends the article text to a Google Gemini model using the Google GenAI SDK.

The model returns structured JSON containing generated tags, which are then parsed, cleaned, and displayed to the user.

---

# Features

- AI-powered semantic tag generation
- Google Gemini integration
- Structured JSON output generation
- Duplicate tag removal
- Interactive notebook-based UI
- Adjustable number of generated tags
- Gemini model selection
- Copy generated tags button
- Live word and token estimation

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Google Gemini API | AI text analysis |
| Google GenAI SDK | Gemini integration |
| Jupyter Notebook | Interactive environment |
| ipywidgets | Interactive UI components |
| HTML/CSS | UI styling and layout |

The project dependencies include:

```text
streamlit>=1.36.0
google-genai>=1.0.0
```

from `requirements.txt`. :contentReference[oaicite:0]{index=0}

---

# Project Structure

```text
AI Auto Tagging Generator/
│
├── ui.py
├── styles.py
├── genai_client.py
├── requirements.txt
├── README.md
└── Code.ipynb
```

---

# File Explanation

## `ui.py`

Contains the interactive user interface logic. :contentReference[oaicite:1]{index=1}

The UI is built using:

- `ipywidgets`
- HTML
- IPython display tools

The interface includes:

- text input area
- API key input
- Gemini model selector
- max tags slider
- generate button
- copy tags button
- live metrics for characters, words, and estimated tokens

The application is mainly designed to run inside a Jupyter or Colab notebook environment.

---

## `genai_client.py`

Handles communication with Google Gemini. :contentReference[oaicite:2]{index=2}

Main responsibilities:

- initializing the Gemini client
- validating the API key
- sending prompts to Gemini
- requesting structured JSON responses
- parsing generated tags
- removing duplicate tags
- returning clean results

The application uses:

```python
response_mime_type="application/json"
response_schema=schema
```

to enforce structured AI output generation.

---

## `styles.py`

Contains all custom CSS styling used by the interface. :contentReference[oaicite:3]{index=3}

The file defines:

- layout styling
- buttons
- cards
- chips/tags
- gradients
- responsive UI elements
- dark mode support

---

## `Code.ipynb`

Notebook used for running the application interactively and testing prompts during development.

The code comments also show that the project was originally developed inside Google Colab.

---

# How to Run the Project

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2. Set Gemini API Key

### Linux / macOS

```bash
export GEMINI_API_KEY="your_api_key_here"
```

### Windows PowerShell

```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

---

## 3. Launch the Notebook

Open:

```text
Code.ipynb
```

using:

- Jupyter Notebook
- JupyterLab
- VS Code
- Google Colab

---

## 4. Run the Application

Inside the notebook:

```python
from auto_tagging_generator.ui import run_app

run_app()
```

The UI will appear interactively inside the notebook environment.

---

# Technical Details

## Architecture

The project follows a simple architecture:

```text
Notebook UI
      ↓
Gemini API Request
      ↓
Structured JSON Response
      ↓
Tag Cleaning
      ↓
Display Generated Tags
```

---

# UI Layer

The UI is implemented with `ipywidgets` instead of Streamlit. :contentReference[oaicite:4]{index=4}

Main UI components include:

- `Textarea`
- `Buttons`
- `Dropdown`
- `Slider`
- `HTML widgets`
- `VBox/HBox layouts`

The interface dynamically updates:

- word count
- character count
- token estimation
- generated tags

The generated tags are rendered visually as styled chips using custom HTML and CSS.

---

# Gemini Integration

The project uses:

```python
from google import genai
```

through the Google GenAI SDK. :contentReference[oaicite:5]{index=5}

The application initializes a Gemini client using:

```python
genai.Client(api_key=key)
```

and sends prompts using:

```python
client.models.generate_content()
```

---

# Structured Output Generation

One important feature of the project is the use of structured JSON generation.

The application defines a response schema:

```python
schema = {
    "type":"object",
    "properties":{
        "tags":{
            "type":"array",
            "items":{"type":"string"}
        }
    },
    "required":["tags"]
}
```

Gemini is then instructed to return only valid JSON output.

This makes the generated results more predictable and easier to parse programmatically.

---

# Post-Processing Logic

After receiving the Gemini response:

1. JSON is parsed
2. Tags are extracted
3. Duplicate tags are removed
4. Empty values are ignored
5. Final cleaned tags are returned

Duplicate filtering is implemented using a Python `set()`.

---

# Internal Application Flow

```text
User enters article
        ↓
UI calls generate_tags()
        ↓
Prompt sent to Gemini
        ↓
Gemini returns JSON tags
        ↓
JSON parsed
        ↓
Duplicate cleaning
        ↓
Tags displayed as UI chips
```

---

# Example Usage

## Example 1

### Input

```text
Machine learning is being used in finance to detect fraud and improve risk analysis.
```

### Output

```text
machine learning
finance
fraud detection
risk analysis
artificial intelligence
```

---

## Example 2

### Input

```text
Climate change is affecting global agriculture and food production.
```

### Output

```text
climate change
agriculture
food production
environment
global warming
```

---

# Conclusion

AI Auto Tagging Generator is a lightweight semantic tagging application that demonstrates how Google Gemini can be used to automatically analyze text and generate structured semantic tags.

The project focuses on simplicity, interactive AI workflows, structured output generation, and practical GenAI integration inside notebook environments.
