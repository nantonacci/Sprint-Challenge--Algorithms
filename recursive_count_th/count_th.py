'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
count = 0

def count_th(word):
    global count

    if "th" not in word:
        total = count
        count = 0
        return total
    elif "th" in word:
        count += 1
        return count_th("0" + word[:word.index("th")] + "0" + word[word.index("th") + 2:])
