import sys

from sage.all import *
from fpylll import IntegerMatrix,LLL

e = 5

N = 84364443735725034864402554533826279174703893439763343343863260342756678609216895093779263028809246505955647572176682669445270008816481771701417554768871285020442403001649254405058303439906229201909599348669565697534331652019516409514800265887388539283381053937433496994442146419682027649079704982600857517093

C = 23701787746829110396789094907319830305538180376427283226295906585301889543996533410539381779684366880970896279018807100530176651625086988655210858554133345906272561027798171440923147960165094891980452757852685707020289384698322665347609905744582248157246932007978339129630067022987966706955482598869800151693

#final padding used
padding='You see a Gold-Bug in one corner. It is the key to a treasure found by '


#converting padding into binary 
bin_padding=[]
for c in padding:
   bin_padding.append(str(bin(ord(c))[2:].zfill(8)))
bin_padding = "".join(bin_padding)

#converting binary padding into integer padding
int_padding=int(bin_padding,2)

ring_over_int_mod_N=Zmod(N)
R, x = ring_over_int_mod_N['x'].objgen()


for i in range(250): 
   
   px=((int_padding<<i)+ x)**e - C  #generating polynomial of form (p+x)^e-C
   
   h=3
   k=e
   t=(h-1)/(h*k-1)
   row = column = h*k
   X = ceil(N**t)
   
   px = px.change_ring(ZZ)  
   
   x = px.parent().gen()
   L = IntegerMatrix(row, column)          #fpylll IntegerMatrix
   
   for r in range(row):
      v=floor(r/k)
      u=r-k*v
      q=(x**u)*(px**v)
      for c in range(column):
         L[r,c]=q[c]*(N**(h-1-v))*(X**c)

   L = LLL().reduction(L)        #LLL Reduction using fpylll library

   shortPoly = 0 
   for c in range(column):
      shortPoly = shortPoly + L[0,c]/(X**c)*x**c                        #shortest Vector
      
   possibleRoots = shortPoly.roots()      #roots of Shortest vector using SAGE
   if possibleRoots:
      print("Roots are : ", possibleRoots) 
      break
