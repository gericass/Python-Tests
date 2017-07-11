# b1016126 高橋啓太

def scorelist(a):
    b = sum(a)/len(a)
    print(b)
    r = [c for c in a if c > b]
    return r

a = [10,30,20,40,50,25,40]
print(scorelist(a))