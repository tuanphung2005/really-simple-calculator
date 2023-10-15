input=str(input('arg:'))
num=['']
j=0
for i in range(len(input)):
    if input[i]=='0' or input[i]=='1' or input[i]=='2' or input[i]=='3' or input[i]=='4' or input[i]=='5' or input[i]=='6' or input[i]=='7' or input[i]=='8' or input[i]=='9':
        num[j]+=input[i]
    else:
        num[j]=int(num[j])
        j+=1
        c=input[i]
        num.append('')
num[j]=int(num[j])
match c:
    case '+':
        print(num[j]+num[j-1])
    case '-':
        print(num[j-1]-num[j])
    case '*':
        print(num[j]*num[j-1])
    case '/':
        print(num[j-1]/num[j])
