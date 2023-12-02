# your code goes here!
class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, input_list):
        matched_words = [i for i in input_list if sorted(i.lower()) == sorted(self.word.lower()) and i.lower() != self.word.lower()]
        return matched_words



