from tkinter import *
import csv

class Gui:
    def __init__(self,window)->None:
        """
        Establishes all the buttons and widgets for the interface
        """
        self.window=window
        self.frame_one=Frame(self.window)
        self.label_name= Label(self.frame_one,text='Student Name')
        self.input_name= Entry(self.frame_one,width=20)
        self.label_name.pack(side='left')
        self.input_name.pack(side='left',padx=5)
        self.frame_one.pack(anchor='w',padx=5,pady=10)

        self.frame_two=Frame(self.window)
        self.label_score= Label(self.frame_two,text='Enter Scores')
        self.label_score.pack(side='left',padx=2)
        self.frame_two.pack(anchor='center',padx=5,pady=10)
        self.frame_shape = Frame(self.window)
        self.radio_score = IntVar()
        self.radio_score.set(0)


        self.frame_score1 = Frame(self.window)
        self.label_score1 = Label(self.frame_score1, text='score 1: ')
        self.input_score1 = Entry(self.frame_score1, width=20)
        self.label_score1.pack(side='left')
        self.input_score1.pack(side='left')
        self.frame_score1.pack()


        self.frame_score2 = Frame(self.window)
        self.label_score2 = Label(self.frame_score2, text='score 2: ')
        self.input_score2 = Entry(self.frame_score2, width=20)
        self.label_score2.pack(side='left')
        self.input_score2.pack(side='left')
        self.frame_score2.pack()


        self.frame_score3 = Frame(self.window)
        self.label_score3 = Label(self.frame_score3, text='score 3: ')
        self.input_score3= Entry(self.frame_score3, width=20)
        self.label_score3.pack(side='left')
        self.input_score3.pack(side='left')
        self.frame_score3.pack()


        self.frame_score4 = Frame(self.window)
        self.label_score4 = Label(self.frame_score4, text='score 4: ')
        self.input_score4 = Entry(self.frame_score4, width=20)
        self.label_score4.pack(side='left')
        self.input_score4.pack(side='left')
        self.frame_score4.pack()







        self.button_save=Button(self.window,text="Enter",command=self.submit)
        self.button_save.pack()
        self.label_bellow = Label(self.window, text="please enter a name")
        self.label_bellow.pack(pady=10)

        self.label_info = Label(self.window, text="Note any score left empty will be recorded as zero",fg="red")
        self.label_info.pack(pady=10)



    def submit(self)->None:
        """
        deals withe validation for the entry widgets and stores data in a csv file
        """
        with open('data.csv', 'w', newline='') as csvfile:
            content = csv.writer(csvfile, delimiter=',')
            content.writerow(["Name", "Score1", "Score2", "Score3", "Score4","Average"])
        try:
            name = str(self.input_name.get().strip())
            if len(name) == 0:
                raise NameError

            score1 = float(self.input_score1.get())
            score2 = float(self.input_score2.get())
            score3 = float(self.input_score3.get())
            score4 = float(self.input_score4.get())

            if score1 < 0 or score1 >100:
                raise ValueError
            elif score2 < 0 or score2 >100:
                raise ValueError
            elif score3 < 0 or score3 >100:
                raise ValueError
            elif score4 < 0 or score4 >100:
                raise ValueError
            if len(self.input_score1.get()) == 0:
                score1=0
            if len(self.input_score2.get()) == 0:
                score2=0
            if len(self.input_score3.get()) == 0:
                score3=0
            if len(self.input_score4.get()) == 0:
                score4=0
        except ValueError:
            self.label_bellow.config(text='Enter a score from 0 to 100',fg='red')
        except NameError:
            self.label_bellow.config(text='Please enter a name', fg="red")
        else:
            if len(self.input_score1.get()) == 0:
                score1=0
            if len(self.input_score2.get()) == 0:
                score2=0
            if len(self.input_score3.get()) == 0:
                score3=0
            if len(self.input_score4.get()) == 0:
                score4=0
            score_list=[score1,score2,score3,score4]
            average_score=sum(score_list)/len(score_list)
            with open('data.csv', 'a', newline='') as csvfile:
                content = csv.writer(csvfile, delimiter=',')

                content.writerow([name,score1,score2,score3,score4,average_score])
                self.input_name.delete(0, END)
                self.input_score1.delete(0, END)
                self.input_score2.delete(0, END)
                self.input_score3.delete(0, END)
                self.input_score4.delete(0, END)
                self.radio_score.set(0)
                self.label_bellow.config(text='Scores saved',fg="white")
                self.input_name.focus_set()