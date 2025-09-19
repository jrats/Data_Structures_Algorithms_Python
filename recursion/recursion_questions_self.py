### sum of digits

def sumDigits(num):
    assert num>=0 and int(num)==num , "The number should be a positive integer"
    if num==0:
        return 0
    else:
        return (num%10) + sumDigits(num//10)
    
print(sumDigits(45))

###power

def pow(base, exp):
    assert int(exp) == exp, "the exp should be an integer"
    if base==0 or base==1:
        return base
    if exp ==0:
        return 1
    if exp<0:
        return (1/base*(pow(base, exp+1)))
    return base* pow(base, exp-1)


print(pow(2,-2))


##gcd 

def gcd(a, b):
    assert int(a) == a and int(b) == b, "The numbers should be integers"
    if b==0:
        return a
    else:
        return gcd(abs(b), abs(a)%abs(b))
    


print(gcd(8, 12))

##decimal to binary

def dec_to_binary(n):
    assert int(n) == n, "The parameter must be an integer"
    if n ==0:
        return '0'
    if n ==1:
        return '1'
    return (dec_to_binary(n//2)) + str(n%2)

print(dec_to_binary(18))
