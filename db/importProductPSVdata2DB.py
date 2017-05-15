import psycopg2
import csv

SQL_STATEMENT = """
    COPY %s FROM STDIN WITH
        CSV
        HEADER
        DELIMITER AS '|'
    """
	
my_file = open('userInteractionData/products.psv')

def process_file(conn, table_name, file_object):
	cursor = conn.cursor()
	cursor.copy_expert(sql=SQL_STATEMENT % table_name, file=file_object)
	conn.commit()
	cursor.close()

connection = psycopg2.connect("host='localhost' port='5432' dbname='luiza_labs' user='luiza_labs' password='luiza_labs'")

try:
    process_file(connection, 'product', my_file)
finally:
    connection.close()





