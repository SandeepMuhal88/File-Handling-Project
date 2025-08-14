# First project
import os

#Create File
def create_file(filename):
    try:
        with open(filename, "w") as f:
            f.write("Hello, world!\n")
        print(f"File {filename} created successfully.")
    except IOError:
        print(f"Error: could not create file {filename}")

#Read File
def read_file(filename):
    try:
        with open(filename, "r") as f:
            contents = f.read()
            print(contents)
    except IOError:
        print(f"Error: could not read file {filename}")

# Add Text to File
def append_file(filename, text):
    try:
        with open(filename, "a") as f:
            f.write(text)
        print(f"Text appended to file {filename} successfully.")
    except IOError:
        print(f"Error: could not append to file {filename}")

# Rename the file
def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print(f"File {filename} renamed to {new_filename} successfully.")
    except IOError:
        print(f"Error: could not rename file {filename}")

#Delete the file
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File {filename} deleted successfully.")
    except IOError:
        print(f"Error: could not delete file {filename}")

# Find the word in file
def find_word(filename, word):
    try:
        with open(filename, "r") as f:
            contents = f.read()
            if word in contents:
                print(f"The word {word} found in file {filename}.")
            else:
                print(f"The word {word} not found in file {filename}.")
    except IOError:
        print(f"Error: could not read file {filename}")
        
# replace the word
def replace_word(filename, word, new_word):
    try:
        with open(filename, "r") as f:
            contents = f.read()
            if word in contents:
                new_contents = contents.replace(word, new_word)
                return
    except IOError:
            
        
            
            
# Delete the word


def menu():
    print("\nChoose an option:")
    print("1. Create a file")
    print("2. Read a file")
    print("3. Append to a file")
    print("4. Rename a file")
    print("5. Delete a file")
    print("Type 'exit' to quit")


if __name__ == "__main__":
    while True:
        menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            filename = input("Enter the filename to create: ")
            create_file(filename)

        elif choice == "2":
            filename = input("Enter the filename to read: ")
            read_file(filename)

        elif choice == "3":
            filename = input("Enter the filename to append: ")
            text = input("Enter the text to append: ")
            append_file(filename, text)

        elif choice == "4":
            filename = input("Enter the current filename: ")
            new_filename = input("Enter the new filename: ")
            rename_file(filename, new_filename)

        elif choice == "5":
            filename = input("Enter the filename to delete: ")
            delete_file(filename)

        elif choice.lower() == "exit":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")