
lists = [('Ella','Karki','24'),('Robin','Buffay','28'),('Isabella','Ripley','24')]
age = []
for i in range(len(lists)):
    age.append(lists[i][2])
print(age)
avg = sum(age)/len(age)
print(avg)

for i in range(len(lists)):
    if lists[i][2] > avg:
        print(lists[i][0] + " is old")
    else:
        print(lists[i][0] + " is young")
