# app/plotting.py
"""
Functions that draw on a matplotlib Axes object. These are synchronous & Tk-safe.
"""

import numpy as np
import matplotlib.pyplot as plt

def draw_histogram(ax, values, title=None, bins=40):
    ax.clear()
    ax.hist(values, bins=bins, alpha=0.95)
    ax.set_title(title or "Histogram")
    ax.set_xlabel("Value")
    ax.set_ylabel("Count")

def draw_boxplot(ax, values, labels=None, title=None):
    ax.clear()
    kwargs = {}
    # Try newer API first
    try:
        kwargs["tick_labels"] = labels
        ax.boxplot(values, **kwargs)
    except TypeError:
        kwargs = {"labels": labels}
        ax.boxplot(values, **kwargs)
    if labels:
        ax.set_xticklabels(labels, rotation=30, ha="right")
    ax.set_title(title or "Boxplot")

def draw_scatter(ax, x, y, title=None, sample_limit=5000):
    ax.clear()
    n = len(x)
    if n > sample_limit:
        idx = np.random.choice(n, size=sample_limit, replace=False)
        x = x[idx]
        y = y[idx]
    ax.scatter(x, y, alpha=0.5, s=18)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title(title or "Scatter")

def draw_heatmap(ax, fig, df_numeric, title=None, vmin=-1, vmax=1):
    ax.clear()
    corr = df_numeric.corr()
    im = ax.imshow(corr.values, cmap="RdYlBu_r", vmin=vmin, vmax=vmax, aspect="auto")
    ax.set_xticks(range(len(corr.columns)))
    ax.set_yticks(range(len(corr.columns)))
    ax.set_xticklabels(corr.columns, rotation=30, ha="right", fontsize=10)
    ax.set_yticklabels(corr.columns, fontsize=10)
    ax.set_title(title or "Correlation Heatmap")
    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    return cbar
