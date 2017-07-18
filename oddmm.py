# b1016126 高橋啓太
def oddmm(a):
    b = []
    for i in a:
       if i % 2 != 0:
           b.append(i)
    return (min(b),max(b))

print(oddmm([3,4,5,6,7]))
print(oddmm([60,45,30]))
print(oddmm([24,36,54,81,121,60,90,135,67,32]))