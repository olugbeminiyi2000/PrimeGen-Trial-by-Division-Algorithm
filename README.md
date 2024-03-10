# Prime Number Generation using Trial by Division Algorithm
## Trial by Division Algorithm

The trial by division algorithm is one of the oldest and simplest methods for determining whether a given number is prime. It involves iteratively dividing the number by the prime factors already found. If no divisor is found other than 1 and the number itself, then the number is prime.

4. If the candidate number is not divisible by any integer other than 1 and itself, it is prime.

By applying this process iteratively to all numbers within a specified range, the trial by division algorithm can efficiently generate prime numbers.

This algorithm serves as the foundation for many other prime number generation algorithms and provides a straightforward approach to identifying prime numbers.



This Python script generates prime numbers up to a specified endpoint using the trial by division algorithm. The algorithm employs recursion and various optimizations to efficiently find prime numbers within the given range.

## Code Explanation

### Utility Functions

#### `checkMultiple(prime_to_start_with_index, length_of_prime_list, natural_number, prime_list)`
- This function recursively checks if a given `natural_number` is a multiple of any primes found so far in the `prime_list`.
- It implements one key optimization:
  - The second optimization is triggered when the division of `natural_number` by 2 is less than or equal to the recent prime factor being checked. This condition indicates that `natural_number` is prime, as all subsequent prime numbers cannot divide it evenly.
- The function returns "Yes" if the number is found to be a multiple of any prime factors, and "No" otherwise.

#### `getAllPrimes(prime_list=[], natural_number=1, endpoint=300)`
- This function initiates the generation of prime numbers up to the specified `endpoint`.
- It recursively calls itself to iterate through natural numbers, checking for primality and adding prime numbers to the `prime_list`.
- It implements one key optimization:
  - The first optimization involves skipping natural numbers whose square roots are integers, as these numbers are not prime. This optimization reduces unnecessary iterations and improves performance.
- The function returns the list of prime numbers up to the specified `endpoint`.

### Execution
- The script measures the execution time of the prime number generation process.
- It prints the list of generated prime numbers and the execution time in seconds.

## Optimization
- The algorithm implements two key optimizations to improve performance:
  - The first optimization, skipping natural numbers with integer square roots, is implemented within the `getAllPrimes()` function.
  - The second optimization, early termination based on the division of `natural_number` by 2, is implemented within the `checkMultiple()` function.

## Usage
- Simply execute the script to generate prime numbers up to the specified `endpoint`.
- Modify the `endpoint` variable to change the range of prime numbers generated.

## Performance
- The performance of the algorithm depends on the specified `endpoint`.
- The optimizations significantly improve efficiency, making the algorithm suitable for generating prime numbers within moderate-sized ranges.

## Conclusion
- The trial by division algorithm, combined with optimizations, provides an efficient approach to generating prime numbers.
- The algorithm's simplicity and effectiveness make it a suitable choice for various applications requiring prime number generation.
