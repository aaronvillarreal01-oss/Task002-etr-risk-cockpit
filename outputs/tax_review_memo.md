# ETR and Pillar Two Risk Review Memo

## 1. Executive Summary

This review covered 10 legal entities across multiple regions. The risk engine identified:

- 1 high-risk entities
- 4 medium-risk entities
- 5 low-risk entities
- 4 entities with total ETR below 15%
- 5 entities without an assigned reviewer

The review is intended to support tax risk identification, Pillar Two readiness, ETR review, and tax reporting controls.

## 2. Methodology

The tool applied deterministic tax controls to entity-level tax and accounting data. These controls reviewed indicators such as profit before tax, current tax expense, deferred tax expense, total tax expense, cash tax paid, statutory tax rate, covered taxes status, Pillar Two relevance, reviewer assignment, and review status.

Reviewer comments were generated to explain the risk profile of each entity. These comments are not final tax advice. They are intended to support human review by the tax team.

The control design follows the principle:

**Deterministic rules calculate the risk. Reviewer comments explain the risk. Human reviewers decide the final tax position.**

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

### MX001 â€” Mexico Distribution SA

- Country: Mexico
- Region: LATAM
- Profit before tax: 900,000
- Total tax expense: 0
- Total ETR: 0.0%
- Risk score: 120
- Triggered controls: ETR-001: Profit before tax exists but total tax expense is zero; ETR-002: Pillar Two relevant entity has total ETR below 15%; ETR-003: Profit before tax exists but current tax expense is zero; ETR-005: Covered taxes flag is missing or marked No; ETR-008: Reviewer is not assigned; ETR-009: High-risk entity remains pending review
- Recommended next action: Reconcile tax expense and confirm whether tax provision is missing; Perform Pillar Two top-up tax risk review; Validate current tax calculation and local tax return position; Confirm whether taxes qualify as covered taxes; Assign tax reviewer; Prioritize review before reporting deadline

## 5. Recommended Actions

Based on the results, the tax team should consider the following actions:

1. Prioritize review of high-risk entities before reporting deadlines.
2. Validate entities with total ETR below 15% for possible Pillar Two exposure.
3. Reconcile entities with profit before tax but no tax expense.
4. Review covered taxes classification for entities marked as No or incomplete.
5. Assign reviewers to all pending high-risk and medium-risk entities.
6. Investigate material gaps between current tax expense and cash tax paid.
7. Document explanations for low ETR outcomes, including tax incentives, losses, deferred tax movements, permanent differences, and local tax attributes.

## 6. Limitations

This memo is generated from sample data and simplified tax control logic. It does not calculate a final Pillar Two effective tax rate and does not replace professional tax analysis. The purpose of the tool is to demonstrate how tax risk review can be supported through automation, structured controls, automatically generated explanations, and human review workflow.

## 7. Conclusion

The ETR and Pillar Two Risk Cockpit provides a structured approach to identifying tax reporting risks across legal entities. The project demonstrates how tax teams can combine deterministic tax controls, risk scoring, reviewer workflow, and automatically generated commentary to improve tax governance and reporting readiness.
