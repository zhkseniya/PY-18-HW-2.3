# Задание
# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла.

import json
from pprint import pprint

def load_json_file(json_file):
    list_news = []
    with open(json_file, 'r', encoding='utf-8') as news_file:
        new_file_data = json.load(news_file)
        for item_list in new_file_data['rss']['channel']['items']:
            temp_list_news = item_list['description'].split()
            list_news += temp_list_news

        return list_news


def sorted_word(name_file):
    list_news = load_json_file(name_file)

    word_count = {}
    for word_item in list_news:
        if len(word_item) >= 6:
            if word_item in word_count.keys():
                word_count[word_item] += 1
            else:
                word_count[word_item] = 1

    temp_list = sorted(word_count, key=word_count.get, reverse=True)
    pprint('В файле {} наиболее часто встречаются следующие слова'.format(name_file))
    for i in range(10):
        pprint('Слово "{}" встречается {} раз'.format(temp_list[i], word_count[temp_list[i]]))



sorted_word('newsafr.json')
# sorted_word('newsfr.json')
# sorted_word('newsfr.json')
# sorted_word('newsit.json')



