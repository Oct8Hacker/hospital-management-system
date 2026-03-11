#Importing Necessary Modules
from tkinter import *
from tkinter import messagebox,ttk,font
import Logic
from functools import reduce
from csvfilereader import AppointmentHistoryManager,login,chat

#Main Menu GUI
class GUI_main_window_login(Tk):

    def __init__(self):
        super().__init__()
        self.title('Main menu')
        self.geometry("800x600")
        self.resizable(False, False)
        self.admin = 1
    
    #Main menu
    def ui(self):
        canvas1= Canvas(self,width = 800,height = 600)
        canvas1.place(x = 0,y = 0)
        
        self.background_image = PhotoImage(file = "GUI.png")
        canvas1.create_image(0,0,image = self.background_image,anchor=NW)
        
        appointment_button = Button(self,text="Book Appointment", bg="#40E0D0",borderwidth=5,command =self.appointment_gui_opener,font="Helvetica 14",relief= "raised")
        appointment_button.place(x= 200, y = 250)
        
        manage_appointment = Button(self, text= "Manage Appointments", bg="#40E0D0",borderwidth=5,command = self.login_dr_page_opener,font="Helvetica 14",relief = "raised")
        manage_appointment.place(x= 400, y = 250)

    #Open patient window
    def appointment_gui_opener(self):
        self.destroy()
        patient_window = GUI_main_window_patient()
        patient_window.ui()
        patient_window.mainloop()

    #Open login page for doctor
    def login_dr_page_opener(self):
        login_page = Toplevel(self)
        login_page.geometry("400x200")
        login_page.grab_set()
        login_page.resizable(False, False)
        login_page.configure(background='black')
        login_page.title("Login")
        
        name_label = Label(login_page,text="Username",foreground='white',background='black',font=font.Font(family ="Helvetica 14",size = 15,weight = 'bold'))
        name_label.pack(pady=5)
        
        name_entry = Entry(login_page,foreground='white',font="Helvetica 14",background='gray')
        name_entry.pack()
        
        password_label = Label(login_page,text="Password",background='black',foreground='white',font=font.Font(family ="Helvetica 14",size = 15,weight = 'bold'))
        password_label.pack(pady=5)
        
        password_entry = Entry(login_page,foreground='white',font="Helvetica 14",show="*",background='gray')
        password_entry.pack()

        confirm_button = Button(login_page,text="Confirm",background='green',foreground='white',font=font.Font(family ="Helvetica 14",size = 15,weight = 'bold'),command = lambda: checker_credentials())
        confirm_button.pack(pady=15)
        name_entry.focus()
        
        #Logic for admin page
        def admin_log(opt,name,pswd=0):
            if opt == 1:
                if Logic.adminLogic.addDr(name,pswd):
                    messagebox.showinfo("Success",'Doctor successfully Added')
                else:
                    messagebox.showinfo("Failure","Doctor already exists")
            elif opt == 2:
                if Logic.adminLogic.remDr(name,pswd):
                    messagebox.showinfo("Success",'Doctor successfully removed')
                else:
                    messagebox.showinfo("Failure","Doctor not found or password is wrong")
            elif opt == 3:
                if Logic.adminLogic.viewDr(name):
                    login_page.destroy()
                    self.destroy()
                    dr_window = GUI_main_window_dr(name)
                    dr_window.ui()
                    dr_window.mainloop()
                else:
                    messagebox.showinfo("Failure","Doctor does not exist")

        #Checks password for both admin and doctor
        def checker_credentials(event = None):
            if self.admin:
                user = name_entry.get()
                pswd = password_entry.get()

                if login.login(user,pswd):
                    login_page.destroy()
                    self.destroy()
                    dr_window = GUI_main_window_dr(user)
                    dr_window.ui()
                    dr_window.mainloop()
                else:
                    messagebox.showerror("Invalid Credentials","Please enter the correct credentials")
            else:
                #Admin Page
                if password_entry.get() == 'admin':
                    login_page.destroy()
                    admin = Toplevel(self)
                    admin.geometry("450x250")
                    admin.resizable(False, False)
                    admin.grab_set()
                    admin.configure(background='black')
                    admin.title("Admin")

                    name_l = Label(admin, text="Name:", bg="black", fg="white",font=font.Font(family ="Helvetica 14",size = 15,weight = 'bold'))
                    name_l.grid(row=0, column=0, padx=10, pady=15)

                    name_e = Entry(admin,font=font.Font(family ="Helvetica 14",size = 15,weight = 'bold'))
                    name_e.grid(row=0, column=1, pady=15)
                    name_e.focus()

                    password_l = Label(admin, text="Password:", bg="black", fg="white",font=font.Font(family ="Helvetica 14",size = 15,weight = 'bold'))
                    password_l.grid(row=1, column=0, padx=10, pady=10)

                    password_e = Entry(admin, show="*",font=font.Font(family ="Helvetica 14",size = 15,weight = 'bold'))
                    password_e.grid(row=1, column=1, pady=10)

                    button_frame = Frame(admin, bg='black')
                    button_frame.grid(row=2, column=0, columnspan=2, pady=10)

                    add_doctor_button = Button(button_frame, command=lambda: admin_log(1,name_e.get(),password_e.get()),text="Register Doctor",bg='Green',fg='white',font=font.Font(family ="Helvetica 14",size = 15,weight = 'bold'))
                    add_doctor_button.grid(row=0, column=0, padx=30, pady=10)

                    remove_doctor_button = Button(button_frame, command=lambda: admin_log(2,name_e.get(),password_e.get()),text="Remove Doctor",bg='red',fg='white',font=font.Font(family ="Helvetica 14",size = 15,weight = 'bold'))
                    remove_doctor_button.grid(row=0, column=1, padx=30, pady=10)

                    view_doctor_button = Button(admin, command=lambda: admin_log(3,name_e.get()),text="View Doctor",bg = 'blue',fg = 'white',font=font.Font(family ="Helvetica 14",size = 15,weight = 'bold'))
                    view_doctor_button.grid(row=3, columnspan=2, pady=10)

                else:
                    messagebox.showerror("Invalid",'Try again')

        #Admin login page
        def admin_login(event = None):
            name_label.destroy()
            name_entry.destroy()
            password_label.config(text='Admin')
            password_entry.focus()
            self.admin=0

        #Keybind for ease of use
        login_page.bind('<Return>',checker_credentials)
        login_page.bind('<Control-o>', admin_login)
        
        login_page.mainloop()

#Doctor GUI
class GUI_main_window_dr(Tk):

    def __init__(self,name):
        super().__init__()
        self.geometry("800x600")
        self.configure(bg="#1C1C1C")
        self.resizable(False, False)
        self.grab_set()
        self.title("Doctor")
        self.doctor = name
    
    def ui(self):

        #Loads all the appointments of that doctor and puts it into a Treeview
        def loadAppointments():
            L = Logic.doctorLogic.loadAppointments(self.doctor)
            if L == []:
                for i in appointments_listbox.get_children():
                    appointments_listbox.delete(i)
                messagebox.showinfo("No Appointments", f"No appointments found for {self.doctor}.")
            else:
                for i in appointments_listbox.get_children():
                    appointments_listbox.delete(i)

                for appointment in L:
                    appointments_listbox.insert("", END, values=appointment)
                while len(appointments_listbox.get_children()) < 23:
                    appointments_listbox.insert("", END, values=("", "", "", "", ""))

        #Logic for confirm appointment
        def confirm():
            if Logic.doctorLogic.complete_appointment(appointments_listbox.item(appointments_listbox.selection(), "values")):
                messagebox.showinfo("Success", "Appointment marked as completed.")
            else:
                messagebox.showinfo("Error"," Try Again")
            loadAppointments()

        #Logic for cancel appointment
        def cancel():
            if Logic.doctorLogic.cancel_appointment(appointments_listbox.item(appointments_listbox.selection(), "values")):
                messagebox.showinfo("Success", "Appointment marked as cancelled.")
            else:
                messagebox.showinfo("Error","Try Again")
            loadAppointments()
  
        frame2 = Frame(self,background = "black" ,width=800, height=600, highlightbackground="black", highlightthickness=1)
        frame2.pack(fill='both',expand=True)

        appointments_listbox = ttk.Treeview(frame2,height=15,columns=("Doctor", "Name", "Age", "Time","Status"), show="headings")
        appointments_listbox.pack(pady=20)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",background="gray",foreground="black",font = font.Font(size = 14),rowheight = 30)
        style.configure("Treeview.Heading",background="#222222",foreground = 'white',relief = 'sunken',font = font.Font(size = 14))
        style.map("Treeview",background=[('selected', 'green')],foreground=[('selected', 'white')])

        for i in ["Doctor", "Name", "Age", "Time","Status"]:
            appointments_listbox.heading(i, text=f"{i}")
            appointments_listbox.column(i, anchor="center",width = 150)

        Button(frame2, fg="white", bg="green", text="Complete Appointment", font="Arial 14",command = confirm).pack(side="left",padx = 24,pady = (0,20),anchor="w")
        Button(frame2, fg="white", bg="red", text="Cancel Appointment", font="Arial 14",command = cancel).pack(side="left",padx = 20,pady = (0,20),anchor="e")
        
        chatbutton = Button(frame2, fg="white", bg="Blue", text="Chat", font="Arial 14",command = lambda:chat_window(self))
        chatbutton.pack(pady=(0,20),side="right",padx = 24,anchor="w")

        def chat_window(self):

            #Displays the message of the patient selected
            def show_message():
                selected_index = chat_listbox.curselection()
                if selected_index:
                    selected_item = chat_listbox.get(selected_index[0])
                    for i in msgs:
                        if selected_item == i[0]:
                            messagebox.showinfo(f"MESSAGE FROM {selected_item}",i[1])
                else:
                    messagebox.showinfo("Error", "Patient not selected")

            #This is a list of lists, with first element as patient name and second as messages
            msgs = chat.getMSG(self.doctor)

            chat_window = Toplevel(self)
            chat_window.geometry("600x400")
            chat_window.resizable(False, False)
            chat_window.grab_set()
            chat_window.configure(background='black')
            
            chat_label = Label(chat_window,text="Message from patients",background='black',foreground='white',font=font.Font(family ="Helvetica 14",size = 20,weight = 'bold' ))
            chat_label.pack(pady=10)

            chat_listbox = Listbox(chat_window,background='gray',selectbackground='Green',activestyle='none',selectforeground='white',font=font.Font(family ="Helvetica 14",size = 15),justify='center')
            for i in msgs:
                chat_listbox.insert(END,i[0])
            chat_listbox.pack(pady = 5,expand=1,fill='both',padx = 100)
            
            sendbutton = Button(chat_window, text="Show",background='Green',foreground='white',font=font.Font(family ="Helvetica 14",size = 15,weight = 'bold'),command=show_message)
            sendbutton.pack(pady = 5)

            chat_window.mainloop()    
        
        loadAppointments()

#Patient GUI
class GUI_main_window_patient(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("550x450")
        self.title("Appointment")
        self.config(background='#40E0D0')
        self.resizable(False, False)
        self.name = StringVar()
        self.age = IntVar(value='')
        self.doctor = StringVar()
        self.timeslot = StringVar()

    def ui(self):
        Label(self, text="Name", font=font.Font(family ="Helvetica 14",size = 15,weight = 'bold'), bg='#40E0D0').pack(padx=5, pady=(5,2))
        nameentry = Entry(self, textvariable=self.name,justify='center', font=font.Font(family ="Helvetica 14",size = 15))
        nameentry.pack(padx=150, pady=(0,5), fill=X)

        Label(self, text="Age", font=font.Font(family ="Helvetica 14",size = 15,weight = 'bold'), bg='#40E0D0').pack(padx=5, pady=(5,2))
        ageentry = Entry(self,textvariable=self.age,justify='center', font=font.Font(family ="Helvetica 14",size = 15))
        ageentry.pack(padx=150, pady=(0,5), fill=X)

        Label(self, text="Doctor",font=font.Font(family ="Helvetica 14",size = 15,weight = 'bold'), bg='#40E0D0').pack(padx=5, pady=(5,2))
        doctorentry = ttk.Combobox(self,justify='center', state="readonly", values=[i[0] for i in login.getDrNames()], textvariable=self.doctor, font=font.Font(family ="Helvetica 14",size = 15))
        doctorentry.pack(padx=150, pady=(0,5), fill=X)

        Label(self, text="Select a time slot", font=font.Font(family ="Helvetica 14",size = 15,weight='bold'), bg='#40E0D0').pack(padx=5, pady=(5,2))
        timeentry = ttk.Combobox(self, state="readonly", justify='center',values=list(reduce(lambda x, y: x + y, [[f"{a}:{b:02}" for b in range(0, 60, 20)] for a in [10, 11, 12, 13, 19, 20, 21]])), textvariable=self.timeslot, font="Arial 14")
        timeentry.pack(padx=150, pady=(0,5), fill=X)

        #Books an appointment for the patient
        def submit():
            appointment_manager = Logic.appointment(nameentry.get(), 0 if ageentry.get() == '' else ageentry.get(), doctorentry.get(), timeentry.get())  
            if appointment_manager.datachecker():
                appointment_history_manager = AppointmentHistoryManager(nameentry.get(), ageentry.get(), doctorentry.get(), timeentry.get())
                if appointment_history_manager.checker():
                    messagebox.showinfo("Appointment Booked", f"Appointment with {doctorentry.get()} has been successfully booked.")
                    submit_btn.config(state='disabled')
                    chat_btn.config(state = 'normal')
                else:
                    messagebox.showerror("Error", "Appointment could not be booked as selected timeslot and Doctor is not available at that time.")
            else:
                messagebox.showerror("Error", "Appointment could not be booked. Please try again.")

        #Chat window for patient
        def chat_with_doctor():
            chat_window = Toplevel(self)
            chat_window.geometry("400x300")
            chat_window.grab_set()
            chat_window.resizable(False, False)
            chat_window.config(background='#40E0D0')

            inputtxt = Text(chat_window, height=5, width=30, font="Helvetica 14", wrap=WORD, relief="sunken")
            inputtxt.pack(padx=15, pady=15,expand=1,fill='both')

            def send_message():
                message = inputtxt.get("1.0", END).strip()
                doctor = self.doctor.get()
                name = nameentry.get()
                
                #Saves the message to csv file
                if message and doctor:
                    AppointmentHistoryManager.chat(doctor,message,name)
                    inputtxt.delete("1.0", END)
                    messagebox.showinfo("Info", "Message sent successfully!")
                    quit()
                else:
                    messagebox.showerror("Error", "Please select a doctor and enter a message.")

            sendbutton = Button(chat_window, text="Send", font="Helvetica 14",fg="white", bg="green",command=send_message)
            sendbutton.pack(padx=5, pady=(0,15))

            chat_window.mainloop()
            
        submit_btn = Button(self, text="Book Appointment", command=submit, font="Arial 14 bold", fg="white", bg="#FF5733", padx=10, pady=5)
        submit_btn.pack(padx=5, pady=15)
        chat_btn = Button(self, text="Chat with Doctor", state='disabled',command=chat_with_doctor, font="Arial 14 bold", fg="white", bg="#FF5733", padx=10, pady=5)
        chat_btn.pack(padx=5, pady=5, side="right")

#For testing purpose
if __name__ == '__main__':
    root = GUI_main_window_login()
    root.ui()
    root.mainloop()