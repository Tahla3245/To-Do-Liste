t = []

with open("test.txt") as file:
    for line in file:
        line = line.replace("\n","")
        print(line)
        t.append(line)

print(t)

na = 0
un = 0
do = 0

for i in t:
    if i == "Name:":
        print("YAY!")