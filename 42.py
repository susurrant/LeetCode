class Solution:
    def trap(self, height):
        if not height:
            return 0

        def f(h):
            s = 0
            i = 0
            num = len(h)
            while  i<num and h[i] == 0:
                i += 1
            j = i+1

            while i!=num:
                tem = 0
                while j < num and h[i] > h[j]:
                    tem += h[i]-h[j]
                    j += 1
                if j != num:
                    s += tem
                    i = j
                    j += 1
                else:
                    if i+1<num-1:
                        s += f(h[i+1:])
                    break
            return s
        return f(height)


s = Solution()
print(s.trap([0,0]))