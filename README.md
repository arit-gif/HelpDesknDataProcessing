[project_readme.md](https://github.com/user-attachments/files/34268966/project_readme.md)
# HelpDesknDataProcessing# Integrated Python Helpdesk & Data Processing Suite

**IT Workshop (Python) Mini Project — 3rd Semester, CSE**  
**Institution:** Budge Budge Institute of Technology (BBIT), Kolkata  
**Academic Year:** 2026–2027  
**Faculty Guide:** Prof. Mrs. Mousumi Ojha  

---

## Team Members
* **Ali Afreen** (27600125039)
* **Arit Chakraborty** (27600125040)
* **Anurag Shankar Shaw** (27600125041)
* **Srijon Ghorui** (27600125042)

---

## Project Overview
The **Integrated Python Helpdesk & Data Processing Suite** is a modular, menu-driven console application built in Python 3 using standard library modules (`csv` and `os`). It integrates two core operational workflows into a single interface:
1. **Helpdesk Ticket Management:** Enables users and technicians to log, view, search, update status (`Open`, `In-Progress`, `Resolved`), and delete support tickets stored persistently in `tickets.csv`.
2. **Data Processing & Analytics:** Allows administrators to record operational metrics in `data_records.csv`, validate numeric entries, and automatically compute descriptive summary statistics (`Count`, `Sum`, `Average`, `Minimum`, `Maximum`), exporting the results to `processed_summary.csv`.

---

## Repository Contents
* `helpdesk_suite.py` — The core modular Python application script.
* `Integrated_Python_Helpdesk_Mini_Project_Report-v2.docx` — The complete formatted mini-project report.
* `tickets.csv` — Persistent CSV storage for support tickets.
* `data_records.csv` — Persistent CSV storage for operational telemetry data.
* `processed_summary.csv` — Exported descriptive statistics summary report.
* `README.md` — Project documentation and setup guide.

---

## How to Run the Application
1. Ensure **Python 3.10** or later is installed on your operating system.
2. Clone this repository or download the project files into a local folder.
3. Open your terminal or command prompt inside the project directory.
4. Execute the Python script:
   ```bash
   python helpdesk_suite.py
   ```
