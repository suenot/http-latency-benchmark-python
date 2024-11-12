import requests
import time
import numpy as np

def median(arr):
    """Calculate the median using the NumPy library"""
    return np.median(arr)

def main():
    repeats = 10  # Number of repetitions
    times = []

    for i in range(repeats):
        start = time.time()  # Record the start time of the request
        
        try:
            response = requests.get("https://api.bybit.com/v2/public/time")
            response.raise_for_status()  # Check if the request was successful
        except requests.RequestException as e:
            print(f"Request {i+1} failed: {e}")
            continue
        
        duration = (time.time() - start) * 1000  # Convert time to milliseconds
        times.append(duration)
        print(f"Request {i+1} duration: {duration:.2f} ms")

    # Calculate the minimum, maximum, and median response times
    min_time = min(times) if times else None
    max_time = max(times) if times else None
    median_time = median(times) if times else None

    print(f"\nResults for {repeats} requests:")
    print(f"Minimum time: {min_time:.2f} ms")
    print(f"Maximum time: {max_time:.2f} ms")
    print(f"Median time: {median_time:.2f} ms")

if __name__ == "__main__":
    main()
