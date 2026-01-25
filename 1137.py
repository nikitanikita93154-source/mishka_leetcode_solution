n=25
memo=[0,1,1]+[-1]*(n-2)


def fibRec(n, memo):
    print(n,memo)
    if n <= 1:
        return n

    # To check if output already exists
    if memo[n] != -1:
        return memo[n]

    # Calculate and save output for future use
    memo[n] = fibRec(n - 1, memo) + fibRec(n - 2, memo)+ fibRec(n - 3, memo)
    return memo[n]
print(fibRec(25,memo))