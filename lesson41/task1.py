from module import Stack
from string import ascii_lowercase as ab

my_stack = Stack()
letters = [*ab]
result = []

for letter in letters:
    my_stack.push_item(letter)

print("Full stack : ", my_stack.show_items())

while my_stack.is_empty() == False:
    result.append(my_stack.get_item())

print("Reverse string : ", result)
print("Empty stack : ", my_stack.show_items())