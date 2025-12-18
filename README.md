# DealDeskAnalyzer
Python-based Deal Desk Analyzer for pricing, margin analysis, and approval decisions
**## Decision Logic

Deals are evaluated based on Margin %:

- **AUTO APPROVE** → Margin ≥ 30%
- **FINANCE REVIEW** → Margin between 15% and 29.99%
- **REJECT** → Margin < 15%**
- 
