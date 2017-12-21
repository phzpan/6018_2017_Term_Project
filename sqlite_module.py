#
class sqlpro():
	""" SQLite module for reading and saving panda dataframe to database."""
	""" save_to_sqlite(sqlite_file, table_name): save dataframe to SQLite database."""
	""" read_from_sqlite(sqlite_file, table_name): read database into dataframe."""
	"""sqlite_file, table_name: database file name, and table name, string."""
		
	def __init__(self):
		"""init"""
		# self.sqlite_file = sqlite_file
		# self.table_name = table_name
	    
	def save_to_sqlite(sqlite_file, table_name):
		"""save dataframe to SQLite database."""
		import pandas as pd
		import sqlite3

		df = pd.read_csv("States.csv", delimiter=",")
		conn = sqlite3.connect(sqlite_file)

		df.to_sql(table_name, conn, if_exists="replace")
		conn.close()
		return None

	def read_from_sqlite(sqlite_file, table_name):
		"""read database into dataframe."""
		import pandas as pd
		import sqlite3
		try:    
			conn = sqlite3.connect(sqlite_file)

			query = """select * from """ + table_name
			df_sql = pd.read_sql(query, conn)
			df_sql = df_sql.drop('index', 1)
			#conn.commit()
		except:    
			pass
		finally:    
			if conn:
				conn.close()

		return df_sql
	    
	def __str__():
		txt = """SQLite3 module with save_to_sqlite and read_from_sqlite functions """
		return txt
    
