import tkinter
from tkinter import *
import random

question = [
    "'OS' computer abbreviation usually means?",
    "'MOV' extension refers usually to what kind of file?",
    "'MPG' extension refers usually to what kind of file?",
    "What is part of a database that holds only one type of information?",
    "Who developed Yahoo?",
    "'DB' computer abbreviation usually means?",
    "'.INI' extension refers usually to what kind of file?",
    "The sampling rate, (how many samples per second are stored) for a CD is?",
    "What do we call a network whose elements may be separated by some distance? It usually involves two or more small networks and dedicated high-speed telephone lines.",
    "Sometimes computers and cache registers in a foodmart are connected to a UPS system. What does UPS mean?",

]

answers_choice = [
    ["Order of Significance","Open Software","Operating System","Optical Sensor"],
    ["Image file","Animation/movie file","Audio file","MS Office document"],
    ["Word Perfect Document file","MS Office document","Animation/movie file","Image file"],
    ["Report","Field","Record"," File"],
    ["Dennis Ritchie & Ken Thompson","David Filo & Jerry Yang","Vint Cerf & Robert Kahn","Steve Case & Jeff Bezos"],
    ["Database","Double Byte","Data Block","Driver Boot"],
    ["Image file","System file","Hypertext related file","Image Color Matching Profile file"],
    ["48.4 kHz"," 22,050 Hz","44.1 kHz","48 kHz"],
    ["URL (Universal Resource Locator)","LAN (Local Area Network)","WAN (Wide Area Network)","World Wide Web"],
    ["United Parcel Service","Uniform Product Support","Under Paneling Storage"," Uninterruptable Power Supply"],
]

answers = [2,1,2,1,1,0,1,2,2,3]

user_answer = []

indexes =[]
def gen():
    global indexes
    while(len(indexes) <5 ):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()



def calc():
    global indexes,user_answer,answers
    x =0
    score =0
    for i in indexes:
        if user_answer == answers[i]:
            score = score+5
        x += 1
    print(score)
    showresult(score)


ques = 1
def selected():
    global radiovar, user_answer
    global lblQuestion, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text= question[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques +=1

    else:
        print(indexes)
        print(user_answer)

        #calc():




def startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion = Label(
        root,
        text= question[indexes[0]],
        font=("consolas",16),
        width=500,
        justify="center",
        wraplength= 400,
        background = "#ffffff",
    )
    lblQuestion.pack(pady=(100,30))


    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text= answers_choice[indexes[0]][0],
        font =("times",12),
        value = 0,
        variable = radiovar,
        command= selected,
        background="#ffffff",
    )
    r1.pack(pady=(5,5))

    r2 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][1],
        font=("times", 12),
        value=1,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r2.pack(pady=(5,5))

    r3 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][2],
        font=("times", 12),
        value=2,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r3.pack(pady=(5,5))

    r4 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][3],
        font=("times", 12),
        value=3,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r4.pack(pady=(5,5))





def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblrules.destroy()
    lblInstruction.destroy()
    btnStart.destroy()
    gen()
    startquiz()


root = tkinter.Tk()
root.title("Quiz")
root.geometry("500x500")
root.config(background="#FFFFFF")
root.resizable(0,0)


img1 = PhotoImage(file="Brain.png")
labelimage = Label(
    root,
    image= img1,
    background="#FFFFFF"
)
labelimage.pack(pady=(10,0))

labeltext = Label(
    root,
    text = "Quiz",
    font = ("Impact",24,"bold"),
    background = "#ffffff"
)
labeltext.pack(pady=(10,0))

img2 = PhotoImage(file="Start.png")
btnStart = Button(
    root,
    image=img2,
    relief=FLAT,
    border=0,
    command = startIspressed,
)
btnStart.pack()
lblInstruction = Label(
    root,
    text="Read the rules and\nclick on START once you are ready",
    background="#ffffff",
    font=("Impact",12),
    justify="center"

)
lblInstruction.pack(pady=(10,100))

lblrules =Label(
    root,
    text="This quiz contains 10 questions\nyou will get 20 sec to solve a question\nonce you select a radio button that will be a final call\nhence think before u answer",
    width=100,
    font=("Times",10),
    background = "#000000",
    foreground ="#FACA2F",
)
lblrules.pack()
root.mainloop()