# make a function that founds frequencies of words within a string

def freq_counter(str):
    counter = {}
    
    words = str.split(' ')
    
    for i in range(len(words)):
        counter[words[i]]=  counter.get(words[i],0) + 1
        
    return counter
    
    


def freq_counter2(str):
    counter = {}
    words = str.split(' ')
    
    for word in words:
        counter[word] = counter.get(word, 0) + 1
        
        
    return counter
sentence = "this is the testing line that will check the frequency counts within the sentence"

print(freq_counter(sentence))
print("----------------------------------------")
print(freq_counter2(sentence))

# {'this': 1, 'is': 1, 'the': 3, 'testing': 1,
# 'line': 1, 'that': 1, 'will': 1, 'check': 1,
# 'frequency': 1, 'counts': 1, 'within': 1, 'sentence': 1}
