  
numbers=map(int,input().split())

total = 0  

for num in numbers:
    if num == -1:
        break  
    total += num  

print(f"Sum: {total}") 

