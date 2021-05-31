p = 19807040628566084398385987581

number = int(input())   #the number whose inverse has to calculate

# Using fermet little theorem, to get the inverse
# => number^(p-1) mod p ≡ 1
# => number^(p-2)*number mod p ≡ 1
# => (number^(p-2) mod p )*(number mod p) mod p ≡ 1
# => number^(-1) ≡ number^(p-2) mod p

inverse = pow(number,p-2,p)

print("Inverse of number is",inverse)

