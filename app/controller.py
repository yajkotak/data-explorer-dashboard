# app/controller.py
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import plotly.express as px

from .data_manager import load_dataset, validate_dataset

class Controller:
    def __init__(self, root, ui):
        self.root = root
        self.ui = ui
        self.df = None
        self.filtered = None
        self.heatmap_active = False

        self.fig, self.ax = plt.subplots(figsize=(9,5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.ui.plot_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        self.ui.load_btn.config(command=self.load_dataset)
        self.ui.apply_btn.config(command=self.plot)
        self.ui.export_btn.config(command=self.export)

        self.ax.text(0.5, 0.5, "Load a dataset to begin", ha="center", va="center", fontsize=16)
        self.canvas.draw()

    # ---------------- Data ----------------
    def load_dataset(self):
        path = self.ui.ask_open_file()
        if not path:
            return
        df = load_dataset(path)
        valid, info = validate_dataset(df)
        if not valid:
            messagebox.showerror("Invalid dataset", info["reason"])
            return

        self.df = df
        self.filtered = df.copy()

        numeric = info["numeric_columns"]
        self.ui.metric_cb["values"] = numeric
        if numeric:
            self.ui.metric_cb.set(numeric[0])

        self.ui.status_label.config(text=f"Loaded {len(df):,} rows | {df.shape[1]} columns")
        self.populate_table(df)
        self.plot()

    def populate_table(self, df):
        cols = list(df.columns[:12])
        self.ui.table["columns"] = cols
        for c in cols:
            self.ui.table.heading(c, text=c)
            self.ui.table.column(c, width=140)
        self.ui.table.delete(*self.ui.table.get_children())
        for _, row in df.head(200).iterrows():
            self.ui.table.insert("", "end", values=[row[c] for c in cols])

    # ---------------- Plot ----------------
    def plot(self):
        if self.df is None:
            return

        self.fig.clear()
        self.ax = self.fig.add_subplot(111)
        self.heatmap_active = False

        plot_type = self.ui.plot_cb.get()
        metric = self.ui.metric_cb.get()

        if plot_type == "Histogram":
            self.ax.hist(self.filtered[metric].dropna(), bins=40)
            self.ax.set_title(f"{metric} distribution")

        elif plot_type == "Boxplot":
            self.ax.boxplot(self.filtered[metric].dropna(), vert=True)
            self.ax.set_title(f"{metric} boxplot")

        elif plot_type == "Scatter":
            nums = self.filtered.select_dtypes(include="number").columns.tolist()
            if len(nums) < 2:
                messagebox.showwarning("Scatter", "Need ≥2 numeric columns")
                return
            x, y = nums[:2]
            self.ax.scatter(self.filtered[x], self.filtered[y], alpha=0.4)
            self.ax.set_xlabel(x)
            self.ax.set_ylabel(y)

        elif plot_type == "Grouped Comparison":
            cats = self.filtered.select_dtypes(include="object").columns.tolist()
            if not cats:
                messagebox.showwarning("Grouped", "No categorical column found")
                return
            g = cats[0]
            groups = self.filtered[g].value_counts().head(8).index
            data = [self.filtered[self.filtered[g]==v][metric].dropna() for v in groups]
            self.ax.boxplot(data, showfliers=False)
            self.ax.set_title(f"{metric} grouped by {g}")

        elif plot_type == "Correlation Heatmap":
            nums = self.filtered.select_dtypes(include="number")
            corr = nums.corr()
            im = self.ax.imshow(corr, cmap="RdYlBu_r", vmin=-1, vmax=1)
            self.ax.set_xticks(range(len(corr)))
            self.ax.set_yticks(range(len(corr)))
            self.ax.set_xticklabels(corr.columns, rotation=30)
            self.ax.set_yticklabels(corr.columns)
            self.fig.colorbar(im, ax=self.ax)
            self.heatmap_active = True

        self.canvas.draw()

    # ---------------- Export ----------------
    def export(self):
        path = self.ui.ask_save_file()
        if not path:
            return

        if path.endswith(".html"):
            # Interactive HTML export
            metric = self.ui.metric_cb.get()
            fig = px.histogram(self.filtered, x=metric, title=f"{metric} distribution")
            fig.write_html(path)
            messagebox.showinfo("Exported", f"Interactive HTML saved:\n{path}")
            return

        if path.endswith(".csv"):
            self.filtered.to_csv(path, index=False)
        elif path.endswith(".xlsx"):
            self.filtered.to_excel(path, index=False)
        else:
            self.filtered.to_parquet(path, index=False)

        messagebox.showinfo("Exported", f"Saved to:\n{path}")