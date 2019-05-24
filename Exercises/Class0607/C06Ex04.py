import json
file = [{'fname': 'Galab', 'occupation': 'Student'},(2, 4)]
print('Original Data: ', file)

with open('ouput.json', 'w') as output:
  json.dump(file, output)


