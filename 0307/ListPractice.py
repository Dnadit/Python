list = [1,2,3]
list[1] = 17
for i in range(4, 7):
    list.append(i)
list.pop(0)
list.sort()
list.insert(3, 25)
print(list)
