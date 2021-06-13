# Average Words Length

# For a given sentence, return the average word length. 
# Note: Remember to remove punctuation first.

sentence1 = "Hi all, my name is ishwar...I am originally from India."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"

def solution(sentence):
    for p in "!?',;.":
        sentence = sentence.replace(p, '')
    words = sentence.split()
    return round(sum(len(word) for word in words)/len(words),2) # {avg = sum of lenght of perticular word/total length} and round of this number with two decimal places
    
print(solution(sentence1))
print(solution(sentence2))