# Question 3: Write a Python program to reverse a string using a stack (using array).
def reverse_string_using_stack(string):
    stack = list(string)  # Using a list as a stack
    reversed_string = ""

    while stack:
        reversed_string += stack.pop()

    return reversed_string


# Demonstration of string reversal
original_string = "hello"
reversed_string = reverse_string_using_stack(original_string)
print(f"Original String: {original_string}")
print(f"Reversed String: {reversed_string}")