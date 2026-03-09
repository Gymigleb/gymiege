#24764

def table(simb, q):
    t = {("l", 0):("1", "Right", 1), ("0", 0):("0", "Right", 1), ("1", 0):("0", "Right", 1),
        ("l", 1):("2", "Right", 2), ("0", 1):("1", "Right", 2), ("1", 1):("1", "Right", 2),
        ("l", 2):("3", "Stop", 0), ("0", 2):("3", "Right", 0), ("1", 2):("3", "Right", 0)
       }
    return t[(simb, q)]

def machine(inpstr, pos, q):
    while True:
        print(pos < 0 or pos > len(inpstr) - 1, pos, len(inpstr) - 1)
        simb, comand, q = table(inpstr[pos], q)
        inpstr = inpstr[:pos] + simb + inpstr[pos+1:]
        if comand == "Nothing": pos = pos
        elif comand == "Stop": return inpstr
        elif comand == "Left": pos -= 1
        elif comand == "Right": pos += 1
        else:
            print(comand, "error unknown comand")
            exit(0)
        if pos < 0 or pos > len(inpstr) - 1:
            print(inpstr, pos, q, "error out of range")
            exit(0)

s = "l" + "01"*500 + "ll"
p = 1
s = machine(s, p, 0)
print(s)
print(sum(map(int, list(s[1:]))))