def solution(rsp):
    rsp_dict = {'2':'0', '0':'5', '5':'2'}
    answer = ''
    for r in rsp :
        answer += rsp_dict[r]
    return answer