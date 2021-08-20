
def NearestGreaterPalindrome(n):
    while(True):
        rev = int(str(n)[::-1])
        if (rev==n):
            return n
        n+=1

n = int(input())
print(NearestGreaterPalindrome(n))