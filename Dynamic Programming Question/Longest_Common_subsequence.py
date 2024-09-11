def Longest_common_subsequence(text1,text2):
    dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
    for i in range(len(text1)):
        for j in range(len(text2)):
            if text1[i] == text2[j]:
                dp[i][j] = dp[i-1][j-1]+1
            if text1[i] != text2[j]:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[len(text1)-1][len(text2)-1]

text1 = "abcde"
text2 = "ace" 
print(Longest_common_subsequence(text1,text2))