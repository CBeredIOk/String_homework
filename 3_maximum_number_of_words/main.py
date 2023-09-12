"""
Вам дан список предложений.
Предложения содержит только слова, которые разделены единичными пробелами.
Необходимо вернуть максимальное количество слов, которое содержится в одном предложении.
sentences[i] - это одно предложение.
Если ни одно из предложений не содержит слов, то нужно вернуть 0
Проверка:
pytest ./3_maximum_number_of_words/test.py
"""


def get_max_number_of_words_from_sentences(sentences: list[str]) -> int:

    len_sentences = len(sentences)

    count_words = []

    for i in range(len_sentences):
        words = sentences[i].split()
        count_words.append(len(words))

    count_words.sort()
    result = count_words[len_sentences - 1]

    return result
