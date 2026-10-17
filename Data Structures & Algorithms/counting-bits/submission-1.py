class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)

        for i in range(1, n+1):
            # Recurrence: count of 1's in i = (last bit of i) + (count of 1's in i // 2)
            # output[i] = (i % 2) + output[i // 2]
            output[i] = (i & 1) + output[i >> 1]

        return output