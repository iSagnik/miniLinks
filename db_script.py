from pymongo import MongoClient
from pymongo.server_api import ServerApi

def connect_db(DB_PASSWORD):
    client_url = f"mongodb+srv://sagnik:{DB_PASSWORD}@minilinks.myi5o.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(client_url, server_api=ServerApi('1'))

    db = client.miniLinks.links
    return (client, db)

def insert_link(db, longURL, shortURL):
    data = {
        "longURL": longURL,
        "shortURL": shortURL
    }
    link_id = db.insert_one(data).inserted_id
    return link_id

def find_link(db, link, link_type):
    if link_type == "short":
        term = "shortURL"
    else:
        term = "longURL"    
    return db.find_one({term: link})



if __name__== "__main__":
    DB_PASSWORD = ""
    client, db = connect_db(DB_PASSWORD)
    # print(find_link(db, "hahaha", "short"))
    # print(find_link(db, "ebceibvueriybverobuh", "short"))
    # print(find_link(db, "http://localhost:5000/wocsa", "short"))
    print(find_link(db, "http://localhost:5000/ehwbewic", "short"))
    client.close()
