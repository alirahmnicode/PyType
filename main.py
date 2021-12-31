from package import text


class Main:
    def text_p(self):
        t = text.Text()
        # give text to user
        t.give_the_text()
        # get user text
        user_text = t.get_the_user_text()
        # Correction user text
        t.correction_text()


if __name__ == '__main__':
    start = Main()
    start.text_p()


