class Score:
    def __init__(self, less_word_count, wrong_count, time):
        self.less_word_count = less_word_count
        self.time = time
        self.wrong_count = wrong_count

    def p(self):
        print('time')
        print(self.time)
        print('les')
        print(self.less_word_count)
        print(self.wrong_count)
