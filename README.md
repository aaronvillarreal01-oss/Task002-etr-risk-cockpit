# Task002 â€” ETR & Pillar Two Risk Cockpit

## 1. Project Overview

This project is a tax technology prototype designed to support entity-level ETR and Pillar Two risk review.

The tool ingests sample tax/accounting data, calculates ETR-related metrics, applies deterministic tax control rules, assigns risk scores, generates reviewer-style comments, and exports audit-ready Excel and memo outputs.

The project demonstrates how international tax teams can combine automation, structured controls, reviewer-style explanation, and human review workflow to improve tax governance and reporting readiness.

Core design principle:

**Deterministic rules calculate the risk. Reviewer comments explain the risk. Human reviewers decide the final tax position.**

---

## 2. Business Problem

Tax teams often review ETR, tax expense, covered taxes, and Pillar Two risk indicators manually in Excel.

This creates several challenges:

* inconsistent review procedures;
* weak audit trail;
* difficulty prioritizing high-risk entities;
* limited visibility over reviewer ownership;
* manual preparation of tax review documentation;
* risk of missing low-ETR or data-quality issues.

This prototype addresses those issues by creating a structured, repeatable, and auditable first-level tax risk review workflow.

---

## 3. Solution

The tool performs the following steps:

1. Reads entity-level tax/accounting data.
2. Calculates ETR metrics.
3. Applies predefined tax control rules.
4. Assigns risk scores and risk ratings.
5. Generates reviewer-style comments.
6. Creates a CSV risk register.
7. Exports an Excel tax risk report.
8. Generates a tax review memo.

The tool is designed as a first-level review workflow, not as a final Pillar Two calculation engine.

---

## 4. Control Framework

The project uses a control-based approach.

Each tax risk indicator is linked to a control ID. This allows the review logic to be documented, tested, audited, and improved over time.

The control framework supports:

* traceability;
* repeatability;
* reviewer accountability;
* audit-ready documentation;
* consistent risk classification;
* tax governance and internal control review.

---

## 5. Architecture

```text
Entity-Level Tax / Accounting Data
        â†“
Data Ingestion Layer
        â†“
ETR Calculation Engine
        â†“
Deterministic Tax Control Rules
        â†“
Risk Scoring & Risk Rating
        â†“
Reviewer Workflow
        â†“
Reviewer Commentary
        â†“
Excel Risk Report + Tax Review Memo
        â†“
Human Tax Review / Final Tax Judgment
```

Project files:

```text
Task002-etr-risk-cockpit/
â”‚
â”œâ”€â”€ data/
â”‚   â””â”€â”€ sample_entity_tax_data.csv
â”‚
â”œâ”€â”€ outputs/
â”‚   â”œâ”€â”€ etr_risk_register.csv
â”‚   â”œâ”€â”€ etr_risk_report.xlsx
â”‚   â””â”€â”€ tax_review_memo.md
â”‚
â”œâ”€â”€ src/
â”‚   â”œâ”€â”€ calculate_etr.py
â”‚   â”œâ”€â”€ risk_rules.py
â”‚   â”œâ”€â”€ reviewer_comments.py
â”‚   â”œâ”€â”€ export_excel.py
â”‚   â””â”€â”€ generate_memo.py
â”‚
â”œâ”€â”€ main.py
â”œâ”€â”€ requirements.txt
â””â”€â”€ README.md
```

---

## 6. Input Data

The input file is:

```text
data/sample_entity_tax_data.csv
```

The dataset includes entity-level tax and accounting information such as:

* entity ID;
* entity name;
* country;
* region;
* revenue;
* profit before tax;
* current tax expense;
* deferred tax expense;
* total tax expense;
* cash tax paid;
* statutory tax rate;
* prior year losses;
* covered taxes flag;
* Pillar Two relevance flag;
* reviewer;
* review status;
* comments.

This sample data includes both normal and high-risk cases to demonstrate how the control engine works.

---

## 7. ETR Metrics Calculated

The ETR calculation engine calculates the following metrics:

```text
current_etr = current_tax_expense / profit_before_tax

total_etr = total_tax_expense / profit_before_tax

cash_tax_rate = cash_tax_paid / profit_before_tax

tax_gap_to_statutory = statutory_tax_rate - total_etr
```

The calculations are performed in:

```text
src/calculate_etr.py
```

The calculation layer is deterministic and transparent. It does not rely on AI to calculate tax metrics.

---

## 8. Tax Risk Controls

The tool applies the following tax controls:

| Control ID | Description                                                | Purpose                                              |
| ---------- | ---------------------------------------------------------- | ---------------------------------------------------- |
| ETR-001    | Profit before tax exists but total tax expense is zero     | Detect missing or incomplete tax provision           |
| ETR-002    | Pillar Two relevant entity has total ETR below 15%         | Identify possible Pillar Two top-up tax review items |
| ETR-003    | Profit before tax exists but current tax expense is zero   | Detect missing current tax calculation               |
| ETR-004    | Statutory tax rate is missing                              | Validate tax master data completeness                |
| ETR-005    | Covered taxes flag is missing or marked No                 | Validate covered tax classification                  |
| ETR-006    | Cash tax paid is materially lower than current tax expense | Identify cash tax/payment timing mismatches          |
| ETR-007    | Loss entity has tax expense                                | Review unusual loss/tax expense combinations         |
| ETR-008    | Reviewer is not assigned                                   | Ensure ownership of tax review                       |
| ETR-009    | High-risk entity remains pending review                    | Prioritize unresolved high-risk items                |

The control logic is implemented in:

```text
src/risk_rules.py
```

---

## 9. Risk Scoring

Each triggered control adds points to the entity risk score.

Risk ratings are assigned as follows:

```text
0â€“20 points = Low Risk
21â€“49 points = Medium Risk
50+ points = High Risk
```

The output includes:

* triggered controls;
* risk score;
* risk rating;
* recommended next action.

This allows the tax team to prioritize review based on objective control indicators.

---

## 10. Reviewer Comments

The project includes an reviewer commentary layer.

This layer generates reviewer-style explanations based on:

* entity name;
* country;
* calculated ETR;
* statutory tax rate;
* triggered controls;
* Pillar Two relevance;
* risk rating;
* recommended next action.

The comments are generated in:

```text
src/reviewer_comments.py
```

In the current version, the comments are template-based and deterministic. This allows the project to run without external API keys.

The design is intentionally controlled:

* reviewer comments explain the issue;
* deterministic rules calculate the risk;
* human reviewers make the final tax decision.

Future versions may replace the template-based commentary with a source-grounded LLM layer.

---

## 11. Outputs Generated

The tool generates three main outputs.

### 1. CSV Risk Register

```text
outputs/etr_risk_register.csv
```

This file contains the entity-level risk review results.

### 2. Excel Risk Report

```text
outputs/etr_risk_report.xlsx
```

The Excel file includes the following tabs:

| Tab                | Purpose                                                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| Summary            | Management-level overview of total entities, high-risk entities, average ETR, low-ETR entities, and unassigned reviewers |
| Risk Register      | Main entity-level tax risk review table                                                                                  |
| High Risk Entities | Filtered view of high-risk entities                                                                                      |
| Reviewer Queue     | List of items requiring review or follow-up                                                                              |
| Control Matrix     | Documentation of control IDs and control purposes                                                                        |

### 3. Tax Review Memo

```text
outputs/tax_review_memo.md
```

The memo summarizes:

* executive summary;
* methodology;
* key risk indicators;
* high-risk entities;
* recommended actions;
* limitations;
* conclusion.

---

## 12. How to Run the Project

From the project folder, activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Run the project:

```powershell
python main.py
```

After running the project, check the `outputs` folder for:

```text
etr_risk_register.csv
etr_risk_report.xlsx
tax_review_memo.md
```

---

## 13. Example Use Case

An international tax team receives entity-level tax reporting data during quarterly or annual close.

The tool performs a first-level review and identifies entities that may require additional tax analysis.

Example risk indicators include:

* entity has profit before tax but no tax expense;
* entity is Pillar Two relevant and has total ETR below 15%;
* covered taxes flag is missing or marked No;
* cash tax paid is materially lower than current tax expense;
* loss-making entity records tax expense;
* high-risk entity has no assigned reviewer.

The output helps the tax team prioritize review, document findings, and maintain a structured tax control workflow.

---

## 14. Limitations

This project is a prototype based on simplified sample data and simplified control logic.

It does not calculate final Pillar Two liability.

A full Pillar Two calculation engine would require additional data and logic, including:

* GloBE income adjustments;
* covered tax adjustments;
* jurisdictional blending;
* deferred tax recapture rules;
* substance-based income exclusion;
* safe harbour analysis;
* top-up tax allocation;
* local country-specific rules;
* source-verified technical analysis.

The current reviewer comments are not tax advice. They are reviewer-support comments generated from the available data and triggered controls.

---

## 15. Future Enhancements

Potential future enhancements include:

* Streamlit dashboard;
* real LLM integration;
* source-grounded RAG layer for country-specific tax context;
* YAML-based configurable tax control rules;
* enhanced Pillar Two safe harbour indicators;
* jurisdictional blending;
* user-uploaded Excel files;
* reviewer status update interface;
* audit log;
* Power BI dashboard;
* GitHub Actions testing workflow;
* unit tests for each control ID.

---

## 16. Disclaimer

This project is for portfolio and educational purposes only.

It is not intended to provide tax advice, calculate final tax liabilities, or replace professional tax review.

All outputs require human tax review and validation.

