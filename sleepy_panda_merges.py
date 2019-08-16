import pandas as pd

visits = pd.read_csv('csv_merge_example\\visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('csv_merge_example\\cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('csv_merge_example\\checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('csv_merge_example\\purchase.csv',
                       parse_dates=[1])

#for x in [visits, cart, checkout, purchase]:
#  print(x.head())

#leftmerge for visits and cart
visitcart = pd.merge(visits, cart, how = 'left')

#df of cart_time with no value and percent of customers who proceeded from visit to cart
empty_visit = visitcart[visitcart['cart_time'].isnull()]
proceed_to_cart = 1 -(len(empty_visit)/float(len(visitcart)))

#same for 'from cart to checkout
cart_checkout = pd.merge(cart, checkout, how = 'left')
empty_cart = cart_checkout[cart_checkout['checkout_time'].isnull()]
proceed_to_checkout = 1- (len(empty_cart)/float(len(cart_checkout)))

#create one global df with leftmerge
all_data = visits
for x in [visits, cart, checkout, purchase]:
  all_data = pd.merge(all_data, x, how = 'left')

#counting total purchase time (from visit to purchase)
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
  
#counting percentage of proceeded from step1 to step2
def compare(text1, text2):
  proceed = 1-(len(all_data[all_data[text2].isnull()])/float(
    len(all_data[text1])))
  print('Percentage {} to {}: {}%'.format(text1, text2, round(proceed*100, 2)))
  return proceed

# % of visitors who actually bought something
print('percentage visit/bought: {}%'.format(round(1 - (
  compare('visit_time', 'cart_time')
+ compare('cart_time', 'checkout_time')
+ compare('checkout_time', 'purchase_time')), 3)*100))

#average time of purchase
print(all_data.time_to_purchase.mean())




