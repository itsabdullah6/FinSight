import pandas as pd
import numpy as np
df=pd.read_csv("data/raw/credit_card_fraud_dataset.csv")

# key performance indicators
total_transaction=len(df)
total_amount=df['Amount'].sum()
average_amount=df['Amount'].mean()
fraud_transaction=df["IsFraud"].sum()
fraud_rate=(fraud_transaction/total_transaction)*100
purchase_transaction=(df['TransactionType']=='purchase').sum()
refund_transaction=(df["TransactionType"]=='refund').sum()

print("-------------- KEY PERFORMANCE INDICATORS -------------")
print(f'Total Transactions      :{total_transaction:,}')
print(f"Total Amount            : ${total_amount:,.2f}")
print(f"Average Transaction     : ${average_amount:,.2f}")
print(f"Fraud Transactions      : {fraud_transaction:,}")
print(f"Fraud Rate              : {fraud_rate:.2f}%")
print(f"Purchase Transactions   : {purchase_transaction:,}")
print(f"Refund Transactions     : {refund_transaction:,}")
