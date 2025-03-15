# Load Data from clipboard ( Copy top 30 rows from tips file).

import pandas as pd

df = pd.read_clipboard()
pd.set_option('display.max_columns', None)
print(df)


"""Output:
                                 import pandas                   as  pd
0                                    df      =  pd.read_clipboard() NaN
1  pd.set_option('display.max_columns',  None)                 None NaN
2                             print(df)   None                 None NaN
"""


"""Output:
  Order_ID     Product  Quantity  Price_per_Unit  Total_Sales  Sale_Date
0   ORD001      Laptop         2             800         1600 2023-01-01
1   ORD002      Mobile         1             500          500 2023-01-02
2   ORD003      Tablet         3             300          900 2023-01-03
3   ORD004  Headphones         1             100          100 2023-01-04
4   ORD005     Charger         5              20          100 2023-01-05
"""