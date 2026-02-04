import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Data.csv')
#price baesed on location
location_price = df.groupby('Location')['Price_lakhs'].mean()
print("Price based on location",location_price)

#minimum price 
min_price = df.loc[df['Price_lakhs'].idxmin()]
print("Minimum price:", min_price)


#maximum price 
max_price = df.loc[df['Price_lakhs'].idxmax()]
print("Maximum price:", max_price)

plt.scatter(df['Area_sqft'], df['Price_lakhs'])
plt.xlabel('Area (sqft)')
plt.ylabel('Price (lakhs)')
plt.title('Area vs Price')
plt.show()

location_price.plot(kind='bar', title='Average Price by Location')
plt.xlabel('Location')
plt.ylabel('Average Price (lakhs)')
plt.show()