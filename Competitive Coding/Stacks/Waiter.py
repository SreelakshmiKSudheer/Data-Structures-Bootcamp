def isPrime(num):
    """
    Check if a number is prime.
    Args:
        num (int): The number to check for primality.
    Returns:
        bool: True if num is a prime number, False otherwise.
    """
    # ...
    
    # ...
    # Numbers less than 2 are not prime
    if num < 2:
        return False
        
    # Only check divisibility up to the square root of num
    limit = int(num ** 0.5) + 1
    for i in range(2, limit):
        # If num is divisible by i, it's not prime
        if num % i == 0:
            return False
        
    # If no divisors found, num is prime
    return True
                
def waiter(number, q):
    """
    Simulates the Waiter problem using stacks and prime numbers.
    Args:
        number (list of int): The initial stack of numbers.
        q (int): The number of iterations (number of primes to use).
    Returns:
        list of int: The sequence of numbers after processing through q iterations,
                     following the rules of the Waiter problem.
    """
    # Write your code here
    # Initialize count for number of primes found
    count = 0
    # List to store the first q prime numbers
    primes = []
    # Start checking for primes from 2
    num = 2
    # Find the first q prime numbers
    while count < q:
        if isPrime(num):
            primes.append(num)
            count += 1
        num += 1

    # Reverse the input list to simulate stack behavior (top at end)
    a = number[::-1]
    # List to store the final answer sequence
    answers = []

    # Process for each prime number
    for prime in primes:
        Ai = []  # Stack for numbers not divisible by current prime
        b = []   # Stack for numbers divisible by current prime

        # Pop elements from stack 'a' and distribute to Ai or b
        while a:
            num = a.pop()
            if num % prime == 0:
                b.append(num)      # If divisible, push to b
            else:
                Ai.append(num)     # Else, push to Ai
        answers += b  # Add all numbers from b to answers
        a = Ai        # Set a to Ai for next iteration

    # After all primes, add remaining numbers in a to answers
    answers += a
    return answers
