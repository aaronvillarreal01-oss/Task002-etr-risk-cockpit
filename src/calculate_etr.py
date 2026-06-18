import pandas as pd


def safe_divide(numerator, denominator):
    """
    Safely divides two numbers.
    Returns None if the denominator is zero or missing.
    """
    if pd.isna(denominator) or denominator == 0:
        return None
    return numerator / denominator


def calculate_etr_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates ETR-related metrics for each entity.
    """

    df = df.copy()

    df["current_etr"] = df.apply(
        lambda row: safe_divide(row["current_tax_expense"], row["profit_before_tax"]),
        axis=1
    )

    df["total_etr"] = df.apply(
        lambda row: safe_divide(row["total_tax_expense"], row["profit_before_tax"]),
        axis=1
    )

    df["cash_tax_rate"] = df.apply(
        lambda row: safe_divide(row["cash_tax_paid"], row["profit_before_tax"]),
        axis=1
    )

    df["tax_gap_to_statutory"] = df["statutory_tax_rate"] - df["total_etr"]

    return df