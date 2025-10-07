# Last updated: 10/7/2025, 10:27:39 AM
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        prefix_map = set()
        
        # Step 1: Build the prefix map for arr1
        for num in arr1:
            str_num = str(num)
            prefix = ""
            for ch in str_num:
                prefix += ch
                prefix_map.add(prefix)
        
        max_length = 0
        
        # Step 2: Check for common prefixes in arr2
        for num in arr2:
            str_num = str(num)
            prefix = ""
            for ch in str_num:
                prefix += ch
                if prefix in prefix_map:
                    max_length = max(max_length, len(prefix))
                else:
                    break
        
        return max_length


        