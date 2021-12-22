#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

from ascii import *

welcome_message = "W wigilijny wieczór w swoim mieszkaniu oczekujesz na swój prezent. Nagle staje przed" \
                  " tobą Nieśmiałek-Sfinks i mówi:\n" \
                  "ABY OTRZYMAĆ, MUISZ WYBRAĆ.\n" \
                  "MIAU.\n" \
                  "ABY WYBRAĆ, MUISZ WIEDZIEĆ, CO WYBIERASZ.\n" \
                  "MIAU.\n" \
                  "BY WIEDZIEĆ CO WYBIERASZ, ODPOWIEDZ NA PYTAŃ SZEŚĆ.\n" \
                  "SZEŚĆ PYTAŃ ODSŁONI TWOJE PRZEZNACZENIEEEE! UUUU!!!\n" \
                  "MIAU! MIAU! POWODZEEENIA!"

bad_response = f"{paws}\n\t\tMIAU MIAU... ŹLE!!!\n\t\t{kitty_bad}\n\n\t\tSPRÓBUJ PONOWNIE\n{paws}"

questions_and_replies = {
    "1": {"question": "Jak nazywa się posiadłość, którą Geralt otrzymał od Anny Henrietty w Toussaint?",
          "answer": f"Corvo Bianco",
          "reply": f"\n{paws}\n\t\t{kitty_good}\n{paws}\n\t\tSUPER! MIAU! DO KOLEJNEGO PYTANIA!\n{paws}"},
    "2": {"question": "Jaki był oryginalny tytuł 'Tamtych dni, tamtych nocy'?",
          "answer": "Call Me By Your Name",
          "reply": f"\n{paws}\n\t\t{kitty_good}\n{paws}\n\t\tCORAZ LEPIEJ!!! MIAU MIAU!\n{paws}"},
    "3": {"question": "Kto grał Ciri w polskim (najlepszym!) serialu 'Wiedźmin'?",
          "answer": "Marta Bitner",
          "reply": f"{paws}\n\t\t{kitty_good}\n{paws}\n\t\tTRZY ZA TOBĄ, JESZCZE TRZY DO KOŃCA! MIAU!\n{paws}"},
    "4": {"question": "Jak można przetłumaczyć źródłosłów nazwy Skellige?",
          "answer": "Kamień Skała Cliff Rock",
          "reply": f"{paws}\n\t\t{kitty_good}\n{paws}\n\t\tJESTEŚ DIAMENTEM MIAU MIAU!!!\n{paws}"},
    "5": {"question": "Na zabudowie jakiego polskiego miasta wzorowane jest Beauclair?",
          "answer": "Zamość Zamościa",
          "reply": f"{paws}\n\t\t{kitty_good}\n{paws}\n\t\tMIAU, OSTATNIE PYTANIE PRZED TOBĄ. GOTOWA?\n{paws}"},
    "6": {"question": "Ile było kart romansowych w grze 'Wiedźmin 1'? (Chodzi o wszystkie karty"
                      " istniejące w grze, nie tylko te, które można zebrać w jednej rozgrywce. Miau.)",
          "answer": "26 25 24 27 28",
          "reply": f"{paws}\n{paws}\n{paws}\n\t\t{kitty_good}\n\t\tMIAU!!! WSPANIALE. WYGRAŁĄŚ. "
                   f"ZARAZ ZNAJDĘ NAGTODĘ\n"
                   f"...\n"
                   f"...\n"
                   f"\t\t{kitty_looks_for_reward}\n"
                   f"...\n"
                   f"...\n"
                   f"...\n"
                   f"...\n"
                   f"OTO ONA:\n"
                   f"\t\thttps://drive.google.com/drive/folders/1SGRQ08q-N2tikmJ4CCVXR7nbTIxbXx7E?usp=sharing"},
}


def main():
    print_slow(niesmialek)
    print_slow(welcome_message)

    for n in range(1, 7):
        ask(n)


def ask(question_num: int):
    q_r = questions_and_replies[str(question_num)]
    print_slow(f"{paws}  {q_r['question']}")
    reply = str(input())
    validation = _validate_response(reply, q_r)
    if validation:
        print_slow(q_r["reply"])
    else:
        print_slow(bad_response)
        ask(question_num)


def print_slow(print_input: str):
    spliced = print_input.split("\n")
    for s in spliced:
        print(s)
        time.sleep(0.1)


def _validate_response(response: str, question_and_reply: dict) -> bool:
    if response == "":
        return False
    return response in question_and_reply['answer']


if __name__ == "__main__":
    main()
