# data loading
import pandas as pd
import numpy as np


df=pd.read_csv("data/raw/credit_card_fraud_dataset.csv")
print(df.head())
print(df.tail())

print("\n Dataset Shape:")
print(df.shape)

print("\n Columns")
print(df.columns)

print("\n Data Types")
print(df.dtypes)

print("\n Missing values")
print(df.isnull().sum())

print("\n Duplicates Rows")
print(df.duplicated().sum())

print("\n Summary Statistics")
print(df.describe())

# feturing engineering
df['TransactionDate']=pd.to_datetime(df["TransactionDate"])
df['Date']=df["TransactionDate"].dt.date
df['Year']=df["TransactionDate"].dt.year
df['Month']=df["TransactionDate"].dt.month
df['MonthName']=df["TransactionDate"].dt.month_name()
df['Day']=df["TransactionDate"].dt.day
df['DayName']=df["TransactionDate"].dt.day_name()
df['hour']=df["TransactionDate"].dt.hour
# weekend/weekday
df['DataType']=np.where(
    df["TransactionDate"].dt.dayofweek>=5,
    "Weekend",
    "Weekday"

)
print("feature enginnering completed")
print(df.head())

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

# location analysis
location_transaction=(
    df.groupby('Location').size().sort_values(ascending=False)
)
print("------- TRANSACTION BY LOCATION ---------")
print("location transaction")

location_amount=(
    df.groupby('Location')['Amount'].sum().sort_values(ascending=False)

)

print("------ TOTAL AMOUNT BY LOCATION -------")
print(location_amount)

# fraud analysis by location
fraud_by_loc=(
    df[df['IsFraud']==1].groupby('Location').size().sort_values(ascending=False)
    )
print("-------- FRAUD TRANSACTION BY LOCATION --------")
print(fraud_by_loc)


# monthly transaction analysis
monthly_amount=(
    df.groupby('MonthName')['Amount'].sum()
)

month_order=[
    'january','february','march','april','May','June','July','August','September','October','November','December'
    ]

monthly_amount=monthly_amount.reindex(month_order)
print('------- MONTHLY TRANSACTION AMMOUNT --------')
print(monthly_amount)

# PEAK TRANSACTION HOURS
hourly_transactions=(
    df.groupby('Hour').size().sort_values(ascending=False)
)

print("-------- TRANSACTION BY HOUR -------")
print(hourly_transactions)