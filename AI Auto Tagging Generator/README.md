# AI Auto Tagging Generator

## Overview

AI Auto Tagging Generator is a lightweight AI-powered application that automatically generates relevant tags from text content using Google Gemini models.

The goal of the project is to simplify content organization and automate the process of semantic tagging.

Instead of manually reading an article and assigning tags, the system analyzes the text and generates meaningful keywords automatically.

---

## Example

### Input

Artificial intelligence is transforming healthcare systems through automation and predictive analytics.

### Output

- artificial intelligence
- healthcare
- automation
- predictive analytics
- technology

---

## How It Works

The workflow of the application is simple:

User enters text
↓
Text is sent to Gemini AI
↓
Gemini analyzes the content
↓
Relevant tags are generated
↓
Final tags are displayed in the UI

The application uses Google Gemini to understand the semantic meaning of the text and extract the most relevant topics and keywords.

---

## Use Cases

This project can be used for:

- article tagging
- SEO workflows
- metadata generation
- content categorization
- semantic text analysis
- blog and news organization

---

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google GenAI SDK

---

## Project Structure

AI Auto Tagging Generator/
│
├── ui.py
├── styles.py
├── genai_client.py
├── requirements.txt
├── README.md
└── Code.ipynb

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
