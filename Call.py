import json

with open('Contents.json', 'r') as file:
  data = json.load(file)

print(data)
