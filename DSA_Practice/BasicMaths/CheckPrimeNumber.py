class PrimeNumber:
    def check_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, n//2 + 1):
            if n % i == 0:
                return False
        return True
    
prime_number = PrimeNumber()
print(prime_number.check_prime(7))