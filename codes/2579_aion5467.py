import sys
input = sys.stdin.readline

num_of_stairs = int(input())
dp = [0 for _ in range(num_of_stairs+3)]
stair_score = [0 for _ in range(num_of_stairs+1)]
for k in range(1,num_of_stairs+1):
    stair_score[k] = int(input())


dp[1] = stair_score[1]
dp[2] = stair_score[1] + stair_score[2]
dp[3] = max(stair_score[1] + stair_score[3] ,stair_score[2] + stair_score[3])


for i in range(4, num_of_stairs+1):
    dp[i] = max( dp[i-3] + stair_score[i-1] + stair_score[i] ,  dp[i-2] + stair_score[i] ) 

print(dp[num_of_stairs])

# index 에러가 떠서 틀린 상황입니다ㅠㅠ