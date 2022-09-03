s = input()
t = s.lower()
a = [0 for _ in range(200)]

for i in t:
    if(i.isalpha()):
        a[ord(i)] += 1
for char, count in enumerate(a):
    if(count > 0):
        print(chr(char), count)
