# Load data from HTML.

import pandas as pd

df = pd.read_html('https://en.wikipedia.org/wiki/List_of_Friends_episodes')     # df not following dataframe commands
pd.set_option('display.max_columns', None)
df = df[0]      # To select the first table from the list of tables and make df behave like a dataframe
print(df)


"""Output:
         Season     Episodes              Originally released                \
         Season     Episodes   Episodes.1      First released Last released   
0             1           24           24  September 22, 1994  May 18, 1995   
1             2           24           24  September 21, 1995  May 16, 1996   
2             3           25           25  September 19, 1996  May 15, 1997   
3             4           24           24  September 25, 1997   May 7, 1998   
4             5           24           24  September 24, 1998  May 20, 1999   
5             6           25           25  September 23, 1999  May 18, 2000   
6             7           24           24    October 12, 2000  May 17, 2001   
7             8           24           24  September 27, 2001  May 16, 2002   
8             9           24           24  September 26, 2002  May 15, 2003   
9            10           18           18  September 25, 2003   May 6, 2004   
10  The Reunion  The Reunion  The Reunion        May 27, 2021  May 27, 2021   

              Rank Rating Viewers (millions)  
    Network   Rank Rating Viewers (millions)  
0       NBC   8[3]   15.6               24.8  
1       NBC   3[4]   18.7               31.7  
2       NBC   4[5]   16.8               26.1  
3       NBC   4[6]   16.1               25.0  
4       NBC   2[7]   15.7               24.7  
5       NBC   5[8]   14.0               22.6  
6       NBC   5[9]   12.6               22.1  
7       NBC  1[10]   15.0               26.4  
8       NBC  2[11]   13.5               23.9  
9       NBC  5[12]   13.6               24.6  
10  HBO Max      —      —                  —  
"""