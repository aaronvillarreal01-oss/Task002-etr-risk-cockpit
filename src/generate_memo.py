import pandas as pd


def generate_tax_review_memo(df: pd.DataFrame, output_file: str) -> None:
    """
    Generates a Markdown tax review memo based on the ETR risk review results.
    """

    total_entities = len(df)
    high_risk_count = len(df[df["risk_rating"] == "High"])
    medium_risk_count = len(df[df["risk_rating"] == "Medium"])
    low_risk_count = len(df[df["risk_rating"] == "Low"])

    below_15_count = len(
        df[(df["profit_before_tax"] > 0) & (df["total_etr"] < 0.15)]
    )

    unassigned_count = len(df[df["reviewer"] == "Unassigned"])

    high_risk_entities = df[df["risk_rating"] == "High"]

    memo = f"""# AI-Assisted ETR and Pillar Two Risk Review Memo

## 1. Executive Summary

This review covered {total_entities} legal entities across multiple regions. The risk engine identified:

- {high_risk_count} high-risk entities
- {medium_risk_count} medium-risk entities
- {low_risk_count} low-risk entities
- {below_15_count} entities with total ETR below 15%
- {unassigned_count} entities without an assigned reviewer

The review is intended to support tax risk identification, Pillar Two readiness, ETR review, and tax reporting controls.

## 2. Methodology

The tool applied deterministic tax controls to entity-level tax and accounting data. These controls reviewed indicators such as profit before tax, current tax expense, deferred tax expense, total tax expense, cash tax paid, statutory tax rate, covered taxes status, Pillar Two relevance, reviewer assignment, and review status.

AI-style reviewer comments were generated to explain the risk profile of each entity. These comments are not final tax advice. They are intended to support human review by the tax team.

The control design follows the principle:

**Deterministic rules calculate the risk. AI-style comments explain the risk. Human reviewers decide the final tax position.**

## 3. Key Risk Indicators

The following risk indicators were reviewed:

- Profit before tax with no tax expense
- Pillar Two relevant entities with total ETR below 15%
- Current tax expense missing or zero
- Missing or incomplete statutory tax rate data
- Covered taxes flag missing or marked as No
- Cash tax paid materially lower than current tax expense
- Loss-making entities with tax expense
- Missing reviewer assignment
- High-risk entities still pending review

## 4. High-Risk Entities

"""

    if high_risk_entities.empty:
        memo += "No high-risk entities were identified.\n\n"
    else:
        for _, row in high_risk_entities.iterrows():
            total_etr = row["total_etr"]

            if pd.isna(total_etr):
                etr_text = "N/A"
            else:
                etr_text = f"{total_etr:.1%}"

            memo += f"""### {row["entity_id"]} — {row["entity_name"]}

- Country: {row["country"]}
- Region: {row["region"]}
- Profit before tax: {row["profit_before_tax"]:,.0f}
- Total tax expense: {row["total_tax_expense"]:,.0f}
- Total ETR: {etr_text}
- Risk score: {row["risk_score"]}
- Triggered controls: {row["triggered_controls"]}
- Recommended next action: {row["next_action"]}

"""

    memo += """## 5. Recommended Actions

Based on the results, the tax team should consider the following actions:

1. Prioritize review of high-risk entities before reporting deadlines.
2. Validate entities with total ETR below 15% for possible Pillar Two exposure.
3. Reconcile entities with profit before tax but no tax expense.
4. Review covered taxes classification for entities marked as No or incomplete.
5. Assign reviewers to all pending high-risk and medium-risk entities.
6. Investigate material gaps between current tax expense and cash tax paid.
7. Document explanations for low ETR outcomes, including tax incentives, losses, deferred tax movements, permanent differences, and local tax attributes.

## 6. Limitations

This memo is generated from sample data and simplified tax control logic. It does not calculate a final Pillar Two effective tax rate and does not replace professional tax analysis. The purpose of the tool is to demonstrate how tax risk review can be supported through automation, structured controls, AI-assisted explanations, and human review workflow.

## 7. Conclusion

The AI-assisted ETR and Pillar Two Risk Cockpit provides a structured approach to identifying tax reporting risks across legal entities. The project demonstrates how tax teams can combine deterministic tax controls, risk scoring, reviewer workflow, and AI-assisted commentary to improve tax governance and reporting readiness.
"""

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(memo)