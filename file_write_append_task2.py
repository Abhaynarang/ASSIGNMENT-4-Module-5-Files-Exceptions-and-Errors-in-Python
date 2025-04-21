# Step 1: Take user input and write it to a file
with open("output.txt", "w") as file1:
    user_input = input("Enter text to write to the file: ")
    file1.write(user_input + "\n")
    file1.close()

# Step 2: Append additional data to the same file
with open("output.txt", "a") as file1:
    additional_input = input("Enter additional text to append: ")
    file1.write(additional_input + "\n")
    file1.close()


# Step 3: Read and display the final content of the file
try:
    with open("output.txt", "r") as file:
        print("Final file content:")
        for line in file:
            print(line.strip())  # Removes extra whitespace or new lines
except FileNotFoundError:
    print("Error: The file 'output.txt' was not found.")
