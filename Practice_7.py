# Load the data of sheet 4 only from the above excel file but it has 2 unused rows at the top.

import pandas as pd

df = pd.read_excel('sample_iowa_liquor_sales_sheets.xlsx', sheet_name='Sheet 4', skiprows=2)
pd.set_option('display.max_columns', None)
print(df.head(10))


"""Output:
  Invoice/Item Number                 Date  Store Number  \
0        S08894500006           11/13/2012          4443   
1        S06021200082  2012-12-06 00:00:00          3390   
2        S22996900012           12/17/2014          2413   
3        S23424900021  2015-12-01 00:00:00          4659   
4        S15431000148           10/30/2013          3820   
5        S21795200005           10/15/2014          5045   
6        S07441800045           08/30/2012          2529   
7        S03642100028           01/18/2012          3928   
8        S15364700018           10/28/2013          4121   
9        S09409900025  2012-11-12 00:00:00          4670   

                             Store Name              Address           City  \
0                        Palo Mini Mart          1204 1ST ST           PALO   
1                 Okoboji Avenue Liquor  1610 OKOBOJI AVENUE        MILFORD   
2                      Beecher Beverage     1691 ASBURY ROAD        DUBUQUE   
3  Casey's General Store #2802 / Conrad         409 E CENTER         CONRAD   
4           Charlie's Wine and Spirits,        507 W 19th St     SIOUX CITY   
5          Central Mart / Hamilton Blvd    800 HAMILTON BLVD     SIOUX CITY   
6    Hy-Vee Drugstore #4 / Cedar Rapids  4825 JOHNSON AVE NW   CEDAR RAPIDS   
7  Smokin' Joe's #12 Tobacco and Liquor   465 HWY 965 UNIT G  NORTH LIBERTY   
8                  Newport Bp / Wapello   13410 STATE HWY 78        WAPELLO   
9           Guppy's On The Go / Tripoli      600, 7TH AVE SW        TRIPOLI   

   Zip Code                                     Store Location  County Number  \
0     52324   1204 1ST ST\nPALO 52324\n(42.070316, -91.795808)             57   
1     51351  1610 OKOBOJI AVENUE\nMILFORD 51351\n(43.331525...             30   
2     52001  1691 ASBURY ROAD\nDUBUQUE 52001\n(42.500858, -...             31   
3     50621                       409 E CENTER\nCONRAD 50621\n             38   
4     51103  507 W 19th St\nSIOUX CITY 51103\n(42.510535, -...             97   
5     51103  800 HAMILTON BLVD\nSIOUX CITY 51103\n(42.50438...             97   
6     52405  4825 JOHNSON AVE NW\nCEDAR RAPIDS 52405\n(41.9...             57   
7     52317  465 HWY 965 UNIT G\nNORTH LIBERTY 52317\n(41.7...             52   
8     52653                13410 STATE HWY 78\nWAPELLO 52653\n             58   
9     50676  600, 7TH AVE SW\nTRIPOLI 50676\n(42.802375, -9...              9   

      County  Category                       Category Name  Vendor Number  \
0       Linn   1062310                          SPICED RUM            260   
1  Dickinson   1011200           STRAIGHT BOURBON WHISKIES             55   
2    Dubuque   1012100                   CANADIAN WHISKIES            260   
3     Grundy   1031080                      VODKA 80 PROOF            260   
4   Woodbury   1012210                  SINGLE MALT SCOTCH            305   
5   Woodbury   1011100                    BLENDED WHISKIES            297   
6       Linn   1071100                  AMERICAN COCKTAILS             55   
7    Johnson   1031080                      VODKA 80 PROOF             55   
8     Louisa   1082900  MISC. IMPORTED CORDIALS & LIQUEURS            192   
9     Bremer   1062200    PUERTO RICO & VIRGIN ISLANDS RUM             35   

                  Vendor Name  Item Number                  Item Description  \
0             Diageo Americas        43336    Captain Morgan Original Spiced   
1       Sazerac North America        21596                          Ten High   
2             Diageo Americas        11297       Crown Royal Canadian Whisky   
3             Diageo Americas        37991        Smirnoff Vodka 80 Prf Mini   
4                     MHW Ltd         5516  Macallan 18yr Single Malt Scotch   
5           Laird And Company        23827                         Five Star   
6       Sazerac North America        57148     Chi-Chi's Margarita W/tequila   
7       Sazerac North America        37934                        Skol Vodka   
8  Sidney Frank Importing Co.        65253              Jagermeister Liqueur   
9        Bacardi U.S.A., Inc.        43126              Bacardi Superior Rum   

   Pack  Bottle Volume (ml)  State Bottle Cost  State Bottle Retail  \
0    12                 750               8.50                12.74   
1    12                 750               4.00                 5.99   
2    12                1000              18.50                27.75   
3    12                 500               7.47                11.21   
4    12                 750              99.95               149.92   
5    12                1000               4.40                 6.60   
6     6                1750               6.49                 9.74   
7    24                 375               1.74                 2.60   
8    48                 200               3.50                 5.26   
9    12                 750               7.53                11.30   

   Bottles Sold  Sale (Dollars)  Volume Sold (Liters)  Volume Sold (Gallons)  
0            12          152.88                  9.00                   2.38  
1            12           71.88                  9.00                   2.38  
2            24          666.00                 24.00                   6.34  
3             1           11.21                  0.50                   0.13  
4             2          299.84                  1.50                   0.40  
5            12           79.20                 12.00                   3.17  
6            12          116.88                 21.00                   5.55  
7             2            5.20                  0.75                   0.20  
8             3           15.78                  0.60                   0.16  
9             2           22.60                  1.50                   0.40  
"""