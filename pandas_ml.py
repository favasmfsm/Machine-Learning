import pandas as pd
data= pd.DataFrame({'Country': ['Russia','Colombia','Chile','Equador','Nigeria'],
                    'Rank':[121,40,100,130,11]})

# print(data)
# print(data.describe())
# data.info()

data = pd.DataFrame({'group':['a', 'a', 'a', 'b','b', 'b', 'c', 'c','c'],'ounces':[4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

# print(data.sort_values(by=['group','ounces'],ascending=[True, False]))


data = pd.DataFrame({'k1':['one']*3 + ['two']*4, 'k2':[3,2,1,3,3,4,4]})


# print(data.sort_values(by='k2'))

print(data.drop_duplicates(subset='k1'))
