from tkinter import *
from tkinter import messagebox

question = [
    {
        'question': 'Когда началась первая мировая война?',
        'answer': '1914'
    },
    {
        'question': 'Когда началась вторая мировая война?',
        'answer': '1939'
    },
    {
        'question': 'Когда закончилась первая мировая война?',
        'answer': '1918'
    }
]

counter_question = 0
guess_questions = 0

root = Tk()
root.geometry("450x150")
root.config(background="grey")


def get_question():
    return question[counter_question]


def show_question():
    question_dict = get_question()
    question_text_label.config(text=question_dict['question'])


def check_answer():
    global guess_questions
    user_answer = user_answer_entry.get()
    question_dict = get_question()
    if user_answer == question_dict['answer']:
        messagebox.showinfo("Success", "This is a correct answer")
        guess_questions += 1
        score_user_label.config(text=f"Отгадано вопросов: {guess_questions}")
    else:
        messagebox.showerror("Error", "This is not Correct")
    user_answer_entry.delete(0, END)
    next_question()


def next_question():
    global counter_question
    counter_question += 1
    if counter_question == len(question):
        messagebox.showinfo("Success", "You are done")
        counter_question = 0
    root.update()
    root.after(1000, show_question())


question_text_label = Label(text="", bg='grey')
question_text_label.pack()

user_answer_entry = Entry()
user_answer_entry.pack()

submit_button = Button(text="Ответить", bg='blue', command=check_answer)
submit_button.pack()

score_user_label = Label(text=f"Отгадано вопросов: {guess_questions}", bg='grey')
score_user_label.pack()

show_question()

root.mainloop()

