# data loading
import pandas as pd
import numpy as np
df=pd.read_csv("data/raw/credit_card_fraud_dataset.csv")

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
df['DayType']=np.where(
    df["TransactionDate"].dt.dayofweek>=5,
    "Weekend",
    "Weekday"

)

df.to_csv(
    "data/processed/cleaned_transaction.csv",
    index=False
)
print("cleaned data exported")