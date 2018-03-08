if __name__ == '__main__':
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append([name,score])
    #remove lowest number from the list
    min_num = min(score_list, key=lambda x:x[1])
    while  min(score_list, key=lambda x:x[1])[1] == min_num[1]:
        score_list.remove(min(score_list, key=lambda x:x[1]))
    newmin = min(score_list, key=lambda x:x[1])
    second_lowest=[] #store names with second_lowest scores
    for e in score_list:
        if e[1]==newmin[1]:
            second_lowest.append(e[0]) #Add the name to the list
        else:
            continue
    second_lowest.sort()
    for i in second_lowest:
        print (i)


