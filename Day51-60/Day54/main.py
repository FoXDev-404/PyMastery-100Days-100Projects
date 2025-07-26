# Project: Function Speed Benchmarking Tool
# This project measures and compares the execution time of multiple functions.

import time

# Decorator to measure the execution time of a function
def speed_calc_decorator(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"Function '{func.__name__}' executed in {end - start:.4f} seconds.")
        return result
    return wrapper

# Example function to simulate fast computation
@speed_calc_decorator
def fast_function():
    for i in range(10_000_000):
        _ = i * i

# Example function to simulate slow computation
@speed_calc_decorator
def slow_function():
    for i in range(100_000_000):
        _ = i * i

# Run benchmark comparison
def run_benchmark():
    print("Starting speed benchmark...")
    fast_function()
    slow_function()
    print("Benchmark complete.")

if __name__ == "__main__":
    run_benchmark()
