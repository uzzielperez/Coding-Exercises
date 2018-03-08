if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    nlist = list(arr)
    z = max(nlist) 
    while max(nlist) ==z:
      nlist.remove(max(nlist))
    print(max(nlist))

