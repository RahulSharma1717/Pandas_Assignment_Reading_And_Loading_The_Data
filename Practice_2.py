# Load CSV data and store it into a dataframe.

import pandas as pd

df = pd.read_csv('sales_data.csv')
pd.set_option('display.max_columns', None)
print(df.head())


"""Output:
  Order_ID     Product  Quantity  Price_per_Unit  Total_Sales Sale_Date
0   ORD001      Laptop         2             800      1600.00  1/1/2023
1   ORD002      Mobile         1             500       500.56  1/2/2023
2   ORD003      Tablet         3             300       900.00  1/3/2023
3   ORD004  Headphones         1             100       100.00  1/4/2023
4   ORD005     Charger         5              20       100.00  1/5/2023
"""