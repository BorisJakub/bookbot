def get_text_from_file(path): #function take as argument path to file and return text from file
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print("There is no such file, check the path!")
        return None
    except Exception as e:
        print(f"An error occured: {e}")
        return None

def count_word_in_text(text): # function take text as argument and count how many words is in
    w_count = text.split()
    return len(w_count)
    


def main():
    while True:
        name_of_book = input("Enter the name of the book from book directory: ").strip()
        book_to_open_path = f"books/{name_of_book}.txt"
        file_contents = get_text_from_file(book_to_open_path)
        if file_contents is None:
            print("The file could not be read.")

        elif len(file_contents) == 0:
            print("The file is empty !")

        else:
            print("File successfully read. Here are the contents:\n")
            print(file_contents)
            words_count = count_word_in_text(file_contents)
            print(f"Did you know this book have word number equal: ")
            print(words_count)

        another_book = input("Did you want open next books ? Y/n ").strip().lower()
        
        if another_book != "y":
            print("Oki Goodbye! :)")
            break

main()

