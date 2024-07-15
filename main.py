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
    
def count_characters(text):
    try:
        text_to_lower = text.lower() # this variable have a full text whih every word is lower_case
        char_dict = {}
        for character in text_to_lower:
            if character.isalpha():
                if character in char_dict:
                    char_dict[character] +=1
                else:
                    char_dict[character] = 1
        return char_dict
    except Exception as e:
        print("i cant do count character function to None-Value")

def sort_on(dict):
    return dict["num"]
def create_raport(file_name):
    new_files = open(f"book_raports/{file_name}_raport.txt", mode='w+')
    return new_files

def main():
    import os
    while True:
        name_of_book = input("Enter the name of the book from book directory: ").strip()
        book_to_open_path = f"books/{name_of_book}.txt"
        fpath=f"book_raports/{name_of_book}_raport.txt"
        file_contents = get_text_from_file(book_to_open_path)
        if file_contents != None and len(file_contents) != 0:
            print("File successfully read. Here are the contents:\n")
            words_count = count_word_in_text(file_contents)
            print(f"Did you know this book have word number equal: ")
            print(words_count)

            results = count_characters(file_contents) #dictonary [key = value] ket--character value--count_character
            print(results)
            print(f"This is the report of the {name_of_book} content: ")
            print(f"{words_count} words found in the document")
            char_count_list = []

            for klucz, wartosc in results.items():  #dla kazdego Key, value in dict result".items() pozwala na dostep do wiecej niz 1 wartsoci"
                char_count = {"char": klucz, "num": wartosc}
                char_count_list.append(char_count)

            char_count_list.sort(reverse=True, key=sort_on)

            for each in range (0, len(char_count_list)):
                print(char_count_list[each])

            print("End of report")
            write_raport = input("Did you want to save this raport: Y/n ").strip().lower()
            raports_contents = get_text_from_file(fpath)

            if write_raport == "y":
                isExist = os.path.exists(fpath)
                if isExist == True and len(raports_contents) != 0:
                    overwrite = input("Hmm its seems a raport is already exist and its not empty do you want to overwrite him ? Y/n ").strip().lower()

                if write_raport =="y" or isExist == False:
                    new_raport =create_raport(name_of_book)
                    new_raport.write("Character Counts: \n")
                    for each in range (0, len(char_count_list)):
                        new_raport.write(str(char_count_list[each])+ "\n")
                    new_raport.write("Words Counts: \n" + str(words_count))
                    new_raport.close()  
            else:
                print("ok maybe next time :P")
        elif file_contents != None and len(file_contents) == 0:
            print("File exist but its empty !")
        
        another_book = input("Did you want open next books ? Y/n ").strip().lower()
        if another_book != "y":
            print("Oki Goodbye! :)")
            break
    
        
    
        
        
main()

