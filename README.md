# SeShat AI Sales Intelligence System

## Overview
The SeShat AI Sales Intelligence System is an AI-powered analytics service designed to analyze electronics sales data, generate business insights, identify risk and performance trends, and provide AI-driven recommendations. It uses a Streamlit frontend, an SQLite database for structured data querying, and LangChain with the Groq API (Llama-3) for natural language insights.

## Project Structure
seshat_ai_analytics/
├── .env
├── requirements.txt
├── init_db.py
├── app.py
├── modules/
│   ├── __init__.py
│   ├── database.py
│   └── llm_engine.py
└── data/
    └── electronics_sales_report_sample.csv

## Prerequisites
* Python 3.10.10
* A valid Groq API Key

## Setup Instructions

### 1. Install Dependencies
Run the following command in your terminal to install the required Python packages:

```bash
#Install required packages
pip install -r requirements.txt

```

### 2. Configure Environment Variables

Create a file named .env in the root directory of the project and add your Groq API key:

```text
GROQ_API_KEY=your_actual_api_key_here

```

### 3. Prepare the Data

Ensure your dataset is named exactly electronics_sales_report_sample.csv and is placed inside the data/ folder.

### 4. Initialize the Database

Run the initialization script to read the CSV file, format the dates, and create the SQLite database (sales_data.db):

```bash
#Initialize SQLite database
python init_db.py

```

### 5. Run the Application

Start the Streamlit dashboard by running the following command:

```bash
#Start the Streamlit server
streamlit run app.py

```

## Core Features

### 1. AI Sales Summary Generator

Aggregates total revenue, top categories, best-selling products, and city-wise performance over a selected date range. Sends a structured context to SeShat AI to generate an executive summary.

### 2. AI Low Performance Detection

Identifies products with low sales volume and low revenue contribution. Uses SeShat AI to explain potential business reasons for underperformance and suggests corrective actions.

### 3. AI Smart Business Query

Allows users to ask natural language questions about the sales data. The system retrieves relevant structured context and uses SeShat AI to provide a business-friendly answer.

### 4. AI Sales Recommendation Engine

Analyzes category performance, city growth opportunities, and payment mode usage to suggest products to promote and strategic areas for business focus.

