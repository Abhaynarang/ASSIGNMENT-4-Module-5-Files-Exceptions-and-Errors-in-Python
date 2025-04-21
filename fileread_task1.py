try:
    # Open the file in read mode
    with open("sample.txt", "r") as file:
        print("Reading file content:")

        # Read and print each line from the file
        for line in file:
            print(line.strip())  # Removes extra whitespace or newline characters

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
    