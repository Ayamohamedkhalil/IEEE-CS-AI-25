if __name__ == '__main__':
    n = int(input())
    my_list = []
    
    for _ in range(n):
        command = input().split()
        operation = command[0]
        
        if operation == "insert":
            index = int(command[1])
            value = int(command[2])
            my_list.insert(index, value)
        elif operation == "print":
            print(my_list)
        elif operation == "remove":
            value = int(command[1])
            my_list.remove(value)
        elif operation == "append":
            value = int(command[1])
            my_list.append(value)
        elif operation == "sort":
            my_list.sort()
        elif operation == "pop":
            my_list.pop()
        elif operation == "reverse":
            my_list.reverse()
        elif operation == "runnerup":
            
            if len(my_list) > 1:
                max_score = max(my_list)
                
              
                while max_score in my_list:
                    my_list.remove(max_score)
                
                
                if my_list: 
                    runner_up = max(my_list)
                    print(runner_up)
                else:
                    print("No runner-up found")
            else:
                print("Not enough elements for runner-up")
