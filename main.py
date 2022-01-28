from package import time, text, score


class Main:
    def text_p(self):
        t = text.Text()

        # give text to user
        t.give_the_text()

        # get start time
        get_time = time.Time()
        get_time.get_start_time()

        # get user text
        user_text = t.get_the_user_text()

        # get end time
        get_time.get_end_time()

        # Correction user text
        correction = t.correction_text()

        # delay time
        secounds = get_time.get_delay_time()

        # calculate score
        get_score = score.Score(
            correction['less_word_count'], correction['wrong_count'], correction['correct_word_count'], correction['word_count']*1.3, secounds)

        calculate = get_score.calculate_score()
        message = print(calculate)


if __name__ == '__main__':
    start = Main()
    start.text_p()
