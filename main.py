from gui import *

def main():
    window = Tk()
    window.title('Student Grade App')
    window.geometry('300x400')
    window.resizable(False,False)
    Gui(window)
    window.mainloop()


if __name__ == "__main__":
    main()