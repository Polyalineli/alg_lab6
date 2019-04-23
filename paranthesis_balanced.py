
def is_paranthesis_balanced(s):
    d={')':'(',']':'[','}':'{','>':'<' }
    a = []
    if len(s)==0:
        return True
    for i in s:
        if i in d and len(a)>0 and d[i]==a[-1]:
            a.pop()
        else:
            a.append(i)
    if len(a)>0:
        return False
    else:
        return True
#s = '()]'
#s = '({[()]}{<>})'
#is_paranthesis_balanced(s)

