
# GPA Machine Learning Pipeline

This project demonstrates a complete data science pipeline for student GPA data, including data cleaning, exploratory analysis, feature engineering, machine learning modeling, and exporting cleaned data. The dataset is downloaded from Kaggle.

---

## Dataset Source

[Student GPA Dataset on Kaggle](https://www.kaggle.com/datasets/mohammadalazawi/student-gpa)

---

## Installation and Setup

1. Clone this repository and navigate into it:

```bash
git clone https://github.com/yourusername/gpa-ml-pipeline.git
cd gpa-ml-pipeline
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Set up Kaggle credentials required by `kagglehub` or the Kaggle API to enable dataset download.  
Follow Kaggle’s instructions to place your `kaggle.json` file in the appropriate location (usually `~/.kaggle/`).

---

## Usage

Run the Jupyter notebook to execute the pipeline step-by-step:

```bash
jupyter notebook Gpa_ML_Pipeline.ipynb
```

The notebook performs the following steps sequentially:

- Download the dataset from Kaggle
- Clean and validate the data
- Engineer new features including semester number and cumulative GPA
- Generate exploratory visualizations such as correlation heatmaps and GPA distributions
- Train and evaluate a Random Forest regression model to predict final GPA
- Export the cleaned and processed data to a CSV file

---

## Project Structure

```bash
.
├── Gpa_ML_Pipeline.ipynb        # Jupyter notebook with full data pipeline
├── requirements.txt             # Python dependencies
├── README.md                    # Project overview and instructions
├── cleaned_data.csv             # Output cleaned dataset (generated after running)
└── utils.py                     # Helper functions for modularization (optional)
```

---

## Dependencies

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- kagglehub (or Kaggle API)
- warnings (standard Python library)
- jupyter (for notebook execution)

---

## Notes

- This project uses the Kaggle dataset: [mohammadalazawi/student-gpa](https://www.kaggle.com/mohammadalazawi/student-gpa).
- Ensure your Kaggle API token is correctly configured before running to enable dataset download.
- The model currently uses two main features: maximum semester number and cumulative GPA to predict final GPA.
- Data cleaning includes handling missing or malformed semester information to avoid empty or invalid plots.
- The pipeline is modular and can be extended with additional features or models.

---

## Contact

For questions, issues, or contributions, please open an issue or submit a pull request on GitHub.

---
