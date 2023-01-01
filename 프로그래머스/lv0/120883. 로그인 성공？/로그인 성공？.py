def solution(id_pw, db):
    answer = ''
    for d in db :
        if id_pw[0] == d[0] and id_pw[1] == d[1] :
            return "login"
        elif id_pw[0] == d[0] and id_pw[1] != d[1] :
            answer = 'wrong pw'
        else :
            pass
    return answer if answer else "fail"