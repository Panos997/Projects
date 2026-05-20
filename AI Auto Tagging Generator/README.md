# AI Auto Tagging Generator

## Overview

AI Auto Tagging Generator is a simple AI-powered application that automatically generates tags from text content using Google Gemini AI models.

The main purpose of the project is to help users quickly identify the most important topics and keywords inside an article or text without manually reading and tagging everything.

The user simply enters a text, and the AI analyzes the meaning of the content and generates relevant tags automatically.

---

# What the Application Does

The application takes a piece of text as input and returns a list of tags that describe the main topics of the content.

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

The system understands that the text is related to AI, healthcare, automation, and technology, then generates tags based on the meaning of the text.

---

# How It Works

The workflow of the application is very simple:

```text
User enters text
        ↓
Text is sent to Gemini AI
        ↓
Gemini analyzes the meaning of the text
        ↓
Relevant tags are generated
        ↓
Tags are displayed in the interface
```

The application does not simply extract random words from the text.

Instead, the AI tries to understand the semantic meaning of the content and generate tags that best describe the article or paragraph.

---

# Why This Project Is Useful

This project can help automate content organization tasks.

Instead of manually assigning tags to articles, the AI can generate them automatically.

Possible use cases include:

- article tagging
- blog organization
- SEO workflows
- metadata generation
- semantic text analysis
- automated categorization

---

# Technologies Used

The project was built using the following technologies and tools:

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | User interface and web app |
| Google Gemini API | AI model for text analysis |
| Google GenAI SDK | Communication with Gemini models |
| Jupyter Notebook | Testing and experimentation |

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

Contains the Streamlit user interface.

Responsible for:
- text input
- buttons
- displaying generated tags
- interaction with the user

---

## `genai_client.py`

Handles communication with Google Gemini.

Responsible for:
- creating the Gemini client
- sending prompts to the AI model
- receiving generated tags
- returning results back to the UI

---

## `styles.py`

Contains styling and visual customization for the Streamlit interface.

---

## `Code.ipynb`

Notebook used for testing, experimentation, and trying prompts during development.

---

# How to Run the Project

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2. Add Gemini API Key

Example:

### Linux / macOS

```bash
export GEMINI_API_KEY="your_api_key_here"
```

### Windows PowerShell

```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

---

## 3. Run the Application

```bash
streamlit run ui.py
```

After running the command, the application opens locally in the browser.

---

# Technical Details

## Application Architecture

The architecture of the project is simple:

```text
Streamlit UI
      ↓
Gemini API Request
      ↓
AI Tag Generation
      ↓
Display Results
```

---

## Internal Flow

```text
ui.py
  ↓
User enters text
  ↓
genai_client.py
  ↓
Prompt sent to Gemini
  ↓
Gemini generates tags
  ↓
Response returned
  ↓
Tags displayed in UI
```

---

## Prompt Workflow

The application sends a structured prompt to Gemini asking the model to:

- analyze the text
- understand the main topics
- generate relevant tags
- avoid duplicates
- return clean output

Example prompt logic:

```text
Analyze the following text and generate relevant tags.

Rules:
- Return only tags.
- Use short keywords or short phrases.
- Avoid duplicates.

Text:
{user_text}
```

---

## Streamlit Execution

The application is executed locally using Streamlit.

Command:

```bash
streamlit run ui.py
```

The terminal starts the application, and Streamlit launches the web interface in the browser.

---

## Google Gemini Integration

The project uses the Google GenAI SDK to communicate with Gemini models.

Typical workflow:

1. User enters text.
2. Text is sent to Gemini.
3. Gemini processes the content.
4. Gemini returns generated tags.
5. Results are displayed in the interface.

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

AI Auto Tagging Generator is a lightweight AI application that demonstrates how Generative AI can automatically analyze text and generate meaningful tags based on semantic understanding.

The project focuses on simplicity, usability, and practical AI-powered content tagging workflows.
