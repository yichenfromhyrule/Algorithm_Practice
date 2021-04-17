# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def stairs(n):
    dp=[0 for i in range(n)]
    dp[0]=1
    dp[1]=1
    for i in range (2,n):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n-1]

def rob(l):
    dp=[0 for i in range(len(l))]
    dp[0]=l[0]
    dp[1]=max(l[0],l[1])
    for i in range(2,len(l)):
        dp[i] = max(dp[i-2]+l[i],dp[i-1])
    return dp[len(l)-1]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(stairs(8))
    print(rob([2,7,9,3,1]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
