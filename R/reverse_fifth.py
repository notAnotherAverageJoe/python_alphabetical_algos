# take a string : "hello world my name is joe"
# and check for each word in the strings length if its above or equal to 5, reverse it

def reverse_fifth(input_string):
    return [string[::-1] if len(string) >= 5 else string for string in input_string]
strings = ["hello", "world", "cat", "programming"]
print(reverse_fifth(strings))  # Output: ['olleh', 'dlrow', 'cat', 'gnimmargorp']


def reverse_fifth2(sentence):
    # if the input is hello world cat programming
    words = sentence.split()  # Split the sentence into words
    reversed_words = [word[::-1] if len(word) >= 5 else word for word in words]
    return ' '.join(reversed_words)  # Join the words back into a sentence

sentences= "hello world cat programming"
print(reverse_fifth2(sentences))


