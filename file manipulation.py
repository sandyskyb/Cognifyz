# Create a new file and write to it
with open('example.txt', 'w') as file:
    file.write('Hello, this is an example file.\n')

# Read from an existing file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Append to an existing file
with open('example.txt', 'a') as file:
    file.write('Appending new content to the file.\n')

# Read the file after appending
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
