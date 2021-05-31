p = 19807040628566084398385987581

g = 192847283928500239481729     # as calculated in findG.py code
a = 324

# password * g^(a) = 11226815350263531814963336315

i = pow(pow(g,a),p-2,p)
password = (i*11226815350263531814963336315)%p

print("Your password is ",password)