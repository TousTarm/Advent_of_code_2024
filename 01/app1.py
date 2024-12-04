arr1 = []
arr2 = []
result = 0

with open("01/input","r") as file:
    for row in file:
        row = list(map(int, row.split()))
        print(row)
        arr1.append(row[0])
        arr2.append(row[1])

arr1.sort()
arr2.sort()

for x in range(len(arr1)):
    diff = int(arr1[x]) - int(arr2[x])
    result += abs(diff)
print(result)