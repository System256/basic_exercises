# Вывести последнюю букву в слове
word = 'Архангельск'
print(f"Последняя буква в слове {word}: {word[-1]}")


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(f"Букв а в слове {word}: {word.lower().count('а')}")


# Вывести количество гласных букв в слове
word = 'Архангельск'
word = word.lower()
vowels = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
count = 0
for letter in word:
    if letter in vowels:
        count += 1
print(f"Количество гласных равно: {count}")


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(f"Количество слов в предложении: {len(sentence.split(' '))}")


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split(' '):
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
length_words = [len(word) for word in sentence.split(' ')]
print(f"Усреднённая длина слов: {sum(length_words) / len(length_words)}")