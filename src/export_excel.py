import pandas as pd


def export_risk_report(df: pd.DataFrame, output_file: str) -> None:
    """
    Exports the ETR risk review results to an Excel file with multiple tabs.
    """

    summary = pd.DataFrame({
        "Metric": [
            "Total entities reviewed",
            "High-risk entities",
            "Medium-risk entities",
            "Low-risk entities",
            "Average total ETR",
            "Entities below 15% ETR",
            "Entities with unassigned reviewer",
        ],
        "Value": [
            len(df),
            len(df[df["risk_rating"] == "High"]),
            len(df[df["risk_rating"] == "Medium"]),
            len(df[df["risk_rating"] == "Low"]),
            round(df["total_etr"].dropna().mean(), 4),
            len(df[(df["profit_before_tax"] > 0) & (df["total_etr"] < 0.15)]),
            len(df[df["reviewer"] == "Unassigned"]),
        ],
    })

    risk_register_columns = [
        "entity_id",
        "entity_name",
        "country",
        "region",
        "profit_before_tax",
        "current_tax_expense",
        "deferred_tax_expense",
        "total_tax_expense",
        "cash_tax_paid",
        "statutory_tax_rate",
        "current_etr",
        "total_etr",
        "cash_tax_rate",
        "tax_gap_to_statutory",
        "pillar_two_relevant",
        "covered_taxes_flag",
        "risk_score",
        "risk_rating",
        "triggered_controls",
        "next_action",
        "ai_reviewer_comment",
        "reviewer",
        "review_status",
    ]

    risk_register = df[risk_register_columns]

    high_risk = risk_register[risk_register["risk_rating"] == "High"]

    reviewer_queue = risk_register[
        (risk_register["risk_rating"].isin(["High", "Medium"]))
        | (risk_register["review_status"] == "Pending")
    ]

    control_matrix = pd.DataFrame({
        "Control ID": [
            "ETR-001",
            "ETR-002",
            "ETR-003",
            "ETR-004",
            "ETR-005",
            "ETR-006",
            "ETR-007",
            "ETR-008",
            "ETR-009",
        ],
        "Control Description": [
            "Profit before tax exists but total tax expense is zero",
            "Pillar Two relevant entity has total ETR below 15%",
            "Profit before tax exists but current tax expense is zero",
            "Statutory tax rate is missing",
            "Covered taxes flag is missing or marked No",
            "Cash tax paid is materially lower than current tax expense",
            "Loss entity has tax expense",
            "Reviewer is not assigned",
            "High-risk entity remains pending review",
        ],
        "Purpose": [
            "Detect missing or incomplete tax provision",
            "Identify possible Pillar Two top-up tax exposure",
            "Detect missing current tax calculation",
            "Validate tax master data completeness",
            "Validate covered tax classification",
            "Identify cash tax/payment timing mismatches",
            "Review unusual loss/tax expense combinations",
            "Ensure ownership of tax review",
            "Prioritize unresolved high-risk items",
        ],
    })

    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        summary.to_excel(writer, sheet_name="Summary", index=False)
        risk_register.to_excel(writer, sheet_name="Risk Register", index=False)
        high_risk.to_excel(writer, sheet_name="High Risk Entities", index=False)
        reviewer_queue.to_excel(writer, sheet_name="Reviewer Queue", index=False)
        control_matrix.to_excel(writer, sheet_name="Control Matrix", index=False)