if __name__ == '__main__':
    n = int(input())
    
    i = n 
    list = []
    while i>0: 
        list.append(i)
        i = i-1
    list.reverse()
    print(*list, sep='')
