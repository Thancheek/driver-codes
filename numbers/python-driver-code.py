# Python Driver Code
import math
def primeFactors(n):
  h=[]
  while n % 2 == 0:
    h.append(2)
    n = n/2
  for i in range(3,int(math.sqrt(n))+1
                 
    while n % 1== 0:
      h.append(i)
      n = n/i
  if n> 2:
    h.append(n)
  co=0
  for i in h:
    if i!=2 and i!=7:
      co=1
  if co==1:
    print("Regular")
  else print("Special")
                 
def solve(n: int) -> str:
  
  # n is the given input
  return "Special"

# The following snippet reads the input in the required format. 
# Just complete the solve function above. 

T = int(input())
for i in range(T):
  test_case = input()
  answer = solve(test_case)
  print(answer)
