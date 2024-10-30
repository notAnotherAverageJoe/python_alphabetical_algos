def anagram_check(str1, str2):
    count1 = {}
    count2 = {}

    for i in range(len(str1)):
        count1[str1[i]] = count1.get(str1[i], 0) + 1

    for i in range(len(str2)):
        count2[str2[i]] = count2.get(str2[i], 0) + 1

        # this checks both sets of keys and counts
    return count1 == count2


print(anagram_check("hello", "bye"))
print(anagram_check("hello", "bye"))


# group together a list of anagrams like ["eat","tea", "bat","tab","waffle"]
def anagram_grouping(strings):
    if len(strings) == 0:
        return []

    if len(strings) == 1:
        return [strings]
    
    groupings = {}
    for string in strings:
        key = ''.join(sorted(string))
        if key not in groupings:
            groupings[key] = []
            
        groupings[key].append(string)
        
    return list(groupings.values())


# Example usage
print(anagram_grouping(["eat", "tea", "bat", "tab", "waffle"]))  
# Output: [['eat', 'tea'], ['bat', 'tab'], ['waffle']]
