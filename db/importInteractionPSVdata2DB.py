import psycopg2
import csv

connection = psycopg2.connect("host='localhost' port='5432' dbname='luiza_labs' user='luiza_labs' password='luiza_labs'")

def isfloat(value):
	try:
		float(value)
		return True
	except ValueError:
		return False

def process_file(conn):
	cursor = conn.cursor()
	with open('userInteractionData/interactions.psv') as csvfile:
		spamreader = csv.reader(csvfile, delimiter='|')
		next(spamreader, None)  # skip the headers
		cursor.execute(
			"""PREPARE interactionplan (text, text, text, text, numeric, timestamp ) AS
			INSERT INTO interaction VALUES($1, $2, $3, $4, $5, $6) ON CONFLICT DO NOTHING;""")
		for row in spamreader:
			print(row)
			if (not(isfloat(row[4]))):
				row[4] = None
			if (row[1] == 'NULL'):
				row[1] = None
			if (row[5] == 'NULL'):
				row[5] = None	
			if "stwu=" in row[0]:
				row[0] = row[0].split('stwu=')[0].split(',')[0]
			if (row[0] == 'uid' or row[1] == 'pid' or row[2] == 'action' or row[3] == 'channel' or row[4] == 'price_at' or row[5] == 'at' or row[1] == 'NULL'):
				continue
			cursor.execute(
				"EXECUTE interactionplan(%s, %s, %s, %s, %s::float8, to_timestamp((%s::double precision)/ 1000));", (row)
				)
	conn.commit()
	cursor.close()

try:
	process_file(connection)
finally:
	connection.close()

#    0     1         2       3            4         5
#  (uid, pid,     action, channel,    price_at,   at)
#['uid', 'NULL', 'action', 'channel', 'price_at', 'NULL']
