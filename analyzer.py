from word_trainer import generate_model_metadata, format_text

def get_common_words(positive_metadata, negative_metadata):
    list_common_words = []
    for i in range(0, len(positive_metadata)):
        for j in range(0, len(negative_metadata)):
            if positive_metadata[i]['word'] == negative_metadata[j]['word']:
                list_common_words.append(positive_metadata[i]['word'])

    return list_common_words

def make_analysis():
    positive_metadata = generate_model_metadata('spanish_positive_reviews.txt')
    negative_metadata = generate_model_metadata('spanish_negative_reviews.txt')
    list_common_words = get_common_words(positive_metadata, negative_metadata)

    # Remove common words
    for common_word in list_common_words:
        delete_word = filter(lambda x: x['word'] == common_word, positive_metadata)[0]
        positive_metadata.remove(delete_word)
        delete_word = filter(lambda x: x['word'] == common_word, negative_metadata)[0]
        negative_metadata.remove(delete_word)

    positive_points = 0
    negative_points = 0
    text = raw_input('Write text: ')

    if text == 'p':
        positive_metadata.sort()
        print positive_metadata
        print "Size: %s" % len(positive_metadata)
        return
    elif text == 'n':
        negative_metadata.sort()
        print negative_metadata
        print "Size: %s" % len(negative_metadata)
        return
    elif text.split(' ')[0] == 'find' and len(text.split(' ')) == 2:
        print "positive %s" % filter(lambda x: x['word'] == text.split(' ')[1], positive_metadata)
        print "negative %s" % filter(lambda x: x['word'] == text.split(' ')[1], negative_metadata)
        return

    list_of_words = []

    for word in format_text(text).split(' '):
        find_positive = filter(lambda x: x['word'] == word, positive_metadata)
        find_negative = filter(lambda x: x['word'] == word, negative_metadata)
        if len(find_positive) > 0:
            positive_points += find_positive[0]['weight']
        if len(find_negative) > 0:
            negative_points += find_negative[0]['weight']

    total_points = positive_points + negative_points
    percentage_positive = float(positive_points) / total_points
    percentage_negative = float(negative_points) / total_points

    print "positive index: %.2f%%" % (percentage_positive * 100)
    print "negative index: %.2f%%" % (percentage_negative * 100)

    if percentage_negative > percentage_positive:
        print "The sentence is negative!"
    if percentage_negative < percentage_positive:
        print "The sentence is positive!"
make_analysis()
