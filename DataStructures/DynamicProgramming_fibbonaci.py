# Recursive Method O(2^n)

def fibb(n):
    if n == 1 or n == 0:
        return n
    return fibb(n-1) + fibb(n-2)

print(fibb(2))

# Memoization  Time Complexity: O(n)  Space: O(n)

def fibb_DP_recurse(n, memo={}):
    if n in memo.keys():
        return memo[n]
    
    if n == 1 or n == 0:
        return n
    
    memo[n] = fibb_DP_recurse(n-1) + fibb_DP_recurse(n-2)

    return memo[n]

# Tabualation

def fibb_DP_tabulation(n):
    fibb_map = {0:1, 1:1}

    if n == 0 or n == 1:
        return n

    for i in range(2, n+1):
        fibb_map[i] = fibb_map[i-1] + fibb_map[i-2]
    
    return fibb_map[n]

print(fibb_DP_tabulation(10000))

