import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub
from kagglehub import KaggleDatasetAdapter


# ────────────────────────────────────────
# PART 1: Load Dataset from Kaggle
# ────────────────────────────────────────

print("\n Part 1: Load + Explore the Dataset")

file_path = "WA_Fn-UseC_-HR-Employee-Attrition.csv"

df = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "pavansubhasht/ibm-hr-analytics-attrition-dataset",
    file_path
)

print("Dataset shape:", df.shape)
print("Columns:\n", df.columns.tolist())
print(df.head())

# ────────────────────────────────────────
# PART 2: Data Cleaning & Setup
# ────────────────────────────────────────

print("\n Part 2: Cleaning Data")

df_clean = df.copy()
df_clean['Attrition'] = df_clean['Attrition'].map({'Yes': 1, 'No': 0})
df_clean['OverTime'] = df_clean['OverTime'].map({'Yes': 1, 'No': 0})

print("Preview Cleaned Columns:\n", df_clean[['Attrition', 'OverTime']].head())
print("Numeric Check:\n", df_clean[['JobSatisfaction', 'EnvironmentSatisfaction', 'YearsAtCompany']].dtypes)
print("Nulls:\n", df_clean.isnull().sum().sort_values(ascending=False).head())

# ────────────────────────────────────────
# PART 3: Flag Turnover Pattern (outside class)
# ────────────────────────────────────────

def flag_turnover_pattern(row):
    if row['OverTime'] == 1 and row['JobSatisfaction'] <= 2 and row['YearsAtCompany'] < 3:
        return "Burnout Risk"
    elif row['JobSatisfaction'] == 1 or row['EnvironmentSatisfaction'] == 1:
        return "Low Satisfaction"
    elif row['YearsAtCompany'] <= 1 and row['Attrition'] == 1:
        return "New Hire Exit Risk"
    elif row['OverTime'] == 0 and row['JobSatisfaction'] >= 3 and row['YearsAtCompany'] >= 5:
        return "Stable Employee"
    else:
        return "No Major Risk"

df_clean['TurnoverPattern'] = df_clean.apply(flag_turnover_pattern, axis=1)
print("\nTurnover Pattern Preview:\n", df_clean[['Attrition', 'OverTime', 'JobSatisfaction', 'YearsAtCompany', 'TurnoverPattern']].head())

# ────────────────────────────────────────
# PART 4: Visualizations Subtle colors
# ────────────────────────────────────────

print("\n Part 4: Turnover Pattern Distribution")

# Plot
plt.figure(figsize=(8, 5))
df_clean['TurnoverPattern'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Distribution of Employee Turnover Patterns")
plt.xlabel("Turnover Pattern")
plt.ylabel("Number of Employees")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n Part 4: Job Satisfaction vs. Years at Company")

plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df_clean,
    x='JobSatisfaction',
    y='YearsAtCompany',
    hue='TurnoverPattern',
    palette="Set2",
    alpha=0.8
)
plt.title("Job Satisfaction vs. Years at Company\nColored by Turnover Pattern")
plt.xlabel("Job Satisfaction")
plt.ylabel("Years at Company")
plt.legend(title='Pattern', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# ────────────────────────────────────────
# PART 5: Class Wrapper With Bright Colors (Optional)
# ────────────────────────────────────────
#I just wanted to have fun with this here :)

class EmployeeTurnoverAnalyzer:
    def __init__(self, dataframe):
        self.df = dataframe.copy()
        self.apply_pattern_detection()

    def flag_turnover_pattern(self, row):
        if row['OverTime'] == 1 and row['JobSatisfaction'] <= 2 and row['YearsAtCompany'] < 3:
            return "Burnout Risk"
        elif row['JobSatisfaction'] == 1 or row['EnvironmentSatisfaction'] == 1:
            return "Low Satisfaction"
        elif row['YearsAtCompany'] <= 1 and row['Attrition'] == 1:
            return "New Hire Exit Risk"
        elif row['OverTime'] == 0 and row['JobSatisfaction'] >= 3 and row['YearsAtCompany'] >= 5:
            return "Stable Employee"
        else:
            return "No Major Risk"

    def apply_pattern_detection(self):
        self.df['TurnoverPattern'] = self.df.apply(self.flag_turnover_pattern, axis=1)

    def plot_pattern_distribution(self):
        pattern_counts = self.df['TurnoverPattern'].value_counts()

        plt.figure(figsize=(9, 6))
        bars = pattern_counts.plot(kind='bar', color=sns.color_palette("bright"))

        plt.title("Distribution of Employee Turnover Patterns")
        plt.xlabel("Turnover Pattern")
        plt.ylabel("Number of Employees")
        plt.xticks(rotation=45)

        # Add count labels on top of each bar
        for i, count in enumerate(pattern_counts):
            plt.text(i, count + 10, f"{count}", ha='center', va='bottom', fontsize=9, fontweight='bold')

        plt.tight_layout()
        plt.show()

    def plot_overtime_vs_satisfaction(self):
        plt.figure(figsize=(9, 6))
        sns.scatterplot(
            data=self.df,
            x='JobSatisfaction',
            y='YearsAtCompany',
            hue='TurnoverPattern',
            palette="bright",
            alpha=0.8
        )

        # Add helpful annotations for interpretation
        plt.text(1.1, 1.5, "Risk Zone:\nLow Satisfaction,\nLow Tenure", fontsize=10, color="darkred")
        plt.text(3.2, 10, "Happy Veterans:\nHigh Satisfaction,\nLong Tenure", fontsize=10, color="green")
        plt.text(2, 5, "Gray Zone:\nMixed Patterns", fontsize=10, color="gray")

        # Add chart details
        plt.title("Job Satisfaction vs. Years at Company\nColored by Turnover Pattern")
        plt.xlabel("Job Satisfaction (1 = Low, 4 = High)")
        plt.ylabel("Years at Company")
        plt.legend(title='Turnover Pattern', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()

# Instantiate for optional use
analyzer = EmployeeTurnoverAnalyzer(df_clean)
analyzer.plot_pattern_distribution()
analyzer.plot_overtime_vs_satisfaction()
