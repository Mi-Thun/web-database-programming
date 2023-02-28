import pickle

a = {"name": "John", "age": 30,"city": "New York"}

with open('D:\\Education\\#CSE_479\\Lab_Project\\Lab_4\\file2.pickle', 'wb') as f:
    pickle.dump(a, f)

with open('D:\\Education\\#CSE_479\\Lab_Project\\Lab_4\\file2.pickle', 'rb') as dbfile:
    db = pickle.loads(dbfile.read())
    print(db)
