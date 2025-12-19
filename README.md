# Data Explorer Dashboard

A **desktop exploratory data analysis (EDA) application** for working with large datasets locally.

**Data Explorer Dashboard** allows users to load CSV, Excel, or Parquet files and instantly explore their data using interactive visualizations — without writing any code.

The application is designed as a **professional, offline EDA tool**, similar in spirit to Tableau or Power BI, but lightweight, open-source, and fully local.

---

## 🚀 Features

### 📂 Dataset Support
- Load datasets in the following formats:
  - CSV (`.csv`)
  - Excel (`.xlsx`)
  - Parquet (`.parquet`)
- Automatically detects:
  - Numeric columns
  - Categorical columns
- Handles large datasets (100,000+ rows tested)

---

### 📊 Visualizations
- **Histogram**
  - Distribution of any numeric column
- **Boxplot**
  - Detect outliers and spread
- **Scatter Plot**
  - Numeric vs numeric comparison
- **Grouped Comparison**
  - Compare a numeric metric grouped by a categorical column
- **Correlation Heatmap**
  - Pearson correlation between numeric columns
  - Toggleable (no duplicated colorbars or UI bugs)

All plots update instantly and are optimized for exploratory analysis.

---

### 📋 Data Preview
- Built-in table view
- Displays the first rows of the dataset
- Useful for quick inspection and sanity checks

---

### 📤 Export Options
- Export the dataset to:
  - CSV
  - Excel
  - Parquet
- Export **interactive HTML visualizations**
  - Uses Plotly
  - Shareable with non-technical users
  - Opens in any browser

---

### 🖥 Desktop Application
- Native Windows desktop application (Tkinter)
- Can be distributed as a **single `.exe`**
- No Python installation required for end users
- Fully offline (no cloud, no tracking)

---

## 🖼 Screenshots

| Histogram | Heatmap | Grouped Comparison |
|----------|---------|-------------------|
| ![](examples/Screenshot%202025-12-19%20123210.png) | ![](examples/Screenshot%202025-12-19%20123228.png) | ![](examples/Screenshot%202025-12-19%20123247.png) |

---

## 🧠 How the Application Works

1. Launch the application
2. Load a dataset (CSV / Excel / Parquet)
3. The app automatically analyzes column types
4. Select:
   - A numeric metric
   - A visualization type
5. Visualizations update immediately
6. Export data or interactive charts if needed

The application focuses on **correct, explainable exploratory analysis**, not black-box machine learning.

---

## 📦 Download (Recommended)

### Windows Executable
You can download the **Windows executable** from the GitHub Releases page:

👉 **Releases → DataExplorer.exe**

- No Python required
- Single file
- Ready to run

---

## 🛠 Running from Source (Developers)

### Requirements
- Python 3.10+
- Windows (tested)

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the application:
```bash
python -m app.main
```

---

## 📁 Project Structure

```
data-explorer-dashboard/
│
├── app/                  # Application source code
│   ├── controller.py     # UI logic and plotting control
│   ├── data_manager.py   # Dataset loading and validation
│   ├── plotting.py       # Visualization helpers
│   ├── ui.py             # Tkinter UI layout
│   └── main.py           # Application entry point
│
├── run_app.py            # EXE-safe launcher for PyInstaller
├── examples/             # Screenshots used in README
├── requirements.txt
└── README.md
```

---

## 🔨 Building the Windows EXE

Install PyInstaller:
```bash
pip install pyinstaller
```

Build a single-file executable:
```bash
python -m PyInstaller --onefile --windowed --name DataExplorer -p . \
  --hidden-import plotly \
  --hidden-import plotly.express \
  --hidden-import pandas \
  --hidden-import matplotlib \
  run_app.py
```

The executable will be created at:
```
dist/DataExplorer.exe
```

---

## 🎯 Use Cases

- Exploratory data analysis for large datasets
- Quick inspection before modeling or reporting
- Teaching statistics and data visualization
- Offline analytics (no cloud dependencies)
- Sharing insights via interactive HTML exports

---

## 📜 License

MIT License — free to use, modify, and distribute.

---

## ✨ Author

**Yaj Kotak**  
Computer Science — Arizona State University

---

⭐ If you find this project useful, consider starring the repository on GitHub.
