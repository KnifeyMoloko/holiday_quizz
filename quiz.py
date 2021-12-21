#!/usr/bin/python
# -*- coding: utf-8 -*-

from ascii import *

welcome_message = "W wigilijny wieczór w swoim mieszkaniu oczekujesz na swój prezent. Nagle staje przed" \
                  " tobą Nieśmiałek-Sfinks i mówi:\n" \
                  "ABY OTRZYMAĆ, MUISZ WYBRAĆ.\n" \
                  "MIAU.\n" \
                  "ABY WYBRAĆ, MUISZ WIEDZIEĆ, CO WYBIERASZ.\n" \
                  "MIAU.\n" \
                  "BY WIEDZIEĆ CO WYBIERASZ, ODPOWIEDZ NA PYTAŃ SZEŚĆ.\n" \
                  "SZEŚĆ PYTAŃ ODSŁONI TWOJE OPCJE!\n" \
                  "MIAU! MIAU! POWODZEEENIA!"

bad_response = f"{paws} MIAU MIAU... ŹLE!!!\n{kitty_bad}\n\nSPRÓBUJ PONOWNIE"
questions_and_replies = {
    "1": {"question": "question 1",
          "answer": f"yes",
          "reply": f"{paws}\n{kitty_good}\n{paws}\nSUPER! MIAU! DO KOLEJNEGO PYTANIA!"},
    "2": {"question": "question 2",
          "answer": "yes",
          "reply": f"{paws}\n{kitty_good}\n{paws}\nCORAZ LEPIEJ!!! MIAU MIAU!"},
    "3": {"question": "question 3",
          "answer": "yes",
          "reply": f"{paws}\n{kitty_good}\n{paws}\nTRZY ZA TOBĄ, JESZCZE TRZY DO KOŃCA! MIAU!"},
    "4": {"question": "question 4",
          "answer": "yes",
          "reply": f"{paws}\n{kitty_good}\n{paws}\nJESTEŚ DIAMENTEM MIAU MIAU!!!"},
    "5": {"question": "question 5",
          "answer": "yes",
          "reply": f"{paws}\n{kitty_good}\n{paws}\nMIAU, OSTATNIE PYTANIE PRZED TOBĄ. GOTOWA?"},
    "6": {"question": "question 6",
          "answer": "yes",
          "reply": f"{paws}\n{kitty_good}\nMIAU!!! WSPANIALE. WYGRAŁĄŚ. ZARAZ ZNAJDĘ NAGTODĘ\n"
                   f"...\n"
                   f"...\n"
                   f"{kitty_looks_for_reward}\n"
                   f"\n"
                   f"\n"
                   f"OTO ONA:\n"
                   f"https://drive.google.com/drive/folders/1SGRQ08q-N2tikmJ4CCVXR7nbTIxbXx7E?usp=sharing"},
}


def main():
    print(welcome_message)
    print(niesmialek)
    for n in range(1, 7):
        ask(n)


def ask(question_num: int):
    q_r = questions_and_replies[str(question_num)]
    print(f"{paws}  {q_r['question']}")
    reply = str(input())
    validation = _validate_response(reply, q_r)
    if validation:
        print(q_r["reply"])
    else:
        print(bad_response)
        ask(question_num)


def _validate_response(response: str, question_and_reply: dict) -> bool:
    if response == "":
        return False
    return response in question_and_reply['answer']


if __name__ == "__main__":
    main()
