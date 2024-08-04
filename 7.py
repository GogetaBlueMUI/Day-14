def conversion(str):
    cleaned=""
    for char in str:
        if char.isalpha():
            cleaned+=char
    return cleaned
def freq(str):
    frequency = {}
    for char in str:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
str1=input("Enter a first string: ")
str2=input("Enter a second string: ")
first = conversion(str1).lower()
second = conversion(str2).lower()
print("Cleaned first string: ", first)
print("Cleaned first string: ", second)
freq1=freq(first)
freq2=freq(second)
print("Freqeuncy of first string: ", freq1)
print("Freqeuncy of second string: ", freq2)
if freq1==freq2:
    print("They are anagrams to each other.")
else:
    print("They are not anagrams to each other.")