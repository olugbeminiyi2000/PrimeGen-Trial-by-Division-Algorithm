#!/usr/bin/env python3
import math
import time


# utility functions
def checkMultiple(prime_to_start_with_index, length_of_prime_list, natural_number, prime_list):
  if prime_to_start_with_index == length_of_prime_list:
    return "No"
  if natural_number % prime_list[prime_to_start_with_index] == 0:
    return "Yes"
  """
  the second optimization is when we are checking if that nutral number
  is a mutiple of the prime factors found if we get to a point where the
  natural number divided by 2 is <= recent prime factor we are trying to
  divide it by that natural number is a prime number this because if we
  are trying to find if a natural number is a prime and half of that number
  becomes less than or equal to the recent prime we are trying to divided
  it by it means that all prime values after that recent prime can never
  be a multiple of that natural number.
  """
  if (natural_number / 2) <= prime_list[prime_to_start_with_index]:
    return "No"
  return checkMultiple(
          prime_to_start_with_index+1,
          length_of_prime_list,
          natural_number,
          prime_list,
        )

# now define a function to get a prime for an endpoint inclusive
def getAllPrimes(prime_list=[], natural_number=1, endpoint=300):
  if natural_number == endpoint + 1:
    return prime_list
  if natural_number == 1:
    return getAllPrimes(prime_list, natural_number+1, endpoint)
  if natural_number == 2:
    prime_list.append(natural_number)
    return getAllPrimes(prime_list, natural_number+1, endpoint)
  """
  now check for the square root of the natural number and if the
  natural number has a squre root that is a number with no fraction
  that natural number is skipped this is the first optimization.
  """
  n_sqrt = math.sqrt(natural_number)
  strc_n_sqrt = str(n_sqrt)
  if len(strc_n_sqrt) == 3:
    n_sqrt = int(n_sqrt)
  if type(n_sqrt) is int:
    return getAllPrimes(prime_list, natural_number+1, endpoint)
  n_sqrt_rnd = math.isqrt(natural_number)
  length_of_prime_list = len(prime_list)
  prime_to_start_with_index = 0
  outcome = checkMultiple(
                      prime_to_start_with_index,
                      length_of_prime_list,
                      natural_number,
                      prime_list,
                    )
  if outcome == "No":
    prime_list.append(natural_number)
    return getAllPrimes(prime_list, natural_number+1, endpoint)
  return getAllPrimes(prime_list, natural_number+1, endpoint)

start_time = time.time()
print(getAllPrimes())
end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
