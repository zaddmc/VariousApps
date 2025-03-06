with open("byer.txt", "r") as r:
    prev_word = ""
    for line in r.readlines():
        line = line.split()[1]
        if len(line) != 5:
            continue
        if line == prev_word:
            continue
        prev_word = line
        print(line)
        continue
        with open("./word_list.csv", "a") as w:
            w.write(line + "\n")
