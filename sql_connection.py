from sql_alchemy import create_engine

conn_string = 'mysql://{user}:{password}@{host}:{port}'.format(
	user='root',
	password='bigredfuck',
	host='35.185.106.88',
	port=''
	)

engine = create_engine(conn_string)
con = engine.connect()

db_name = 'sightings'
create_db_query = "CREATE DATABASE IF NOT EXISTS {db} DEFAULT CHARACTER SET 'utf8'".format(db=db_name)

# Create a database
engine.execute(create_db_query)
