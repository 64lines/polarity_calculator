from word_trainer import generate_model_metadata, format_text

def make_analysis():
    # Model with the positive/negative words already analized and
    # weighted using the files training files especified.

    # Trained model with positive training data
    positive_metadata = generate_model_metadata('spanish_positive_reviews.txt')

    # Trained model with negative training data
    negative_metadata = generate_model_metadata('spanish_negative_reviews.txt')

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

    percentage_difference_neutrality = 0.10
    if abs(percentage_negative - percentage_positive) < percentage_difference_neutrality:
        print "The sentence is neutral!"
    elif percentage_negative > percentage_positive:
        print "The sentence is negative!"
    elif percentage_negative < percentage_positive:
        print "The sentence is positive!"
make_analysis()
