from __future__ import annotations

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

TEMPLATE = "plotly_dark"
COLOR_SEQUENCE = ["#38bdf8", "#10b981", "#f59e0b", "#ef4444", "#a78bfa", "#22c55e", "#eab308"]


def bar_chart(data: pd.DataFrame, x: str, y: str, title: str, color: str | None = None) -> go.Figure:
    """Create a professional bar chart for segment comparisons."""
    fig = px.bar(
        data,
        x=x,
        y=y,
        color=color,
        title=title,
        template=TEMPLATE,
        color_discrete_sequence=COLOR_SEQUENCE,
    )
    fig.update_layout(margin=dict(l=20, r=20, t=60, b=40), title_x=0.02)
    return fig


def line_chart(data: pd.DataFrame, x: str, y: str, title: str, color: str | None = None) -> go.Figure:
    """Create a trend chart for vintage or performance monitoring."""
    fig = px.line(
        data,
        x=x,
        y=y,
        color=color,
        markers=True,
        title=title,
        template=TEMPLATE,
        color_discrete_sequence=COLOR_SEQUENCE,
    )
    fig.update_layout(margin=dict(l=20, r=20, t=60, b=40), title_x=0.02)
    return fig


def donut_chart(data: pd.DataFrame, names: str, values: str, title: str) -> go.Figure:
    """Create a donut chart where share of portfolio is the main question."""
    fig = px.pie(
        data,
        names=names,
        values=values,
        hole=0.58,
        title=title,
        template=TEMPLATE,
        color_discrete_sequence=COLOR_SEQUENCE,
    )
    fig.update_traces(textposition="inside", textinfo="percent+label")
    fig.update_layout(margin=dict(l=20, r=20, t=60, b=40), title_x=0.02)
    return fig


def histogram(data: pd.DataFrame, x: str, title: str, nbins: int = 40) -> go.Figure:
    """Create a distribution chart for risk or profitability diagnostics."""
    fig = px.histogram(
        data,
        x=x,
        nbins=nbins,
        title=title,
        template=TEMPLATE,
        color_discrete_sequence=["#38bdf8"],
    )
    fig.update_layout(margin=dict(l=20, r=20, t=60, b=40), title_x=0.02)
    return fig


def scatter_chart(data: pd.DataFrame, x: str, y: str, title: str, color: str | None = None, size: str | None = None) -> go.Figure:
    """Create a risk-return scatter plot for portfolio management decisions."""
    fig = px.scatter(
        data,
        x=x,
        y=y,
        color=color,
        size=size,
        title=title,
        template=TEMPLATE,
        color_discrete_sequence=COLOR_SEQUENCE,
        hover_data=data.columns,
    )
    fig.update_layout(margin=dict(l=20, r=20, t=60, b=40), title_x=0.02)
    return fig


def gauge(value: float, title: str, min_value: float = 0, max_value: float = 100) -> go.Figure:
    """Create a simple executive gauge for portfolio health."""
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            title={"text": title},
            gauge={
                "axis": {"range": [min_value, max_value]},
                "bar": {"color": "#38bdf8"},
                "steps": [
                    {"range": [0, 40], "color": "rgba(239, 68, 68, .35)"},
                    {"range": [40, 70], "color": "rgba(245, 158, 11, .35)"},
                    {"range": [70, 100], "color": "rgba(16, 185, 129, .35)"},
                ],
            },
        )
    )
    fig.update_layout(template=TEMPLATE, margin=dict(l=20, r=20, t=40, b=20), height=260)
    return fig
