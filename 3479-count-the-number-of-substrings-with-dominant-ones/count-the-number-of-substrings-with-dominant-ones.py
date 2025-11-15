class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        zero_indices = []

        for i, char in enumerate(s):
            if char == '0':
                zero_indices.append(i)

            l = 0
            while l <= len(zero_indices):
                # Calculate the required number of '1's for the current window size 'l'
                target_length = l * l + l
                if target_length > i + 1:
                    break

                # Determine the left and right boundaries of the current window
                left_index = zero_indices[-1 - l] if l < len(zero_indices) else -1
                right_index = zero_indices[-l] if l > 0 else i

                # Calculate the minimum and maximum possible lengths of the substring with 'l' zeros
                min_length = i - right_index + 1
                max_length = i - left_index

                # Count valid substrings within the current window
                if min_length >= target_length:
                    count += max_length - min_length + 1
                elif min_length <= target_length <= max_length:
                    count += max_length - target_length + 1

                l += 1

        return count