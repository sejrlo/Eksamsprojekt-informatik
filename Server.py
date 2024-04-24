import DatabaseManager as dm
import Table
import time
import bcrypt

server_id = "12345"

def register(data, context):
    user = Table.get("user", {"username":data["username"]})
    if user != None:
        response = {"request":data["request"], "status":"username taken"}
        new_data = {"userID":user.get("id")}
        return new_data, response
    salt = bcrypt.gensalt()
    user = Table.Table("user", {
        "username":data["username"], 
        "displayname":data["username"],
        "passwordhash":bcrypt.hashpw(str.encode(data["password"]), salt), 
        "creationdate":round(time.time()*1000),
        "salt":salt,
        "emailaddress":data["email"] 
        })
    if user != None:
        response = {"request":data["request"], "status":"success"}
        new_data = {"userID": user.get("id")}
        return new_data, response
    
    else:
        response = {"request":data["request"], "status":"failed"}
        new_data = {}
        return new_data, response

def login(data, context):
    user = Table.get("user", {"username":data["username"]})
    if user == None: return {}, {"request":data["request"], "status":"Username or password incorrect"}
    if user.get("passwordhash") == bcrypt.hashpw(str.encode(data["password"]), user.get("salt")):
        response = {"request":data["request"], "status":"success"}
        new_data = {"userID": user.get("id")}
        return new_data, response
    
    else:
        response = {"request":data["request"], "status":"Username or password incorrect"}
        return {}, response

def create_media(data, context):
    if context["userid"] == -1:
        return {}, {"request":data["request"], "status": "Not logged in"}
    
    #Medie(~MedieID[ASCII]~, MedieNavn[Unicode], Beskrivelse[Unicode], OprettelsesDato[Timestamp], Data[Bytes], DataType[ASCII])
    Table.Table("media", {
        "medianame":data["medianame"],
        "description":data["description"],
        "creationdate":round(time.time()*1000),
        "data":data["data"],
        "datatype":data["datatype"]
    })
    return {}, {"request":data["request"], "status": "Media created"}


def get_media(data, context):
    media = Table.get("media", {"id":data["mediaid"]})
    if media != None:
        return {}, {"request":data["request"], "status":"fail"}
    else:
        return {}, {"request":data["request"], "status":"success","media": media.data}

def del_media(data, context):
    pass

def search(data, context):
    return {}, {"request":data["request"], "status":"success"}