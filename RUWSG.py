import os
import sys
import json
import random




print(
"██████╗ ██╗   ██╗███████╗███████╗██╗ █████╗ ███╗   ██╗   \n" 
"██╔══██╗██║   ██║██╔════╝██╔════╝██║██╔══██╗████╗  ██║    \n"   
"██████╔╝██║   ██║███████╗███████╗██║███████║██╔██╗ ██║      \n" 
"██╔══██╗██║   ██║╚════██║╚════██║██║██╔══██║██║╚██╗██║      \n" 
"██║  ██║╚██████╔╝███████║███████║██║██║  ██║██║ ╚████║      \n" 
"╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝      \n" 
"                                                                                \n"  
"██████╗ ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗ █████╗ ██████╗ ██╗   ██╗      \n" 
"██╔══██╗██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔══██╗██╔══██╗╚██╗ ██╔╝      \n" 
"██║  ██║██║██║        ██║   ██║██║   ██║██╔██╗ ██║███████║██████╔╝ ╚████╔╝       \n" 
"██║  ██║██║██║        ██║   ██║██║   ██║██║╚██╗██║██╔══██║██╔══██╗  ╚██╔╝        \n" 
"██████╔╝██║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║██║  ██║██║  ██║   ██║         \n" 
"╚═════╝ ╚═╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝         \n" 
"                                                                                 \n" 
" _ _ _           _        _____ _         _        _____                 \n" 
"| | | |___ ___ _| |___   |   __| |_ _ _ _| |_ _   |   __|___ _____ ___   \n" 
"| | | | . |  _| . |_ -|  |__   |  _| | | . | | |  |  |  | .'|     | -_|  \n" 
"|_____|___|_| |___|___|  |_____|_| |___|___|_  |  |_____|__,|_|_|_|___|  \n" 
"                                           |___|                         \n" 
"           \n" 
" |_        \n" 
" |_|  |/   \\n" 
"      /  :  \n" 
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓█░░░▓▓▓▒▒▒▓▓██▒▓▓█▓▓▓█████████████████████████████████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓█░░░▓█▒░▒░▓▓▓▓▓▒▓███▒█████████████████████████████████ \n" 
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓█░░░█▓▒▓▒▒░▒█▓▒▒▒████▓▓▓██████████████████████████████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░██▓▒░▒▒▓▓▓▒▓▓▓██▓▓████████████████████████████████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▓░░░███▒░▒░▓█▓█▓█▓████████████████████████████████████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓░░░▓▓▓▒░░░▒▒▒▒▓█▓▓▓██████████████████████████████████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒███████▓▒▒▓▓▓▓▒▒██▓▓▓▒█████████████████████████████████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓███████▓▓▓▓███▓▓▓▓█▒▓▓▓████████████████████████████████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓███████████████████▓▒██████████████████████████████████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒████████████▓██████▒█▓▓▓███████████████████████████████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒██████████▓░░░░████▓▓█▓████████▓████▓██████████████████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░▒███▓░░░░██▓░░░▒█████▓█████▓███████▓█████▓██████████████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░███▒░░░▓█████████████████▓▓███▓▓█████▓█████████████████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░▓████████████████████████▓█▓▓▓▓████████████████████████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓███████████████████████████▓▓█████████████████████████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒██████████████████████▓▓▓▓▓█▓████████████████████████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░▒▓█░█████████████████████▓▓▓▓▓▓██████████████████████████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓░▒▒▒▓███████████▓▓█████▓▓▓▓▓██████████████████████████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓░░▒█▒▓█▓███████████████▓▓▓▓▓██████████████████████████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██▒░░▒▓▓▒████▓▓██████▓███▓▓█████▓███████████████████████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓██▒░░░▓▓▓▒█████████████▓░░░▓▓▓▒░░░▓████████████████████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒███▓█▓▓▒░▒▓██▓▓▓███▓▓▓▓████░░░▒███▓▒▓░░░▓▒████████████████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓███▒▓▓▓▓▒░▒██▓▒▒▓█▓▒▒███▓███▒░░░██▓██▓█░▓▒░▒░▒█████▒███████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒█████░▒▓█▓▓██▓▓▓▓▒▒████▓▓▓█▓░░░▓▒▓▓▓░█▓█▒░▒░▒▓▓▓█▓▓███████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒███▓▓▓███▓▓█▓▓▒▒▒▒███▒▒█▓█░░░▒░▒░█▓█▓▓░░░░▒▓█▓█▓████████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▒▓█▓▓▓▒▓▓▒▒▓▓█▓▓▓▓▓▒███▒▓█▒▓███▒░░░▒▓▓███▓▓░░░░▒▓▓▒░░▒▓██████ \n"
" ░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓░░░░░░░▒▒▓▓░░░▓░░▓▓██▓▒░▒█▓▓██▒░░░▓▓▓███▓▒▒▒▓▓▓▓▓█▓██▓██████ \n"
" ░░░░░░▒▒▒▒▒▒▓▓▓▒░░░░░░░░▒▒▒▓░▒▒▒▓░▒▓▓▓█▓▓▓▒░░░░░░░▒▓▒░░░▓▓██▓░░░▒▓▓████▓██▓▓▒▒▓█▓▒███████▓ \n"
" █████████████▒░░░░░░░░▓▓▓▓▓▓▓██▓▓▓█████▓▒███▒▓█▓▒▓░░░░░░░░▒██░░░░██████████▓▓████▓▓█████▓█ \n"
" ██████████▓▒▒░░░░░░░░░░▒▒▒█████▓▓█████████████▒░▒▒░░▓░░░░░█░▒░░░░▓▒█████████████▓▓▓▓▓█████ \n"
" █████████▓░░░░░░░░░░▒▓▒▓▓███████▓██████████▒░░░░░░▓▒▒▓░░▒▒▓▒▒▒░░░▒██▓█████████████▓▓▓▒▒▓▓█ \n"
" ████████░░░░░░░░░░▓▓▓▓▓▓█████████▒▓███████▒░░░░░▒▓▒▒██▓▓▓█▓▓▓░▓▒░░███████████████████▒▓▓██ \n"
" ████▓▓▓▓░░░░░░░░░░▒▒▓▓▓▓▓███████▒▓█████▓▒░░░▒░▒███▓▓▓██▓▒▒░░▓░░▓▓░░██▓▓▓████▓░▒▒▓▒▒▓██████ \n"
" ▓▓▓▒░▒▓▓░░░░░░░░░░░▒▓▓█▓██████████████▒░░░▒▒░▓█████▓█▓▓██▒▒▒▓█▒░░▒▒▓█████▓▒░░▒▓████▓▓█▓▓▓▓ \n"
" ▒▒▒░░▒░▒░░░░░░░▒▓█▒░▓███▓▓▓██████▓▒█▒░░░▒▒░▓█████████▓▓▓▒░▓▓▒▒▒░█▒░▒▒▓██▓██▓▒█▒▓░░░▒▓▓████ \n"
" ░░░░░░░░░░░░░░█▓▒▒░▓█████████████▓███▓▒▒▒▓███████████░░░▒▒█▓░░▓██▓█▒▒▒░░░▒▒▓███▓▒█████████ \n"
" ░░░░░░▒▒░░░░░████▓████▓██████████▒▓████▓███████████▓░░░██▓▓▓▒░██▓▓▒▒▓▓█▒▒██▒██████████████ \n"
" ░░░░░░░░░░░░░██▓██████████████████████████████████▓▒░░▒████████▓█████▓▓▓██████████████████ \n"
" ░░░░░░░░░░░░░▓█▓██████████▒▒█████▓▒▒▓██▓████████▓░░▓▓███▓██▓▓█████████████████████████████ \n"
" ░░░░░░░░░░░░░▓████████████░▓████▒▒▒▒▓██▓██████▓▓█▓▓██████▓▓▓█▓██████▓████████████████████▓ \n"
" ▓███▓▓▒▒░░░░░▓████████████░▓████░▒▒██████████▒██████████████████████▓▒█████████████████▓██ \n"
" ░░░░▒▒▓████▓▓▒▓██████████▓░▓███████████████████████████████████████▓▓▒▓▒██████████▓███████ \n"
" ░░░░░░░░░░░░▒▓▓██████████▒░███████████████████████████████████████▓█▓██▓▒▓███████▓░███████ \n"
" ░░░░░░░░░░░░░░░░░░▒▒▒▓▓█▓▒█████████████████████████████████████████████▒▒▒▒██████▒░██▓▓███ \n"
" ░░░░░░▒▒░░░░░░░░░░░░░░░░░▒▓████████▓████████████████████████████████▓███▓░▒▓████▓░░███████ \n"
"                                                                                            \n"
"_//                            _//                  _//                                     \n"
"_//                            _//                  _//                                     \n"
"_//  _//_/ _///_//     _//     _//_//     _//_/ _///_//  _//                                \n"
"_// _//  _//    _//   _//  _// _// _//   _//  _//   _// _//                                 \n"
"_/_//    _//     _// _//  _/   _//  _// _//   _//   _/_//                                   \n"
"_// _//  _//      _/_//   _/   _//   _/_//    _//   _// _//                                 \n"
"_//  _//_///       _//     _// _//    _//    _///   _//  _//                                \n"
"                                                                                            \n"
)



# Menu inicial
def main_menu():
    print(
        " \n"
        "______________________________________________ \n"
        " \n"
        "░█▄█░█▀█░▀█▀░█▀█░░░█▄█░█▀▀░█▀█░█░█ \n"
        "░█░█░█▀█░░█░░█░█░░░█░█░█▀▀░█░█░█░█ \n"
        "░▀░▀░▀░▀░▀▀▀░▀░▀░░░▀░▀░▀▀▀░▀░▀░▀▀▀ \n"
        "______________________________________________ \n"
        " \n"
        "1. Start game \n"
        "2. See words and their translations \n"
        "3. Instructions \n"
        "4. Contribute/Donate \n"
        "5. Exit \n"
        "_____________________________________________ \n"
    )
    option_choice = input("Type the option number you want and press enter: \n")
    print("-------------------------------------------------------- \n")
    return option_choice


def resource_path(relative_path):
    # Retorna o caminho absoluto ao rodar como script ou executável.
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)  # PyInstaller
    return os.path.join(os.path.abspath("."), relative_path)


# Seleção de dificuldade
def select_difficulty():
    level_choice = input("Choose your difficulty: \n")

    base_path = resource_path("data")
    level_files = {
        "A1": os.path.join(base_path, "A1.json"),
        "A2": os.path.join(base_path, "A2.json"),
        "B1": os.path.join(base_path, "B1.json"),
        "B2": os.path.join(base_path, "B2.json"),
        "C1": os.path.join(base_path, "C1.json"),
        "C2": os.path.join(base_path, "C2.json")
    }


    messages = {
        "A1": (
            " \n"
            "░█▀█░▀█░░░░░░░█▀█░█▀█░█▀█░█▀▄   \n"
            "░█▀█░░█░░░░░░░█░█░█░█░█░█░█▀▄ \n"
            "░▀░▀░▀▀▀░▀░░░░▀░▀░▀▀▀░▀▀▀░▀▀░ \n"
        ),
        "A2": (
            " \n"
            "░█▀█░▀▀▄░░░░░░█▀▄░█▀▀░█▀▀░█▀▀░▀█▀░█▀█░█▀▀░█▀▄ \n"
            "░█▀█░▄▀░░░░░░░█▀▄░█▀▀░█░█░█░█░░█░░█░█░█▀▀░█▀▄ \n"
            "░▀░▀░▀▀▀░▀░░░░▀▀░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀ \n"
        ),
        "B1": (
            " \n"
            "░█▀▄░▀█░░░░░░░▀█▀░█▀█░▀█▀░█▀▀░█▀▄░█▄█░█▀▀░█▀▄░▀█▀░█▀█░▀█▀░█▀▀ \n"
            "░█▀▄░░█░░░░░░░░█░░█░█░░█░░█▀▀░█▀▄░█░█░█▀▀░█░█░░█░░█▀█░░█░░█▀▀ \n"
            "░▀▀░░▀▀▀░▀░░░░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀░░▀▀▀░▀░▀░░▀░░▀▀▀ \n"
        ),
        "B2": (
            " \n"
            "░█▀▄░▀▀▄░░░░░░█▀█░█▀▄░█░█░█▀█░█▀█░█▀▀░█▀▀░█▀▄ \n"
            "░█▀▄░▄▀░░░░░░░█▀█░█░█░▀▄▀░█▀█░█░█░█░░░█▀▀░█░█ \n"
            "░▀▀░░▀▀▀░▀░░░░▀░▀░▀▀░░░▀░░▀░▀░▀░▀░▀▀▀░▀▀▀░▀▀░ \n"
        ),
        "C1": (
            " \n"
            "░█▀▀░▀█░░░░░░░█▀▀░█░░░█░█░█▀▀░█▀█░▀█▀ \n"
            "░█░░░░█░░░░░░░█▀▀░█░░░█░█░█▀▀░█░█░░█░ \n"
            "░▀▀▀░▀▀▀░▀░░░░▀░░░▀▀▀░▀▀▀░▀▀▀░▀░▀░░▀░ \n"
        ),
        "C2": (
            " \n"
            "░█▀▀░▀▀▄░░░░░░█▀▀░█░█░█▀█░█▀▀░█▀▄░▀█▀ \n"
            "░█░░░▄▀░░░░░░░█▀▀░▄▀▄░█▀▀░█▀▀░█▀▄░░█░ \n"
            "░▀▀▀░▀▀▀░▀░░░░▀▀▀░▀░▀░▀░░░▀▀▀░▀░▀░░▀░ \n"
        )
    }

    if level_choice in level_files:
        print(messages[level_choice])
        with open(level_files[level_choice], encoding='utf-8') as words:
            RU = json.load(words)
        return RU
    else:
        print("Invalid difficulty level. Please choose A1, A2, B1, B2, C1, or C2.")
        return None


# Função para iniciar o jogo
def start_game(RU):
    correct_count = 0
    incorrect_count = 0

    print(
        " \n"
        "░█▀▀░█▀█░█▀█░█▀▄░░░█▀▀░█▀█░█▄█░█▀▀░█░█░█ \n"
        "░█░█░█░█░█░█░█░█░░░█░█░█▀█░█░█░█▀▀░▀░▀░▀ \n"
        "░▀▀▀░▀▀▀░▀▀▀░▀▀░░░░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀ \n"
    )

    while True:
        print("---------------------------------------- \n")
        aleatorio = random.choice(RU)

        print(aleatorio['palavra'])
        resposta = input("The translation is: \n")
        print(" \n")

        if resposta == aleatorio['tradução']:
            print("Correct!!!")
            correct_count += 1
        else:
            print(f"Error!!! ... Correct Answer: {aleatorio['tradução']}")
            incorrect_count += 1

        print(" \n")
        print(f"Correct answers: {correct_count} | Incorrect answers: {incorrect_count}")
        print("-------------------------------------- \n")

        if input("Press Enter to continue or 'N' to go back to the menu \n").lower() == 'n':
            break  # Sai do loop do jogo

# Função para exibir palavras e traduções
def see_words(RU):
    for word in RU:
        print(word['palavra'], "=", word['tradução'])
    input("\nPress Enter to go back to the main menu.\n")

# Função para mostrar instruções
def instructions():
    print(
        " \n"
        "░▀█▀░█▀█░█▀▀░▀█▀░█▀▄░█░█░█▀▀░▀█▀░▀█▀░█▀█░█▀█░█▀▀ \n"
        "░░█░░█░█░▀▀█░░█░░█▀▄░█░█░█░░░░█░░░█░░█░█░█░█░▀▀█ \n"
        "░▀▀▀░▀░▀░▀▀▀░░▀░░▀░▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀░▀░▀▀▀ \n"
        " \n"
        "To begin with, you need to understand that the words are divided into blocks of \n"
        "difficulty, which are: \n"
        " \n"    
        "A1: Noob \n"
        "A2: Beginner \n"
        "B1: Intermediate \n"
        "B2: Advanced \n"
        "C1: Fluent \n"
        "C2: Expert \n"
        "  \n"
        "It is recommended that you start by first studying the words and their translations, you will  \n"
        "find it in option 2 of the main menu, when you enter you choose the difficulty level of the  \n"
        "words and then all the words will appear with their respective translations of the chosen  \n"
        "level. \n"
        "  \n"
        "If you have already studied and are ready to start, start the game in option 1 of the main  \n"
        "menu, then choose the difficulty level of the words. The words in Russian will be displayed  \n"
        "randomly and you must type the answer correctly according to the order and writing seen in  \n"
        "option 2 of the main menu. \n"
    )
    input("\nPress Enter to go back to the main menu.\n")

# Função para mostrar opção de contribuição
def contribute():
    print(
        " \n"
        "░█▀▀░█▀█░█▀█░▀█▀░█▀▄░▀█▀░█▀▄░█░█░▀█▀░█▀▀░░░█░█▀▄░█▀█░█▀█░█▀█░▀█▀░█▀▀ \n"
        "░█░░░█░█░█░█░░█░░█▀▄░░█░░█▀▄░█░█░░█░░█▀▀░▄▀░░█░█░█░█░█░█░█▀█░░█░░█▀▀ \n"
        "░▀▀▀░▀▀▀░▀░▀░░▀░░▀░▀░▀▀▀░▀▀░░▀▀▀░░▀░░▀▀▀░▀░░░▀▀░░▀▀▀░▀░▀░▀░▀░░▀░░▀▀▀ \n"
        " \n"
    )
    print("Bitcoin: bc1qs4mfwfl26wtzzj09tqk4ssxes789eervuwrrd4 \n")
    print("ETH: 0x23c2F6B72147e82bc47b2a0bD606B4bfC75F9023 \n")
    print("Solana: EZGzyto7XMjNZ2iymMSqT9UFZwCR8qFdjTWDMedGgS2c \n")
    print("XMR: 49k3xgJ5uKFNb4Lzi6kZCTc2zPxp5B7FadSvwjut1QB79wD3DmmMw4UFxF1oaeHQPA7VERj8YwvCRYwNW784coCFTnwERt5 \n")
    print(" \n")
    input("Press Enter to go back to the main menu.\n")

# Execução do programa principal
while True:
    choice = main_menu()
    
    if choice == '1':
        RU = select_difficulty()
        if RU:
            start_game(RU)
    elif choice == '2':
        RU = select_difficulty()
        if RU:
            see_words(RU)
    elif choice == '3':
        instructions()
    elif choice == '4':
        contribute()
    elif choice == '5':
        print(
            " \n"
            "░█▀▀░█░█░▀█▀░▀█▀░▀█▀░█▀█░█▀▀░░░█▀█░█▀▄░█▀█░█▀▀░█▀▄░█▀█░█▄█ \n"
            "░█▀▀░▄▀▄░░█░░░█░░░█░░█░█░█░█░░░█▀▀░█▀▄░█░█░█░█░█▀▄░█▀█░█░█ \n"
            "░▀▀▀░▀░▀░▀▀▀░░▀░░▀▀▀░▀░▀░▀▀▀░░░▀░░░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░▀ \n"
            "░█▀▀░█▀█░█▀█░█▀▄░█▀▄░█░█░█▀▀░█░█░█                         \n"
            "░█░█░█░█░█░█░█░█░█▀▄░░█░░█▀▀░▀░▀░▀                         \n"
            "░▀▀▀░▀▀▀░▀▀▀░▀▀░░▀▀░░░▀░░▀▀▀░▀░▀░▀ \n"
        )
        break
    else:
        print("Invalid option. Please choose a number between 1 and 5.\n")

