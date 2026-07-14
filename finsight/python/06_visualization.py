import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data/processed/cleaned_transaction.csv")

# chart1
month_order=[
    'january','february','march','april'
    'May','June','July','August','September',
    'October','November','December'
]
monthly_amount=(
    df.groupby('MonthName')['Amount'].sum().reindex(month_order)
    )
plt.figure(figsize=(10,5))
plt.plot(monthly_amount.index, monthly_amount.values,marker="o")
plt.title("Monthly Transaction Amount")
plt.xlabel("Month")
plt.ylabel("Amount ($)")
plt.xticks(rotation=30)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(
    "dashboard_images/monthly_transaction_trend.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# chart2
location_amount=(
    df.groupby('Location')['Amount'].sum().sort_values(ascending=False)
)

plt.figure(figsize=(10,6))
location_amount.plot(kind='bar')
plt.title("Transaction Amount by Location")
plt.xlabel('location')
plt.ylabel('Amount ($)')
plt.tight_layout() 
plt.savefig(
    "dashboard_images/monthly_transaction_trend.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# chart3
transaction_type = df['TransactionType'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(
    transaction_type,
    labels=transaction_type.index,
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Purchase vs Refund")
plt.savefig(
    "dashboard_images/monthly_transaction_trend.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# chart4
fraud_location = (
    df[df['IsFraud'] == 1]
    .groupby('Location')
    .size()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,6))
fraud_location.plot(kind='bar')
plt.title("Fraud Transactions by Location")
plt.xlabel("Location")
plt.ylabel("Fraud Count")
plt.tight_layout()
plt.savefig(
    "dashboard_images/monthly_transaction_trend.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# chart5
hourly = df.groupby('hour').size()
plt.figure(figsize=(10,5))
plt.plot(hourly.index, hourly.values, marker='o')
plt.title("Transactions by Hour")
plt.xlabel("Hour")
plt.ylabel("Number of Transactions")
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(
    "dashboard_images/monthly_transaction_trend.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# chart6
daytype = df.groupby('DataType')['Amount'].sum()
plt.figure(figsize=(6,5))
daytype.plot(kind='bar')
plt.title("Weekday vs Weekend Spending")
plt.xlabel("Day Type")
plt.ylabel("Amount ($)")
plt.tight_layout()
plt.savefig(
    "dashboard_images/monthly_transaction_trend.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# Chart7 
plt.figure(figsize=(10,5))
plt.hist(
    df['Amount'],
    bins=30,
    edgecolor='black',
    linewidth=0.8
)
plt.title("Transaction Amount Distribution")
plt.xlabel("Transaction Amount ($)")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(
    "dashboard_images/monthly_transaction_trend.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()
