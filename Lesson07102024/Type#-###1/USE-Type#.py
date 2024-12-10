file = open('Я_памятник_себе_воздвиг_нерукотворный.txt')
data = file.read()
def count_letters_dict(text):
    symbols = set(text)
    result = {}
    for symbol in symbols:
        result[symbol] = text.count(symbol)
    return result

print(count_letters_dict(data))