import pandas as pd

#Essentials 
#EXAMPLE 
inventory = pd.read_csv('inventory.csv')


#create a df with first ten rows if inventory
staten_island = inventory.iloc[:10]


#df with the 'product_description' col data
product_request = staten_island['product_description']


#df if product_type is 'seeds' AND location is 'Brooklyn'
seed_request = inventory[(inventory.product_type == 'seeds') & (inventory.location == 'Brooklyn')]


#in_stock is True if quantity more than 0 else False
inventory['in_stock'] = inventory['quantity'].apply(lambda x: True if x > 0 else False)


#total_value = price * quantity for each row (axis = 1)
inventory['total_value'] = inventory.apply(lambda r: r.price * r.quantity, axis = 1)


#full_description = text for each row (axis = 1)
combine_lambda = lambda r: '{} - {}'.format(r.product_type, r.product_description)
inventory['full_description'] = inventory.apply(combine_lambda, axis = 1)


