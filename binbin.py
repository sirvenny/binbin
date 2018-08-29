import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
import os
import csv

"""
    Converts binary file to two decimal arrays, p and q, where p = every even value and q every odd value (e.g. dec=12345678, p=[1,3,5,7] q=[2,4,6,8]).
    Also ouputs adjusted p -> padj = p / 25.6 -1  q -> qadj = q / 25.6
"""

#creates frame

class FRM(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
root = Tk()
app = FRM(master=root)
app.master.title("Binary to P/Q")

frame = Frame(root)

frame.pack(side = LEFT)



def generate():
    Tk().withdraw()

    path = filedialog.askopenfilename(title = "Select binary file to convert to p and q decimal arrays")

    recp=[]
    recq=[]
    i=2
    bytee=0
    byte=0
    print("Number of rows: " + str(os.path.getsize(path)/2))
    with open(path, "rb") as file:
        csvfile = os.path.basename(file.name) + ".csv"
        # for x in range (0, 1000):
        while byte != b"":
            byte = file.read(1)
            # print(byte)
            bytee = int.from_bytes(byte, byteorder='big')
            # print(str(i-1)+ " " + str(bytee))
            # if bytee == 0:
            #     pass
            # else:
            if i % 2 == 0:
                recp.append(bytee)
            else:
                recq.append(bytee)

            i += 1

    p = [ x / 25.6 -1 for x in recp ]
    q = [ x / 25.6 for x in recq ]
    print(p)

    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(zip(p, q))
        # for i in range(int(os.path.getsize(path)/2)):
        #     writer.writerows(zip(p, q))

title_label = Label(frame, text="Generates P/Q data from raw")
title_label.pack(side = TOP, padx = 30, pady = 5)

generate_btn = tkinter.Button(frame, text="Generate!", command=generate)
generate_btn.pack(side = BOTTOM, padx = 30, pady = 20)


frame.mainloop()
