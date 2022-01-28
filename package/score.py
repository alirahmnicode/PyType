from email.policy import default


class Score:
    def __init__(self, less_word_count, wrong_count, correct_count,standard_time, time):
        self.less_word_count = less_word_count
        self.correct_count = correct_count
        self.standard_time = standard_time
        self.time = time
        self.wrong_count = wrong_count
        self.default_score = 100
        self.less_sore = 0

    def calculate_score(self):
        # less 3 score for any less words
        self.less_sore += (self.less_word_count * 3)
        # less 3 sore for any worng words
        self.less_sore += (self.wrong_count * 3)
        # less 3 score for any 5 secounds
        if self.standard_time > self.time:
            less_time = 0
        else:
            less_time = int(self.time - self.standard_time)
        self.less_sore += (int((less_time / 5)) * 3)
        # give score
        if self.less_sore > 100 or self.correct_count < self.wrong_count:
            score = 0
        else:
            score = self.default_score - self.less_sore
        context = {
            "less_word_count": self.less_word_count,
            "wrong_count": self.wrong_count,
            "standard_time": self.standard_time,
            "correct_count":self.correct_count,
            "time": self.time,
            "score":score,
        }
        return context
