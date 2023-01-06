def solution(n, words):
    answer = [words[0]]

    for i, w in enumerate(words[1:], start=1) :
        if answer[-1][-1] != w[0] :
            return [i%n+1, i//n+1]
        if w in answer :
            return [i%n+1, i//n+1]
        answer.append(w)
    return [0, 0]