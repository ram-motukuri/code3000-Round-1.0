def Roman(number):
    ans=""
    num = [1, 4, 5, 9, 10, 40, 50, 90,100, 400, 500, 900, 1000] 
    sym = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"] 
    i = 12
    while number: 
        div = number // num[i] 
        number %= num[i] 
        while div: 
            ans=ans+sym[i] 
            div -= 1
        i -= 1
    return ans
l=[2312,2001,3100,1666]
for num in l:
    roman=Roman(num)
    res=""
    for i in roman:
        res=res+str(ord(i)-64)
    print(num,roman,res)
