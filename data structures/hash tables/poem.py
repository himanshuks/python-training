# Program to count occurrences of word reading from file

words_dict = {}

with open(
    "D:\\visual studio\\python practice\\data structures\\hash tables\\poem.txt"
) as f:

    for line in f:
        tokens = line.split(" ")

        # Token will store items in LIST format
        for x in tokens:

            # Replace the next line from each ITEM of LIST
            x = x.replace("\n", "")

            # Check if it is present WORDS DICTIONARY
            # Based on that increase the counter
            if x in words_dict:
                words_dict[x] += 1
            else:
                words_dict[x] = 1


print(words_dict)
