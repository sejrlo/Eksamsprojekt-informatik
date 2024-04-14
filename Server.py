import DatabaseManager as dm
import Table
import time

server_id = "12345"

def create_user(username, password, email):
    user = Table.Table("user", {
        "Username":username, 
        "DisplayName":username,
        "PasswordHash":password, 
        "CreationDate":round(time.time()*1000),
        "EmailAddress":email, 
        "Server":server_id
        })



def login(data, conn, call_back):
    user = Table.Table("user", {"username":data["username"], "passwordHash":data["password"]})
    if user != None:
        new_data = {"request":data["request"], "status":"success", "user":user}
        call_back(new_data, conn)
    
    else:
        new_data = {"request":data["request"], "status":"Username or password incorrect"}
        call_back(new_data, conn)

print("username:")
username = input("")

print("password:")
password = input("")

print("email:")
email = input("")

create_user(username, password, email)