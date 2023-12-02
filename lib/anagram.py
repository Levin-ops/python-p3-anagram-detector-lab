# your code goes here!
class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, input_list):
        matching_words = [i for i in input_list if sorted(i.upper()) == sorted(self.word.upper()) and i.lower() != self.word.lower()]
        return matching_words



