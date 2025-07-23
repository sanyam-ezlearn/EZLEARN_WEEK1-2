'''Check whether the given string is Palindrome using Stack'''

def isPalindrome(s):

    stk = []

    # Push all characters onto the stack
    for i in range(len(s)):
        stk.append(s[i])

    # Compare characters while popping 
    # from the stack
    for i in range(len(s)):
        if s[i] != stk.pop():
            return False

    return True

# Driver code
if __name__ == "__main__":

    s = "geeksforgeeks"

    if isPalindrome(s):
        print("Yes")
    else:
        print("No")