class Text:
    def __init__(self, *args, **kwargs):
        self.text = []
        self.user_text = None
        self.wrong_count = 0
        self.word_count = 0
        self.user_word_count = 0

    def give_the_text(self):
        with open('F:\projects\python\pytype\package\s.txt', 'r') as f:
            for s in f.readlines():
                print(s)
                # self.text += s
                words = s.split(' ')
                for word in words:
                    if word != '\n':
                        self.text.append(word)
                        self.word_count += 1

    def get_the_user_text(self):
        user_text = input('type yor text ')
        self.user_text = user_text
        return user_text

    def correction_text(self):
        user_words = self.user_text.split(' ')
        for word in user_words:
            print(word)
            if word != '\n' and word != '':
                self.user_word_count += 1
                if word not in self.text:
                    self.wrong_count += 1
