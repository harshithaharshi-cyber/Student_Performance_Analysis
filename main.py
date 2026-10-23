"""
Student Performance Analysis
Analyzes student marks using Pandas and NumPy, creates Matplotlib charts,
and exports a multi-sheet Excel report.
Run: python main.py
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "student_performance.csv"
OUTPUT_DIR = ROOT / "outputs"
CHART_DIR = OUTPUT_DIR / "charts"
EXCEL_FILE = OUTPUT_DIR / "student_performance_report.xlsx"
SUBJECTS = ["Math", "Science", "English", "Computer", "Social_Studies"]

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    CHART_DIR.mkdir(parents=True, exist_ok=True)

    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_FILE}")

    df = pd.read_csv(DATA_FILE)
    required = {"Student_ID", "Student_Name", *SUBJECTS}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"CSV is missing required columns: {sorted(missing)}")

    # Clean and validate numeric marks.
    for subject in SUBJECTS:
        df[subject] = pd.to_numeric(df[subject], errors="coerce")
    if df[SUBJECTS].isna().any().any():
        raise ValueError("Some marks are missing or non-numeric. Please correct the CSV.")
    if ((df[SUBJECTS] < 0) | (df[SUBJECTS] > 100)).any().any():
        raise ValueError("Marks must be between 0 and 100.")

    df["Total_Marks"] = df[SUBJECTS].sum(axis=1)
    df["Average_Marks"] = df[SUBJECTS].mean(axis=1).round(2)
    df["Percentage"] = (df["Total_Marks"] / (len(SUBJECTS) * 100) * 100).round(2)
    df["Result"] = np.where(df[SUBJECTS].min(axis=1) >= 35, "Pass", "Needs Improvement")
    df["Grade"] = np.select(
        [df["Percentage"] >= 90, df["Percentage"] >= 80, df["Percentage"] >= 70,
         df["Percentage"] >= 60, df["Percentage"] >= 50],
        ["A+", "A", "B", "C", "D"], default="F"
    )
    df = df.sort_values("Percentage", ascending=False).reset_index(drop=True)
    df.insert(0, "Rank", np.arange(1, len(df) + 1))

    subject_analysis = pd.DataFrame({
        "Subject": SUBJECTS,
        "Average_Marks": [round(df[s].mean(), 2) for s in SUBJECTS],
        "Highest_Marks": [int(df[s].max()) for s in SUBJECTS],
        "Lowest_Marks": [int(df[s].min()) for s in SUBJECTS],
        "Pass_Count": [int((df[s] >= 35).sum()) for s in SUBJECTS],
    })

    summary = pd.DataFrame({
        "Metric": [
            "Number of Students", "Overall Average Percentage",
            "Highest Student Percentage", "Lowest Student Percentage",
            "Students Passed All Subjects", "Students Needing Improvement"
        ],
        "Value": [
            int(len(df)), round(df["Percentage"].mean(), 2),
            round(df["Percentage"].max(), 2), round(df["Percentage"].min(), 2),
            int((df["Result"] == "Pass").sum()),
            int((df["Result"] != "Pass").sum())
        ]
    })

    # Chart 1: average marks by subject
    plt.figure(figsize=(9, 5))
    plt.bar(subject_analysis["Subject"], subject_analysis["Average_Marks"])
    plt.title("Average Marks by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average marks (out of 100)")
    plt.ylim(0, 100)
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig(CHART_DIR / "average_marks_by_subject.png", dpi=160)
    plt.close()

    # Chart 2: top 10 students by percentage
    top10 = df.head(10).sort_values("Percentage")
    plt.figure(figsize=(9, 5))
    plt.barh(top10["Student_Name"], top10["Percentage"])
    plt.title("Top 10 Students by Percentage")
    plt.xlabel("Percentage")
    plt.xlim(0, 100)
    plt.tight_layout()
    plt.savefig(CHART_DIR / "top_10_students.png", dpi=160)
    plt.close()

    # Export an Excel workbook with analysis sheets.
    with pd.ExcelWriter(EXCEL_FILE, engine="openpyxl") as writer:
        summary.to_excel(writer, sheet_name="Summary", index=False)
        df.to_excel(writer, sheet_name="Student Results", index=False)
        subject_analysis.to_excel(writer, sheet_name="Subject Analysis", index=False)
        for sheet_name in writer.sheets:
            ws = writer.sheets[sheet_name]
            ws.freeze_panes = "A2"
            ws.auto_filter.ref = ws.dimensions
            for column_cells in ws.columns:
                max_len = max(len(str(cell.value or "")) for cell in column_cells)
                ws.column_dimensions[column_cells[0].column_letter].width = min(max_len + 2, 30)

    print("Analysis completed successfully.")
    print(f"Students analyzed: {len(df)}")
    print(f"Average percentage: {df['Percentage'].mean():.2f}%")
    print(f"Excel report: {EXCEL_FILE}")
    print(f"Charts saved in: {CHART_DIR}")

if __name__ == "__main__":
    main()
