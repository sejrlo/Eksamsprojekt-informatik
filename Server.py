import DatabaseManager as dm
import Table
import time
import bcrypt

server_id = "12345"

def register(data, conn, call_back):
    user = Table.get("user", {"username":data["username"]})
    if user != None: call_back(conn, {"request":data["request"], "status":"username taken"})
    salt = bcrypt.gensalt()
    print(salt)
    user = Table.Table("user", {
        "username":data["username"], 
        "displayname":data["username"],
        "passwordhash":bcrypt.hashpw(str.encode(data["password"]), salt), 
        "creationdate":round(time.time()*1000),
        "salt":salt,
        "emailaddress":data["email"] 
        })
    if user != None:
        call_back(conn, {"request":data["request"], "status":"success", "user":
                            {"id":user.get("id"), "username":user.get("username"), "displayname":user.get("displayname"), 
                            "creationdate":user.get("creationdate"), "email":user.get("emailaddress"), "server":server_id}
                            })



def login(data, conn, call_back):
    user = Table.get("user", {"username":data["username"]})
    if user.get("passwordhash") == bcrypt.hashpw(str.encode(data["password"]), user.get("salt")):
        new_data = {"request":data["request"], "status":"success", "user":user.data}
        call_back(conn, new_data)
    
    else:
        new_data = {"request":data["request"], "status":"Username or password incorrect"}
        call_back(conn, new_data)


def search(data, conn, call_back):
    call_back({"request":data["request"], "status":"success"}, conn)