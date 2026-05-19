# Key Information Retrieval & Borderless Table Location in Scanned Legal Documents

 **Award-Winning Master's Thesis** This repository contains the source code and documentation for my Master's Thesis, conducted at the **Athens University of Economics and Business (AUEB)** in collaboration with the LegalTech company **Cognitiv+**.

>  **Award:** This thesis was awarded as the **Best Master's Thesis** of the academic year.

The project is unified under a single research goal but is divided into two main core sections:

---

## Project Structure & Components

### 1. Intelligent Borderless Table Detection in Scanned Legal Documents
Financial statements and legal documents often contain critical data embedded in tables that **lack visible borders or gridlines**. Traditional OCR tools and layout parsers frequently fail here, mixing up text columns. 

This component treats table detection as an **Object Detection** problem to accurately locate and extract data from these "blind spots."

* **How it works:** We trained and evaluated state-of-the-art computer vision models—specifically **YOLOv8** and **DETR**—to pinpoint the exact boundaries of hidden, borderless tables. 
* **Extraction:** The **Img2Table** library is then utilized to map out rows and columns, seamlessly converting unstructured image data into clean Excel files.

### 2. Intelligent Invoice Understanding Using Multimodal Language Models
Extracting high-value data points (like issue dates, vendor names, line items, or total amounts) from scanned invoices is a classic but challenging problem in Document Intelligence due to layout variations.

This component explores the capabilities of modern **Multimodal Language Models (Vision-Language Models)** to "read" and understand the context of an invoice.

* **How it works:** Instead of relying on rigid templates, this system uses cutting-edge AI for **Visual Question Answering (Visual QA)**. 
* **Models Used:** We evaluated and fine-tuned **LayoutLM** (which processes text tokens alongside their spatial coordinates/bounding boxes) as well as state-of-the-art Large Language Models like **GPT-4 Vision** and **IDEFICS** to extract information using natural language prompts.

---

## Key Benefits & Impact
* **Award-Winning Project:** Recognized for its performance and real-world impact.
* **Massive Time Savings:** Automates the tedious task of manually reviewing hundreds of legal and financial pages.
* **Layout Awareness:** Combines **Natural Language Processing (NLP)** with **Computer Vision** so the AI understands not just the words, but *where* they are placed on a page.
* **Robustness:** Successfully handles the notoriously difficult problem of borderless tables where standard OCR software usually fails.

---

## Credits
* **Author:** Panagiotis Antoniozas
* **Supervisor:** Ion Androutsopoulos (AUEB NLP Group)
* **Industry Partner:** Cognitiv+
