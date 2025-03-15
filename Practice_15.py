# Create a JSON structure that takes input from user and store product id,name, price, and qty for 3 products and converts it into a data frame.

import pandas as pd
import json

product_dict = {'product_id': [], 'name': [], 'price': [], 'qty': []}
key_list = ['product_id', 'name', 'price', 'qty']

for _ in range(3):
    for key in key_list:
        user_input = input(f"Enter {key.title()} of product: ").title()
        product_dict[key].append(user_input)
    print()

print("Dictionary generated post 3 entries:")
print(product_dict)

json_data = json.dumps(product_dict, indent=4)
print("\nJSON Data:")
print(json_data)

df = pd.read_json(json_data)
print("\nDataFrame:")
print(df)


"""Output:
Enter Product_Id of product: 101
Enter Name of product: scones
Enter Price of product: 250
Enter Qty of product: 150

Enter Product_Id of product: 102
Enter Name of product: baguette
Enter Price of product: 159
Enter Qty of product: 120

Enter Product_Id of product: 103
Enter Name of product: muffins
Enter Price of product: 329
Enter Qty of product: 90

Dictionary generated post 3 entries:
{'product_id': ['101', '102', '103'], 'name': ['Scones', 'Baguette', 'Muffins'], 'price': ['250', '159', '329'], 'qty': ['150', '120', '90']}

JSON Data:
{
    "product_id": [
        "101",
        "102",
        "103"
    ],
    "name": [
        "Scones",
        "Baguette",
        "Muffins"
    ],
    "price": [
        "250",
        "159",
        "329"
    ],
    "qty": [
        "150",
        "120",
        "90"
    ]
}

DataFrame:
   product_id      name  price  qty
0         101    Scones    250  150
1         102  Baguette    159  120
2         103   Muffins    329   90
"""