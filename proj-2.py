import math
import random
import time


def generate_sorted_asc_array(n):
    return list(range(n))

def right_shift(arr, k):
    n = len(arr)
    k = k % n  # In case k is greater than n
    return arr[-k:] + arr[:-k]


def find_right_shift_number(arr):
    # This was my initial attemp before realizing that this idea was stupid :)
    if not arr:
        return 0
    left, right = 0, len(arr) - 1
    arr_size = len(arr)

    if arr[left] < arr[right]:
        return 0  # Array is not shifted
    
    shift_count = 0
    # Maximu shift possible should be n-1
    while( arr[left] > arr[right] ):
        left += 1
        right -= 1
        shift_count += 1
    
    if arr[right] > arr[right+1]:
        return arr_size - left , shift_count
    else:
        return left , shift_count

    return left, shift_count


def find_log_base_two (n):
    if n <= 0:
        return 0
    return math.log2(n)

def find_max_in_shifted_array(arr):
    """
    Find the maximum element in a circularly (rotated) sorted array.

    Parameters
    ----------
    arr : list[int]
        A sorted list of integers that has been rotated to the right
        by an unknown number of positions.

    Returns
    -------
    int
        The maximum element in the array.

    Examples
    --------
    >>> find_max_in_shifted_array([35, 42, 5, 15, 27, 29])
    42
    >>> find_max_in_shifted_array([27, 29, 35, 42, 5, 15])
    42
    >>> find_max_in_shifted_array([1, 2, 3, 4, 5])
    5
    """
    # Start measuring time precisely
    start_time = time.perf_counter()

    n = len(arr)
    if n == 0:
        raise ValueError("Array must contain at least one element.")

    lo, hi = 0, n - 1 # Initialize indices (low and high)

    # Handle case when array is not rotated at all
    if arr[lo] < arr[hi]:
        end_time = time.perf_counter()
        return arr[hi], end_time - start_time

    # Binary search to find the index of the minimum element
    while lo < hi:
        mid = lo + (hi - lo) // 2

        if arr[mid] > arr[hi]:
            # Minimum lies in the right half
            lo = mid + 1
        else:
            # Minimum lies at mid or in left half
            hi = mid

    min_idx = lo
    max_idx = (min_idx - 1 + n) % n

    end_time = time.perf_counter()
    return arr[max_idx], end_time - start_time

if __name__ == "__main__":
    # Generate a sorted random array of random length n
    print(f"{'[Array Length]':<15}{'[Shifted by]':<15}{'[Actual Max]':<15}{'[Computed Max]':<16}{'[Theoretical time]':<19}{'[Experimental time]':<21}{'[Ratio (Experimental/Theoretical)]':<30}")
    # Add a nice line :)
    print("-" * 90)

    ratios = []
    for i in range(1,10):
        array_length = 10**i

        arr = generate_sorted_asc_array(array_length) # Generate sorted array

        k = random.randint(1, array_length-1) # Random shift between 1 and n-1

        shifted_arr = right_shift(arr, k) # Right shift the array by k positions

        actual_max = max(shifted_arr) # Calculate actual max of the array for reference

        # Run the function multiple times and take a mean of experimental time to reduce noise and garbage collter effects etc
        total_experimental_time = []
        for _ in range(10000):
            computed_max, experimental_time = find_max_in_shifted_array(shifted_arr)
            total_experimental_time.append(experimental_time)

        # Calculate the median experimental time
        total_experimental_time.sort()
        experimental_time = total_experimental_time[len(total_experimental_time)//2]

        theoretical_time = find_log_base_two(array_length)
        ratios.append((experimental_time*1e9)/theoretical_time) # Convers time of nanoseconds

        print(f"{array_length:<16,d}{k:<15,d}{actual_max:<15,d}{computed_max:<17,d}{theoretical_time:<20.2f}{experimental_time*1e9:<22.2f}{(experimental_time*1e9)/theoretical_time:<30.2f}")
    # Print medin ratio
    ratios.sort()
    median_ratio = ratios[len(ratios)//2]
    print("-" * 90)
    print(f"{'Median Ratio (Experimental/Theoretical)':<70}{median_ratio:<.2f}")
