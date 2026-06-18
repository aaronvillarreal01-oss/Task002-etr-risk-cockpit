import pandas as pd

from src.calculate_etr import calculate_etr_metrics
from src.risk_rules import apply_risk_rules
from src.ai_comments import add_reviewer_comments
from src.export_excel import export_risk_report
from src.generate_memo import generate_tax_review_memo


INPUT_FILE = "data/sample_entity_tax_data.csv"
OUTPUT_CSV = "outputs/etr_risk_register.csv"
OUTPUT_EXCEL = "outputs/etr_risk_report.xlsx"
OUTPUT_MEMO = "outputs/tax_review_memo.md"


def main():
    df = pd.read_csv(INPUT_FILE)

    df = calculate_etr_metrics(df)
    df = apply_risk_rules(df)
    df = add_reviewer_comments(df)

    columns_to_show = [
        "entity_id",
        "entity_name",
        "country",
        "profit_before_tax",
        "total_tax_expense",
        "statutory_tax_rate",
        "total_etr",
        "risk_score",
        "risk_rating",
        "triggered_controls",
        "next_action",
        "ai_reviewer_comment",
    ]

    risk_register = df[columns_to_show]

    print(risk_register)

    risk_register.to_csv(OUTPUT_CSV, index=False)
    export_risk_report(df, OUTPUT_EXCEL)
    generate_tax_review_memo(df, OUTPUT_MEMO)

    print(f"\nCSV risk register saved to: {OUTPUT_CSV}")
    print(f"Excel risk report saved to: {OUTPUT_EXCEL}")
    print(f"Tax review memo saved to: {OUTPUT_MEMO}")


if __name__ == "__main__":
    main()