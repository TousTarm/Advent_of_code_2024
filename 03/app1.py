result = 0

with open("03/input","r") as file:
    string = file.read()

# O HODINU POZDEJI MI DOSLO ZE MUZU PROSTE POUZIT REGEX

for x in range(1000):
    for y in range(1000):
        if ("mul("+str(x)+","+str(y)+")" in string):
            c = string.count("mul("+str(x)+","+str(y)+")")
            result += x * y * c
        print("searching:",x,y)
print(result)