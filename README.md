# Student Performance Analysis

A beginner-friendly Python data analysis project using **Python, Pandas, NumPy, Matplotlib, and Excel**.

## Features
- Reads student marks from a CSV file.
- Calculates total marks, average, percentage, grade, result, and rank.
- Summarizes average/highest/lowest marks by subject.
- Creates Matplotlib charts for subject averages and the top 10 students.
- Exports a formatted Excel workbook with `Summary`, `Student Results`, and `Subject Analysis` sheets.

## Project structure
```text
Student_Performance_Analysis/
├── data/
│   └── student_performance.csv
├── outputs/
│   ├── charts/
│   │   ├── average_marks_by_subject.png
│   │   └── top_10_students.png
│   └── student_performance_report.xlsx
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements
- Python 3.9 or newer
- Packages listed in `requirements.txt`

## Run on Windows
1. Install Python from https://www.python.org/downloads/ and select **Add Python to PATH** during setup.
2. Extract the ZIP file.
3. Open the extracted `Student_Performance_Analysis` folder.
4. In File Explorer, click the address bar, type `cmd`, and press Enter.
5. Run:
   ```bash
   python -m pip install -r requirements.txt
   python main.py
   ```
6. Open `outputs/student_performance_report.xlsx` in Microsoft Excel or a compatible spreadsheet app. Charts are saved in `outputs/charts/`.

The included CSV is sample data. Replace it with your own data while keeping the same column names. Marks should be between 0 and 100.

## Add this project to GitHub
### Option A: Upload through the GitHub website
1. Sign in to GitHub and open your repository.
2. Choose **Add file → Upload files**.
3. Extract this ZIP on your computer first, then upload the *contents* of the `Student_Performance_Analysis` folder (not the ZIP itself).
4. Enter a commit message such as `Add Student Performance Analysis project`.
5. Click **Commit changes**.

### Option B: Push with Git
Open Command Prompt inside the extracted project folder and run:
```bash
git init
git add .
git commit -m "Add Student Performance Analysis project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```
Replace the remote URL with your actual repository URL. If the repository already has a remote, check it first with `git remote -v` and do not add a second `origin`.

## Notes
- The Excel report and chart images are included as ready-made outputs and will also be regenerated when you run `python main.py`.
- If your repository already contains files, review them before replacing or deleting anything.
