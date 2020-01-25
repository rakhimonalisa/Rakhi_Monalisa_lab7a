import pandas as pd
import os
path = "C:/Users/300997447/Desktop/Data Wirehouse/New folder/Chapter 2"
filename = 'titanic3.csv'
fullpath = os.path.join(path,filename)
## read
data_mayy = pd.read_csv(fullpath)
print (data_mayy.head(10))

import pandas as pd
data1_mayy = pd.read_csv('C:/Users/300997447/Desktop/Data Wirehouse/New folder/Chapter 2/Customer Churn Model.txt')
data1_mayy.columns.values
print(data1_mayy.columns.values)
data1_mayy.dtypes
for col in data1_mayy.columns: 
    print(col)

data=open('C:/Users/300997447/Desktop/Data Wirehouse/New folder/Chapter 2/Customer Churn Model.txt','r')
cols=data.readline().strip().split(',')
no_cols=len(cols)
print(no_cols)
#### Finding the nuber of rows
counter=0
main_dict={}
for col in cols:
    main_dict[col]=[]
    print(main_dict)
for line in data:
    values = line.strip().split(',')
    for i in range(len(cols)):
        main_dict[cols[i]].append(values[i])
    counter += 1
print ("The dataset has %d rows and %d columns" % (counter,no_cols))
import pandas as pd
df_mayy=pd.DataFrame(main_dict)
print (df_mayy.head(5))

import pandas as pd
medal_data_mayy=pd.read_csv('http://winterolympicsmedals.com/medals.csv')
print (medal_data_mayy.head(5))
