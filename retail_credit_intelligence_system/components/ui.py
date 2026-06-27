from __future__ import annotations

from pathlib import Path
from typing import Iterable

import streamlit as st


def load_css(path: str = "assets/styles.css") -> None:
    """Load project CSS if present; the app remains usable if CSS is missing."""
    css_path = Path(path)
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)


def hero(title: str, subtitle: str) -> None:
    """Render the page header with business context."""
    st.markdown(
        f"""
        <div class="bank-hero">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def metric_card(label: str, value: str, note: str = "") -> None:
    """Render a compact executive KPI card."""
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def insight_box(text: str, kind: str = "info") -> None:
    """Render a business insight block with a controlled visual hierarchy."""
    css_class = {
        "info": "insight-box",
        "warning": "warning-box",
        "danger": "danger-box",
    }.get(kind, "insight-box")
    st.markdown(f"<div class='{css_class}'>{text}</div>", unsafe_allow_html=True)


def page_caption(items: Iterable[str]) -> None:
    """Show concise user-facing context for the current page."""
    st.caption(" • ".join(items))


def format_currency(value: float, symbol: str = "$") -> str:
    """Format currency values in compact banking dashboard style."""
    try:
        value = float(value)
    except (TypeError, ValueError):
        return "N/A"
    abs_value = abs(value)
    if abs_value >= 1_000_000_000:
        return f"{symbol}{value / 1_000_000_000:,.2f}B"
    if abs_value >= 1_000_000:
        return f"{symbol}{value / 1_000_000:,.2f}M"
    if abs_value >= 1_000:
        return f"{symbol}{value / 1_000:,.1f}K"
    return f"{symbol}{value:,.0f}"


def format_pct(value: float) -> str:
    """Format ratios as percentages."""
    try:
        return f"{float(value):.2%}"
    except (TypeError, ValueError):
        return "N/A"
