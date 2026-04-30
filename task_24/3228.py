with open("./files/24_3228.txt") as f:
    s = f.readline().strip()

s = " " + s + " "

for i in range(2):
    s = s.replace("AA", "A A")
    s = s.replace("BB", "B B")
    s = s.replace("CC", "C C")
    s = s.replace("BC", "B C")
    s = s.replace("CB", "C B")
    s = s.replace(" C", " C ")
    s = s.replace(" B", " B ")
    s = s.replace("A ", " A ")

s = s.split()

# print(s)

print(len(max(s, key=len))/2)