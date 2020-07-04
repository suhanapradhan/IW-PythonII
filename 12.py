def is_palindrome(a):
    
    p=a[::-1]
    if a == p:
        return "is a palindrome"
    else:
        return "not a palindrome"

print(is_palindrome('rarar'))
print(is_palindrome('python'))