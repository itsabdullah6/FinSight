import pandas as pd
import numpy as np
df=pd.read_csv("data/raw/credit_card_fraud_dataset.csv")

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