import sys

def remove_trailing_chars(file_path, char_to_remove):
    # Read the content from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Process the content
    processed_lines = [line.rstrip(char_to_remove).rstrip() + '\n' for line in lines]

    # Write the processed content back to the same file
    with open(file_path, 'w') as file:
        file.writelines(processed_lines)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python rmlinsfx.py <file_path> <char_to_remove>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    char_to_remove = sys.argv[2]

    remove_trailing_chars(file_path, char_to_remove)
    print(f"Processed file '{file_path}'.")
