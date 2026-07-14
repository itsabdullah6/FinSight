import pandas as pd
import numpy as np
df=pd.read_csv("data/raw/credit_card_fraud_dataset.csv")

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
