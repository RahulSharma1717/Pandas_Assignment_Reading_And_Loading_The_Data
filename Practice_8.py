# Load the data from the above CSV file with the separator '-'

import pandas as pd

df = pd.read_csv('sales_data_new.csv', delimiter='-')
pd.set_option('display.max_columns', None)
print(df)


"""Output:
   Order_ID     Product  Quantity  Price_per_Unit  Total_Sales  Sale_Date
0    ORD001      Laptop         2             800      1600.00   1/1/2023
1    ORD002      Mobile         1             500       500.56   1/2/2023
2    ORD003      Tablet         3             300       900.00   1/3/2023
3    ORD004  Headphones         1             100       100.00   1/4/2023
4    ORD005     Charger         5              20       100.00   1/5/2023
5    ORD006      Laptop         2             800      1600.00   1/6/2023
6    ORD007      Tablet         1             300       300.00   1/7/2023
7    ORD008      Mobile         3             500      1500.00   1/8/2023
8    ORD009  Headphones         2             100       200.00   1/9/2023
9    ORD010     Charger         4              20        80.00  1/10/2023
10   ORD011      Laptop         1             800       800.00  1/11/2023
11   ORD012      Mobile         3             500      1500.00  1/12/2023
12   ORD013      Tablet         2             300       600.00  1/13/2023
13   ORD014  Headphones         1             100       100.00  1/14/2023
14   ORD015     Charger         5              20       100.00  1/15/2023
"""