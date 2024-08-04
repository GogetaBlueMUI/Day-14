def matching(str, pat):
    if not len(str)==len(pat):
        return False
    for schar, pchar in zip(str, pat):
        if pchar.isalpha() and schar.isalpha():
            if pchar==schar:
                return True
            else:
                return False
        elif pchar.isdigit() and schar.isdigit():
            if pchar==schar:
                return True
            else:
                return False
        else:
            return False
print("Matching Status 1: ", matching("a1b2c3","a1b2c3"))
print("Matching Status 2: ", matching("a1b2c3","a1b2c3"))