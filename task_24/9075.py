f = open("24_9075.txt")
data = f.read().strip()

print(data[:100])

for i in range(0, 10, 2):
    data = data.replace(str(i), "0")
for i in range(1, 10, 2):
    data = data.replace(str(i), "1")

print(data[:100])

while "01" in data: data = data.replace("01", "0 1")
while "10" in data: data = data.replace("10", "1 0")

print(data[:100])

data = data.split()
l = list(len(i) for i in data)

print(max(l))
