import sys

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return len([line for line in lines if not is_comment_or_blank(line)])
    except FileNotFoundError:
        sys.exit("File does not exist")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")

def is_comment_or_blank(line):
    cleaned_line = line.strip()
    return cleaned_line == '' or cleaned_line.startswith('#') or cleaned_line.startswith('"""') or cleaned_line.startswith("'''")

def count_lines_exclude_docstrings(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            in_docstring = False
            return len([line for line in lines if not is_comment_or_blank(line, in_docstring)])
    except FileNotFoundError:
        sys.exit("File does not exist")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")

def is_comment_or_blank(line, in_docstring):
    cleaned_line = line.strip()

    if in_docstring:
        if cleaned_line.endswith('"""') or cleaned_line.endswith("'''"):
            in_docstring = False
        return True
    else:
        if cleaned_line.startswith('"""') or cleaned_line.startswith("'''"):
            in_docstring = True
        return cleaned_line == '' or cleaned_line.startswith('#')

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")

    file_path = sys.argv[1]
    
    if not file_path.endswith('.py'):
        sys.exit("Not a Python file")

    lines_count = count_lines_exclude_docstrings(file_path)
    print(lines_count)

if __name__ == "__main__":
    main()
