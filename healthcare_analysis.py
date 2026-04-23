"""
Healthcare Patient Data Analysis
=================================
Author  : [Laurel Anangwe]
Dataset : Health_dataset_py.xlsx  |  8,000 patients  |  2022–2024
Purpose : Exploratory data analysis and visualization of multi-hospital
          patient records covering disease burden, treatment outcomes,
          demographic patterns, and hospital performance.

Usage:
    python healthcare_analysis.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ── Theme ─────────────────────────────────────────────────────────────────
DARK_BG      = "#1A1F2E"
CARD_BG      = "#242B3D"
TEAL         = "#00C9B1"
CORAL        = "#FF6B6B"
AMBER        = "#FFB347"
BLUE         = "#4A90D9"
PURPLE       = "#9B59B6"
GREEN        = "#27AE60"
WHITE        = "#FFFFFF"
LIGHT_GREY   = "#B0BEC5"
PALETTE      = [TEAL, CORAL, AMBER, BLUE, PURPLE, GREEN,
                "#E74C3C", "#F39C12", "#1ABC9C", "#8E44AD",
                "#2980B9", "#D35400", "#16A085", "#C0392B", "#7F8C8D"]

plt.rcParams.update({
    "figure.facecolor":  DARK_BG,
    "axes.facecolor":    CARD_BG,
    "axes.edgecolor":    "#2E3850",
    "axes.labelcolor":   LIGHT_GREY,
    "axes.titlecolor":   WHITE,
    "text.color":        WHITE,
    "xtick.color":       LIGHT_GREY,
    "ytick.color":       LIGHT_GREY,
    "grid.color":        "#2E3850",
    "grid.linestyle":    "--",
    "grid.alpha":        0.4,
    "font.family":       "DejaVu Sans",
})

# ── Load Data ─────────────────────────────────────────────────────────────
print("Loading data...")
df = pd.read_excel(
    '/mnt/user-data/uploads/Health_dataset_py.xlsx',
    sheet_name='Health_dataset'
)
df['Admission Date'] = pd.to_datetime(df['Admission Date'])
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])
df['Year']  = df['Admission Date'].dt.year
df['Month'] = df['Admission Date'].dt.to_period('M')

# ── Derived metrics ────────────────────────────────────────────────────────
disease_counts   = df['Disease'].value_counts()
status_counts    = df['Treatment Status'].value_counts()
hospital_counts  = df['Hospital'].value_counts()
gender_counts    = df['Gender'].value_counts()
age_counts       = df['Age level'].value_counts()
total            = len(df)
recovery_rate    = round(df['Treatment Status'].eq('Recovered').mean() * 100, 1)
mortality_rate   = round(df['Treatment Status'].eq('Deceased').mean() * 100, 1)

disease_status = df.groupby(['Disease', 'Treatment Status']).size().unstack(fill_value=0)
disease_gender = df.groupby(['Disease', 'Gender']).size().unstack(fill_value=0)
hosp_rates     = df.groupby('Hospital')['Treatment Status'].value_counts(normalize=True).unstack(fill_value=0)
age_disease    = df.groupby(['Disease', 'Age level']).size().unstack(fill_value=0)
disease_los    = df.groupby('Disease')['Length of Stay(Days)'].mean().sort_values(ascending=False)
disease_mort   = (disease_status['Deceased'] / disease_counts * 100).sort_values(ascending=False)

print(f"  ✓ {total:,} patients | {recovery_rate}% recovery | {mortality_rate}% mortality")

# ══════════════════════════════════════════════════════════════════════════
# FIGURE 1 — DISEASE BURDEN & DEMOGRAPHICS
# ══════════════════════════════════════════════════════════════════════════
print("Generating Figure 1: Disease Burden & Demographics...")
fig1 = plt.figure(figsize=(20, 14), facecolor=DARK_BG)
fig1.suptitle("HEALTHCARE PATIENT ANALYTICS  •  Disease Burden & Demographics",
              fontsize=16, fontweight='bold', color=TEAL, y=0.98)

gs = gridspec.GridSpec(2, 3, figure=fig1, hspace=0.45, wspace=0.38)

# 1A — Horizontal bar: disease counts
ax1 = fig1.add_subplot(gs[0, :2])
colors_bar = [TEAL if i < 3 else (AMBER if i < 7 else CORAL)
              for i in range(len(disease_counts))]
bars = ax1.barh(disease_counts.index[::-1], disease_counts.values[::-1],
                color=colors_bar[::-1], edgecolor='none', height=0.7)
for bar, val in zip(bars, disease_counts.values[::-1]):
    ax1.text(bar.get_width() + 15, bar.get_y() + bar.get_height()/2,
             f'{val:,}', va='center', ha='left', fontsize=8, color=LIGHT_GREY)
ax1.set_xlabel("Patient Count", color=LIGHT_GREY, fontsize=9)
ax1.set_title("Disease Burden — Total Cases", fontsize=12, fontweight='bold', pad=10)
ax1.axvline(total/len(disease_counts), color=WHITE, linestyle='--', alpha=0.3, linewidth=1)
ax1.text(total/len(disease_counts) + 5, -0.6, 'avg', fontsize=7, color=WHITE, alpha=0.5)
ax1.set_xlim(0, disease_counts.max() * 1.15)
ax1.grid(axis='x')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# 1B — Pie: gender
ax2 = fig1.add_subplot(gs[0, 2])
g_vals  = [gender_counts.get('Male', 0), gender_counts.get('Female', 0)]
g_labels= ['Male\n65.1%', 'Female\n34.9%']
wedge_props = dict(width=0.55, edgecolor=DARK_BG, linewidth=2)
ax2.pie(g_vals, labels=None, colors=[BLUE, CORAL],
        autopct=None, wedgeprops=wedge_props, startangle=90)
ax2.text(0, 0, f'{total:,}\npatients', ha='center', va='center',
         fontsize=10, fontweight='bold', color=WHITE)
ax2.set_title("Gender Split", fontsize=12, fontweight='bold', pad=10)
legend_patches = [mpatches.Patch(color=BLUE,  label=f'Male  {g_vals[0]:,}'),
                  mpatches.Patch(color=CORAL, label=f'Female  {g_vals[1]:,}')]
ax2.legend(handles=legend_patches, loc='lower center', fontsize=8,
           framealpha=0, labelcolor=LIGHT_GREY, ncol=2, bbox_to_anchor=(0.5, -0.08))

# 1C — Stacked bar: age groups by disease
ax3 = fig1.add_subplot(gs[1, :2])
age_pcts = age_disease.div(age_disease.sum(axis=1), axis=0) * 100
diseases_sorted = disease_counts.index.tolist()
young_vals = [age_pcts.loc[d, 'Young']       if d in age_pcts.index and 'Young'       in age_pcts.columns else 0 for d in diseases_sorted]
mid_vals   = [age_pcts.loc[d, 'Middle-Aged'] if d in age_pcts.index and 'Middle-Aged' in age_pcts.columns else 0 for d in diseases_sorted]
old_vals   = [age_pcts.loc[d, 'Old']         if d in age_pcts.index and 'Old'         in age_pcts.columns else 0 for d in diseases_sorted]

x = range(len(diseases_sorted))
ax3.bar(x, young_vals, label='Young',       color=GREEN,  alpha=0.9, width=0.65)
ax3.bar(x, mid_vals,   label='Middle-Aged', color=AMBER,  alpha=0.9, width=0.65, bottom=young_vals)
ax3.bar(x, old_vals,   label='Old',         color=CORAL,  alpha=0.9, width=0.65,
        bottom=[y+m for y,m in zip(young_vals, mid_vals)])
ax3.set_xticks(x)
ax3.set_xticklabels(diseases_sorted, rotation=40, ha='right', fontsize=8)
ax3.set_ylabel("% of Disease Cases", fontsize=9)
ax3.set_title("Age Distribution by Disease (%)", fontsize=12, fontweight='bold', pad=10)
ax3.legend(fontsize=8, framealpha=0, loc='upper right', labelcolor=LIGHT_GREY)
ax3.set_ylim(0, 115)
ax3.grid(axis='y')
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

# 1D — Donut: age groups overall
ax4 = fig1.add_subplot(gs[1, 2])
age_vals = [age_counts.get('Young', 0), age_counts.get('Middle-Aged', 0), age_counts.get('Old', 0)]
ax4.pie(age_vals, labels=None, colors=[GREEN, AMBER, CORAL],
        wedgeprops=dict(width=0.55, edgecolor=DARK_BG, linewidth=2), startangle=120)
ax4.text(0, 0.1, 'Age', ha='center', va='center', fontsize=9, color=LIGHT_GREY)
ax4.text(0, -0.15, 'Groups', ha='center', va='center', fontsize=9, color=LIGHT_GREY)
ax4.set_title("Age Group Split", fontsize=12, fontweight='bold', pad=10)
age_labels = [f'Young  {age_vals[0]:,}', f'Mid-Age  {age_vals[1]:,}', f'Old  {age_vals[2]:,}']
age_patches = [mpatches.Patch(color=c, label=l) for c, l in zip([GREEN, AMBER, CORAL], age_labels)]
ax4.legend(handles=age_patches, loc='lower center', fontsize=7.5,
           framealpha=0, labelcolor=LIGHT_GREY, ncol=1, bbox_to_anchor=(0.5, -0.18))

plt.savefig('/home/claude/fig1_disease_demographics.png', dpi=150, bbox_inches='tight',
            facecolor=DARK_BG)
plt.close()
print("  ✓ Figure 1 saved")

# ══════════════════════════════════════════════════════════════════════════
# FIGURE 2 — TREATMENT OUTCOMES & MORTALITY
# ══════════════════════════════════════════════════════════════════════════
print("Generating Figure 2: Treatment Outcomes & Mortality...")
fig2 = plt.figure(figsize=(20, 14), facecolor=DARK_BG)
fig2.suptitle("HEALTHCARE PATIENT ANALYTICS  •  Treatment Outcomes & Mortality",
              fontsize=16, fontweight='bold', color=CORAL, y=0.98)
gs2 = gridspec.GridSpec(2, 3, figure=fig2, hspace=0.45, wspace=0.38)

# 2A — Mortality rate by disease (horizontal bar)
ax5 = fig2.add_subplot(gs2[0, :2])
mort_sorted = disease_mort.sort_values()
bar_colors  = [CORAL if v > 6 else (AMBER if v > 5 else TEAL) for v in mort_sorted.values]
ax5.barh(mort_sorted.index, mort_sorted.values, color=bar_colors, height=0.7, edgecolor='none')
for i, (disease, val) in enumerate(mort_sorted.items()):
    ax5.text(val + 0.05, i, f'{val:.1f}%', va='center', fontsize=8, color=LIGHT_GREY)
ax5.axvline(mortality_rate, color=WHITE, linestyle='--', alpha=0.5, linewidth=1.2)
ax5.text(mortality_rate + 0.05, -0.8, f'avg {mortality_rate}%', fontsize=7.5, color=WHITE, alpha=0.6)
ax5.set_xlabel("Mortality Rate (%)", fontsize=9)
ax5.set_title("Mortality Rate by Disease  (red > 6%, amber > 5%)", fontsize=12, fontweight='bold', pad=10)
ax5.set_xlim(0, mort_sorted.max() * 1.2)
ax5.grid(axis='x')
ax5.spines['top'].set_visible(False)
ax5.spines['right'].set_visible(False)

# 2B — Pie: treatment status overall
ax6 = fig2.add_subplot(gs2[0, 2])
st_vals = [status_counts.get('Recovered', 0),
           status_counts.get('Under Treatment', 0),
           status_counts.get('Deceased', 0)]
ax6.pie(st_vals, labels=None, colors=[GREEN, AMBER, CORAL],
        wedgeprops=dict(width=0.55, edgecolor=DARK_BG, linewidth=2), startangle=90)
ax6.text(0, 0.1, f'{recovery_rate}%', ha='center', va='center',
         fontsize=14, fontweight='bold', color=GREEN)
ax6.text(0, -0.18, 'recovered', ha='center', va='center', fontsize=8, color=LIGHT_GREY)
ax6.set_title("Treatment Status", fontsize=12, fontweight='bold', pad=10)
st_patches = [
    mpatches.Patch(color=GREEN, label=f'Recovered  {st_vals[0]:,}'),
    mpatches.Patch(color=AMBER, label=f'Active  {st_vals[1]:,}'),
    mpatches.Patch(color=CORAL, label=f'Deceased  {st_vals[2]:,}'),
]
ax6.legend(handles=st_patches, loc='lower center', fontsize=7.5,
           framealpha=0, labelcolor=LIGHT_GREY, ncol=1, bbox_to_anchor=(0.5, -0.22))

# 2C — Average LOS by disease
ax7 = fig2.add_subplot(gs2[1, :2])
los_sorted = disease_los.sort_values(ascending=True)
bar_colors_los = [BLUE if v > disease_los.mean() else TEAL for v in los_sorted.values]
ax7.barh(los_sorted.index, los_sorted.values, color=bar_colors_los, height=0.7, edgecolor='none')
ax7.axvline(disease_los.mean(), color=AMBER, linestyle='--', alpha=0.7, linewidth=1.2)
ax7.text(disease_los.mean() + 0.1, -0.6, f'avg {disease_los.mean():.1f}d', fontsize=7.5, color=AMBER)
for i, (d, v) in enumerate(los_sorted.items()):
    ax7.text(v + 0.1, i, f'{v:.1f}d', va='center', fontsize=8, color=LIGHT_GREY)
ax7.set_xlabel("Average Length of Stay (Days)", fontsize=9)
ax7.set_title("Average Length of Stay by Disease", fontsize=12, fontweight='bold', pad=10)
ax7.grid(axis='x')
ax7.spines['top'].set_visible(False)
ax7.spines['right'].set_visible(False)

# 2D — Hospital recovery rates
ax8 = fig2.add_subplot(gs2[1, 2])
hosp_short = {
    "Lifeline Hospital": "Lifeline",
    "Greenfield Medical": "Greenfield",
    "Hope Medical Center": "Hope Med.",
    "Global Health Clinic": "Global",
    "MetroCare Hospital": "MetroCare",
    "City General Hospital": "City Gen.",
    "Sunrise Clinic": "Sunrise",
}
h_names = [hosp_short.get(h, h) for h in hosp_rates.index]
h_rec   = hosp_rates['Recovered'].values * 100
h_dec   = hosp_rates['Deceased'].values  * 100
x_h = range(len(h_names))
ax8.bar(x_h, h_rec, color=GREEN,  alpha=0.9, label='Recovery %', width=0.5)
ax8.bar(x_h, h_dec, color=CORAL,  alpha=0.9, label='Mortality %', width=0.5,
        bottom=[r - d for r, d in zip(h_rec, h_dec)])
ax8.set_xticks(x_h)
ax8.set_xticklabels(h_names, rotation=35, ha='right', fontsize=7.5)
ax8.set_ylabel("Rate (%)", fontsize=9)
ax8.set_title("Hospital Outcomes", fontsize=12, fontweight='bold', pad=10)
ax8.legend(fontsize=8, framealpha=0, labelcolor=LIGHT_GREY)
ax8.set_ylim(0, 100)
ax8.grid(axis='y')
ax8.spines['top'].set_visible(False)
ax8.spines['right'].set_visible(False)

plt.savefig('/home/claude/fig2_outcomes_mortality.png', dpi=150, bbox_inches='tight',
            facecolor=DARK_BG)
plt.close()
print("  ✓ Figure 2 saved")

# ══════════════════════════════════════════════════════════════════════════
# FIGURE 3 — HOSPITAL & OPERATIONAL INSIGHTS
# ══════════════════════════════════════════════════════════════════════════
print("Generating Figure 3: Hospital & Operational Insights...")
fig3 = plt.figure(figsize=(20, 14), facecolor=DARK_BG)
fig3.suptitle("HEALTHCARE PATIENT ANALYTICS  •  Hospital & Operational Insights",
              fontsize=16, fontweight='bold', color=PURPLE, y=0.98)
gs3 = gridspec.GridSpec(2, 3, figure=fig3, hspace=0.48, wspace=0.38)

# 3A — Hospital patient load
ax9 = fig3.add_subplot(gs3[0, :2])
hosp_labels = [hosp_short.get(h, h) for h in hospital_counts.index]
bar_colors_h = [PURPLE if i == 0 else BLUE for i in range(len(hosp_labels))]
ax9.barh(hosp_labels[::-1], hospital_counts.values[::-1], color=bar_colors_h[::-1],
         height=0.65, edgecolor='none')
for i, (h, v) in enumerate(zip(hosp_labels[::-1], hospital_counts.values[::-1])):
    pct = round(v / total * 100, 1)
    ax9.text(v + 10, i, f'{v:,}  ({pct}%)', va='center', fontsize=8.5, color=LIGHT_GREY)
ax9.set_xlabel("Total Patients", fontsize=9)
ax9.set_title("Patient Load by Hospital", fontsize=12, fontweight='bold', pad=10)
ax9.set_xlim(0, hospital_counts.max() * 1.22)
ax9.grid(axis='x')
ax9.spines['top'].set_visible(False)
ax9.spines['right'].set_visible(False)

# 3B — Treatment type distribution
ax10 = fig3.add_subplot(gs3[0, 2])
tx_counts = df['Treatment'].value_counts()
ax10.pie(tx_counts.values, labels=None, colors=PALETTE[:len(tx_counts)],
         wedgeprops=dict(width=0.6, edgecolor=DARK_BG, linewidth=1.5), startangle=90)
ax10.set_title("Treatment Mix", fontsize=12, fontweight='bold', pad=10)
tx_patches = [mpatches.Patch(color=PALETTE[i], label=f'{t}  {v:,}')
              for i, (t, v) in enumerate(tx_counts.items())]
ax10.legend(handles=tx_patches, loc='lower center', fontsize=7,
            framealpha=0, labelcolor=LIGHT_GREY, ncol=1, bbox_to_anchor=(0.5, -0.38))

# 3C — Monthly admissions trend
ax11 = fig3.add_subplot(gs3[1, :2])
monthly = df.groupby('Month').size()
months_str = [str(m) for m in monthly.index]
m_vals  = monthly.values
ax11.fill_between(range(len(months_str)), m_vals, alpha=0.2, color=TEAL)
ax11.plot(range(len(months_str)), m_vals, color=TEAL, linewidth=2, marker='o',
          markersize=4)
tick_positions = list(range(0, len(months_str), 3))
ax11.set_xticks(tick_positions)
ax11.set_xticklabels([months_str[i] for i in tick_positions], rotation=35, ha='right', fontsize=8)
ax11.axhline(m_vals[:-1].mean(), color=AMBER, linestyle='--', alpha=0.6, linewidth=1)
ax11.text(0.5, m_vals[:-1].mean() + 3, f'avg {m_vals[:-1].mean():.0f}', fontsize=7.5, color=AMBER)
ax11.set_ylabel("Admissions", fontsize=9)
ax11.set_title("Monthly Admissions Trend (2022–2024)", fontsize=12, fontweight='bold', pad=10)
ax11.grid(axis='y')
ax11.spines['top'].set_visible(False)
ax11.spines['right'].set_visible(False)
ax11.set_xlim(0, len(months_str) - 1)

# 3D — Gender mortality heatmap (disease × gender mortality rate)
ax12 = fig3.add_subplot(gs3[1, 2])
gender_mort = df.groupby(['Disease', 'Gender'])['Treatment Status'].apply(
    lambda x: (x == 'Deceased').mean() * 100
).unstack(fill_value=0)
sns.heatmap(gender_mort, ax=ax12, cmap='YlOrRd', annot=True, fmt='.1f',
            linewidths=0.5, linecolor=DARK_BG, annot_kws={'size': 7},
            cbar_kws={'label': 'Mortality %'})
ax12.set_title("Mortality % by Disease & Gender", fontsize=11, fontweight='bold', pad=10)
ax12.set_xlabel("")
ax12.set_ylabel("")
ax12.tick_params(axis='x', labelsize=8)
ax12.tick_params(axis='y', labelsize=7.5, rotation=0)

plt.savefig('/home/claude/fig3_hospital_operations.png', dpi=150, bbox_inches='tight',
            facecolor=DARK_BG)
plt.close()
print("  ✓ Figure 3 saved")

# ══════════════════════════════════════════════════════════════════════════
# SUMMARY STATS PRINT
# ══════════════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("  HEALTHCARE ANALYTICS — SUMMARY STATISTICS")
print("="*60)
print(f"  Total Patients          : {total:,}")
print(f"  Recovery Rate           : {recovery_rate}%")
print(f"  Mortality Rate          : {mortality_rate}%")
print(f"  Average Length of Stay  : {df['Length of Stay(Days)'].mean():.1f} days")
print(f"  Average Patient Age     : {df['Age'].mean():.1f} years")
print(f"  Top Disease             : {disease_counts.index[0]} ({disease_counts.iloc[0]:,} cases)")
print(f"  Largest Hospital        : {hospital_counts.index[0]} ({hospital_counts.iloc[0]:,} patients)")
print(f"  Highest Mortality       : {disease_mort.index[0]} ({disease_mort.iloc[0]:.1f}%)")
print("="*60)
print("\n✅ All 3 figures saved to /home/claude/")
