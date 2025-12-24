print(str(input("What is the string to reverse? ")[::-1]))

# Alternative implementation without slicing
text = input("Enter a string: ")

reversed_text = ""

for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]

print(reversed_text)
