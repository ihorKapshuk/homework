my_string = "one one one two two three"
my_list = my_string.split(" ")
my_dict = {}
counter_of_words = list(set(my_list))

for word in counter_of_words:
    my_dict[word] = my_string.count(word)

print("Речення : ", my_string)
print("Словник з унікальними словами та їх кількістю в реченні : ", my_dict)