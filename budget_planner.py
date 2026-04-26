# Budget Planner & Forecasting Tool

import csv
from collections import defaultdict

def load_transactions(filepath):
    transactions = []
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            transactions.append({
                'month': row['month'],
                'category': row['category'],
                'type': row['type'],       # income or expense
                'amount': float(row['amount'])
            })
    return transactions

def monthly_summary(transactions):
    summary = defaultdict(lambda: {'income': 0, 'expense': 0})
    for t in transactions:
        summary[t['month']][t['type']] += t['amount']
    return summary

def forecast_next_month(summary):
    months = sorted(summary.keys())
    if len(months) < 2:
        print("Need at least 2 months of data to forecast.")
        return
    expenses = [summary[m]['expense'] for m in months]
    avg_change = (expenses[-1] - expenses[0]) / (len(expenses) - 1)
    forecast = expenses[-1] + avg_change
    print(f"\nForecast for next month's expenses: ₹{forecast:.2f}")

def print_report(summary):
    print("\n--- Monthly Budget Report ---")
    for month in sorted(summary.keys()):
        income = summary[month]['income']
        expense = summary[month]['expense']
        net = income - expense
        print(f"{month}: Income ₹{income:.2f} | Expenses ₹{expense:.2f} | Net ₹{net:.2f}")

if __name__ == "__main__":
    transactions = load_transactions("sample_data/sample_budget.csv")
    summary = monthly_summary(transactions)
    print_report(summary)
    forecast_next_month(summary)
