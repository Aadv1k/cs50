from cs50 import get_string

def main():
    text = get_string("Text: ")
    letters, words, sentences = count_text(text)
    grade = calculate_grade(letters, words, sentences)
    print_grade(grade)

def count_text(text):
    letters = sum(c.isalpha() for c in text)
    words = len(text.split())
    sentences = text.count('.') + text.count('!') + text.count('?')
    return letters, words, sentences

def calculate_grade(letters, words, sentences):
    L = letters / words * 100
    S = sentences / words * 100
    index = 0.0588 * L - 0.296 * S - 15.8
    return round(index)

def print_grade(grade):
    if grade < 1:
        print("Before Grade 1")
    elif grade >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")

if __name__ == "__main__":
    main()

