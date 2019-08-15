import pandas as pd
import numpy as np

#Aggregates (groupby().___.count().reset_index().pivot(
#                       columns = '', index = '', values = '').reset_index())
#EXAMPLE 
orders = pd.read_csv('orders.csv')


#creates new df with shoe_color and point at which price 25% of shoes lower than 75%
#and .reset_index() converts Series class into DataFrame
cheap_shoes = orders.groupby('shoe_color').price.apply(
    lambda x: np.percentile(x, 25)).reset_index()


#creates a new df with the combination shoe_type and shoe_color and NUMBER of
#these combinations in original df. converts to DF class
shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count(
    ).reset_index()


#rename the column 'id' into 'amount
shoe_counts = shoe_counts.rename(columns = {'id':'amount'})



#EXAMPLE 
user_visits = pd.read_csv('page_visits.csv')


#df click sources
click_source = user_visits.groupby('utm_source').id.count().reset_index()


#df click source and months and values
click_source_by_month = user_visits.groupby(
    ['utm_source', 'month']).id.count().reset_index()


#pivot new df
click_source_by_month_pivot = click_source_by_month.pivot(
    columns = 'month', index = 'utm_source', values = 'id').reset_index()



#EXAMPLE
ad_clicks = pd.read_csv('ad_clicks.csv')


#count how many views by source
views = ad_clicks.groupby('utm_source').day.count().reset_index()


# ~ == NOT .isnull() == null(nan) value.is_click in each row == was ad_click_timestamp null or not (True or False)
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()


#sources as rows, T/F cols and amount as value. pivoted as a new df + percent_clicked col
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

clicks_pivot = clicks_by_source.pivot(
    columns = 'is_click', index = 'utm_source', values = 'user_id').reset_index()

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + 
    clicks_pivot[False])


#pivot new df with experimental_groups (A/B) rows T/F cols and amount as value
ex_g = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count(
    ).reset_index().pivot(columns = 'is_click', index = 'experimental_group', values = 'user_id').reset_index()


#Series of DF for A and B experimental groups
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']

b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']


#Pivot two new DFs for A & B. days as rows, T/F as col, amount of A or B as val + percentage of A or B in total
a_pivot = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(
    columns = 'is_click', index = 'day', values = 'user_id').reset_index()

a_pivot['percentage'] = a_pivot[True] / (a_pivot[True]+a_pivot[False])

b_pivot = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(
    columns = 'is_click', index = 'day', values = 'user_id').reset_index()

b_pivot['percentage'] = b_pivot[True] / (b_pivot[True]+b_pivot[False])
