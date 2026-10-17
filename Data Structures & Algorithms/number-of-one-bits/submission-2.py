class Solution:
    def hammingWeight(self, n: int) -> int:
        count, i= 0, 0
        print("init", n)
        while i < 32:
            last = n%2
            if last == 0:
                n = n >> 1
                print(n)
                i +=1
                continue
            count +=1
            n = n >> 1
            i+=1      
        return count