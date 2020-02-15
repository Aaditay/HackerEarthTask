def check(s):
    res = s % 6
    if res==0 or res==1 :
        print("WS")
    elif res==2 or res==5 :
        print("MS")
    elif res==3 or res == 4 :
        print("AS")


inp = int(input())
seats = []
for i in range(inp):
    seats.append(int(input()))

for seat in seats :
   print( check(seat), end = ' ')
   print(seat , end = ' ' )
    
  
