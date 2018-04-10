import pandas as pd

df = pd.read_csv('electronic-search-warrant-notifications.csv')

search_items = df['Items to be searched for:']

# Count number of instances of 'Location information'
count_locinfo = 0
for index_val, series_val in search_items.iteritems(): # iterate over ea row; row obj type is string
	for line in series_val.split('\n'): # split ea row by delimiter \n; iterate over each line
		print(line)		
		if line == 'Location information':
			count_locinfo += 1 
			print("There is Location Info in this cell!")
print(count_locinfo) # 341 instances of 'Location information'

# Modify df to only include rows with 'Location information'
new_df = df[df['Items to be searched for:'].str.contains('Location information') == True]
print(len(new_df)) # 347


# Write to csv file
new_df.to_csv('only-locinfo-rows.csv')

