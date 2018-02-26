#Practical 35: Count numbers of vowels
#https://stackoverflow.com/questions/19967001/count-vowels-in-string-python

sentence = input("Sentence: ")

counts = { i : 0 for i in 'aeiouAEIOU'}
for char in sentence:
    if char in counts:
        counts[char] += 1
        
for k,v in counts.items():
    print(k, v)