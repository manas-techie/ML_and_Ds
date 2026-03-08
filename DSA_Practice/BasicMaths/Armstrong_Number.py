class ArmstrongNumber:
    def isArmStrong(self, n):
        sum = 0
        temp = n
        no_of_digits = len(str(n))
        while temp > 0:
            digit = temp % 10
            sum = sum + digit ** no_of_digits
            temp = temp // 10
        
        return sum == n
    
armstrong = ArmstrongNumber()
print(armstrong.isArmStrong(153))