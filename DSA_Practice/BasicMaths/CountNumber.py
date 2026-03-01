class  Solution:
    def countDigit(self, n):
        count =  0

        if n == 0:
            return 1
        while n > 0:
            count += 1
            n = n // 10

        return count
    

solution = Solution()
print(solution.countDigit(234))