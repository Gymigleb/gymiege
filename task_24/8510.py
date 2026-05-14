with open("./files/24_8510.txt") as f:
    s = f.readline().strip()

s = s.replace("N", "*").replace("O", "*").replace("P", "*")
while "**" in s: s = s.replace("**", "* *")

s = s.split()

print(len(max(s, key=len)))