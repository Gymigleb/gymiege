with open("./1_24.txt") as f:
    s = f.readline().strip()

cnt_M = 0
# s = "110W1111111WWWW001110WWWW11110WWWW"
# k = 4
k = 30

for i in "2468": s = s.replace(i, "0")
s = s.replace("0", " 0").split()
# print(s)

for i in s:
    # print(i)
    for j in range(len(i)+1):
        if i[:j].count("W") == k:
            cnt_M = max(cnt_M, len(i[:j]))
            # print("////", i[:j], len(i[:j]))
print(cnt_M)

# l = 0
# r = 0
# cnt_M = 0
# fstart = False
# # k = 30

# s = "110WWWW001110WWWW1111"
# k = 4
# while l < len(s) and  r <= len(s):
#     if s[l:r+1][0] in "02468":
#         print(cnt_M, " "*l,s[l:r+1])
#         if sum(s[l:r+1].count(i) for i in "02468") == 1:
#             if s[l: r].count("W") == k:
#                 cnt_M = max(cnt_M, r-l)
#             if s[l: r].count("W") > k:
#                 l = r
#         else:
#             if s[l: r].count("W") == k:
#                 cnt_M = max(cnt_M, r-l)
#             l = r
#     else:
#         l = r
#     r += 1
# print(cnt_M)