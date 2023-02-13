def solution(lines):
    lines = [set(range(line[0],line[1])) for line in lines]

    return len((lines[0]&lines[1]) | (lines[1]&lines[2]) | (lines[2]&lines[0]))