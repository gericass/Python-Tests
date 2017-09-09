# b1016126 高橋啓太
import math
def distance(p1,p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def distance_list(a):
    sum = 0
    b = a.copy()
    b.pop(0)
    b.append(a[0])

    for p1,p2 in zip(a,b):
        sum += distance(p1,p2)

    '''
    for i in range(len(a)):
        if i != len(a)-1:
            sum += distance(a[i],a[i+1])
        else:
            sum += distance(a[0],a[i])
    '''
    return sum

print(distance_list([(0,0),(2,0),(0,2),(5,2),(3,0),(5,0)]))
print(distance_list([(0,0),(1,0),(1,2),(0,2)]))