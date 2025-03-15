# Load the data from the html link.
# 1. Check the number of tables present on that page.
# 2. Print the sixth table.

import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_Friends_episodes"
tables = pd.read_html(url)

print(f"Number of tables found: {len(tables)}")
pd.set_option('display.max_columns', None)

if len(tables) >= 6:
    print("\nSixth table:")
    print(tables[5])
else:
    print("There are fewer than 6 tables on this page.")


"""Output:
Number of tables found: 17

Sixth table:
    No.overall  No. inseason                                       Title  \
0         98.0           1.0            "The One After Ross Says Rachel"   
1         99.0           2.0              "The One with All the Kissing"   
2        100.0           3.0                         "The One Hundredth"   
3        101.0           4.0            "The One Where Phoebe Hates PBS"   
4        102.0           5.0                     "The One with the Kips"   
5        103.0           6.0                     "The One with the Yeti"   
6        104.0           7.0               "The One Where Ross Moves In"   
7        105.0           8.0  "The One with the Thanksgiving Flashbacks"   
8        106.0           9.0               "The One with Ross' Sandwich"   
9        107.0          10.0     "The One with the Inappropriate Sister"   
10       108.0          11.0          "The One with All the Resolutions"   
11       109.0          12.0        "The One with Chandler's Work Laugh"   
12       110.0          13.0                   "The One with Joey's Bag"   
13       111.0          14.0         "The One Where Everybody Finds Out"   
14       112.0          15.0       "The One with the Girl Who Hits Joey"   
15       113.0          16.0                      "The One with the Cop"   
16       114.0          17.0    "The One with Rachel's Inadvertent Kiss"   
17       115.0          18.0               "The One Where Rachel Smokes"   
18       116.0          19.0            "The One Where Ross Can't Flirt"   
19       117.0          20.0               "The One with the Ride-Along"   
20       118.0          21.0                     "The One with the Ball"   
21       119.0          22.0             "The One with Joey's Big Break"   
22       120.0          23.0                          "The One in Vegas"   
23       121.0          24.0                          "The One in Vegas"   
24         NaN           NaN                                         NaN   

            Directed by                                         Written by  \
0       Kevin S. Bright                                       Seth Kurland   
1        Gary Halvorson                                        Wil Calhoun   
2       Kevin S. Bright                       David Crane & Marta Kauffman   
3        Shelley Jensen                                     Michael Curtis   
4   Dana DeVally Piazza                                      Scott Silveri   
5        Gary Halvorson                                        Alexa Junge   
6        Gary Halvorson                         Gigi McCreery & Perry Rein   
7       Kevin S. Bright                                  Gregory S. Malins   
8        Gary Halvorson                           Ted Cohen & Andrew Reich   
9   Dana DeVally Piazza                              Shana Goldberg-Meehan   
10        Joe Regalbuto  Story by : Brian BoyleTeleplay by : Suzie Vill...   
11      Kevin S. Bright                              Alicia Sky Varinaitis   
12         Gail Mancuso  Story by : Michael CurtisTeleplay by : Seth Ku...   
13      Michael Lembeck                                        Alexa Junge   
14      Kevin S. Bright                                         Adam Chase   
15          Andrew Tsao  Story by : Alicia Sky VarinaitisTeleplay by : ...   
16       Shelley Jensen                           Andrew Reich & Ted Cohen   
17         Todd Holland                                     Michael Curtis   
18         Gail Mancuso                                        Doty Abrams   
19       Gary Halvorson               Shana Goldberg-Meehan & Seth Kurland   
20       Gary Halvorson  Story by : Scott SilveriTeleplay by : Gregory ...   
21       Gary Halvorson  Story by : Shana Goldberg-MeehanTeleplay by : ...   
22      Kevin S. Bright                           Ted Cohen & Andrew Reich   
23      Kevin S. Bright                  Gregory S. Malins & Scott Silveri   
24                  NaN                                                NaN   

   Original release date  Prod.code U.S. viewers(millions) Rating/share(18–49)  
0     September 24, 1998   467651.0             31.12[163]        16.6/46[164]  
1        October 1, 1998   467652.0             25.36[165]        13.3/40[166]  
2        October 8, 1998   467653.0             26.82[167]                 NaN  
3       October 15, 1998   467654.0             24.09[168]        12.7/38[169]  
4       October 29, 1998   467655.0             25.87[170]        13.5/38[171]  
5       November 5, 1998   467656.0             24.99[172]        13.1/36[173]  
6      November 12, 1998   467657.0             24.44[174]        12.9/36[175]  
7      November 19, 1998   467659.0             23.92[176]        12.4/35[177]  
8      December 10, 1998   467658.0             23.03[178]        11.9/35[179]  
9      December 17, 1998   467661.0             23.67[180]        12.0/36[181]  
10       January 7, 1999   467660.0             27.02[182]        14.2/37[183]  
11      January 21, 1999   467663.0             24.82[184]        13.3/35[185]  
12      February 4, 1999   467662.0             24.92[186]        13.2/36[187]  
13     February 11, 1999   467664.0             27.70[188]        15.0/41[189]  
14     February 18, 1999   467665.0             29.31[190]        15.3/40[191]  
15     February 25, 1999   467666.0             26.02[192]        13.9/37[193]  
16        March 18, 1999   467667.0             24.48[194]        12.7/35[195]  
17         April 8, 1999   467668.0             21.88[196]        11.8/38[197]  
18        April 22, 1999   467669.0             20.85[198]        10.9/36[199]  
19        April 29, 1999   467670.0             19.63[200]        10.8/34[201]  
20           May 6, 1999   467671.0             20.92[202]        11.2/36[203]  
21          May 13, 1999   467672.0             21.28[204]        11.2/35[205]  
22       May 20, 1999[b]   467673.0             25.90[206]        14.2/42[207]  
23       May 20, 1999[b]   467674.0             25.90[206]        14.2/42[207]  
24                   NaN        NaN                    NaN                 NaN 
"""