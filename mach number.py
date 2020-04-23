from tkinter import *
import tkinter.messagebox





class mach:
    def __init__(self):
        window = Tk()
        window.title("Aircraft Analyser v1.0")
        image1 = PhotoImage(file='giphy.gif')
        w = image1.width()
        h = image1.height()
        window.geometry("%dx%d+120+120" % (w, h))
        window.resizable(0, 0)

        panel1 = Label(window, image=image1)
        panel1.pack(side='top', fill='both', expand='yes')

        panel1.image = image1

        Label(window, text="Mach number", bg="#4677BA", fg="white", font="none 40 bold").place(x=85, y=10)
        Label(window, text="Enter velocity", bg="#4677BA", fg="white", font="none 10 bold").place(x=130, y=200)
        Label(window, text="Enter altitude", bg="#4677BA", fg="white", font="none 10 bold").place(x=130, y=150)
        Label(window, text="The Mach number is : ", bg="#DBAF4E", fg="white", font="none 10 bold").place(x=130, y=250)
        Label(window, text="m/s", bg="#4677BA", fg="white", font="none 10 bold").place(x=400, y=200)
        Label(window, text="ft", bg="#4677BA", fg="white", font="none 10 bold").place(x=400, y=150)

        self.ip1=StringVar()
        self.ip2 = StringVar()
        self.ip2 = StringVar()
        self.op1 = StringVar()
        self.op2 = StringVar()
        Entry(window, width=20, bg="white",textvariable=self.ip1).place(x=250, y=200)
        Entry(window, width=20, bg="white", textvariable=self.op1).place(x=250, y=250)
        Entry(window, width=20, bg="white", textvariable=self.ip2).place(x=250, y=150)
        Button(window, text="submit", width=20,command=self.cal,bg="#4677BA").place(x=180, y=300)
        exitButton = Button(window, text="exit", width=20, command=window.destroy,bg="#4677BA").place(x=180, y=330)
        window.mainloop()

    def cal(self):
        from ADRpy import atmospheres as at
        from ADRpy import unitconversions as co
        from tkinter import  messagebox as msg

        ip1 = float(self.ip1.get())
        ip2=float(self.ip2.get())

        isa_minus10 = at.Atmosphere(offset_deg=-10)
        # Query altitude
        altitude_m = co.feet2m(ip2)
        m=isa_minus10.vsound_mps(altitude_m)
        op1 = (ip1/m)
        self.op1.set(op1)
        if op1<1:
            msg.showinfo("Type of aircraft",message="subsonic")
        elif op1==1:
            msg.showinfo("Type of aircraft", message="transonic")
        elif ((op1>=1)and(op1<=1.5)) :
            msg.showinfo("Type of aircraft", message="sonic")
        elif ((op1>=1.6)and(op1<5)) :
            msg.showinfo("Type of aircraft", message="supersonic")
        elif op1>5:
            msg.showinfo("Type of aircraft", message="hypersonic")


mach()