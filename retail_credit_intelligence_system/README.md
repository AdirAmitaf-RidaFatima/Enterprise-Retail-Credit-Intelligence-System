# Enterprise Retail Credit Intelligence System

A production-style Streamlit dashboard that converts banking-grade credit risk modelling outputs into a decision-support platform for retail credit risk, borrower intelligence, model governance, and portfolio monitoring.

## What this system demonstrates

- Retail credit business understanding
- Borrower-level credit assessment
- Probability of Default (PD) prediction output consumption
- Risk banding and lending recommendation logic
- Expected Loss and expected return estimation
- Facility, tenor, grade, geography, and decision segmentation
- Executive portfolio analytics
- Model performance, calibration, and explainability reporting
- Report exports for committees, audit, and demonstrations

## Project methodology

The application follows the approved project logic:

`Applicant / facility data → PD → risk band → expected loss → expected return → lending decision → dashboard monitoring`

The dashboard uses scored outputs generated in Phase 3 of the project. It does not retrain models inside the UI. This is intentional: enterprise banking systems separate model development, model validation, model deployment, and dashboard consumption.

## Folder structure

```text
retail_credit_intelligence_system/
├── app.py
├── pages/
├── components/
├── services/
├── utils/
├── config/
├── data/
├── reports/
├── plots/
├── models/
├── assets/
├── docs/
├── outputs/
└── screenshots/
```

## Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Required data

The app expects this file:

```text
data/scored_portfolio.csv
```

This package already includes a dashboard-ready scored portfolio sample.

## Pages

1. **Executive Dashboard** — portfolio KPIs, exposure, average PD, expected loss, expected return, risk distribution, facility mix, tenor mix, geography, portfolio health score.
2. **Borrower Intelligence** — borrower search, PD, risk band, expected loss, expected return, lending recommendation, risk drivers, credit memo export.
3. **Portfolio Analytics** — drill-down by facility, tenor, grade, purpose, employment, home ownership, geography, risk band, and decision.
4. **Credit Decision Simulator** — scenario testing for DTI, utilization, tenor, delinquency, loan amount, rate, and LGD.
5. **Model Intelligence** — champion/challenger model metrics, calibration, confusion matrices, feature importance, SHAP summary.
6. **Risk & Portfolio Monitoring** — expected loss concentration, high-risk exposure, negative-return exposure, vintage proxy, and management attention list.
7. **Executive Insights** — computed business insights and policy action candidates.
8. **Reports & Export** — CSV, Excel, committee summary, and model-report downloads.

## Deployment on Streamlit Community Cloud

1. Push this folder to GitHub.
2. Confirm `requirements.txt` is in the repository root.
3. Confirm `app.py` is in the repository root.
4. Keep the sample data below GitHub file-size limits. If the data file is too large, store it externally and update `services/data_loader.py`.
5. Deploy from Streamlit Community Cloud using `app.py` as the entry point.

## Governance note

This is a production-style educational prototype. It is not a live bank decision engine. A real bank would require full data lineage, access controls, model validation approval, audit logging, override management, privacy controls, KYC/AML integration, eCIB/bureau integration, and regulatory sign-off before production use.
