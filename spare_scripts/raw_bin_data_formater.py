data = open("...","rb").read()
high = bytes(b >> 4 for b in data)
open("...","wb").write(high)
