from Client_socket import Connection
import json

username = "test_user"
username = 33*"u"+"dmkmngksdg"
password = "test_password"
email = "test@test.test"

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

print("Disconnecting...")
new_connection.disconnect()