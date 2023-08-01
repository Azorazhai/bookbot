import string

with open("books/frankenstein.txt") as f:
    file_contents = f.read()

words = file_contents.split()

#print(words)

count = {k: 0 for k in string.ascii_lowercase}

def count_letters(file):
    for word in file:
        for letter in word.lower():
            if letter in string.ascii_lowercase:
                count[letter] += 1
    print(count)

count_letters(words)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{len(words)} words found in the document", end='\n\n')

for k, v in count.items():
    print(f"There {k} character was found {v} times")

print("--- End report ---")