import emoji

if __name__ == "__main__":
    user_input = input("Input: ")
    print("Output:", emoji.emojize(user_input, language='alias'))
