def modify_text(text):
    return text.upper()


def main():
    filename = input("Enter the filename to read: ").strip()

    try:
        with open(filename, "r") as file:
            original_content = file.read()

        modified_content = modify_text(original_content)

        output_filename = "modified_" + filename
        with open(output_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Success! File was read and modified. Saved as: {output_filename}")

    except FileNotFoundError:
        print("Error: That file doesn’t exist. Make sure it's in the same folder and try again.")
    except PermissionError:
        print("Error: Permission denied. Try a different location or filename.")
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()

