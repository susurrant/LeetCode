class Solution:
    def groupAnagrams(self, strs):
        d = {}
        const = 'abcdefghijklmnopqrstuvwxyz'
        for s in strs:
            tem = [0]*26
            for c in s:
                tem[const.index(c)] += 1
            tem = tuple(tem)
            if tem not in d:
                d[tem] = []
            d[tem].append(s)

        r = []
        for item in d.values():
            r.append(item)
        return r


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

