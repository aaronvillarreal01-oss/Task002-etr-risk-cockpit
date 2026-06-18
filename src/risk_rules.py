def apply_risk_rules(df):
    """
    Applies ETR and Pillar Two risk rules to each entity.
    Adds:
    - triggered_controls
    - risk_score
    - risk_rating
    - next_action
    """

    df = df.copy()

    triggered_controls_list = []
    risk_scores = []
    next_actions = []

    for _, row in df.iterrows():
        controls = []
        score = 0
        actions = []

        profit_before_tax = row["profit_before_tax"]
        total_tax_expense = row["total_tax_expense"]
        current_tax_expense = row["current_tax_expense"]
        total_etr = row["total_etr"]
        cash_tax_paid = row["cash_tax_paid"]
        statutory_tax_rate = row["statutory_tax_rate"]
        covered_taxes_flag = row["covered_taxes_flag"]
        pillar_two_relevant = row["pillar_two_relevant"]
        reviewer = row["reviewer"]
        review_status = row["review_status"]

        # ETR-001: Profit exists but no tax expense
        if profit_before_tax > 0 and total_tax_expense == 0:
            controls.append("ETR-001: Profit before tax exists but total tax expense is zero")
            score += 30
            actions.append("Reconcile tax expense and confirm whether tax provision is missing")

        # ETR-002: Pillar Two relevant entity below 15%
        if (
            pillar_two_relevant == "Yes"
            and profit_before_tax > 0
            and total_etr is not None
            and total_etr < 0.15
        ):
            controls.append("ETR-002: Pillar Two relevant entity has total ETR below 15%")
            score += 30
            actions.append("Perform Pillar Two top-up tax risk review")

        # ETR-003: Current tax expense missing or zero
        if profit_before_tax > 0 and current_tax_expense == 0:
            controls.append("ETR-003: Profit before tax exists but current tax expense is zero")
            score += 20
            actions.append("Validate current tax calculation and local tax return position")

        # ETR-004: Statutory tax rate missing
        if statutory_tax_rate is None:
            controls.append("ETR-004: Statutory tax rate is missing")
            score += 15
            actions.append("Update statutory tax rate master data")

        # ETR-005: Covered taxes flag missing or No
        if covered_taxes_flag != "Yes":
            controls.append("ETR-005: Covered taxes flag is missing or marked No")
            score += 20
            actions.append("Confirm whether taxes qualify as covered taxes")

        # ETR-006: Cash tax paid materially lower than current tax expense
        if current_tax_expense > 0 and cash_tax_paid < current_tax_expense * 0.5:
            controls.append("ETR-006: Cash tax paid is materially lower than current tax expense")
            score += 10
            actions.append("Review cash tax payment timing and tax payable balance")

        # ETR-007: Loss entity with tax expense
        if profit_before_tax < 0 and total_tax_expense > 0:
            controls.append("ETR-007: Loss entity has tax expense")
            score += 15
            actions.append("Review deferred tax, withholding tax, or non-deductible expense drivers")

        # ETR-008: Reviewer not assigned
        if reviewer == "Unassigned":
            controls.append("ETR-008: Reviewer is not assigned")
            score += 10
            actions.append("Assign tax reviewer")

        # ETR-009: High-risk item still pending
        if review_status == "Pending" and score >= 50:
            controls.append("ETR-009: High-risk entity remains pending review")
            score += 10
            actions.append("Prioritize review before reporting deadline")

        triggered_controls_list.append("; ".join(controls) if controls else "No controls triggered")
        risk_scores.append(score)
        next_actions.append("; ".join(actions) if actions else "No immediate action required")

    df["triggered_controls"] = triggered_controls_list
    df["risk_score"] = risk_scores
    df["next_action"] = next_actions

    df["risk_rating"] = df["risk_score"].apply(assign_risk_rating)

    return df


def assign_risk_rating(score):
    if score >= 50:
        return "High"
    elif score >= 21:
        return "Medium"
    else:
        return "Low"