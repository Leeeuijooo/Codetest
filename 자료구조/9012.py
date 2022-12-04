# boj.kr/9012
# 9012. 괄호
for _ in range(int(input())):
    stk=[]
    isVPS = True
    for ch in input(): 
        if ch == '(':
            stk.append(ch)
        else : 
            if len(stk) > 0:
                stk.pop()
            else :
                isVPS = False
    if len(stk) > 0 : 
        isVPS = False
        break;
    
        
    print('YES' if isVPS else 'NO')
    
            
    
        