'''Problem Statement 03 
New array becomes {1, 
2} which follows A1 = 1, 
A2 = 2
 Alice has recently learnt about the bitwise operation & She designed 
function of her own called as Fun, this function takes 2 integers as input 
and outputs an integer.
 Fun(A, B)= A + B-2*(A&B)
 Here & is the bitwise And of the two numbers.
 Score of an array AR of size N is Sum of Fun(Fun(AR[i], AR[j], AR[k]) for 
every triplet of i , j , k where 1 <= I < j < k <=N .  
She took an array of N numbers called AR and decides to find the score of 
this array. Your task is to find the Score of the AR. Since this value can be 
very large return the result modulo 10^9 + 7'''
def fun(a, b):
    
    return a + b - 2 * (a & b)

def calculate_score():
    """
    Calculates the score of the array AR.
    
    Returns:
    int: The score of the array AR modulo 10^9 + 7.
    """
    N = int(input())
    AR = []
    for _ in range(N):
        AR.append(int(input()))

    score = 0
    for i in range(N):
        for j in range(i + 1, N):
            fun_ij = fun(AR[i], AR[j])
            for k in range(j + 1, N):
                fun_ijk = fun(fun_ij, AR[k])
                score += fun_ijk
                score %= 10**9 + 7

    return score
#input statement
print(calculate_score())
