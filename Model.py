from typing import List
from spellchecker import SpellChecker
from textblob import TextBlob



class SpellCheckerModule:
    def __init__(self):
        self.spell_check = SpellChecker()
        self.grammar_check = TextBlob("")

    def check_spellings(self, text):
        """
        Method to check spellings in the given text.
        """
        words = text.split()
        corrected_words = []
        for word in words:
            corrected_word = str(TextBlob(word).correct())
            corrected_words.append(corrected_word)
        return " ".join(corrected_words)

    def check_grammar(self, text):
        """
        Method to check grammar in the given text.
        """
        # Perform part-of-speech tagging
        blob = TextBlob(text)
        pos_tags = blob.tags

        # Extract nouns and pronouns
        grammar_mistakes = [word for word, pos in pos_tags if pos in ['NN', 'NNS', 'NNP', 'NNPS', 'PRP']]
        grammar_mistakes_count= len(grammar_mistakes)
        return grammar_mistakes,grammar_mistakes_count


# Example usage:
if __name__ == "__main__":
    checker = SpellCheckerModule()

    # Example text
    example_text = "I like machinnne learning "

    # Spell checking
    misspelled_words = checker.check_spellings(example_text)
    print("Misspelled words:", misspelled_words)

    # Grammar checking (extracting nouns and pronouns)
    grammar_mistakes , cnt = checker.check_grammar(example_text)
    print("Potential grammar mistakes:", grammar_mistakes , cnt)
