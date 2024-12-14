from tkinter import *
import csv
import os
class Gui:
    def __init__(self,window):
        self.window=window

        self.frame_one=Frame(self.window)
        self.label_name= Label(self.frame_one,text='Student Name')
        self.input_name= Entry(self.frame_one,width=20)
        self.label_name.pack(side='left')
        self.input_name.pack(side='left',padx=5)
        self.frame_one.pack(anchor='w',padx=5,pady=10)

        self.frame_two=Frame(self.window)
        self.label_score= Label(self.frame_two,text='No. Of Scores')
        self.label_score.pack(side='left',padx=2)
        self.frame_two.pack(anchor='center',padx=5,pady=10)
        self.frame_shape = Frame(self.window)
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_one = Radiobutton(self.frame_shape, text='one', variable=self.radio_1, value=1,
                                        command=self.submit)
        self.radio_two = Radiobutton(self.frame_shape, text='two', variable=self.radio_1, value=2,
                                        command=self.submit)
        self.radio_three = Radiobutton(self.frame_shape, text='three', variable=self.radio_1, value=3,
                                           command=self.submit)
        self.radio_four = Radiobutton(self.frame_shape, text='four', variable=self.radio_1, value=4,
                                          command=self.submit)
        self.radio_one.pack(side='left')
        self.radio_two.pack(side='left')
        self.radio_three.pack(side='left')
        self.radio_four.pack(side='left')
        self.frame_shape.pack(anchor='w', pady=10)


        self.frame_score1 = Frame(self.window)
        self.label_score1 = Label(self.frame_score1, text='score 1: ')
        self.input_score1 = Entry(self.frame_score1, width=20)
        self.label_score1.pack(side='left')
        self.input_score1.pack(side='left')
        self.frame_score1.pack()

        self.label_score1.pack_forget()
        self.input_score1.pack_forget()
        self.frame_score1.pack_forget()

        self.frame_score2 = Frame(self.window)
        self.label_score2 = Label(self.frame_score2, text='score 2: ')
        self.input_score2 = Entry(self.frame_score2, width=20)
        self.label_score2.pack(side='left')
        self.input_score2.pack(side='left')
        self.frame_score2.pack()

        self.label_score2.pack_forget()
        self.input_score2.pack_forget()
        self.frame_score2.pack_forget()

        self.frame_score3 = Frame(self.window)
        self.label_score3 = Label(self.frame_score3, text='score 3: ')
        self.input_score3= Entry(self.frame_score3, width=20)
        self.label_score3.pack(side='left')
        self.input_score3.pack(side='left')
        self.frame_score3.pack()

        self.label_score3.pack_forget()
        self.input_score3.pack_forget()
        self.frame_score3.pack_forget()

        self.frame_score4 = Frame(self.window)
        self.label_score4 = Label(self.frame_score4, text='score 4: ')
        self.input_score4 = Entry(self.frame_score4, width=20)
        self.label_score4.pack(side='left')
        self.input_score4.pack(side='left')
        self.frame_score4.pack()

        self.label_score4.pack_forget()
        self.input_score4.pack_forget()
        self.frame_score4.pack_forget()






        self.button_save=Button(self.window,text="Enter",command=self.submit)
        self.button_save.pack()
        self.button_submit = Button(self.window, text="Submit", command=self.enter)
        self.button_submit.pack()
        self.label_bellow=Label(self.window,text="please enter into entry box")
        self.label_bellow.pack(pady=10)

        self.button_submit = Button(self.window, text="Enter", command=self.enter)
        self.button_submit.pack()
    def show_score1(self):
        self.label_score1.pack()
        self.input_score1.pack()

    def submit(self):
        shape = self.radio_1.get()
        try:
            name= str(self.input_name.get().strip())
            if len(name) == 0:
                self.label_bellow.config(text='Please enter a name',fg="red")
        except ValueError:
            self.label_bellow.config(text='Enter a number for no. of scores',fg='red')
        else:
            if shape == 1:
                self.label_score1.pack()
                self.input_score1.pack()
                self.frame_score1.pack()

                self.label_score2.pack_forget()
                self.input_score2.pack_forget()
                self.frame_score2.pack_forget()

                self.label_score3.pack_forget()
                self.input_score3.pack_forget()
                self.frame_score3.pack_forget()

                self.label_score4.pack_forget()
                self.input_score4.pack_forget()
                self.frame_score4.pack_forget()
            elif shape == 2:
                self.label_score1.pack()
                self.input_score1.pack()
                self.frame_score1.pack()

                self.label_score2.pack()
                self.input_score2.pack()
                self.frame_score2.pack()

                self.label_score3.pack_forget()
                self.input_score3.pack_forget()
                self.frame_score3.pack_forget()

                self.label_score4.pack_forget()
                self.input_score4.pack_forget()
                self.frame_score4.pack_forget()

            elif shape == 3:
                self.label_score1.pack()
                self.input_score1.pack()
                self.frame_score1.pack()

                self.label_score2.pack()
                self.input_score2.pack()
                self.frame_score2.pack()

                self.label_score3.pack()
                self.input_score3.pack()
                self.frame_score3.pack()

                self.label_score4.pack_forget()
                self.input_score4.pack_forget()
                self.frame_score4.pack_forget()
            else:
                self.label_score1.pack()
                self.input_score1.pack()
                self.frame_score1.pack()

                self.label_score2.pack()
                self.input_score2.pack()
                self.frame_score2.pack()

                self.label_score3.pack()
                self.input_score3.pack()
                self.frame_score3.pack()

                self.label_score4.pack()
                self.input_score4.pack()
                self.frame_score4.pack()
    def enter(self):
        with open('data.csv', 'a', newline='') as csvfile:
            """content = csv.writer(csvfile, delimiter=',')
            content.writerow([, age, status])
            self.input_name.delete(0, END)
            self.input_age.delete(0, END)
            self.radio_answer.set(0)
            self.label_bellow.config(text='')
            self.input_name.focus_set()"""
