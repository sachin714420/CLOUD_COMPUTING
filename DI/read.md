# 📘 Azure Document Intelligence Project

This project demonstrates how to use **Microsoft Azure Document Intelligence (Form Recognizer)** to analyze documents such as images (PNG), extract data, and process it efficiently.

---

## 🚀 Project Overview

In this project, I created an Azure Document Intelligence resource using Microsoft Azure Foundry and used it to analyze a PNG document.

---

## 🛠️ Steps Followed

### 1. Login to Azure Portal
- Open the Azure Portal: https://portal.azure.com
- Login using your Microsoft account.

---

### 2. Search for Document Intelligence
- In the search bar, type **Document Intelligence**
- Select **Azure AI Document Intelligence** (Form Recognizer)

---

### 3. Create a New Resource
- Click on **Create**
- Fill in the required details:
  - Subscription
  - Resource Group
  - Region
  - Name
  - Pricing Tier
- Click on **Review + Create**
- Then click **Create**

---

### 4. Access the Resource
- After deployment is complete, go to **Go to Resource**
- Note down:
  - **Endpoint**
  - **API Key**

---

### 5. Open Document Intelligence Studio
- Navigate to: https://documentintelligence.ai.azure.com/
- Select your created resource

---

### 6. Upload a Document (PNG Image)
- Click on **Document Analysis**
- Choose a prebuilt model (e.g., Read / Layout / Invoice)
- Upload a **PNG image file**

---

### 7. Analyze the Document
- Click on **Run Analysis**
- Azure processes the document using AI

---

### 8. View Results
- Extracted data is displayed, including:
  - Text
  - Key-value pairs
  - Tables
- You can view:
  - JSON output
  - Structured data

---

### 9. Export Results
- Download or copy the results
- Use them in your application or project

---

## 📂 Features

- Document text extraction
- Image (PNG) analysis
- Structured data output (JSON)
- AI-powered document understanding

---

## 💻 Technologies Used

- Microsoft Azure
- Azure Document Intelligence (Form Recognizer)
- Python (optional, if used in your project)

---
