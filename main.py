import tkinter as tk
from package import time, text, score

window = tk.Tk()
showing_text = 0



logo = tk.Label(text="Typing", background="#34A2FE",
                width=10, height=10)

# text buttons
default_text = tk.Button(
    text='get text',
)


# text input
user_text = tk.Text()

# finish btn
finish_btn = tk.Button(
    text='finish',
)


def show_text(text):
    text_label = tk.Label(text=text)
    text_label.pack()


def give_text_to_user(event):
    # create text object
    global t
    t = text.Text()
    # give text to user
    give_text = t.give_the_text()
    show_text(give_text)
    # start time
    global get_time
    get_time = time.Time()
    get_time.get_start_time()
        

def finish(event):
    # # get end time
    get_time.get_end_time()
    u_text = user_text.get("1.0", "end-1c")
    # get user text
    t.get_the_user_text(u_text)
    # Correction user text
    correction = t.correction_text()
    score_game(correction)


def score_game(obj):
    # # delay time
    secounds = get_time.get_delay_time()
    get_score = score.Score(obj['less_word_count'], obj['wrong_count'],
                            obj['correct_word_count'], obj['word_count']*1.3, secounds)
    user_score = get_score.calculate_score()
    message_box(user_score)


def message_box(obj):
    less_word_count = obj['less_word_count']
    wrong_count = obj['wrong_count']
    standard_time = obj['standard_time']
    correct_count = obj['correct_count']
    time = obj['time']
    score = obj['score']

    text = f'your score is {score},\n you have {less_word_count} less word count,\n you have {wrong_count} wrong word ,\n standard time is {standard_time} ,\n your time is {time} ,\n you have {correct_count} correct word'
    message = tk.Label(text=text)
    message.pack()


default_text.bind('<Button>', give_text_to_user)
finish_btn.bind('<Button>', finish)


# pascks
default_text.pack()
user_text.pack()
finish_btn.pack()

window.mainloop()
