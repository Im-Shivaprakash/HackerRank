#Perform operations on list

if __name__ == '__main__':
    N = int(input())
    out_list = []
        
    for _ in range(N):
        task = input().split()
        
        if task[0] == 'append':
            out_list.append(int(task[1]))
        
        elif task[0] == 'insert':
            index = int(task[1])
            value = int(task[2])
            out_list.insert(index, value)
                    
        elif task[0] == 'remove':
            value = int(task[1])
            out_list.remove(value)
        
        elif task[0] == 'sort':
            out_list.sort()
            
        elif task[0] == 'pop':
            if len(task) > 1:
                index = int(task[1])
                out_list.pop(index)
            else:
                out_list.pop()
                
        elif task[0] == 'reverse':
            out_list.reverse()
        
        elif task[0] == 'print':
            print(out_list)
