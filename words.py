import pyautogui
import time

with open("dict.txt", "r") as dict_file:
    word_list = dict_file.read().splitlines()
    
mainly_used_words = []
used_words = {}

def find_words_with_combination(letter_combination):
    return [word for word in word_list if letter_combination.lower() in word.lower()]

def click_at_position(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    
def type_word(word):
    pyautogui.write(word, interval=0.1)
    pyautogui.press('enter')
    
def main():
    i = 1
    while True:
        letter_combination = input("Enter a letter combination: ")
        matching_words = find_words_with_combination(letter_combination)
        
        if not matching_words:
            print(f"No words found containing {letter_combination}")
        else:
            if letter_combination in used_words.keys():
                used_words[letter_combination][0] -= 1
            else:
                matching_words = [word for word in matching_words]
                matching_words.sort(key=len)
                used_words[letter_combination] = [-1, matching_words]

            while used_words[letter_combination][1][used_words[letter_combination][0]] in mainly_used_words:
                used_words[letter_combination][0] -= 1
            mainly_used_words.append(used_words[letter_combination][1][used_words[letter_combination][0]]
                                     )
            print(f"{i}. found word {used_words[letter_combination][1][used_words[letter_combination][0]]}")        
            click_at_position(1500, 1000) # other part
            type_word(used_words[letter_combination][1][used_words[letter_combination][0]])
            click_at_position(500, 1000) # terminal
        
        i += 1
            
if __name__ == '__main__':
    main()

    # with open("dict.txt", "w") as dict_file:
    #     for word in word_list:
    #         dict_file.write(word + "\n")