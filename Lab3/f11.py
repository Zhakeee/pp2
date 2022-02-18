def palindrome(x):
    
    if x[::-1]==x:
        return True
    else:
        return False

print(palindrome(input()))