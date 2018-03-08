if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        #name, *line = input().split()
        item = input().split()
        name, scores = item[0], item[1:]
        scores = list(map(float, scores))
        student_marks[name] = scores
    query_name = input()
    query_scores = student_marks[query_name]
    sum_scores = sum(query_scores)
    avg = sum_scores/len(query_scores)
    print("%.2f" % avg)
