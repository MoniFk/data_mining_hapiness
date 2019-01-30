import pandas as pd
import numpy as np
import pycountry

def valuation_formula(x):
	print(x)
	if x=='Bolivia' or x=='Congo (Brazzaville)' or x=='Congo (Kinshasa)' or x=='Czech Republic' or x=='Iran' or x=='Ivory Coast' or x=='Kosovo' or x=='Macedonia' or x=='Moldova' or x=='North Cyprus' or x=='Palestinian Territories' or x=='Russia' or x=='South Korea' or x=='Syria' or x=='Tanzania' or x=='Venezuela' or x=='Vietnam':
		return 'Unknown'
	else:
		return (pycountry.countries.get(name=x).alpha_3)
	#Bolivia

df = pd.read_csv('D:/STUDIA/ed/NASZ/data2017.csv')


df=pd.DataFrame(data=df)
df['country_code'] = df.apply(lambda row: valuation_formula(row['Country']), axis=1)

df.head()

#print(df)

#df=pd.DataFrame(data=df)
df.to_csv('data2017converted.csv')
