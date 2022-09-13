
def generate_hashtag(s):
    new = '#'
    i = 0
    if s != '' and len(s) <= 140:
        for letter in s:
            if letter != ' ':
                if s[i-1] == ' ': new += letter.upper()
                elif i == 0: new += letter.upper()
                else: new += letter.lower()
            i += 1
        return print(new)
    return False
Hashtag = input('Insert the phrase you want to be hastagged: ')
generate_hashtag(Hashtag)
