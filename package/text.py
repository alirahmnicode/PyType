from . import score


class Text:
    def __init__(self, *args, **kwargs):
        self.text = ''
        self.text_words = []
        self.word_count = 0
        self.user_text = None
        self.user_word_count = 0
        self.wrong_count = 0
        self.correct_word_count = 0
        self.game_over = False

    def give_the_text(self):
        with open('F:\projects\python\pytype\package\s.txt', 'r') as f:
            for s in f.readlines():
                self.text += s
                words = s.split(' ')
                for word in words:
                    if word != '\n' and len(word) > 1:
                        self.text_words.append(word)
            self.word_count = len(self.text_words)
        return self.text

    def get_the_user_text(self , user_text):
        self.user_text = user_text
        return user_text

    def correction_text(self):
        user_words = self.user_text.split(' ')
        for word in user_words:
            if word != '\n' and word != '' and len(word) > 1:
                if word in self.text_words:
                    self.correct_word_count += 1
                # get user text words count
                self.user_word_count += 1
                # get user wrong words
                if word not in self.text_words:
                    self.wrong_count += 1

        context = {
            "less_word_count": self.word_count - self.user_word_count,
            "wrong_count": self.wrong_count,
            "word_count": self.word_count,
            "correct_word_count":self.correct_word_count
        }
        return context
