class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0 

        for _ in range(32):
            last_bit = n % 2
            result = result * 2 #shift by one 
            result += last_bit
            n = n//2

        return result   
