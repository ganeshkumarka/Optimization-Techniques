def knapSack(C, W, m, n):
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif W[i-1]<=j:
                dp[i][j]=max(C[i - 1] + dp[i - 1][j- W[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    selected = []
    i = n
    j = m
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected.append(i - 1)
            j -= W[i - 1]
        i -= 1
    selected.reverse()
    print("Selected items: ", selected)
    return dp[n][m]
    
if __name__=='__main__':
    m = int(input("Enter the capacity: "))
    n = int(input("Enter the number of items : "))
    C = []
    W = []
    for i in range(n):
        C.append(int(input("Enter the cost of item {}: ".format(i + 1))))
        W.append(int(input("Enter the weight of item {}: ".format(i + 1))))
    result = knapSack(C,W,m,n)
    print("The maximum value that can be obtained is:", result)