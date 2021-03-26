nr = [[3, 3, 8, 8], [3, 8, 3, 8], [3, 8, 8, 3], [8, 3, 3, 8], [8, 3, 8, 3], [8, 8, 3, 3],
      [33, 8, 8], [38, 3, 8], [83, 3, 8], [88, 3, 3],
      [8, 33, 8], [38, 8, 3], [83, 8, 3], [3, 88, 3],
      [8, 8, 33], [3, 38, 8], [3, 83, 8], [3, 3, 88],
      [3, 8, 38], [3, 8, 83],
      [8, 38, 3], [8, 83, 3],
      [8, 3, 38], [8, 3, 83],
      [338, 8], [383, 8], [388, 3], [833, 8], [838, 3], [883, 3],
      [8, 338], [8, 383], [3, 388], [8, 833], [3, 838], [3, 883]]
op = ['', '(', ')', '+', '-', '*', '/', '+(', '-(', '*(', '/(', ')+', ')-', ')*', ')/']


def tanga(list):
    s = ''
    for el in list:
        s += str(el)
    return s


def closet(list):
    count_open = 0
    count_close = 0
    for el in list:
        if el in ['+(', '-(', '*(', '/(', '(']:
            count_open += 1
        if el in [')+', ')-', ')*', ')/', ')']:
            count_close += 1
    if count_open > count_close:
        return True
    else:
        return False


def back(list, pos, max):
    global op
    for o in op:
        if pos == 0 and (o == '(' or o == ''):
            new = list.copy()
            new.insert(0, o)
            back(new, pos + 2, max)
        if (0 < pos < max) and o not in ['', '(', ')']:
            if o in [')+', ')-', ')*', ')/'] and closet(list):
                new = list.copy()
                new.insert(pos, o)
                back(new, pos + 2, max)
            if o not in [')+', ')-', ')*', ')/']:
                new = list.copy()
                new.insert(pos, o)
                back(new, pos + 2, max)
        if pos == max and ((o == ')' and closet(list)) or o == ''):
            new = list.copy()
            new.insert(pos, o)
            try:
                if not closet(new) and (eval(tanga(new)) == 24 or (
                        round(eval(tanga(new))) == 24 and abs(round(eval(tanga(new))) - eval(tanga(new))) < 0.1)):
                    print(tanga(new), eval(tanga(new)))
            except:
                count = 0


for list in nr:
    max = 2 * len(list)
    back(list, 0, max)
