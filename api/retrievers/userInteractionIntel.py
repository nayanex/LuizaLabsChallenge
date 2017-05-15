import pandas as pd
import math 

from .utils import get_connection, cook_sql_productsBought, cook_sql_AllLastViewedBeforeBuy

class UserInteractionIntel:
	def __init__(self):
		self._connection = get_connection()
	
	def getProductsBought(self):
		sql = cook_sql_productsBought()
		productsBought = pd.read_sql(sql, con=self._connection)
		return (productsBought.loc[0,'action'])

	def getAllLastViewBeforeBuy(self, user, product, time_of_action):
		sql = cook_sql_AllLastViewedBeforeBuy(user, product, time_of_action)
		mobilityColorMap = pd.read_sql(sql, con=self._connection)
		return (productsBought.loc[0,'at'])
