import pandas as pd


df_morse = pd.read_csv("data/morse.csv", index_col=0)
df_phonetic = pd.read_csv("data/phonetic_alphabet.csv", index_col=0)


def morse(text):
    """Recebe como argumento uma string e a retorna convertida em código morse"""
    text_list = list(text.upper())
    return " ".join([df_morse["Morse"][letter] if letter in df_morse.index else letter for letter in text_list])


def phonetic_alphabet(text, phonetic_alpha):
    """Recebe como argumento uma string e um integer, com o qual será selecionado a coluna correspondente
    ao tipo de alfabeto de soletração selecionado. Retorna a string soletrada"""
    text_list = list(text.upper())
    chosen_col = df_phonetic.iloc[:, phonetic_alpha - 1]
    return ", ".join([chosen_col.loc[letter] if letter in chosen_col.index else letter for letter in text_list])


def finish():
    """Retorna False caso o usuário não queira mais converter nenhum texto. True caso queira continuar."""
    out = input("Você gostaria de sair? (S/N)\n").upper()
    while out != "S" and out != "N":
        out = input("Digite S ou N para sair ou não.\n").upper()
    return out == "N"


options = ["1", "2", "3", "4", "5", "6"]

print("Bem-vindo ao conversor de texto em Morse e em Alfabeto Fonético.")

on = True
while on:
    user_choice = input("Escolha a codificação:\n1 - Morse\n2 - Alfabeto Fonético\n")
    while user_choice not in options[:2]:
        user_choice = input("Não há essa opção.\nEscolha entre 1 e 2:\n1 - Morse\n2 - Alfabeto Fonético\n")

    if user_choice == "1":
        text = input("Digite o seu texto:\n")
        morse_code = morse(text)
        print(morse_code)

    elif user_choice == "2":
        phonetic_alpha_choice = input("Escolha o tipo de alfabeto:\n1 - Otan,\t2 - Inglês,\t"
                                      "3 - Americano,\t4 - Italiano,\t5 - Alemão,\t6 - Internacional\n")
        while phonetic_alpha_choice not in options:
            phonetic_alpha_choice = input("Não há essa opção.\nEscolha entre 1 a 6:\n1 - Otan,\t2 - Inglês,\t"
                                          "3 - Americano,\t4 - Italiano,\t5 - Alemão,\t6 - Internacional\n")

        text = input("Digite o seu texto:\n")
        phonetic_alpha_choice = int(phonetic_alpha_choice)
        phone_code = phonetic_alphabet(text, phonetic_alpha_choice)
        print(phone_code)

    on = finish()
