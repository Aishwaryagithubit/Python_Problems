def words(input_str):
     return len(input_str.split())

input_str = "If you count the words in this sentence you will get twelve"
num_words = words(input_str)
print("Number of words:",num_words)
