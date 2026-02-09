line = [x for x in [10, 150, 160, 240, 250, 300]]
linex = [x+1 for x in [10, 150, 160, 240, 250, 300]]

def f(x):
    p = 10 <= x <= 150
    q = 160 <= x <= 250
    r = 240 <= x <= 300
    a = s <= x <= e
    return (q <= p) or ((not a) <= r)

out = []

for s in line:
    for e in line:
        if all(f(x) for x in linex):
            out += [e-s]

print(min(out), out)