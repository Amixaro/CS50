def main():
    user_input = input("enter a text: ")
    output = shorten(user_input)
    print("new text:" + output)


def shorten(word):
    vowels = "AEIOUaeiou"
    result = "".join(char for char in word if char not in vowels)
    return result



if __name__ == "__main__":
    main()
