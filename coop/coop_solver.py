import csv

potential_words = []


with open("word_list.csv", "r") as word_file:
    word_list = csv.reader(word_file)
    for row in word_list:
        potential_words.append(row[0])


def remove_letter(letter, at: int = -1):
    for word in potential_words.copy():
        if at != -1:
            if word[at] == letter:
                potential_words.remove(word)
            continue
        if letter in word:
            potential_words.remove(word)


def include_letter(letter, at: int = -1):
    for word in potential_words.copy():
        if letter not in word:
            potential_words.remove(word)
            continue
        if at != -1:
            if word[at] != letter:
                potential_words.remove(word)


while True:
    print(potential_words)
    print(len(potential_words))

    next_action = input("Next action: ")
    if len(next_action) == 0:
        continue
    match next_action[0]:
        case "r":
            if len(next_action) > 2:
                for let in next_action[2:]:
                    remove_letter(let)
            else:
                remove_letter(input("Letter to remove: "))
        case "e":
            remove_letter(next_action[2], int(next_action[4]))
        case "i":
            if len(next_action) > 4:
                include_letter(next_action[2], int(next_action[4]))
            elif len(next_action) > 2:
                include_letter(next_action[2])
            else:
                include_letter(input("Letter to include: "))
