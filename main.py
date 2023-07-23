from pymongo import MongoClient

#Replace <uri> with ypur MonoDB Atlas connection string
uri="mongodb+srv://user2:user2@dsreactpy.cun0qwy.mongodb.net/"
client = MongoClient(uri)

#Replace <databse-name> with the name of your database
db=client["Database1"]

#Replace <collection-name> with the name of your collection
collection =db ["Database1"]

# check the connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

document = {"name":"Danial","age":36}

#Insert the document into the collection
insert_result = collection.insert_one(document)

#Print the ID of the inserted document
print("Inserted Document ID:", insert_result.inserted_id)

client.close()

