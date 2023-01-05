def solution(s):
    answer = 0
    main_cnt = 1
    sub_cnt = 0
    main = s[0]
    for i, word in enumerate(s[1:]) :
        if main == 0 :
            main = word
            main_cnt = 1
            continue
                
        if word == main :
            main_cnt += 1
        else : 
            sub_cnt += 1
        
        if main_cnt == sub_cnt :
            main = 0
            main_cnt, sub_cnt = 0, 0
            answer += 1
        
    return answer if main_cnt == sub_cnt else answer + 1