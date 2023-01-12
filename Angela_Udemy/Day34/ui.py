THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface():
    #   file dosent know data type (quiz_brain)  hence add a parameter : QuizBrain
    def __init__(self, quiz_brain : QuizBrain):
        self.score = 0
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.geometry("650x500")

        self.window.title("Quizzler", )
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.label = Label(text=f"Score: 0 ", bg=THEME_COLOR, fg='white', font=('arial', 15))
        self.label.grid(column=1, row=0)

        self.canvas = Canvas(bg='white', width=600, height=250)
        ##################### BELOW WIDTH=370 is lenght of text line, to make it fit in given space,
        self.question_text = self.canvas.create_text(300, 100, width=370, text="Some Question Text", fill=THEME_COLOR, font=('arial', 20, 'italic'))
        self.canvas.grid(row=1, column=1, columnspan=2)

        self.true_button_image = PhotoImage(file="/Users/ma088/Desktop/PYTH/Angela_Udemy\Day34/images/true.png")
        self.true_button = Button(image=self.true_button_image, command=self.choice_true)
        self.true_button.grid(column=2, row=2)

        self.false_button_image = PhotoImage(file="/Users/ma088/Desktop/PYTH/Angela_Udemy\Day34/images/false.png")
        self.false_button = Button(image=self.false_button_image, command=self.choice_false)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="snow")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:

            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz !")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def choice_true(self):
        self.feed_back(self.quiz.check_answer("True"))

    def choice_false(self):
        self.feed_back(self.quiz.check_answer("False"))

    def feed_back(self, is_right):
        if is_right == True:
            self.label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="lawn green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)




