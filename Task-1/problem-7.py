num = int(input())
divisors = []


for i in range(1, num + 1):
    if num % i == 0:
        divisors.append(i)


for d in divisors:
    if d > 1:  
        prime = True
        for j in range(2, d):  
            if d % j == 0:
                prime = False
                break
        if prime:
            print(d, end=" ")
