import pandas as pd

df = pd.read_csv('/content/Smartphones_cleaned_dataset.csv')
df.info()

# 1. How many unique smarphone brands are present?

n = df['brand_name'].nunique()

print(f' These are {n} unique brands in the dataset')


#2 .what is the average price of smartphones?

a =  df['price'].mean()
print(f'the average price of all the smartphones is ₹ {round(a)}')

#3 .Which smartphone has the highest price?

name =  df[df['price'] == df['price'].max()]['brand_name'][427]

print(f'The smartphone with the higest price is {name}')

#4 . what is the most common processor

p =  df['processor_brand'].mode()[0]

print(f'The most common processor is {p} 🐉🐲')

#5 what is the average rating of smartphones?
a =  df['rating'].mean()
print(f'The average rating of smartphones is {round(a)} ')


#6 which brand has the most models listed?

df['brand_name'].value_counts().idxmax()

#7 Count of smarphones supporting 5G ?

n =  df['has_5g'].sum()
print(f'Count of smarphones supporting 5G is {n}')

#8 Average RAM across all the smartphones?

n = round(df['ram_capacity'].mean())

print(f' THe average RAM across all is {n}')

#9 Which phone has the largest battery?

df[df['battery_capacity'] == df['battery_capacity'].max()]['brand_name'][843]

#10 MOst commmon screen refresh rate?

df['refresh_rate'].mode()[0]

#11 what's the average number pf rear cameras?

round(df['num_rear_cameras'].mean())

#12 HOw many smarphones suppost fast charging?
df['fast_charging_available'].sum()

#13 What is the average processor speed?

df['processor_speed'].mean()


#14 Which OS is used by most smartphones?

df['os'].mode()[0]

#15 How namy smartphones have an IR blaster?

df['has_ir_blaster'].sum()

#16 What is the correlation between RAM and price?

df['ram_capacity'].corr(df['price'])


#17 Top 5 most expensive phones (brand + model) ?


df[['brand_name','model','price']].sort_values(by = 'price', ascending = False).head()


#18 Average front camera megapixels?

df['primary_camera_front'].mean()


#19 Do all smartphones support extended memory?

df.columns

df['extended_memory_available'].value_counts()

#20 Distribution of phones by resolution width?

df['resolution_width'].value_counts().head()
