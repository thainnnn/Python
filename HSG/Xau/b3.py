s = input()

print(s.translate({ord(i) : None for i in "123456789"}))
