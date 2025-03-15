# Load the data of sheet 3 only from the above excel file.

import pandas as pd

df = pd.read_excel('sample_iowa_liquor_sales_sheets.xlsx', sheet_name='Sheet 3')
pd.set_option('display.max_columns', None)
print(df.head())


"""Output:
  Invoice/Item Number                 Date  Store Number  \
0        S28868100001  2015-09-11 00:00:00          2555   
1        S10699400047           02/20/2013          4794   
2        S23647700049           01/26/2015          4742   
3        S08792800017  2012-06-11 00:00:00          2459   
4        S04854100048  2012-03-04 00:00:00          2487   

                             Store Name                 Address  \
0            Hy-Vee Food Store / Keokuk               3111 MAIN   
1  Smokin' Joe's #17 Tobacco and Liquor  110 S ROOSEVELT HWY 61   
2  No Frills Supermarkets #786 / Counci        1817, W BROADWAY   
3                        Reinhart Foods     200 STATE PO BOX 98   
4                  Anamosa Family Foods           402 EAST MAIN   

             City  Zip Code  \
0          KEOKUK     52632   
1      BURLINGTON     52601   
2  COUNCIL BLUFFS     51501   
3  GUTHRIE CENTER     50115   
4         ANAMOSA     52205   

                                      Store Location  County Number  \
0   3111 MAIN\nKEOKUK 52632\n(40.414975, -91.403338)             56   
1  110 S ROOSEVELT HWY 61\nBURLINGTON 52601\n(40....             29   
2  1817, W BROADWAY\nCOUNCIL BLUFFS 51501\n(41.26...             78   
3        200 STATE PO BOX 98\nGUTHRIE CENTER 50115\n             39   
4  402 EAST MAIN\nANAMOSA 52205\n(42.108289, -91....             53   

          County   Category                       Category Name  \
0            Lee        NaN                                 NaN   
1     Des Moines  1082900.0  MISC. IMPORTED CORDIALS & LIQUEURS   
2  Pottawattamie  1062200.0    PUERTO RICO & VIRGIN ISLANDS RUM   
3        Guthrie  1062300.0                        FLAVORED RUM   
4          Jones  1081300.0                 PEPPERMINT SCHNAPPS   

   Vendor Number           Vendor Name  Item Number  \
0             65       Jim Beam Brands          237   
1            305               MHW Ltd        64000   
2             35  Bacardi U.S.A., Inc.        43128   
3             65       Jim Beam Brands        44499   
4            434        Luxco-St Louis        80578   

                 Item Description  Pack  Bottle Volume (ml)  \
0  Knob Creek w/ Crystal Decanter     3                1750   
1                         Absente    12                 750   
2            Bacardi Superior Rum     6                1750   
3                Cruzan Mango Rum    12                 750   
4       Arrow Peppermint Schnapps     6                1750   

   State Bottle Cost  State Bottle Retail  Bottles Sold  Sale (Dollars)  \
0              35.55                53.34             3          160.02   
1              21.67                32.50             4          130.00   
2              15.00                22.50            12          270.00   
3               6.82                10.24             3           30.72   
4               7.04                10.56             3           31.68   

   Volume Sold (Liters)  Volume Sold (Gallons)  
0                  5.25                   1.39  
1                  3.00                   0.79  
2                 21.00                   5.55  
3                  2.25                   0.59  
4                  5.25                   1.39  
"""
