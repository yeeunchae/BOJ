for tc in range(10):
    stack = []
    howmany = int(input())
    Data = input()
    ans = 0
    for i in range(howmany):
        if(Data[i]) in '({[<':
            stack.append(Data[i])
        elif (Data[i]==')' and stack[-1]=='(') or (Data[i]=='}' and stack[-1]=='{') or (Data[i]==']' and stack[-1]=='[') or (Data[i]=='>' and stack[-1]=='<'):
            stack.pop()
            if not stack: ans = 0
        else:
            break
    if not stack : ans = 1
    print(f'#{tc+1} {ans}')