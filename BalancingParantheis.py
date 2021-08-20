

open = ["{","(","["]
close = ["}",")","]"]
def Balancing(string):
    stack = []
    for i in string:
        if i in open:
            stack.append(i)
        elif i in close:
            pos = close.index(i)
            if (open[pos]==stack[len(stack)-1]) and (len(stack)>0):
                stack.pop()
            else:
                print("Unbalanced")
                return
    if (len(stack)==0):
        print("Balanced")
        return
    else:
        print("Unbalanced")
        return




string = "{[]()}"
Balancing(string)