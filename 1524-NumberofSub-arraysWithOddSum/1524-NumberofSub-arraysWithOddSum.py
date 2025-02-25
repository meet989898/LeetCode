def numOfSubarrays(self, arr: List[int]) -> int:
    odd_subarrays = 0
    even_subarrays = 0
    count = 0
    for num in arr:
        if num % 2 == 0:  # Even number
            even_subarrays += 1
        else:  # Odd number
            even_subarrays, odd_subarrays = odd_subarrays, even_subarrays
            odd_subarrays += 1
        count += odd_subarrays
    return count % (10**9 + 7)