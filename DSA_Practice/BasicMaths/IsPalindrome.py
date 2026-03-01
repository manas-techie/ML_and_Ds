class Solution: 
    def IsPalindrome(self, num):
        actual_num = num
        rev_num = 0
        while num > 0:
            digit = num % 10
            rev_num = rev_num * 10 + digit
            num = num // 10

        if actual_num == rev_num: 
            return True
        else: 
            return False
        
solution = Solution()
print(solution.IsPalindrome(121))