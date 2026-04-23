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
git clone https://github.com/[your-username]/healthcare-analytics.git
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

# ✉️ CV / RESUME PROJECT ENTRY

*Copy one of the versions below directly into your CV under a "Projects" section.*

---

## VERSION A — Concise (1–2 lines, for tight CVs)

**Healthcare Patient Analytics Dashboard** | Excel · Python (pandas, matplotlib)
Analysed 8,000 patient records across 7 hospitals to surface disease burden, mortality drivers, and treatment outcomes; built an interactive Excel dashboard and Python visualizations revealing an 85% recovery rate and a 30% hospital load concentration. [[GitHub Link]](#)

---

## VERSION B — Detailed (3–4 lines, for data analyst roles)

**Healthcare Patient Analytics Dashboard** | Excel · Python · Data Visualization
Designed and executed an end-to-end data analysis project on an 8,000-patient multi-hospital dataset spanning 2022–2024. Engineered a multi-sheet Excel dashboard covering disease burden, treatment outcomes, demographic segmentation, and hospital performance metrics. Extended the analysis in Python using pandas and matplotlib to produce publication-quality visualizations. Key findings included an 85.2% system-wide recovery rate, a 65:35 male-to-female patient ratio, and a critical resource concentration at a single hospital handling 30% of all cases. [[GitHub Link]](#)

---

## VERSION C — Achievement-Focused (for competitive applications)

**Healthcare Patient Analytics Dashboard** | Excel · Python
- Cleaned, structured, and analysed 8,000 patient records across 15 disease categories and 7 hospitals
- Built a 6-sheet Excel dashboard with KPI cards, disease performance matrices, and hospital comparison tables
- Produced 3 Python visualization panels (matplotlib/seaborn) covering demographics, outcomes, and operations
- Identified Diabetes as the highest-mortality disease (6.9%) and flagged a 2.5-day gender gap in Hypertension stay length — insights with direct clinical relevance
- Demonstrated proficiency in data wrangling, pivot analysis, visual design, and data storytelling [[GitHub Link]](#)

---

## 💡 WHERE TO LIST IT ON YOUR CV

Place it in a **Projects** section, ideally between your Work Experience and Education sections.
If you don't have a Projects section yet, add one — for data roles, strong projects often outweigh short work experience.

**Section header options:**
- `Projects`
- `Data Projects`
- `Portfolio Projects`
- `Independent Projects`

---

## 🔗 HOW TO LINK IT

1. **GitHub** (best for technical roles) — Upload the folder as a public repo, link directly from your CV
2. **LinkedIn** — Add it under `Featured` or `Projects` on your profile; paste the GitHub URL
3. **Notion / Google Sites** — Turn the README into a visual case study with embedded screenshots
4. **PDF Portfolio** — Screenshot the Excel dashboard, include 1–2 Python charts, add the CV write-up

---

*Healthcare Patient Analytics Dashboard — built with Excel & Python | Dataset: Health_dataset_py.xlsx*
