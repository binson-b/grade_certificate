#!/usr/bin/python3 

from tkinter import *
from tkinter import filedialog 
import csv
class App:
    def __init__(self,master):
        frame1 = Frame(master)
        master.minsize(200,200)
        master.maxsize(600,600)
        self.college_name = StringVar()
        self.fileloc = StringVar()
        self.workshop_date = StringVar()
        self.workshop_category = IntVar()
        frame1.pack(side=TOP,fill=X,padx=5, pady=5)
        Label(frame1, text="College Name", width=15).pack(side=LEFT)
        e1 = Entry(frame1, textvariable=self.college_name)
        e1.pack(side=RIGHT,expand=YES,fill=X)
        frame2 = Frame(master)
        frame2.pack(side=TOP,fill=X,padx=5, pady=5)
        Label(frame2, text="Workshop Date",width=15).pack(side=LEFT)
        e2 = Entry(frame2,textvariable=self.workshop_date)
        e2.pack(side=RIGHT,expand=YES,fill=X)
        frame3 = Frame(master)
        frame3.pack(side=TOP,fill=X,padx=5, pady=5)
        Label(frame3, text="Open csv",width=15).pack(side=LEFT)
        self.button = Button(frame3,text="open",command=self.f_open)
        self.button.pack(side=LEFT)
        frame4 = Frame(master)
        frame4.pack(side=TOP,fill=X,padx=5, pady=5)
        Label(frame4,text="""Workshop Category""",justify = LEFT).pack()
        Radiobutton(frame4,text="3-Day",padx = 20,variable=self.workshop_category,value=1).pack(anchor=W)
        Radiobutton(frame4,text="1-Day",padx = 20,variable=self.workshop_category,value=0).pack(anchor=W)
        Radiobutton(frame4,text="Fellowship",padx = 20,variable=self.workshop_category,value=2).pack(anchor=W)
        frame5 = Frame(master)
        frame5.pack(side=TOP,fill=X,padx=5, pady=5)
        button = Button(frame5,text="Generate",command=self.generate)
        button.pack(side=LEFT)
        button = Button(frame5,text="Quit",command=master.destroy)
        button.pack(side=RIGHT)
	
    def generate(self):
        data = open('data_{}.csv'.format(self.college_name.get()),'w')
        fieldnames = ['id','name','email','paper','purpose','college','ws_date','is_coordinator']
        writer = csv.DictWriter(data,fieldnames=fieldnames)
        writer.writeheader()
        with open("{}".format(self.fileloc)) as f:
            reader =  csv.DictReader(f)
            quiz_fieldnames = [k for k in reader.fieldnames if 'quiz' in k.lower()]
            for row in reader:
                name_title = (row['first_name']+' '+row['last_name']).title()
                email = row['email']
                total_quiz_mark = sum([float(row[k]) for k in quiz_fieldnames])
                out_of_mark = 52 if (self.workshop_category.get()==1) else 45
                if self.workshop_category.get()==2:
                    out_of_mark = 65
                percentage = total_quiz_mark/out_of_mark
                if percentage > 0.9:
                    paper = 'A+'
                elif .80 < percentage <= 0.9:
                    paper = 'A'
                elif .65 < percentage <= 0.8:
                    paper = 'B+'
                elif .50 < percentage <= .65:
                    paper = 'B'
                elif .35 < percentage <= .50:
                    paper = 'C'
                else:
                    paper = 'Fail'
                purpose = 'P3W' if (self.workshop_category.get()==1) else 'PWS'
                college = self.college_name.get()
                ws_date = self.workshop_date.get()
                is_coordinator = 0
                if paper !='Fail':
                    writer.writerow({'id':'','name':name_title,'email':email,'paper':paper,'purpose':purpose,
                                     'college':college,'ws_date':ws_date,'is_coordinator':is_coordinator})
                else:
                    pass
    def f_open(self):
        dlg = filedialog.Open()
        self.fileloc = dlg.show()


def main():
    root = Tk()
    app = App(root)
    root.wm_title("FOSSEE-Workshop-Grader")
    root.mainloop()
if __name__=='__main__':
    main()
