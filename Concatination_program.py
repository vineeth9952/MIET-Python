#3,2,6,5,1,4,8,9
n = list(map(int, input().split(",")))
#print(n)
number1 = sum(n[:n.index(5)]+ n[n.index(8)+1:])
#print(number1)

temp = n[n.index(5):n.index(8)+1]
#print(temp)
number2 = ""

for i in temp:
    number2 = number2 + str(i)

print(int(number2)+number1)
