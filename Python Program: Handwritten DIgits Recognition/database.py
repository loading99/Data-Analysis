import logging


log = logging.getLogger()

log.setLevel('INFO')

handler = logging.StreamHandler()

handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))

log.addHandler(handler)

#from cassandra.cluster import Cluster

#from cassandra import ConsistencyLevel

from cassandra.cluster import Cluster

from cassandra.query import SimpleStatement


KEYSPACE = "mykeyspace"



#Create keyspace and table for first time
def createKeySpace(Raw_image, Result):

   cluster = Cluster(contact_points=['172.17.0.2'])

   session = cluster.connect()

   log.info("Creating keyspace...")

   try:
    session.execute("""

          CREATE KEYSPACE IF NOT EXISTS %s

          WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2' }

          """ % KEYSPACE)


    log.info("setting keyspace...")

    session.set_keyspace(KEYSPACE)

      
    log.info("creating table...")

    session.execute("""

      CREATE TABLE IF NOT EXISTS mytable0 (

          id int,

          Raw_image text,

          Result int,

          upload_time date,

          PRIMARY KEY (id,upload_time)
        )

        """)

    idlist=session.execute("""SELECT id from mytable0""")
    index=idlist[-1].id+1
    log.info('Add record')
    session.execute("""
      INSERT INTO mytable0
        (id,Raw_image,Result,upload_time)
        VALUES (%s,%s,%s,toDate(now()))
        """,
        (index,Raw_image,Result))
       
   except Exception as e:

       log.error("Unable to create keyspace")

       log.error(e)
