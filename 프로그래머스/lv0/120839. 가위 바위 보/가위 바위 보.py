def solution(rsp):
    rsp_dict = {'2':'0', '0':'5', '5':'2'}
    answer = ''
    for i in rsp :
        answer += rsp_dict[i]
    return answer