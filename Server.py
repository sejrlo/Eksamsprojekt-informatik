import DatabaseManager as dm
import Table
import time
import bcrypt
import os

server_id = "12345"

media_path = os.path.join(os.path.dirname(__file__), "Media")

def register(data, context):
    user = Table.get("user", {"username":data["username"]})
    if user != None:
        response = {"request":data["request"], "status":"username taken"}
        new_data = {"userid":user.get("id")}
        return new_data, response
    salt = bcrypt.gensalt()
    
    d = {
        "username":data["username"], 
        "displayname":data["username"],
        "passwordhash":bcrypt.hashpw(str.encode(data["password"]), salt).hex(), 
        "creationdate":round(time.time()*1000),
        "salt":salt.hex(),
        "emailaddress":data["email"] 
        }
    #print(1, d)
    user = Table.Table("user", d)
    if user != None:
        response = {"request":data["request"], "status":"success", "username":user.get("username"), "displayname": user.get("displayname")}
        new_data = {"userid": user.get("id")}
        return new_data, response
    
    else:
        response = {"request":data["request"], "status":"failed"}
        new_data = {}
        return new_data, response

def login(data, context):
    user = Table.get("user", {"username":data["username"]})
    if user == None: return {}, {"request":data["request"], "status":"Username or password incorrect"}
    print(user.data.keys())
    if bytes.fromhex(user.get("passwordhash")) == bcrypt.hashpw(str.encode(data["password"]), bytes.fromhex(user.get("salt"))):
        response = {"request":data["request"], "status":"success", "username":user.get("username"), "displayname":user.get("displayname"),}
        new_data = {"userid": user.get("id")}
        return new_data, response
    
    else:
        response = {"request":data["request"], "status":"Username or password incorrect"}
        return {}, response

def create_media(data, context):
    if context["userid"] == -1:
        return {}, {"request":data["request"], "status": "Not logged in"}
    
    media = Table.Table("media", {
        "medianame":data["medianame"],
        "description":data["description"],
        "creationdate":round(time.time()*1000),
        "datatype":data["datatype"], 
        "ownerid":context["userid"]
    })
    with open(os.path.join(media_path, f"{media.get('id')}.{media.get('datatype')}"), "wb") as f:
        f.write(bytes.fromhex(data["data"]))
    
    return {}, {"request":data["request"], "status": "Media created"}

def get_media(data, context):
    media = Table.get("media", {"id":data["mediaid"]})
    if media != None:
        with open(os.path.join(media_path, f"{media.get('id')}.{media.get('datatype')}"), "rb") as f:
            return {}, {"request":data["request"], "status":"success", "data":f.read().hex(), "datatype":media.get("datatype"), "medianame":media.get("medianame")}
    else:
        return {}, {"request":data["request"], "status":"fail"}

def del_media(data, context):
    pass

def search(data, context):
    return {}, {"request":data["request"], "status":"success"}