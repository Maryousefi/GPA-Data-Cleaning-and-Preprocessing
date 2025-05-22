# 🎓 GPA Data Cleaning and Preprocessing

This project focuses on cleaning, preprocessing, and exploring student GPA data sourced from a Kaggle dataset. The goal is to transform raw CSV data into a clean and structured format suitable for further analysis or machine learning applications.

Dataset Source: [Student GPA Dataset on Kaggle](https://www.kaggle.com/datasets/mohammadalazawi/student-gpa)

---

## 📌 Features

- Downloads data directly from Kaggle using `kagglehub`
- Cleans and filters raw CSV data
- Drops irrelevant or unnamed columns
- Handles missing values and invalid rows
- Visualizes GPA distributions and missing data
- Exports a cleaned CSV file for future use

---

## 📊 Example Insights

- **GPA Distribution**: Understand the spread of student GPAs
- **Missing Value Overview**: Identify data quality issues
- **Student Count per Semester**: Spot trends over academic terms (if available)

---

## 🛠 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/gpa-data-cleaning.git
cd gpa-data-cleaning
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install pandas matplotlib seaborn kagglehub
```

> **Note**: You must also have access to Kaggle and be authenticated with `kagglehub`.

### 3. Run the Notebook

```bash
jupyter notebook student_gpa_cleaning_updated.ipynb
```

> **Make sure your Kaggle credentials are configured** to allow dataset downloads.

---

## 📂 File Structure

```
.
├── student_gpa_cleaning_updated.ipynb  # Jupyter notebook with full workflow
├── cleaned_data.csv                    # Exported cleaned dataset
└── README.md                           # Project documentation
```

---

## 🔮 Future Improvements

- Add outlier detection for GPA
- Create GPA trend features (semester-over-semester changes)
- Apply ML models (e.g., predict dropout or honor eligibility)

---

## 📄 License

This project is released under the [MIT License](LICENSE).
