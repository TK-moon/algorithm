def solution(s):
    indicator = 0
    result = ''
    for word in s:
        if word == ' ':
            indicator = 0
            result += ' '
        elif indicator & 1:
            indicator += 1
            result += word.lower()
        else:
            indicator += 1
            result += word.upper()
    
    return result