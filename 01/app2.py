arr1 = []
arr2 = []
result = 0

with open("01/input","r") as file:
    for row in file:
        row = list(map(int, row.split()))
        arr1.append(row[0])
        arr2.append(row[1])

arr1.sort()
arr2.sort()

for x in range(len(arr1)):
    if (arr1[x] in arr2):
        result += int(arr1[x]) * int(arr2.count(arr1[x]))
print(result)