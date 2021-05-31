# Code to find value of g with fixed value of g^9189 and g^2021

a1 = 324
a2 = 2345
a3 = 9513

p = 19807040628566084398385987581  # prime number


g = 2021 # 2345 - 324
n = 9189 # 9513 - 324

G = 7021284369301638640577066679

value = 3426347385144995225825016781

while g>1:
    #print(G)
    q = n//g
    #print(q)
    r = n%g
    #print(r)
    i = pow((pow(G,q)),p-2,p)
    #print(i)
    G = (value*i)%p
    #print(G)
    g = r
    #print(".....................")

print("Value of g is",G)



