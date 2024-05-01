from Client_socket import Connection
import os

username = "test_user"
password = "test_password"
email = "test@test.test"

media_path = os.path.join(os.path.dirname(__file__), "Client_Media")

#test_data = "424DBA000000000000008A0000007C0000000400000004000000010018000000000030000000232E0000232E000000000000000000000000FF0000FF0000FF000000000000004247527300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000FFFFFFFFFFFF000000FFFFFFFFFFFF000000FFFFFFFFFFFF000000FFFFFFFFFFFF000000FFFFFFFFFFFF000000"
test_file_name = "1"
test_file_type = "bmp"
test_file_description = "en billed test fil"
test_file_id = 5

with open(os.path.join(media_path, f"{test_file_name}.{test_file_type}"), "rb") as f:
        test_data = f.read().hex()

print("Connecting to DB...")
new_connection = Connection()

print("Create user...")
message = {"request":"Register", "username":username, "password":password, "email":email}
new_connection.send(message)

print("Receiving answer...")
answer = new_connection.receive()

print(f"Answer: {answer}")

print("Login with created user...")
message = {"request":"Login", "username":username, "password":password}
new_connection.send(message)

print("Receiving answer...")
answer = new_connection.receive()

print(f"Answer: {answer}")

print("Creating media...")
message = {"request":"Create_media", "medianame":test_file_name, "description":test_file_description, "datatype":test_file_type, "data":test_data}
new_connection.send(message)

print("Receiving answer...")
answer = new_connection.receive()

print(f"Answer: {answer}")

print("Creating media...")
message = {"request":"Get_media", "mediaid":test_file_name}
new_connection.send(message)

print("Receiving answer...")
answer = new_connection.receive()
if answer["status"] == "success":
        print(f"Got media {answer['medianame']}.{answer['datatype']}! ")
        with open(os.path.join(media_path, f"{answer['medianame']}.{answer['datatype']}"), "wb") as f:
                f.write(bytes.fromhex(answer["data"]))
else: 
        print("failed")


print("Searching for media...")
message = {"request":"Search", "search":test_file_id}
new_connection.send(message)

# print("Receiving answer...")
# answer = new_connection.receive()

print("Logging out...")

new_connection.send(message)

print("Receiving answer...")
answer = new_connection.receive()

print(f"Answer: {answer}")

print("Disconnecting...")
new_connection.disconnect()