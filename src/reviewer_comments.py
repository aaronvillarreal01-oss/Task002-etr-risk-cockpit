import pandas as pd


def generate_reviewer_comment(row: pd.Series) -> str:
    """
    Generates a reviewer-style tax comment based on the entity's risk profile.
    """

    entity = row["entity_name"]
    country = row["country"]
    total_etr = row["total_etr"]
    statutory_rate = row["statutory_tax_rate"]
    risk_rating = row["risk_rating"]
    controls = row["triggered_controls"]
    pillar_two_relevant = row["pillar_two_relevant"]
    next_action = row["next_action"]

    if pd.isna(total_etr):
        etr_text = "not available because profit before tax is zero or missing"
    else:
        etr_text = f"{total_etr:.1%}"

    if pd.isna(statutory_rate):
        statutory_text = "not available"
    else:
        statutory_text = f"{statutory_rate:.1%}"

    if risk_rating == "High":
        comment = (
            f"{entity} in {country} has been classified as HIGH risk. "
            f"The entity shows a total ETR of {etr_text}, compared with a statutory tax rate of {statutory_text}. "
            f"The following controls were triggered: {controls}. "
        )

        if pillar_two_relevant == "Yes":
            comment += (
                "Because the entity is marked as Pillar Two relevant, the tax team should assess whether "
                "the low ETR or data-quality issue could affect top-up tax exposure, covered taxes, or reporting positions. "
            )

        comment += f"Recommended next action: {next_action}."

    elif risk_rating == "Medium":
        comment = (
            f"{entity} in {country} has been classified as MEDIUM risk. "
            f"The total ETR is {etr_text}, compared with a statutory tax rate of {statutory_text}. "
            f"The triggered controls indicate that the entity requires tax review, but the issue may be explainable "
            f"through timing differences, deferred tax, local tax attributes, or data-quality matters. "
            f"Recommended next action: {next_action}."
        )

    else:
        comment = (
            f"{entity} in {country} has been classified as LOW risk. "
            f"The total ETR is {etr_text}, compared with a statutory tax rate of {statutory_text}. "
            "No significant ETR or Pillar Two risk indicators were identified based on the current control logic. "
            "No immediate action is required, but the entity should remain subject to standard periodic review."
        )

    return comment


def add_reviewer_comments(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds reviewer comments to the risk register.
    """

    df = df.copy()
    df["reviewer_comment"] = df.apply(generate_reviewer_comment, axis=1)

    return df