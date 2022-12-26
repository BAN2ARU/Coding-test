def solution(num_list, n):
    answer = [[num_list[n*j+i]for i in range(n)] for j in range(len(num_list)//n)]
    return answer