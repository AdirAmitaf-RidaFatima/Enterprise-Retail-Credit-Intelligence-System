from __future__ import annotations

import streamlit as st

from components.ui import hero, insight_box, load_css
from services.data_loader import load_portfolio

st.set_page_config(
    page_title="Retail Credit Intelligence System",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)
load_css()

hero(
    "Enterprise Retail Credit Intelligence System",
    "A banking-grade decision support platform for PD, expected loss, expected return, borrower intelligence, and portfolio monitoring.",
)

st.markdown(
    """
This application converts the approved credit-risk modelling outputs into an enterprise-style banking portal. It is designed for executive management, credit risk analysts, underwriters, portfolio managers, and model validation teams.

The system follows the project methodology: **PD → risk band → expected loss → expected return → lending decision → portfolio monitoring**.
"""
)

try:
    df = load_portfolio()
    st.success(f"Scored portfolio loaded: {len(df):,} borrower records.")
except Exception as exc:  # pragma: no cover - user-facing fallback
    st.error(str(exc))
    st.stop()

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Executive Management")
    st.write("Portfolio health, exposure, risk mix, expected loss, and business actions.")
with col2:
    st.subheader("Credit & Underwriting")
    st.write("Borrower-level PD, decision recommendation, risk drivers, and credit memo outputs.")
with col3:
    st.subheader("Model Governance")
    st.write("Champion/challenger metrics, calibration, explainability, and monitoring views.")

insight_box(
    "Use the pages in the sidebar to move from executive portfolio view to borrower intelligence, simulator, model intelligence, monitoring, and exports.",
    kind="info",
)

st.markdown("---")
st.subheader("System Coverage Against Original Assignment")
st.dataframe(
    {
        "Requirement": [
            "Retail credit business understanding",
            "Borrower evaluation",
            "Facility and tenor analysis",
            "Probability of Default prediction",
            "Expected loss and potential return",
            "Decision support",
            "Model explainability",
            "Portfolio analytics",
        ],
        "Implemented In": [
            "Executive Dashboard / Insights",
            "Borrower Intelligence / Simulator",
            "Portfolio Analytics / Risk Monitoring",
            "Model outputs and scored portfolio",
            "Risk engine and KPI cards",
            "Approve / Conditions / Review / Decline logic",
            "Model Intelligence / reason-code proxy / SHAP plot",
            "Segmentation, drilldowns, exports",
        ],
    },
    use_container_width=True,
)
