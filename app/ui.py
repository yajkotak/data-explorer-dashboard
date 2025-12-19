# app/ui.py
import tkinter as tk
from tkinter import ttk, filedialog

class AppUI:
    def __init__(self, root):
        self.root = root
        root.title("Data Explorer Dashboard")
        root.geometry("1300x880")

        self.top = tk.Frame(root, bg="#F7F7F7", padx=8, pady=8)
        self.top.pack(fill="x")

        self.load_btn = ttk.Button(self.top, text="Load Dataset")
        self.load_btn.pack(side="left", padx=(6,10))

        self.status_label = ttk.Label(self.top, text="No dataset loaded")
        self.status_label.pack(side="left", padx=10)

        ttk.Label(self.top, text="Metric:", font=("Segoe UI", 10, "bold")).pack(side="left")
        self.metric_cb = ttk.Combobox(self.top, width=22)
        self.metric_cb.pack(side="left", padx=6)

        ttk.Label(self.top, text="Plot:", font=("Segoe UI", 10, "bold")).pack(side="left", padx=(6,0))
        self.plot_cb = ttk.Combobox(
            self.top,
            values=[
                "Histogram",
                "Boxplot",
                "Scatter",
                "Grouped Comparison",
                "Correlation Heatmap"
            ],
            width=28
        )
        self.plot_cb.set("Histogram")
        self.plot_cb.pack(side="left", padx=6)

        self.apply_btn = ttk.Button(self.top, text="Plot")
        self.apply_btn.pack(side="left", padx=6)

        self.export_btn = ttk.Button(self.top, text="Export")
        self.export_btn.pack(side="left", padx=6)

        # Plot area
        self.middle = tk.Frame(root)
        self.middle.pack(fill="both", expand=True, padx=10, pady=6)
        self.plot_frame = tk.Frame(self.middle)
        self.plot_frame.pack(side="left", fill="both", expand=True)

        # Table
        bottom = tk.Frame(root)
        bottom.pack(fill="both", padx=12, pady=(0,12))
        self.table = ttk.Treeview(bottom, show="headings", height=8)
        self.table.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(bottom, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

    def ask_open_file(self):
        return filedialog.askopenfilename(
            title="Open dataset",
            filetypes=[
                ("CSV","*.csv"),
                ("Excel","*.xlsx;*.xls"),
                ("Parquet","*.parquet"),
                ("All","*.*")
            ]
        )

    def ask_save_file(self):
        return filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[
                ("CSV","*.csv"),
                ("Excel","*.xlsx"),
                ("Parquet","*.parquet"),
                ("HTML","*.html")
            ]
        )
