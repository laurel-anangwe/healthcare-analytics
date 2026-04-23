# Healthcare Patient Analytics Dashboard
### Multi-Hospital Data Analysis | Excel · Python · Data Visualization

---

## 📋 PROJECT OVERVIEW

An end-to-end data analysis project exploring **8,000 patient records** across 7 hospitals, covering disease burden, treatment outcomes, demographic patterns, and operational performance over a 2-year period (2022–2024).

The project demonstrates the full analytics workflow: raw data → cleaning → multi-sheet analysis → interactive Excel dashboard → Python visualizations → written insights.

---

## 🎯 BUSINESS QUESTIONS ANSWERED

1. Which diseases carry the highest patient burden, and who is most affected?
2. How do treatment outcomes (recovery, mortality, active treatment) vary across diseases and hospitals?
3. Are there demographic patterns (age, gender) that predict worse outcomes?
4. Which hospitals are under the most operational pressure?
5. What are the leading causes of death, and which diseases drive them?

---

## 📁 PROJECT STRUCTURE

```
healthcare-analytics/
│
├── data/
│   └── Health_dataset_py.xlsx          # Source data (8,000 records, 7 sheets)
│
├── excel/
│   └── Healthcare_Analytics_Dashboard.xlsx   # Final Excel dashboard
│
├── python/
│   └── healthcare_analysis.py          # Full analysis & visualizations
│
├── visuals/
│   ├── fig1_disease_demographics.png   # Disease burden & demographics
│   ├── fig2_outcomes_mortality.png     # Treatment outcomes & mortality
│   └── fig3_hospital_operations.png   # Hospital & operational insights
│
└── README.md
```

---

## 🔍 KEY FINDINGS

| Metric | Value |
|---|---|
| Total Patients | 8,000 |
| Overall Recovery Rate | **85.2%** |
| Mortality Rate | 5.2% |
| Average Hospital Stay | 16.5 days |
| Average Patient Age | 53.9 years |
| Most Prevalent Disease | Malaria (1,193 cases, 14.9%) |
| Highest Mortality Disease | Diabetes (6.9%) |
| Busiest Hospital | Lifeline Hospital (2,400 patients, 30%) |

**Highlighted Insights:**
- Males represent 65% of all patients — a gender gap consistent across every disease category
- 53% of patients are elderly ("Old" age group), signalling a heavily aged patient population
- Lifeline Hospital handles nearly double the load of the next-largest facility
- Dialysis is the most administered treatment (31% of all treatments), despite infectious diseases dominating caseload
- Multiple Organ Failure, Respiratory Failure, and Cardiac Arrest account for 77% of all deaths

---

## 🛠️ TOOLS & SKILLS DEMONSTRATED

**Microsoft Excel**
- Pivot tables (disease burden, average LOS, treatment outcomes, age distribution)
- Multi-sheet workbook architecture with a dedicated dashboard
- Conditional formatting and data validation
- Custom formatting for dark-themed professional presentation

**Python**
- `pandas` — data loading, cleaning, groupby analysis, aggregation
- `matplotlib` & `seaborn` — multi-panel dashboards, heatmaps, stacked bars, donut charts
- Custom dark-theme styling applied globally via `rcParams`
- Modular, well-documented code ready for reuse or extension

**Analytical Skills**
- Exploratory data analysis (EDA)
- Demographic segmentation (age, gender, disease)
- Comparative performance analysis (hospitals, treatments)
- Mortality and outcome rate calculation
- Data storytelling — translating numbers into actionable insights

---

## ▶️ HOW TO RUN

```bash
# Clone the repository
git clone https://github.com/laurel-anangwe/healthcare-analytics.git
cd healthcare-analytics

# Install dependencies
pip install pandas matplotlib seaborn openpyxl

# Run the analysis
python python/healthcare_analysis.py
```

Output: 3 high-resolution visualization figures saved to `/visuals/`

---

## 📸 DASHBOARD PREVIEW

> *(Add a screenshot of your Excel dashboard here after uploading to GitHub)*
> Tip: On Windows — `Snipping Tool`. On Mac — `Cmd + Shift + 4`. Save as PNG and drag into the repo.

---

## 🔮 POTENTIAL EXTENSIONS

- **Power BI / Tableau** version of the dashboard for interactive web sharing
- **Time-series forecasting** of monthly admissions using `statsmodels`
- **Predictive model** — logistic regression to predict mortality risk by patient profile
- **Geographic mapping** if hospital location data is available

---

---
---


*Healthcare Patient Analytics Dashboard — built with Excel & Python | Dataset: Health_dataset_py.xlsx*
