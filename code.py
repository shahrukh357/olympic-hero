# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data=pd.read_csv(path)
data.rename(columns={'Total': 'Total_Medals'}, inplace=True)
data.head(10)

#Code starts here



# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')

data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event'])
better_event=data['Better_Event'].value_counts().index[0]
print(better_event)



# --------------
#Code starts here
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries=top_countries.drop(146)
#print(top_countries.tail(3))
#t=top_countries.nlargest(10,'Total_Summer')['Country_Name']
#print(list(t))


def top_ten(x):
    country_list=[]
    country_list=list(top_countries.nlargest(10,x)['Country_Name'])
    return country_list

top_10_summer=top_ten('Total_Summer')
top_10_winter=top_ten('Total_Winter')
top_10=top_ten('Total_Medals')  

print(top_10_summer)
print(top_10_winter)
print(top_10) 
common=list(set(top_10)&set(top_10_summer)&set(top_10_winter))
print(common)



# --------------
#Code starts heresummer

summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]
#print(summer_df)
x=summer_df['Country_Name']
y=summer_df['Total_Summer'].sort_values()
plt.xlabel("Country Names ")
plt.ylabel("medals counts")
plt.bar(x,y)
plt.show()
a=winter_df['Country_Name']
b=winter_df['Total_Winter'].sort_values()
plt.bar(a,b)
plt.xlabel("Country Names ")
plt.ylabel("medals counts")
plt.show()
x=top_df['Country_Name']
y=top_df['Total_Summer'].sort_values()
plt.bar(x,y)
plt.xlabel("Country Names ")
plt.ylabel("medals counts")
plt.show()


# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=summer_df['Golden_Ratio'].max()
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
print(summer_max_ratio)
print(summer_country_gold)

winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=winter_df['Golden_Ratio'].max()
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
print(winter_max_ratio)
print(winter_country_gold)

top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=top_df['Golden_Ratio'].max()
top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']
print(top_max_ratio)
print(top_country_gold)


# --------------
#Code starts here
#print(data.tail(3))
data_1=data[:-1]
#print(data_1.tail(3))
data_1['Total_Points']=(data_1['Gold_Total']*3)+(data_1['Silver_Total']*2)+(data_1['Bronze_Total'])

most_points=data_1['Total_Points'].max()
best_country=data_1.loc[data_1['Total_Points'].idxmax(),"Country_Name"]
print(most_points)
print(best_country)


# --------------
#Code starts here
#print(data.columns)
best=data[data['Country_Name']==best_country]
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
#print(best.head())

best.plot(kind='bar',stacked=True)
plt.xlabel('United States')
plt.ylabel('Medas Tally')
plt.xticks(rotation=45)



