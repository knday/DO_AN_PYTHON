from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk

class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")


        #============title==============
        lb1_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",10,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lb1_title.place(x=0,y=0,width=1295,height=50)


        #============logo===============
        img2=Image.open("C:\KIM NGỌC\PYTHON\hotel images\logohotel.png")
        img2=img2.resize((100,40),Image.BICUBIC)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbimg.place(x=5,y=2,width=100,height=40)

        #============labelFrame===========
        labelframeleft=LabelFrame(self.root,relief=RIDGE,text="Customner Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #=========labels and entrys========
        #custRef
        lb1_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lb1_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        entry_ref.grid(row=0,column=1)

        #cust name
        cname=Label(labelframeleft,font=("arial",12,"bold"),text="Customer Name:",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtcname.grid(row=1,column=1)

        #mother name
        lb1mname=Label(labelframeleft,font=("arial",12,"bold"),text="Mother Name:",padx=2,pady=6)
        lb1mname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtmname.grid(row=2,column=1)

        #gender combobox
        label_gender=Label(labelframeleft,font=("arial",12,"bold"),text="Gender:",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)


        #postcode
        lb1PostCode=Label(labelframeleft,font=("arial",12,"bold"),text="Post Code:",padx=2,pady=6)
        lb1PostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=4,column=1)

        #mobilenumber
        lb1Mobile=Label(labelframeleft,font=("arial",12,"bold"),text="Mobile:",padx=2,pady=6)
        lb1Mobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=5,column=1)

        #email
        lb1Email=Label(labelframeleft,font=("arial",12,"bold"),text="Email:",padx=2,pady=6)
        lb1Email.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtEmail.grid(row=6,column=1)

        #nationality
        lb1Nationality=Label(labelframeleft,font=("arial",12,"bold"),text="Nationality:",padx=2,pady=6)
        lb1Nationality.grid(row=7,column=0,sticky=W)

        combo_Nationality=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Nationality["value"]=("Indian","American","Britist")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)


        #idproof type combobox
        lb1IdProof=Label(labelframeleft,font=("arial",12,"bold"),text="Nationality:",padx=2,pady=6)
        lb1IdProof.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_id["value"]=("Adhacard","DrivingLicence","Passport")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        #id number
        lb1IdNumber=Label(labelframeleft,font=("arial",12,"bold"),text="Id Number:",padx=2,pady=6)
        lb1IdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)

        #address
        lb1Address=Label(labelframeleft,font=("arial",12,"bold"),text="Address:",padx=2,pady=6)
        lb1Address.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtAddress.grid(row=10,column=1)

        #==========btn===============
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #=================table frame========
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="CView Details And Search System",font=("times new roman",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W)

        combo_Search=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Mobile","Ref",)
        combo_Search.current(0)
        combo_Search.grid(row=8,column=1)

        txtSearch=ttk.Entry(Table_Frame,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        #============Show data Table==============
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)



        self.Cust_Details_Table.pack(fill=BOTH,expand=1)






























if __name__ == "__main__":  
    root=Tk()  
    obj=Cust_Win(root)
    root.mainloop()  