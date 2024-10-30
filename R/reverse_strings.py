

# time complexity O(n)
# space complexity O(n)
# this slices the end of the string
def easy_reverse(str):
    return str[::-1]

print(easy_reverse("hello"))



# time complexity O(n)
# space complexity O(n)
def for_loop_reverse(string):
    return ''.join([string[i] for i in range(len(string) - 1, -1, -1)])
print(for_loop_reverse("hello"))


# time complexity O(n)
# space complexity O(n)
def rev_function(str):

    return ''.join(reversed(str))

print(rev_function("hello"))
