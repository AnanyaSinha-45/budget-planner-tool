# Data Flow Diagram — Budget Planner Tool

## Level 0 (Context Diagram)
User → [Budget Planner System] → Budget Report & Forecast

## Level 1 (Main Processes)
1. Input Handling — reads transaction data from CSV
2. Categorisation — groups by month and category
3. Summary Generation — calculates income, expense, and net balance
4. Forecasting — estimates next month using trend analysis
5. Report Output — prints a formatted monthly report

## Data Stores
- D1: Transaction CSV file (input)
- D2: Monthly summary dictionary (in-memory)

## External Entities
- User (provides data, receives report)
