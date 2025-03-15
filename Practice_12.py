# Create a dictionary from user input where the keys are product, price, quantity and convert that dictionary into a data frame.

import pandas as pd

user_dict = {}
keys_list = ['product', 'price', 'quantity']

for i in keys_list:
    dict_key = i
    value_list = []
    while True:
        value_input = input(f"Enter {dict_key}s separated by spaces: ")
        value_list = value_input.split()
        break
    user_dict[dict_key] = value_list

df = pd.DataFrame(user_dict)
print("\nThe DataFrame generated from user inputs:")
print(df)


"""Output:
Enter products separated by spaces: kitkat marshmallow froyo oreo eclair cupcake
Enter prices separated by spaces: 24 52 40 28 35 45
Enter quantitys separated by spaces: 60 40 25 30 20 25

The DataFrame generated from user inputs:
       product price quantity
0       kitkat    24       60
1  marshmallow    52       40
2        froyo    40       25
3         oreo    28       30
4       eclair    35       20
5      cupcake    45       25
"""