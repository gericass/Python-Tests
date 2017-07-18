# b1016126 高橋啓太
def factor(a):
    res = []
    for num in a:
        for num2 in a:
            if num == num2 or num > num2:
                continue
            if num % num2 == 0 or num2 %num ==0:
                res.append((num,num2))

    return res

print(factor([1080,1260,301,501,5400,1080,10020,167]))