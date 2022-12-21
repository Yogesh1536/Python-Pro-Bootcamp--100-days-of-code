from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.windows = Tk()
        self.windows.title("Quizzler")
        self.windows.config(padx=20, pady=20, bg=THEME_COLOR)

        self.mark = Label(text="score: 0", fg="white", bg=THEME_COLOR)
        self.mark.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, width=280, text="Question", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        tick_image = PhotoImage(file="./images/true.png")
        self.tick = Button(image=tick_image, highlightthickness=0, command=self.right_button)
        self.tick.grid(row=2, column=0)

        cross_image = PhotoImage(file="./images/false.png")
        self.cross = Button(image=cross_image, highlightthickness=0, command=self.cross_button)
        self.cross.grid(row=2, column=1)

        self.get_next_question()

        self.windows.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.mark.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You reached the end of the quiz.")
            self.tick.config(state="disabled")
            self.cross.config(state="disabled")

    def right_button(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def cross_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.windows.after(1000, func=self.get_next_question)


