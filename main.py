import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = list()
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html.parser')
    for watch_title in soup.findAll('a', {'class': 'yt-uix-sessionlink yt-uix-'
                                          'tile-link yt-ui-ellipsis yt-ui-elli'
                                          'psis-2 spf-link '}):
        content = watch_title.string
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)


def clean_up_list(word_list):
    clean_word_list = list()
    for word in word_list:
        symbols = '!@#$%^&*()_+{}:"<>?,./;\'[]-=~`|\\'
        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


def create_dictionary(clean_word_list):
    word_count = dict()
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for k, v in reversed(sorted(word_count.items(),
                                key=operator.itemgetter(1))):
        print(k, v)


if __name__ == '__main__':
    start('https://www.youtube.com/results?search_query=adele+hello')
