from tkinter import *
from tkinter import messagebox
import math, random, os

class Billing_Application:
    cosmeticsprice  = [ 5,10,15,20,25,30]
    groceryprice    = [10,20,30,40,50,60]
    stationaryprice = [ 1, 2, 3, 4, 5, 6]
    
    cosmeticstaxrate  = 0.10
    grocerytaxrate    = 0.05
    stationarytaxrate = 0.05

    Total_bill = 0.0

    def __init__(self, t):
        self.t = t
        self.t.resizable(0,0)
        self.t.geometry("1350x700")
        self.t.title("GTA Billing Software V01.00")
        title = Label(self.t,text="GT Aloha Billing Software",font=("times new roman",33,"bold"),pady=2,bg="#ebebe0",fg="#800080")
        title.place(x=0,y=0,width=1350)

        #variables
        #customers
        self.cname = StringVar()
        self.cphone = StringVar()

        #billno
        self.billno = StringVar()
        x = random.randint(10000,99999)
        self.billno.set(x)

        #search 
        self.search = StringVar()

        #cosmetics quantity (used to capture the values entyered by the user )
        self.cosmeticsqty01 = IntVar()
        self.cosmeticsqty02 = IntVar()
        self.cosmeticsqty03 = IntVar()
        self.cosmeticsqty04 = IntVar()
        self.cosmeticsqty05 = IntVar()
        self.cosmeticsqty06 = IntVar()

        #grocery quantity (used to capture the values entyered by the user )
        self.groceryqty01 = IntVar()
        self.groceryqty02 = IntVar()
        self.groceryqty03 = IntVar()
        self.groceryqty04 = IntVar()
        self.groceryqty05 = IntVar()
        self.groceryqty06 = IntVar()

        #stationary quantity (used to capture the values entyered by the user )
        self.stationaryqty01 = IntVar()
        self.stationaryqty02 = IntVar()
        self.stationaryqty03 = IntVar()
        self.stationaryqty04 = IntVar()
        self.stationaryqty05 = IntVar()
        self.stationaryqty06 = IntVar()

        #total amount (Used to store the Cosmetics, Grocery and Stationary total before tax) 
        self.cosmeticsum   = StringVar()
        self.grocerysum    = StringVar()
        self.stationarysum = StringVar()

        #Tax amount (Used to store the Cosmetics, Grocery and Stationary tax) 
        self.cosmetictax   = StringVar()
        self.grocerytax    = StringVar()
        self.stationarytax = StringVar()


        #customer detail
        frame1 = LabelFrame(self.t,text="Customer Details",bd=10,bg="#ebebe0",fg="black",font=("times new roman",15, "bold"))
        frame1.place(x=5,y=55,width=1345)

        cu1 = Label(frame1,text="Customer Name",bg="#ebebe0",fg="black",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        ce1 = Entry(frame1,width=15,font=("arial",15),bd=7,textvariable=self.cname).grid(row=0,column=1,padx=20,pady=5)
        cu2 = Label(frame1,text="Phone No", bg="#ebebe0",fg="black",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        ce2 = Entry(frame1, width=15, font=("arial", 15), bd=7, textvariable=self.cphone).grid(row=0, column=3, padx=20,pady=5)
        cu3 = Label(frame1, text="Bill No", bg="#ebebe0", fg="black",font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        ce3 = Entry(frame1, width=15, font=("arial", 15), bd=7, textvariable=self.billno).grid(row=0, column=5, padx=20, pady=5)
        cb1 = Button(frame1,width=10,command=self.findbill,text="Search",font="arial 12 bold").grid(row=0,column=6,padx=20,pady=5)

        #cosmetics
        cosmeticsframe = LabelFrame(self.t,text="Cosmetics",bd=7,bg="#ebebe0",fg="black",font=("times new roman",15, "bold"))
        cosmeticsframe.place(x=5,y=140,width=275,height=380)
        cv1 = Label(cosmeticsframe,text="Bath Soap",bg="#ebebe0",fg="black",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        cv1 = Label(cosmeticsframe,text="Face Cream", bg="#ebebe0", fg="black", font=("times new roman", 18, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        cv1 = Label(cosmeticsframe, text="Face Wash", bg="#ebebe0", fg="black",font=("times new roman", 18, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        cv1 = Label(cosmeticsframe, text="Hair Spray", bg="#ebebe0", fg="black",font=("times new roman", 18, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky="w")
        cv1 = Label(cosmeticsframe, text="Hair Gel", bg="#ebebe0", fg="black",font=("times new roman", 18, "bold")).grid(row=4, column=0, padx=10, pady=10, sticky="w")
        cv1 = Label(cosmeticsframe, text="Body Cream", bg="#ebebe0", fg="black",font=("times new roman", 18, "bold")).grid(row=5, column=0, padx=10, pady=10, sticky="w")

        cs1 = Entry(cosmeticsframe, width=6, font=("arial", 15), bd=7, textvariable=self.cosmeticsqty01).grid(row=0, column=1, padx=20,pady=5)
        cs2 = Entry(cosmeticsframe, width=6, font=("arial", 15), bd=7, textvariable=self.cosmeticsqty02).grid(row=1, column=1,padx=20,pady=5)
        cs3 = Entry(cosmeticsframe, width=6, font=("arial", 15), bd=7, textvariable=self.cosmeticsqty03).grid(row=2,column=1,padx=20, pady=5)
        cs4 = Entry(cosmeticsframe, width=6, font=("arial", 15), bd=7, textvariable=self.cosmeticsqty04).grid(row=3,column=1,padx=20, pady=5)
        cs5 = Entry(cosmeticsframe, width=6, font=("arial", 15), bd=7, textvariable=self.cosmeticsqty05).grid(row=4, column=1, padx=20,pady=5)
        cs6 = Entry(cosmeticsframe, width=6, font=("arial", 15), bd=7, textvariable=self.cosmeticsqty06).grid(row=5, column=1, padx=20, pady=5)


        groceryframe = LabelFrame(self.t,text="Grocery",bd=7,bg="#ebebe0",fg="black",font=("times new roman",15, "bold"))
        groceryframe.place(x=290,y=140,width=290,height=380)
        gu1 = Label(groceryframe,text="Rice",bg="#ebebe0",fg="black",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        gu2 = Label(groceryframe,text="Food Oil", bg="#ebebe0", fg="black", font=("times new roman", 18, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        gu3 = Label(groceryframe, text="Wheat", bg="#ebebe0", fg="black",font=("times new roman", 18, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        gu4 = Label(groceryframe, text="Sugar", bg="#ebebe0", fg="black",font=("times new roman", 18, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky="w")
        gu5 = Label(groceryframe, text="Daal", bg="#ebebe0", fg="black",font=("times new roman", 18, "bold")).grid(row=4, column=0, padx=10, pady=10, sticky="w")
        gu6 = Label(groceryframe, text="Tea Powder", bg="#ebebe0", fg="black",font=("times new roman", 18, "bold")).grid(row=5, column=0, padx=10, pady=10, sticky="w")

        ge1 = Entry(groceryframe, width=6, font=("arial", 15), bd=7, textvariable=self.groceryqty01).grid(row=0, column=1,padx=20,pady=5)
        ge2 = Entry(groceryframe, width=6, font=("arial", 15), bd=7, textvariable=self.groceryqty02).grid(row=1,column=1,padx=20,pady=5)
        ge3 = Entry(groceryframe, width=6, font=("arial", 15), bd=7, textvariable=self.groceryqty03).grid(row=2,column=1,padx=20,pady=5)
        ge4 = Entry(groceryframe, width=6, font=("arial", 15), bd=7, textvariable=self.groceryqty04).grid(row=3,column=1,padx=20, pady=5)
        ge5 = Entry(groceryframe, width=6, font=("arial", 15), bd=7, textvariable=self.groceryqty05).grid(row=4, column=1, padx=20,pady=5)
        ge6 = Entry(groceryframe, width=6, font=("arial", 15), bd=7, textvariable=self.groceryqty06).grid(row=5,column=1,padx=20, pady=5)

        stationaryframe = LabelFrame(self.t,text="Stationary",bd=7,bg="#ebebe0",fg="black",font=("times new roman",15, "bold"))
        stationaryframe.place(x=590,y=140,width=325,height=380)
        su1 = Label(stationaryframe,text="Pen",bg="#ebebe0",fg="black",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        su2 = Label(stationaryframe,text="pencil", bg="#ebebe0", fg="black", font=("times new roman", 18, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        su3 = Label(stationaryframe, text="Eraser", bg="#ebebe0", fg="black",font=("times new roman", 18, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        su4 = Label(stationaryframe, text="Exam Pad", bg="#ebebe0", fg="black",font=("times new roman", 18, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky="w")
        su5 = Label(stationaryframe, text="Scale", bg="#ebebe0", fg="black",font=("times new roman", 18, "bold")).grid(row=4, column=0, padx=10, pady=10, sticky="w")
        su6 = Label(stationaryframe, text="Geometry Box", bg="#ebebe0", fg="black",font=("times new roman", 18, "bold")).grid(row=5, column=0, padx=10, pady=10, sticky="w")

        se1 = Entry(stationaryframe, width=8, font=("arial", 15), bd=7, textvariable=self.stationaryqty01).grid(row=0, column=1,padx=20, pady=5)
        se2 = Entry(stationaryframe, width=8, font=("arial", 15), bd=7, textvariable=self.stationaryqty02).grid(row=1, column=1,padx=20, pady=5)
        se3 = Entry(stationaryframe, width=8, font=("arial", 15), bd=7, textvariable=self.stationaryqty03).grid(row=2, column=1,padx=20, pady=5)
        se4 = Entry(stationaryframe, width=8, font=("arial", 15), bd=7, textvariable=self.stationaryqty04).grid(row=3, column=1,padx=20, pady=5)
        se5 = Entry(stationaryframe, width=8, font=("arial", 15), bd=7, textvariable=self.stationaryqty05).grid(row=4, column=1,padx=20, pady=5)
        se6 = Entry(stationaryframe, width=8, font=("arial", 15), bd=7, textvariable=self.stationaryqty06).grid(row=5, column=1,padx=20, pady=5)

        #billarea
        billareaframe = Frame(self.t,bd=10,relief=GROOVE)
        billareaframe.place(x=920,y=140,width=430,height=380)

        bu1 = Label(billareaframe,text="Bill Area",bg="#ebebe0",relief=GROOVE,bd =7,font=('arial',15,"bold")).pack(fill=X)
        bsb = Scrollbar(billareaframe,orient=VERTICAL)
        self.txtarea = Text(billareaframe,yscrollcommand=bsb.set)
        bsb.pack(side=RIGHT,fill=Y)
        bsb.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #Bill Sub Total and Tax frame
        billmenuframe = LabelFrame(self.t,text="Bill Sub Total and Tax",bd=7,bg="#ebebe0",fg="black",font=("times new roman",15, "bold"),relief=GROOVE)
        billmenuframe.place(x=5,y=525,relwidth=1,height=160)

        bm1 = Label(billmenuframe, text="Cosmetic Total Amt", bg="#ebebe0", fg="black", font=("times new roman", 14, "bold")).grid(row=0,column=0,padx=20,pady=5, sticky="w")
        bm2 = Label(billmenuframe, text="Grocery Total Amt", bg="#ebebe0", fg="black", font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=5, sticky="w")
        bm3 = Label(billmenuframe, text="Stationary Total Amt", bg="#ebebe0", fg="black", font=("times new roman", 14, "bold")).grid(row=2, column=0,padx=20,pady=5,sticky="w")

        bme1 = Entry(billmenuframe, width=16, font=("arial", 12), bd=7,relief=SUNKEN, textvariable=self.cosmeticsum).grid(row=0, column=1,padx=20, pady=1)
        bme2 = Entry(billmenuframe, width=16,font=("arial", 12), bd=7,relief=SUNKEN, textvariable=self.grocerysum).grid(row=1, column=1,padx=20, pady=1)
        bme3 = Entry(billmenuframe, width=16, font=("arial", 12), bd=7,relief=SUNKEN, textvariable=self.stationarysum).grid(row=2, column=1,padx=20, pady=1)


        bm4 = Label(billmenuframe, text="Cosmetic Tax", bg="#ebebe0", fg="black", font=("times new roman", 14, "bold")).grid(row=0,column=2,padx=20,pady=5, sticky="w")
        bm5 = Label(billmenuframe, text="Grocery Tax", bg="#ebebe0", fg="black", font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=5, sticky="w")
        bm6 = Label(billmenuframe, text="Stationary Tax", bg="#ebebe0", fg="black", font=("times new roman", 14, "bold")).grid(row=2, column=2,padx=20,pady=5,sticky="w")

        bme4 = Entry(billmenuframe, width=16, font=("arial", 12), bd=7,relief=SUNKEN, textvariable=self.cosmetictax).grid(row=0, column=3,padx=20, pady=1)
        bme5 = Entry(billmenuframe, width=16, font=("arial", 12), bd=7,relief=SUNKEN, textvariable=self.grocerytax).grid(row=1, column=3,padx=20, pady=1)
        bme6 = Entry(billmenuframe, width=16, font=("arial", 12), bd=7,relief=SUNKEN, textvariable=self.stationarytax).grid(row=2, column=3,padx=20, pady=1)

        #buttonframe
        buttonframe = Frame(billmenuframe,bd=7,relief=GROOVE)
        buttonframe.place(x=780,height=115,width=550)

        totbtn = Button(buttonframe,text="Total",command=self.total,pady=15,width=8,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=10)
        gbbtn = Button(buttonframe,text="Generate bill",command=self.billarea,pady=15,width=12,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=10)
        clearbtn = Button(buttonframe,text="Clear",command=self.clear,pady=15,width=8,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=10)
        exitbtn = Button(buttonframe,text="Exit",command=self.exit,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=10)

        self.welcome()

    def total(self):

        self.cosmetictotal01 = float(self.cosmeticsqty01.get() * self.cosmeticsprice[0] ) 
        self.cosmetictotal02 = float(self.cosmeticsqty02.get() * self.cosmeticsprice[1] )
        self.cosmetictotal03 = float(self.cosmeticsqty03.get() * self.cosmeticsprice[2] )
        self.cosmetictotal04 = float(self.cosmeticsqty04.get() * self.cosmeticsprice[3] )
        self.cosmetictotal05 = float(self.cosmeticsqty05.get() * self.cosmeticsprice[4] )
        self.cosmetictotal06 = float(self.cosmeticsqty06.get() * self.cosmeticsprice[5] )

        self.cosmeticsum.set( str (self.cosmetictotal01 + self.cosmetictotal02 + self.cosmetictotal03 + self.cosmetictotal04 + self.cosmetictotal05 + self.cosmetictotal06 ) )


        self.grocerytotal01 = float(self.groceryqty01.get() * self.groceryprice[0] )
        self.grocerytotal02 = float(self.groceryqty02.get() * self.groceryprice[1] )
        self.grocerytotal03 = float(self.groceryqty03.get() * self.groceryprice[2] )
        self.grocerytotal04 = float(self.groceryqty04.get() * self.groceryprice[3] )
        self.grocerytotal05 = float(self.groceryqty05.get() * self.groceryprice[4] )
        self.grocerytotal06 = float(self.groceryqty06.get() * self.groceryprice[5] )

        self.grocerysum.set( str ( self.grocerytotal01 + self.grocerytotal02 + self.grocerytotal03 + self.grocerytotal04 + self.grocerytotal05 + self.grocerytotal06 ) )


        self.stationarytotal01 = float(self.stationaryqty01.get() * self.stationaryprice01)
        self.stationarytotal02 = float(self.stationaryqty02.get() * self.stationaryprice02)
        self.stationarytotal03 = float(self.stationaryqty03.get() * self.stationaryprice03)
        self.stationarytotal04 = float(self.stationaryqty04.get() * self.stationaryprice04)
        self.stationarytotal05 = float(self.stationaryqty05.get() * self.stationaryprice05)
        self.stationarytotal06 = float(self.stationaryqty06.get() * self.stationaryprice06)

        self.stationarysum.set(  str( self.stationarytotal01 + self.stationarytotal02 + self.stationarytotal03 + self.stationarytotal04 + self.stationarytotal05 + self.stationarytotal06  )  )

        self.cosmetictax.set( str(float(self.cosmeticsum.get()) * self.cosmeticstaxrate))
        self.grocerytax.set(str(float(self.grocerysum.get()) * self.grocerytaxrate))
        self.stationarytax.set(str(float(self.stationarysum.get()) * self.stationarytaxrate))

        self.Total_bill = float(self.cosmeticsum.get()) + float(self.grocerysum.get()) + float(self.stationarysum.get()) + float(self.cosmetictax.get()) + float(self.grocerytax.get()) + float(self.stationarytax.get())


    def welcome(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\n\tWelcome GT Mart")
        self.txtarea.insert(END, f"\n\n Bill Number   :  {self.billno.get()}")
        self.txtarea.insert(END, f"\n Cutomer Name  :  {self.cname.get()} ")
        self.txtarea.insert(END, f"\n Phone No      :  {self.cphone.get()}")
        self.txtarea.insert(END, f"\n===============================================")
        self.txtarea.insert(END, f"\n Products\t\t\t Qty\t\tPrice")
        self.txtarea.insert(END, f"\n===============================================")

    def clear(self):
        op = messagebox.askyesno("Exit", "Do you really want to Clear")
        if op > 0 :
            self.cosmeticsqty01.set(0)
            self.cosmeticsqty02.set(0)
            self.cosmeticsqty03.set(0)
            self.cosmeticsqty04.set(0)
            self.cosmeticsqty05.set(0)
            self.cosmeticsqty06.set(0)

            self.groceryqty01.set(0)
            self.groceryqty02.set(0)
            self.groceryqty03.set(0)
            self.groceryqty04.set(0)
            self.groceryqty05.set(0)
            self.groceryqty06.set(0)

            self.stationaryqty01.set(0)
            self.stationaryqty02.set(0)
            self.stationaryqty03.set(0)
            self.stationaryqty04.set(0)
            self.stationaryqty05.set(0)
            self.stationaryqty06.set(0)

            self.cosmeticsum.set("")
            self.grocerysum.set("")
            self.stationarysum.set("")
            self.cosmetictax.set("")
            self.grocerytax.set("")
            self.stationarytax.set("")

            self.cname.set("")
            self.cphone.set("")

            self.billno.set("")
            x = random.randint(10000, 99999)
            self.billno.set(str(x))
            self.search.set()
            self.welcome()

    def exit(self):

        op = messagebox.askyesno("Exit","Do you want to Exit")
        if op > 0:
            self.t.destroy()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if op > 0:
            self.data = self.txtarea.get("1.0", END)
            f1 = open("bills/" + str(self.billno.get()) + ".txt", "w")
            f1.write(self.data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill No : {self.billno.get()}  Saved Sucessfully ")
        else:
            return

    def billarea(self):
        if self.cname.get() == "" or self.cphone.get() == "":
            messagebox.showerror("Error", "Customer Detail are Must")
        elif self.cosmeticsum.get() == "0.0" and self.grocerysum.get() == "0.0" and self.stationarysum.get() == "0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome()
            # cosmetics

            if self.cosmeticsqty01.get() != 0:
                self.txtarea.insert(END, f"\n Bath Soap \t\t\t  {self.cosmeticsqty01.get()}\t\t{self.cosmetictotal01}")
            if self.cosmeticsqty02.get() != 0:
                self.txtarea.insert(END, f"\n Face Cream \t\t\t  {self.cosmeticsqty02.get()}\t\t{self.cosmetictotal02}")
            if self.cosmeticsqty03.get() != 0:
                self.txtarea.insert(END, f"\n Face Wash \t\t\t  {self.cosmeticsqty03.get()}\t\t{self.cosmetictotal03}")
            if self.cosmeticsqty04.get() != 0:
                self.txtarea.insert(END, f"\n Hair Spray \t\t\t  {self.cosmeticsqty04.get()}\t\t{self.cosmetictotal04}")
            if self.cosmeticsqty05.get() != 0:
                self.txtarea.insert(END, f"\n Hair Gel \t\t\t  {self.cosmeticsqty05.get()}\t\t{self.cosmetictotal05}")
            if self.cosmeticsqty06.get() != 0:
                self.txtarea.insert(END, f"\n Body Cream \t\t\t {self.cosmeticsqty06.get()}\t\t{self.cosmetictotal06}")


            # grocery
            if self.groceryqty01.get() != 0:
                self.txtarea.insert(END, f"\n Rice \t\t\t  {self.groceryqty01.get()}\t\t{self.grocerytotal01}")
            if self.groceryqty02.get() != 0:
                self.txtarea.insert(END, f"\n Food Oil \t\t\t  {self.groceryqty02.get()}\t\t{self.grocerytotal02}")
            if self.groceryqty03.get() != 0:
                self.txtarea.insert(END, f"\n Wheat \t\t\t  {self.groceryqty03.get()}\t\t{self.grocerytotal03}")
            if self.groceryqty04.get() != 0:
                self.txtarea.insert(END, f"\n Daal \t\t\t  {self.groceryqty04.get()}\t\t{self.grocerytotal04}")
            if self.groceryqty05.get() != 0:
                self.txtarea.insert(END, f"\n Sugar \t\t\t  {self.groceryqty05.get()}\t\t{self.grocerytotal05}")
            if self.groceryqty06.get() != 0:
                self.txtarea.insert(END, f"\n Tea Powder \t\t\t  {self.groceryqty06.get()}\t\t{self.grocerytotal06}")


            # stationary
            if self.stationaryqty01.get() != 0:
                self.txtarea.insert(END, f"\n Pen \t\t\t {self.stationaryqty01.get()}\t\t{self.stationarytotal01}")
            if self.stationaryqty02.get() != 0:
                self.txtarea.insert(END, f"\n Pencil \t\t\t  {self.stationaryqty02.get()}\t\t{self.stationarytotal02}")
            if self.stationaryqty03.get() != 0:
                self.txtarea.insert(END, f"\n Eraser \t\t\t  {self.stationaryqty03.get()}\t\t{self.stationarytotal03}")
            if self.stationaryqty04.get() != 0:
                self.txtarea.insert(END, f"\n Exam Pad \t\t\t  {self.stationaryqty04.get()}\t\t{self.stationarytotal04}")
            if self.stationaryqty05.get() != 0:
                self.txtarea.insert(END, f"\n Scale \t\t\t  {self.stationaryqty05.get()}\t\t{self.stationarytotal05}")
            if self.stationaryqty06.get() != 0:
                self.txtarea.insert(END, f"\n Geometry Box \t\t\t  {self.stationaryqty06.get()}\t\t{self.stationarytotal06}")

            self.txtarea.insert(END, f"\n-----------------------------------------------")
            if self.cosmetictax.get() != "0.0":
                self.txtarea.insert(END, f"\n Cosmetics Tax \t\t\t\t\t {self.cosmetictax.get()}")
            if self.grocerytax.get() != "0.0":
                self.txtarea.insert(END, f"\n Grocery Tax \t\t\t\t\t {self.grocerytax.get()}")
            if self.stationarytax.get() != "0.0":
                self.txtarea.insert(END, f"\n Stationary Tax \t\t\t\t\t {self.stationarytax.get()}")
            self.txtarea.insert(END, f"\n-----------------------------------------------")

            self.txtarea.insert(END, f"\n Total Bill :\t\t\t\t {self.Total_bill}")

            self.txtarea.insert(END, f"\n-----------------------------------------------")
            self.save_bill()

    def findbill(self):
        present = "no"
        for i in os.listdir("bills/"):

            #print(i.split('.')[0] )
            #print(self.billno)
            
            if i.split('.')[0] == self.billno.get():
                f1 = open(f"bills/{i}", "r")
                print(f1)
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)

                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No.")

# __main__
t = Tk()
billObject = Billing_Application(t)
t.mainloop(0)

