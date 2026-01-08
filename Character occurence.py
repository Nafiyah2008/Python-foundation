word = input("What word? ")
letter = input("What letter? ")
i = 0
count = 0
while i < len(word):
    if word[i] == letter:
        count += 1
    i += 1
print("Total number of times" ,letter ,"has occured" ,count)