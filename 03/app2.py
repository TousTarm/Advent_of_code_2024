import re
result = 0

with open("03/input","r") as file:
    string = file.read()

segments = []

string = string.split("do()")
for line in string:
    line = "do()" + str(line)
    new_line = line.split("don't()")
    for row in new_line:
        segments.append("don't()"+ str(row))
print(segments)

for line in segments:
    if ("don't()do()" in line):
        patern = r"mul\(\d+,\d+\)"
        for mul in re.findall(patern,line):
            mul_new = mul.split(",")
            num1 = ''.join([char for char in mul_new[0] if char.isdigit()])
            num2 = ''.join([char for char in mul_new[1] if char.isdigit()])
            result += int(num1) * int(num2)
print(result)
