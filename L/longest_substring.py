def longest_substring(s):
    longest = ""  # Store the longest substring without repeating characters
    char_counter = {}  # Dictionary to keep track of the last seen index of each character
    start = 0  # Starting index of the current substring

    for i in range(len(s)):
        # If the character is already in the dictionary and is part of the current substring
        if s[i] in char_counter and char_counter[s[i]] >= start:
            # Move the start index just after the last occurrence of the current character
            start = char_counter[s[i]] + 1

        # Update the last seen index of the character
        char_counter[s[i]] = i

        # Check if the current substring is the longest
        if i - start + 1 > len(longest):
            longest = s[start:i + 1]  # Update the longest substring

    return longest

# Example usage
input_string = "abcabcbb"
print(longest_substring(input_string))  # Output: "abc"
