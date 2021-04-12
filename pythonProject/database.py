import pymongo

def get_database():
    # init pymongo
    try:
        connection = pymongo.MongoClient(
            host="localhost",
            port=27017,
            serverSelectionTimeoutMS=1000
        )
        database = connection.brandi
        connection.server_info()  # trigger exception if cannot connect to db
        print("******************")
        print("Database connected")
        print("******************\n")
        return database
    except Exception as ex:
        print("******************")
        print("ERROR - Cannot connect to db")
        print(ex)
        print("******************\n")

