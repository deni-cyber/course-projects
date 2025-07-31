#File Read & Write Challenge 🖋️: Create a program that reads a file and writes
#a modified version to a new file.


#creating a file containing some text
with open('input.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")
    file.write("Let's modify this content.\n")

# Reading the content from the input file
with open('input.txt', 'r') as file:
    content = file.read()

# Modifying the content
if content:
    modified_content = content.upper().replace(' ', '_')
    print(modified_content) #to show the modified content
    # Writing the modified content to the output file
    with open('output.txt', 'w') as file:
        file.write(modified_content)
        print("Modified content written to output.txt")
else:
    print("No content to modify.")

#: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
try:
    filename = input("Enter the filename to read: ")
    with open(filename, 'r') as file:
        content = file.read()
        print(f"Content of {filename}:\n{content}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except IOError:
    print(f"Error: The file '{filename}' cannot be read.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
# End of file_handler.py

