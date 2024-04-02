# File Creation
try:
    # Create a new text file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write at least three lines of text to the file
        file.write("Hello, am Clement juma, Full-Stack Developer\n")
        file.write("2024\n")
        file.write("Am also a freelancer\n")
except PermissionError:
    print("Permission denied. Unable to create file.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File creation process completed.")

# File Reading and Display
try:
    # Open "my_file.txt" in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read and display the contents of the file
        print("Contents of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File reading process completed.")

# File Appending
try:
    # Open "my_file.txt" in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the existing content
        file.write("Fourth line\n")
        file.write("Fifth line with a number: 456\n")
        file.write("Sixth line\n")
except PermissionError:
    print("Permission denied. Unable to append to file.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File appending process completed.")