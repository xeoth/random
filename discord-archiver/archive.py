import fileinput


def any_of_tuple_in_str(tpl: tuple, string: str) -> bool:
    for i in tpl:
        if i in string:
            return True
    return False


keywords = ('Today', 'Yesterday')

meta_line = True  # every second line contains nickname and date
for line in fileinput.input('raw.txt'):
    line = line.rstrip()
    if not any_of_tuple_in_str(keywords, line) and meta_line:
        line = line[:-10]  # cut off the 'dd/mm/yyyy' part
    elif any_of_tuple_in_str(keywords, line) and meta_line:
        for word in keywords:
            if word in line:
                line = line[:(-12-len(word))]

    if meta_line:
        print(f'<{line}>', end=' ')
    else:
        print(line)

    meta_line = not meta_line
