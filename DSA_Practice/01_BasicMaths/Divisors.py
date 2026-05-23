class Divisors:
    def all_divisors(self, n):
        divisor = []
        for i in range(1,n+1):
            if n % i == 0:
                divisor.append(i)
        return divisor
    

divisors = Divisors()
print(divisors.all_divisors(30))