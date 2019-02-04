"""
6. ZigZag Conversion
"""

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        size = len(s)
        if size <= numRows:
            return s

        rs = ''
        interval = numRows*2 - 2
        for i in range(numRows):
            j  = 0
            ivs = [0]
            if 0 < i < numRows-1:
                ivs.append(interval-2*i)
            while True:
                tag = False

                for iv in ivs:
                    idx = i + iv + interval * j
                    if idx < size:
                        rs += s[idx]
                    else:
                        tag = True
                        break

                if tag:
                    break
                else:
                    j += 1


        return rs

        """
        P0       I6          N12
        A1    L5 S7     I11  G13
        Y2 A4    H8 R10
        P3       I9
        
        P0    A4    H8      N12
        A1 P3 L5 S7 I9  I11 G13
        Y2    I6    R10
        
        P0           H8
        A1        S7 I9
        Y2     I6    R10
        P3  L5       I11  G13
        A4           N12
        
        """

class Reference(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            print(x, index, step, L)
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)

if __name__ == '__main__':
    l = 'PAYPALISHIRING'
    numRows = 3
    s = Reference()
    print(s.convert(l, numRows))