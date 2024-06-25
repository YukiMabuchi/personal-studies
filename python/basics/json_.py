import json

j = {
    "employee": [
        {"id": 1, "name": "Mike"},
        {"id": 2, "name": "Nancy"}
    ]
}

"""
Doc: https://docs.python.org/3/library/json.html

dump => Serialize obj as a JSON formatted stream to fp
dumps => Serialize obj to a JSON formatted str

load => Deserialize fp to a Python object
laods => Deserialize s (ste, bytes, ...) to a Python object
"""

jj = json.dumps(j) # encode
jj = json.loads(jj) # decode

with open('python/basics/test.json', 'w') as f:
    json.dump(j, f) # write into file

with open('python/basics/test.json', 'r') as f:
    print(json.load(f)) # read from file