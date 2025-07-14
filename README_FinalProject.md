# Employee Turnover Patterns

This project explores patterns of employee turnover using Python. By analyzing HR data from the IBM Attrition dataset, we uncover potential reasons why employees leave and categorize them into human-centered risk patterns such as "Burnout Risk" or "Stable Employee."

This project was built as part of the LIS4930 Intro to Python Summer 2025 course.

---

#### Project Overview

Goal: 
Identify and visualize common employee turnover patterns to help HR better understand and possibly prevent attrition.

Dataset:  
IBM HR Analytics Employee Attrition & Performance  
[Source on Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

---

#### Features

- Cleaned and transformed HR data using 'pandas'
- Applied logic-based classification to label employee risk types:
  - Burnout Risk
  - Low Satisfaction
  - New Hire Exit Risk
  - Stable Employee
  - No Major Risk
- Visualized turnover trends using 'matplotlib' and 'seaborn'
- Wrapped logic in a reusable Python class 'EmployeeTurnoverAnalyzer'

---

#### How It Works

The script:
1. Loads and cleans the HR dataset
2. Flags each employee with a turnover pattern using defined conditions
3. Displays visualizations of employee risk distribution and trends
4. Optionally uses a class to modularize the analysis

---

## File Structure

- LIS4930_FinalProject.py # Full project script with class and visualizations
- WA_Fn-UseC_-HR-Employee-Attrition.csv # Data file (download via Kaggle)


---

## ▶️ To Run

1. Install required packages (if you haven’t already):
   ```bash
   pip install pandas matplotlib seaborn kagglehub

---

## Run the script:
python LIS4930_FinalProject.py

---

#### About Me

Hi! I'm Sardys Avile-Martinez — a student, data enthusiast, and passionate explorer of how Python can help us understand human behavior through data. I love visual storytelling and making beginner-friendly projects that people can relate to.

---

#### Acknowledgments
1. Professor Alon Friedman, for the support and guidance throughout the course
2. IBM and Kaggle for the dataset
