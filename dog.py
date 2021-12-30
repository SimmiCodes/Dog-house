from os import name
from tkinter.font import names
import connection
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
window = Tk()

window.iconbitmap("h.ico")
window.title("MY DOGGO HOUSE")

def add_dog():
    filename = None
    var = IntVar()
    gen_dic = {1:'Female', 2: "Male"}
    def browse():
        nonlocal filename
        filename = filedialog.askopenfilename(initialdir="/",title="Select Image", filetypes=(('Jpg files',"*.jpg"),('Jpeg files',"*.jpeg"),('Png files',"*.png")))
        print(filename)

    def insert():
        n_val = name.get()
        img_val = filename
        b_val = breed_e.get()
        gen_val = gen_dic[var.get()]
        about_val = about_entry.get('1.0',END)
        meet_val = meet_entry.get('1.0', END)
        price_val=price_entry.get('1.0', END)
        
        print(n_val, img_val, b_val, gen_val, about_val, meet_val,price_val)
        connection.insert_data(n_val, img_val, b_val, gen_val, about_val, meet_val,price_val)
        messagebox.showinfo("Success","Insert record successfully")
        

    global frame
    frame.destroy()
    frame = Frame(window,bg="#227093",width=650,height=400)
    frame.pack(fill=BOTH,expand=YES)

    heading = Label(frame,text="Add Dog",fg="white",font=("Comic Sans MS", 20,"bold underline"),bg="#227093",)
    heading.place(x=230,y=40)

    name_label = Label(frame,text="Name: ",fg="white",font=("Comic Sans MS", 11,),bg="#227093",)
    name_label.place(x=150,y=90)
    name = Entry(frame,fg="white",font=("Comic Sans MS", 11,),bg="#227093",)
    name.place(x=280,y=90)

    image = Label(frame,text="Upload image",fg="white",font=("Comic Sans MS", 11),bg="#227093",)
    image.place(x=150,y=130)
    upload = Button(frame,text='Browse',fg="white",font=("Comic Sans MS", 11,"bold underline"),bg="#227093",bd=0,command=browse)
    upload.place(x=280,y=130)

    breed_l = Label(frame,text="Breed",fg="white",font=("Comic Sans MS", 11),bg="#227093",)
    breed_l.place(x=150,y=170)
    breed_e = Entry(frame,fg="white",font=("Comic Sans MS", 11,),bg="#227093",)
    breed_e.place(x=280,y=170)

    gender = Label(frame,text="Gender: ",fg="white",font=("Comic Sans MS", 11,),bg="#227093",)
    gender.place(x = 150,y=210)

    
    gender_female = Radiobutton(frame,text="Female",fg="white",font=("Comic Sans MS", 11,),bg="#227093",variable=var,value=1, selectcolor='#227093')
    gender_female.place(x=280,y=210)

    gender_male = Radiobutton(frame,text="Male",fg="white",font=("Comic Sans MS", 11,),bg="#227093",variable=var,value=2, selectcolor='#227093')
    gender_male.place(x=380,y=210)

    about = Label(frame,text="About: ",fg="white",font=("Comic Sans MS", 11,),bg="#227093",)
    about.place(x = 150,y=260)

    about_entry = Text(frame,fg="white",width=30,height=2,font=("Comic Sans MS", 11,),bg="#227093",wrap=WORD)
    about_entry.place(x=280,y=260)

    meet = Label(frame,text="Meet"+name.get()+" : ",fg="white",font=("Comic Sans MS", 11,),bg="#227093",)
    meet.place(x = 150,y=340)

    meet_entry = Text(frame,fg="white",width=30,height=2,font=("Comic Sans MS", 11,),bg="#227093",)
    meet_entry.place(x=280,y=340)
    

    price = Label(frame,text="price: "  ,fg="white",font=("Comic Sans MS", 11,),bg="#227093",)
    price.place(x = 150,y=400)

    price_entry = Text(frame,fg="white",width=30,height=1,font=("Comic Sans MS", 11,),bg="#227093",)
    price_entry.place(x=280,y=400)


    back_b = Button(frame,text="Back",width=7,fg="white",font=("Comic Sans MS", 11,),bg="#227093",command=mainFrame)
    back_b.place(x=190,y=450)

    next_b = Button(frame,text="Next",width=7,fg="white",font=("Comic Sans MS", 11,),bg="#227093",command=insert)
    next_b.place(x=380,y=450)



def convert_to_image(path, content):
    with open(path,'wb') as file:
        file.write(content)

def show_data(records, n):
    if n >=0 and n < len(records):
        record = records[n]
        global frame 
        frame.destroy()
        frame = Frame(window,bg="#227093",width=650,height=430)
        frame.pack(fill=BOTH, expand=True)

        name = Label(frame,text="Name : " + record[1],font=("Arial Unicode MS",13),fg="white",bg="#227093")
        name.place(x=400,y=50)
        breed = Label(frame,text="Breed : "+record[3],font=("Arial Unicode MS",13),fg="white",bg="#227093")
        breed.place(x=400,y=90)


        img = record[2]
        path = "C:\\Users\\Win\\Desktop\\python class\\dog image"+ record[1]+ ".jpg" 
        image = convert_to_image(path,img)

        img = Image.open(path).resize((200,180))
        render = ImageTk.PhotoImage(img)
        dog_image = Label(frame,width=200,height=180,image=render,bg="#7f8c8d")
        dog_image.image = render
        dog_image.place(x=120,y=50)

        gender = Label(frame,text="Gender: " +record[4],font=("Arial Unicode MS",13),fg="white",bg="#227093")
        gender.place(x=400,y=130)

        about = Text(frame,width=19,font=("Arial Unicode MS",11),fg="white",bg="#227093",height=5,bd=0,wrap=WORD)
        about.place(x=400,y=170)
        about.insert(END,"About: " + record[5])
        about.config(state=DISABLED)
    

        meet = Text(frame,font=("Arial Unicode MS",8),fg="white",bg="#227093",width=34,bd=0,wrap=WORD)
        meet.place(x=120,y=210)
        meet.insert(END,"Meet : " + record[6])
        meet.config(state=DISABLED)

        price = Label(frame,text="price : " + record[7],font=("Arial Unicode MS",13),fg="white",bg="#227093")
        price.place(x=400,y=200)



        next = Button(frame,text="Next",bg="#227093",font=("Arial Unicode MS", 11),
    
        fg="white",padx=20,pady=2,bd=0.5, command=lambda : show_data(records,n+1))
        next.place(x=330,y=350)

        previous = Button(frame,text="Previous",bg="#227093",font=("Arial Unicode MS", 11),
        fg="white",padx=20,pady=2,bd=0.5,command=lambda : show_data(records,n-1))
        previous.place(x=200,y=350)

        back = Button(frame,text="Back",bg="#227093",font=("Arial Unicode MS", 11),fg="white",padx=20,pady=2,bd=0.5, command=mainFrame)
        back.place(x=430,y=350)

        buy = Button(frame,text="Buy",bg="#227093",font=("Arial Unicode MS", 11),fg="white",padx=20,pady=2,bd=0.5,command=lambda : customer_detail(record[1], record[3],record[7],record[0]))
        buy.place(x=530,y=350)
    elif n >= len(records):
            show_data(records, 0)
    else:
        show_data(records, len(records)-1)

def see_all_dogs():
    global frame 
    frame.destroy()
    records=connection.select_all_data()
    frame = Frame(window,bg="#227093",width=650,height=430)
    frame.pack(fill=BOTH, expand=True)
    print(len(records))

    if len(records) == 0:
        name = Label(frame,text="No Records Available ",font=("Arial Unicode MS",13),fg="white",bg="#227093")
        name.place(x=400,y=50)
    
    else:
        show_data(records,0)
 
 
def see_all_dogs_by_species():
    def records_get():
        breed = list.get(ACTIVE)
        records = connection.select_by_breed(breed)
        show_data(records,0)
    global frame
    frame.destroy()   
    frame = Frame(window, bg = '#227093')
    frame.pack(fill=BOTH, expand=True)
    

    f1 = Frame(frame,bg = 'red')
    f1.place(x = 150, y = 150)
    scroll = Scrollbar(f1)
    scroll.pack(side=RIGHT, fill=Y)

    list = Listbox(f1, width = 20, height=4,bg = '#227093', font=('Comic Sans MS',20, 'bold'),fg="white")
    list.pack()

    list.config(yscrollcommand=scroll.set)
    scroll.config(command=list.yview)

    records = connection.select_breed()
    for breed in records:
        list.insert(END,breed[0])
        

    next = Button(frame,text="Next",bg="#227093",font=("Arial Unicode MS", 11),
    
    fg="white",padx=20,pady=2,bd=0.5, command=records_get)
    next.place(x=330,y=350)

    back = Button(frame,text="Back",bg="#227093",font=("Arial Unicode MS", 11),
    fg="white",padx=20,pady=2,bd=0.5,command=mainFrame)
    back.place(x=200,y=350)

def customer_detail(name1,breed1,price,id):
    def buy_dog():
        
        c_name = customer_name.get()
        number = phone_number.get()
        feedback = feedback_entry.get(1.0,END)
        connection.insert_customer_data(name1,breed1,c_name,number,feedback,price)
        messagebox.showinfo("Checkout","THANKS FOR BUYING")
        connection.remove_dog(id)

        

    global frame 
    frame.destroy()
    frame = Frame(window,bg='#34ace0')
    frame.pack(fill=BOTH, expand=True)

   

    #labels
    l = Label(frame,text='Customer Details',font=('Comic Sans Ms',16,'bold','underline'),bg='#34ace0')
    l.place(x=250,y=20)

    #label for Customer name 
    l1 = Label(frame,text='Customer Name: ',bg='#34ace0',font=('Comic Sans Ms',12))
    l1.place(x=150,y=70)

    #name entry box
    customer_name = Entry(frame,width=27)
    customer_name.place(x=310,y=70)

    #label to add breed
    l3 = Label(frame,text='Breed:',bg='#34ace0',font=('Comic Sans Ms',12))
    l3.place(x=150,y=100)

    #entry for breed
    t2 = Label(frame,text=breed1,width=27)
    t2.place(x=310,y=102)

    #label to gender
    l4 = Label(frame,text='Dog Name:',bg='#34ace0',font=('Comic Sans Ms',12))
    l4.place(x=150,y=130)

        #gender

    l21 = Label(frame,text=name1,width=27)
    l21.place(x=310,y=130)

    #label to consumer number
    l5 = Label(frame,text='Consumer Number:',bg='#34ace0',font=('Comic Sans Ms',12))
    l5.place(x=150,y=160)

    #label to price
    l6 = Label(frame,text='Price:',bg='#34ace0',font=('Comic Sans Ms',12))
    l6.place(x=150,y=190)

    

    #entrybox for consumer number
    phone_number = Entry(frame,width=26)
    phone_number.place(x=310,y=160)

    #Entrybox for price
    t4 = Label(frame,text =price,width=26)
    t4.place(x=310,y=192)



    #label to feedback
    l7 = Label(frame,text='Feedback:',bg='#34ace0',font=('Comic Sans Ms',12))
    l7.place(x=150,y=250)
    #Entrybox for feedback
    feedback_entry = Text(frame,height=3,width=20,wrap=WORD)
    feedback_entry.place(x=310,y=250)

    #buttton for Buy 
    bnext = Button(frame,text='Buy',bg='#34ace0',width=10,command=buy_dog)
    bnext.place(x=390,y=340)

    #buttton for back 
    bback = Button(frame,text='Back',bg='#34ace0',width=10,command = mainFrame)
    bback.place(x=160,y=340)

        
        
def customer_details():
        global frame
        frame.destroy()
        frame=Frame(window,bg="#7f8c8d",width=650,height=430)
        frame.pack(fill=BOTH,expand=YES)
        treev=ttk.Treeview(frame,selectmode="browse")

        treev.pack(side="left",expand=YES,fill=BOTH)
        
        verscrlbar=ttk.Scrollbar(frame,
                                orient="vertical",
                                command=treev.yview)
        
        verscrlbar.pack(side="right",fill="y")

        treev.configure(yscrollcommand=verscrlbar.set)

        treev["columns"]=("1","2","3","4","5","6")

        treev["show"]="headings"

        treev.column('1',width = 30,anchor='c')
        treev.column('2',width = 30,anchor='c')
        treev.column('3',width = 30,anchor='c')
        treev.column('4',width = 30,anchor='c')
        treev.column('5',width = 30,anchor='c')
        treev.column('6',width = 30,anchor='c')

        treev.heading('1',text="Customerid")
        treev.heading('2',text="Dog_Name")
        treev.heading('3',text="Dog_Breed")
        treev.heading('4',text="Customer_Name")
        treev.heading('5',text="Customer_no.")
        treev.heading('6',text="Feedback")

        records=connection. select_customer_detail()
        for i in records:

         treev.insert("",END,
                      values=(i[0],i[1],i[2],i[3],i[4],i[5]))

        back = Button(frame,text="Back",bg="black",font=("Arial Unicode MS", 11),
        fg="white",padx=20,pady=2,bd=0.5,command=mainFrame)
        back.place(x=250,y=500)
        
def mainFrame():
    global frame
    frame.destroy()
    
    def rb_select():
        val = var_rb.get()
        if val == 1:
            print("See All Dogs")
            see_all_dogs()
        elif val == 2:
            print("See All dogs By Species")
            see_all_dogs_by_species()
        elif val == 3:
            print("Add Dog")
            add_dog()
        else:
            print("Customer Detail")
            customer_details()            


    var_rb = IntVar()
    frame = Frame(window, bg = '#227093')
    frame.pack(fill=BOTH, expand=True)
    see_all_rb = Radiobutton(frame, text="See All Dogs",bg = '#227093', font=('Comic Sans MS',20, 'bold'),fg="white",activebackground="#227093",activeforeground="white",variable=var_rb, value=1, selectcolor="#227093", command=rb_select)
    see_all_rb.place(x=100,y=100)
    see_by_species_rb = Radiobutton(frame, text="See All Dogs By Species",bg = '#227093', font=('Comic Sans MS',20, 'bold'),fg="white",activebackground="#227093",activeforeground="white",variable=var_rb, value=2,selectcolor="#227093", command=rb_select)
    see_by_species_rb.place(x=100,y=150)
    add_rb = Radiobutton(frame, text="Add Dog",bg = '#227093', font=('Comic Sans MS',20, 'bold'),fg="white",activebackground="#227093",activeforeground="white",variable=var_rb, value=3,selectcolor="#227093", command=rb_select)
    add_rb.place(x=100,y=200)
    customer_rb = Radiobutton(frame, text="Customer Details",bg = '#227093', font=('Comic Sans MS',20, 'bold'),fg="white",activebackground="#227093",activeforeground="white",variable=var_rb, value=4,selectcolor="#227093", command=rb_select)
    customer_rb.place(x=100,y=250)


frame = Frame(window, bg = '#227093')
frame.pack(fill=BOTH, expand=True)

label1 = Label(frame, text="Welcome To",bg = '#227093', font=('Comic Sans MS',25, 'bold'),fg="white")
label1.place(x = 180, y= 150)

label2 = Label(frame, text="The Doggo House",bg = '#227093', font=('Comic Sans MS',23,'bold'),fg="white")
label2.place(x = 140, y= 200)

frame.after(2000, mainFrame)


window.geometry('600x550')
window.mainloop()