class Solution:
    
    def reverse(self, x: int) -> int:
        
        k = 1 if x >= 0 else -1
        r = int(''.join(reversed(abs(x))))*k
        
        return r if -2**31 <= r <= 2**31-1 else 0
    
n = -123
p = Solution()
print(p.reverse(n))





