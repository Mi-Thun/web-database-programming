import json

x = {"name": "John", "age": 30,"city": "New York"}

xJSON = json.dumps(x)
print(xJSON)
print(type(xJSON))

with open("D:\\Education\\#CSE_479\\Lab_Project\\Lab_4\\file1.txt", "a") as file:
    file.write(xJSON)

with open("D:\\Education\\#CSE_479\\Lab_Project\\Lab_4\\file1.txt", "r") as f:
    y1 = f.readline()
    print(y1)
    aDict = json.loads(y1)
    print(aDict)
    print(type(aDict))
