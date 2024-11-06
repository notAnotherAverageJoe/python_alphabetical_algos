def find_needle(haystack):
    target = "needle"
    for i in range(len(haystack)):
        if haystack[i] == target:
            return f"Found the needle at position {i}"

def find_needle2(haystack):
    return f"Found the needle at position {haystack.index('needle')}"


haystack = ["hay", "straw", "grass", "needle", "more hay"]

print(find_needle(haystack))     # Should output: Found the needle at position 3
print(find_needle2(haystack))    # Should output: Found the needle at position 3
