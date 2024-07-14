def get_text_from_file(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print("There is no such file, check the path!")
        return None
    except Exception as e:
        print(f"An error occured: {e}")
        return None

def text_to_list(book_text):
    w_count = book_text.split()
    return len(w_count)
    


def main():
    while True:
        name_of_book = input("Enter the name of the book from book directory: ").strip()
        book_to_open_path = f"books/{name_of_book}.txt"
        file_contents = get_text_from_file(book_to_open_path)
        if file_contents:
            print("File successfully read. Here are the contents:\n")
            print(file_contents)
            words_count = text_to_list(file_contents)
            print(f"Did you know this book have word number equal: ")
            print(words_count)
        if len(file_contents) == 0:
            print("The file is empty")
        another_book = input("Did you want open next books ? Y/n ").strip().lower()

        if another_book != "y":
            print("Oki Goodbye! :)")
            break

main()

