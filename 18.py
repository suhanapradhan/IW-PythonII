import json
data={ "name": "Suhana", "age":"21", }

with open("file.json", "w") as write:
    json.dump(data, write)

with open("file.json", "r") as read:
    a= json.load(read)
print(a)