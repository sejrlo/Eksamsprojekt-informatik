import json, bcrypt

data = json.dumps({"byte": b"sdfghjkl,.".hex()})
print(data)

txt = json.loads(data)
print(bytes.fromhex(txt["byte"]))

salt = bcrypt.gensalt()
hash = bcrypt.hashpw(str.encode("f"), salt)

print(len(hash))

salt = bcrypt.gensalt()
hash = bcrypt.hashpw(str.encode("f"*72), salt)

print(len(hash))