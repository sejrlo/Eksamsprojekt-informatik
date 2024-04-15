import json

data = json.loads("{\"request\": \"Register\", \"username\": \"testUser\", \"password\": \"t\", \"email\": \"fisk@tuta.io\"}")
print(data, type(data))