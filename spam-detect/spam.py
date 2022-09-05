# A spam detector with text highlighting

data = str(input(">>"))


SPECIAL_CHARS = ['!', "@", "#", "$", "%", "&", "^", "*"]


class COLORS:
    # Red
    FAIL = '\033[91m'
    # Default
    ENDC = '\033[0m'


def load_words():
    with open("words.txt", 'r') as f:
        words = f.read()
    words_list = words.split("\n")
    return words_list


def check_spam(data: str):
    words = load_words()
    # getting invalid texts
    new_data = " ".join([i for i in data.lower().split(" ") if i not in words])
    if new_data == '':
        return "The given text is not a spam"
    
    # Removing special characters
    for sp in SPECIAL_CHARS:
        if sp in new_data:
            new_data = new_data.replace(sp, "")

    # Converting str to list without spaces removed
    data_lst = [x for x in new_data]
    #spam_cnt = 0
    
    for i in range(0, len(data_lst)):
        # Starting char
        s = data_lst[i].replace("\x1b[0m", '')
        if i != len(data_lst)-1:
            # Adjacent chars
            a = data_lst[i+1]
            p = data_lst[i-1].replace("\x1b[91m", '').replace("\x1b[0m", '')
            # Checking if current char is equal to adjacent chars and either of them aren't spaces
            if (s == a or s == p) and (s != " " or a != " " or p != " "):
                #spam_cnt += 1
                # Identifying the spam chars
                s_itm = data_lst.pop(i)
                data_lst.insert(i, f"{COLORS.FAIL}{s_itm}")
                e_itm = data_lst.pop(i+1)
                data_lst.insert(i+1, f"{e_itm}{COLORS.ENDC}")
    #result = f"\nSpam count: {spam_cnt}\n"
    return "\nThe given text is a spam!\n" "Text: " + "".join(data_lst) + "\n" if "\x1b[91m" in "".join(data_lst) else "\nThe " \
        "given text is not a spam"


print(check_spam(data))