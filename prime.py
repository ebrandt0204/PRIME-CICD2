def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

if __name__ == "__main__":
    import sys

if len(sys.argv) > 1:
    n = int(sys.argv[1])  # Read the first command-line argument
else:
    n = 10  # Default value if no input is provided

print(f"First {n} prime numbers: {generate_primes(n)}")