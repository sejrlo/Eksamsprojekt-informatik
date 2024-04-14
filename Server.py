import DatabaseManager as dm
import Table

def create_user(username, password, email):
    user = Table.Table("user", {"username":username, "password":password, "email":email})
    print(user)
    print(Table.get("user", {"username":username}))

print("username:")
username = input("")

print("password:")
password = input("")

print("email:")
email = input("")

create_user(username, password, email)