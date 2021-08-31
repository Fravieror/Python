# File error
# with open("a_file.txt") as file:
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    value = a_dictionary["non_existent_key"]
except FileNotFoundError:
    # Create file from scratch
    file = open("a_file.txt", "w")
    file.write("Something")
    # error_message catch the name of variable that cause the error
except KeyError as error_message:
    print(f"The key {error_message} error getting ")
# else is executed when does not exists exception
else:
    content = file.read()
    print(content)
finally:
    file.close()

# Kinds of errors
# # Key error
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]
#
# # IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]
#
# # Type error
# text = "abc"
# print(text + 5)
