

class Solution:
    def combinationSum(self, candidates, target):

        s = {}
        for i in range(1, target+1):
            #print(i)
            s[i] = []
            for j in candidates:
                if i == j:
                    s[i].append([i])
                elif i > j:
                    #print(j, i-j)
                    for qj in s[j]:
                        for qij in s[i-j]:
                            tem = qj[:]+qij[:]
                            tem.sort()
                            if tem not in s[i]:
                                s[i].append(sorted(tem))

        return s[target]


s = Solution()
print(s.combinationSum([2,3,6,7],7))