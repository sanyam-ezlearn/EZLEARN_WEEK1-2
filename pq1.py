'''Problem Statement 01 
You are given a string S. Each character in the string S is either a digit 
 
You can perform the following operation on the string S: 
symbol with any digit from 0-9 
After replacing all symbol om the string S with a digit you will get an 
integer. The integer may start with leading zeros too. 
Your task is to count the number of helpful integers generated after 
replacing each with an integer. Since the answer can be very large, 
return it to modulo 109 + 7.
 A helpful integer is defined as an integer whose remainder is equal to 7 
when divided by 13 and 11.'''
def count_helpful_integers(s):
    MOD = 10**9 + 7
    N = len(s)
    dp = [[0] * 143 for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for remainder in range(143):
            if s[i] == '?':
                for digit in range(10):
                    new_remainder = (remainder * 10 + digit) % 143
                    dp[i + 1][new_remainder] += dp[i][remainder]
                    dp[i + 1][new_remainder] %= MOD
            else:
                digit = int(s[i])
                new_remainder = (remainder * 10 + digit) % 143
                dp[i + 1][new_remainder] += dp[i][remainder]
                dp[i + 1][new_remainder] %= MOD

    target_remainder = 7  # remainder when divided by both 13 and 11
    return dp[N][target_remainder] % MOD

s = input("enter the word to enter").strip()
result = count_helpful_integers(s)
print(result)
