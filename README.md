# 📊 Sales Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.33+-red?logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.20+-purple?logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.2+-green?logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Production-brightgreen)

An end-to-end, production-grade interactive sales analytics platform built with **Python, Pandas, Streamlit, and Plotly**. Designed to surface regional performance trends, product profitability rankings, and time-series insights from ~2,000 retail transactions — all through a clean, filterable dashboard.

---

## 🚀 Live Demo

Deploy this app for free on **Streamlit Community Cloud**:

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Select this repo → set main file to `app.py` → Deploy

---

## 📁 Project Architecture

```
sales-analytics-dashboard/
│
├── data/
│       └── raw-sales-data.csv      # Immutable source dataset (~2,000 records)
│
├── analysis.py                      # EDA & feature engineering pipeline
├── app.py                           # Production Streamlit dashboard
├── requirements.txt                 # Pinned dependencies
├── .gitignore                       # Python / venv / VS Code / OS exclusions
└── README.md                        # You are here
```

### Two-Layer Design

| File | Role |
|------|------|
| `analysis.py` | Offline pipeline — data cleaning, feature engineering, aggregated EDA output printed to console |
| `app.py` | Live dashboard — cached data loading, sidebar filters, interactive Plotly charts, real-time KPI cards |

---

## 📊 Key Analytical Insights

### 1. 📈 Correct Global Profit Margin
Standard row-level averaging overstates profitability. This project computes the **true global margin**:
```
Global Margin = (Σ Profit / Σ Sales) × 100
```
This correctly weights large-revenue orders and exposes the real health of each segment.

### 2. 🗺️ Regional Performance Decomposition
Sales and profit are broken down by region alongside average discount rates — revealing which regions are discounting aggressively at the cost of margin vs. generating healthy organic growth.

### 3. 📅 Time-Series Trend Analysis
Order dates are decomposed into year and month components, enabling:
- Year-over-year revenue and profit comparison
- Seasonal peak identification
- Month-level drill-down within any filtered year range

### 4. 🛍️ Product Sub-Category Profitability Ranking
Categories are ranked by **total profit** (not sales), exposing cases where high-revenue sub-categories are net margin detractors — critical for inventory and pricing decisions.

---

## ⚙️ Tech Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| Language | Python | 3.11+ |
| Data Manipulation | Pandas | 2.2+ |
| Visualization | Plotly Express | 5.20+ |
| Dashboard Framework | Streamlit | 1.33+ |
| Data Format | CSV | — |

---

## 🛠️ Local Installation & Setup

### Prerequisites
- Python 3.9 or higher
- `pip` and `venv` (included with standard Python)
- Git

### Step 1 — Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/sales-analytics-dashboard.git
cd sales-analytics-dashboard
```

### Step 2 — Create & Activate Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
# Windows: .venv\Scripts\activate
```

### Step 3 — Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4 — Run the EDA Pipeline *(optional — validates the dataset)*
```bash
python analysis.py
```

### Step 5 — Launch the Dashboard
```bash
streamlit run app.py
```

The dashboard opens automatically at **http://localhost:8501** 🎉

---

## 🎛️ Dashboard Features

| Feature | Description |
|---------|-------------|
| 📅 Year Filter | Sidebar selectbox to isolate any fiscal year |
| 🌍 Region Filter | Multi-select to compare any combination of regions |
| 💰 KPI Cards | Real-time Total Sales, Total Profit, Quantity Sold, Avg Margin |
| 📈 Line Chart | Sales & Profit trend over time |
| 📊 Bar Chart | Total Sales by Region |
| 🥧 Pie Chart | Average Profit Margin distribution by Region |
| 📆 Yearly Comparison | Grouped Sales vs. Profit by year |

---

## 📂 Dataset

| Property | Details |
|----------|---------|
| **File** | `data/raw/raw-sales-data.csv` |
| **Records** | ~2,000 retail transactions |
| **Key Columns** | Order Date, Region, Category, Sub-Category, Sales, Quantity, Discount, Profit |
| **Source** | *(Document your data source here)* |

---

## 🗺️ Roadmap

- [ ] RFM (Recency, Frequency, Monetary) customer segmentation scatter plot
- [ ] Prophet-based trend forecasting for next-quarter sales projection
- [ ] Sub-category drill-down with margin waterfall chart
- [ ] Automated data refresh via scheduled pipeline
- [ ] Unit tests with `pytest` for EDA pipeline functions
- [ ] Docker deployment support

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

```bash
# Create a feature branch
git checkout -b feat/your-feature-name

# Commit your changes
git commit -m "feat: describe your change"

# Push and open a Pull Request
git push origin feat/your-feature-name
```

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for details.

---

## 👤 Author

**Mohammed Dahi**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/mohammeddahi/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/Mohammed-Dahi)

---

*Built with ❤️ using Python, Streamlit & Plotly*
