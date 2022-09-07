arr3 = [1,2,3,4,5,6,7,8,9,10,11]
for i in range(0, 11):
    if i % 2 == 0:
        arr3.append(i)
    else:
        arr3.append(i * 2)
        print(arr3)