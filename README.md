# 🧠 BCG GenAI – Financial Chatbot Job Simulation

This repository showcases my completion of the **Boston Consulting Group (BCG) – GenAI Consulting Simulation** on [Forage](https://www.theforage.com/simulations/bcg/gen-ai-anlo). The project focuses on designing a rule-based AI chatbot that simplifies complex financial data using Python.

## 📌 Project Overview

In this job simulation, I worked as a **GenAI Consultant** at BCG and built a **financial chatbot prototype** that can answer predefined queries based on financial reports (10-K and 10-Q). The goal was to demonstrate how AI can make financial insights more accessible to users.

## 🛠️ Tools & Technologies

- **Python** (Chatbot logic)
- **Pandas** (Data extraction & analysis)
- **Flask** (Web framework)
- **HTML / CSS** (UI for the chatbot)
- **Jupyter Notebook** (Data analysis)
- **10-K / 10-Q Reports** (Financial documents)

## ✅ Key Features

- Extracted and analyzed financial data (Revenue, Net Income, Total Liabilities, etc.)
- Defined predefined queries and responses for the chatbot
- Built a simple Flask-based web app for user interaction
- Enhanced the UI using HTML, CSS, and background design
- Packaged the solution into a demo-ready prototype

## 🧾 Project Workflow

1. **Task 1 – Data Extraction & Analysis**  
   - Loaded company financials (CSV)
   - Used `pandas` to extract insights from 10-K / 10-Q reports  
   - Performed basic trend analysis over fiscal years

2. **Task 2 – Chatbot Design & Development**  
   - Created rule-based responses for key queries
   - Developed the logic in Python using `if-else` structure
   - Set up a basic web UI using Flask and HTML

3. **UI Improvement**  
   - Added background, color themes, and buttons
   - Created a user-friendly chatbot interface

## 🔍 Sample Queries Handled

- What is the total revenue?
- How has net income changed over the last year?
- What is the total liability in the latest report?

## 🚀 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/aniketpatil-6448/BCG-GenAI---Financial-Chatbot-Job-Simulation.git

# 2. Navigate to project folder
cd BCG-GenAI---Financial-Chatbot-Job-Simulation

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask app
python chatbot/app.py
