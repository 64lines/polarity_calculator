# -*- coding: latin-1 -*-
def get_reviews(file_name):
    file_data = open(file_name, 'r+')
    list_reviews = file_data.readlines()
    file_data.close()
    return list_reviews

def format_text(text):
    return text.lower().strip() \
        .replace('.', '') \
        .replace(', ', '') \
        .replace(',', ' ') \
        .replace('!', '') \
        .replace('?', '') \
        .replace('¿', '') \
        .replace('¡', '') \
        .replace('(', '') \
        .replace(')', '')

def generate_model_metadata(file_name):
    list_reviews = get_reviews(file_name)
    big_data_list = []

    # Setting the words up
    for review in list_reviews:
        for word in format_text(review).split(' '):
            is_new = True

            for i in range(0, len(big_data_list)):
                if big_data_list[i]['word'] == word:
                    is_new = False
                    big_data_list[i]['weight'] += 1

            if is_new:
                word_model = {'word':'', 'weight': 1}
                word_model['word'] = word
                if word_model not in big_data_list:
                    big_data_list.append(word_model)

    return big_data_list
