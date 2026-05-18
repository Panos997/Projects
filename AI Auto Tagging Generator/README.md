# AI Auto Tagging Generator

AI-powered tagging system that automatically generates relevant tags for articles and text content using Google Gemini GenAI models.

---

# Overview

AI Auto Tagging Generator is a lightweight AI application designed to automatically generate semantic tags from article content.

The system reads a text or article, analyzes its meaning using Google Gemini models, and returns a list of relevant tags that describe the content.

The project was designed as a simple and practical prototype for automated content classification, semantic tagging, and metadata generation workflows.

It can be useful for:

- news articles
- content management systems
- SEO workflows
- automated categorization
- semantic content analysis

---

# How the System Works

The application follows a simple workflow:

```text
User Input
    ↓
Gemini API Processing
    ↓
Semantic Analysis
    ↓
Tag Generation
    ↓
Cleaned Final Tags
```

The user pastes article text into the interface.

The system then:

1. Sends the text to the Gemini model
2. Analyzes the semantic meaning of the article
3. Generates relevant tags
4. Removes duplicates and cleans the results
5. Displays the final tags in the UI

---

# Example

## Input

```text
Artificial intelligence is transforming healthcare systems through automation and predictive analytics.
```

## Output

```text
artificial intelligence
healthcare
automation
predictive analytics
technology
```

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

Main user interface logic.

Responsible for:

- rendering the interface
- receiving user input
- displaying generated tags
- handling interaction flow

---

## `genai_client.py`

Core AI logic.

Responsible for:

- Gemini API connection
- API key validation
- prompt generation
- semantic tag generation
- result cleaning and deduplication

---

## `styles.py`

Contains the CSS styling used for the interface design.

---

## `Code.ipynb`

Notebook version used for testing and experimentation inside Google Colab or Jupyter environments.

---

## `requirements.txt`

Contains all required dependencies for the project.

Install them using:

```bash
pip install -r requirements.txt
```

---

# Requirements

Before running the project, the following are required:

- Python environment
- Gemini API Key
- Internet connection

---

# How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the notebook or UI application.

Example:

```python
from AI.auto_tagging_generator.ui import run_app
run_app()
```

---

# What This Project Demonstrates

This project demonstrates:

- AI-powered semantic tagging
- automated metadata generation
- content classification workflows
- prompt-based information extraction
- lightweight AI application design
- interactive GenAI interfaces

---

# Conclusion

AI Auto Tagging Generator demonstrates how modern language models can automate semantic tagging and content understanding workflows through simple AI-powered interfaces.

The project focuses on lightweight experimentation, usability, and practical semantic content analysis using Gemini GenAI models.
