#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns the number of characters written.

    Args:
        filename (str): Name of the file to write.
        text (str): Text to write to the file.

    Returns:
        int: Number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
