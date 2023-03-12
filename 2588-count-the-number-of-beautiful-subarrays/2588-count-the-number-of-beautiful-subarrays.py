class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        prefix_freq = {0: 1}
        # Initialize the current xor value and the count of beautiful subarrays
        curr_xor = 0
        beautiful_count = 0

        # Loop through the array and update the current xor value and beautiful count
        for num in nums:
            # Update the current xor value
            curr_xor ^= num
            # Update the beautiful count with the frequency of prefix xors that can make the current xor value 0
            beautiful_count += prefix_freq.get(curr_xor, 0)
            # Update the prefix frequency dictionary
            prefix_freq[curr_xor] = prefix_freq.get(curr_xor, 0) + 1

        return beautiful_count