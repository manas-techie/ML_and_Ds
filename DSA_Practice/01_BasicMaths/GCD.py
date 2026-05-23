class Solution:
    def GCD(self, a, b):
        len = min(a,b)
        for i in range (len, 0, -1):
            if a % i == 0 and b % i == 0:
                return i
        return 1
    
    def GCD2 (self, a, b):
        while a > 0 and b > 0:
            if a > b:
                a = a - b
            else:
                b = b-a
            if a == 0:
                GCD = b
                break
            if b == 0:
                GCD = a
                break

        return GCD

solution = Solution()
print(solution.GCD(48, 18))
print(solution.GCD2(48, 18))