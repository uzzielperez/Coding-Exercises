if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    nlist = sorted(list(set(arr)))
    second_highest = nlist[-2]
    print(second_highest)
