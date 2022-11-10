# %%
# Enter comma separated name together
name= input('Enter name: ')
L1= name.split(",")

# Enter comma separated marks together
marks= input('Enter marks: ')
marks_list= marks.split(",")

# String to integer conversion
L2 = []
for mark in marks_list:
    L2.append(int(mark))

# Print both list l1 for name, marks 
print(L1)
print(L2)

# declare dictionary variable d
d = {}

for index in range(0, len(L2), 1):
  if L2[index] >= 80:
    grade = "A"
  elif L2[index] >= 70:
    grade = "B"
  else:
    grade = "F"
  d[L1[index]] = ((L2[index]), grade)

print(d)

#%%
n = int(input("Enter the number of students: "))
res = {}
names = input().split(" ")
numbers = input().split(" ")
grades = input().split(" ")

for i in range(len(names)):
    res[names[i]] = (numbers[i], grades[i])

L1 = []
L2 = []
for key, value in res.items():
    L1.append(key)
    L2.append(value[0])

print(L1)
print(L2)

#%%

input1 = int(input())

n1 = 0
n2 = 1
cnt = 2
res = [0, 1]

if input1 == 0:
    print(0)
else:
    while True:
        tmp = n1 + n2
        n1 = n2
        n2 = tmp
        if n2 > input1:
            break
        res.append(n2)

    print(res)
