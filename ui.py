from tkinter import *
from tkinter import Label
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title('Quizzler')
        self.window.config(padx=100,pady=50,bg=THEME_COLOR)
        self.label=Label(text='Score : 0',fg='white',bg=THEME_COLOR)
        self.label.grid(column=1,row=0,pady=20)


        self.canvas=Canvas(width=450,height=400,bg="white")
        self.question_text=self.canvas.create_text(225,
                                          200,
                                          text="Amazon acquired Twitch in august 2014 for $970 million dollars",
                                          fill="black",
                                          font=('Arial',15,'italic'),
                                          width=300
                                          )
        self.canvas.grid(column=0,row=1,columnspan=2)

        self.right=PhotoImage(file='images/true.png')
        self.right_button=Button(image=self.right,highlightthickness=0,bg=THEME_COLOR,borderwidth=0,command=self.right1)
        self.right_button.grid(row=2,column=0,pady=20)

        self.wrong=PhotoImage(file='images/false.png')
        self.wrong_button=Button(image=self.wrong,highlightthickness=0,bg=THEME_COLOR,borderwidth=0,command=self.wrong1)
        self.wrong_button.grid(row=2,column=1,pady=20)

        self.next_question()

        # self.score=self.canvas.create_text(200,200,text="Score : 0",fill='white',font=('Ariel',40,'bold'))



        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
          q_text=self.quiz.next_question()
          self.label.config(text=f"Score : {self.quiz.score}")
          self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="u have reached at the end of quiz")
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def right1(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong1(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
           self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.next_question)