## il esxiste des methodes read_pickle et to_pickle de pandas
## series.to_frame permet de convertir une series en dataframe

##prend un array en parametre en remplace les nan par des 0
np.nan_to_num()


## apres un groupby agg , drop du premier niveau du multilabel column et renommage
data = orders_products.groupby(['user_id', 'product_id']).agg({'user_id': 'size',
	                                                       'order_number': ['min', 'max'],
                                                               'add_to_cart_order': ['mean', 'median'],
                                                               'days_since_prior_order': ['mean', 'median'],
                                                               'order_dow': ['mean', 'median'],
                                                               'order_hour_of_day': ['mean', 'median'],
                                                               'add_to_cart_order_inverted': ['mean', 'median'],
                                                               'add_to_cart_order_relative': ['mean', 'median'],
                                                               'reordered': ['sum']})

data.columns = data.columns.droplevel(0)
data.columns = ['up_orders', 'up_first_order', 'up_last_order', 'up_mean_cart_position', 'up_median_cart_position',
                'days_since_prior_order_mean', 'days_since_prior_order_median', 'order_dow_mean',
                'order_dow_median',
                'order_hour_of_day_mean', 'order_hour_of_day_median',
                'add_to_cart_order_inverted_mean', 'add_to_cart_order_inverted_median',
                'add_to_cart_order_relative_mean', 'add_to_cart_order_relative_median',
                'reordered_sum']

#autre facon de se debarasser d'un multiIndex : passer l'index de ligne de dernier niveau en index de colonne
df.unstack()
