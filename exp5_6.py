input_sentence = input("Enter a sentence: ")

words = input_sentence.split()

unique_words = set(words)

unique_words_count = len(unique_words)

print(f"The number of unique words in the given sentence is: {unique_words_count}")
