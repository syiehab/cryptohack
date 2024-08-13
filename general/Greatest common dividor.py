def gdb(a,b):
    if a < b:
        a,b = b,a
        
    r = b % a
    q = b//a
    print("q:", q)
    print("r:", r)

    while r != 0 :
        print(r)
        b = a
        a = r
        r = b % a
        q = b//a
        


print(gdb(52920,66528))
