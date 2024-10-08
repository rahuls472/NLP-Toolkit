import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from mydb import dataset
from myapi import API
# import nlpcloud

class NLPApp:
    def __init__(self):
        self.root = ttk.Window(themename="darkly")  # Initialize the ttkbootstrap window with a theme
        self.root.title("NLP Application")  # Set the window title
        self.root.geometry("400x600")  # Set the window size
        self.obj = dataset()
        self.obj1 = API()
        self.login_interface()
        self.root.mainloop()

    # Preparation of login GUI.
    def login_interface(self):
        self.clear()

        label = ttk.Label(self.root, text="Welcome to the NLP Application!", bootstyle="info")  # Example Label widget
        label.configure(font=('san serif', 12))
        label.pack(pady=(30, 30))

        label1 = ttk.Label(self.root, text=('Enter Email'))
        label1.pack()

        # Email Box
        self.email_input = ttk.Entry(self.root, width=40, bootstyle="success")
        self.email_input.pack(pady=(20, 15), ipady=4)

        label2 = ttk.Label(self.root, text=('Enter Password'))
        label2.pack()

        # Password Box
        self.password_input = ttk.Entry(self.root, width=40, show="*", bootstyle="success")
        self.password_input.pack(pady=(20, 15), ipady=4)

        # Adding Button to login
        btn1 = ttk.Button(self.root, text="Submit", command=self.perform_login, bootstyle=PRIMARY)
        btn1.pack()

        # Adding a button for Register
        label3 = ttk.Label(self.root, text="Not a member?")
        label3.pack(pady=(20))

        btn2 = ttk.Button(self.root, text="Register", command=self.register_gui, bootstyle=SECONDARY)
        btn2.pack(pady=(15))

    # Preparation of Registration GUI.
    def register_gui(self):
        self.clear()

        label = ttk.Label(self.root, text="Welcome to the NLP Application!", bootstyle="info")  # Example Label widget
        label.configure(font=('san serif', 12))
        label.pack(pady=(30, 30))

        label0 = ttk.Label(self.root, text=('Enter Name'))
        label0.pack()

        # Name Box
        self.name_input = ttk.Entry(self.root, width=40, bootstyle="success")
        self.name_input.pack(pady=(20, 15), ipady=4)

        label1 = ttk.Label(self.root, text=('Enter Email'))
        label1.pack()

        # Email Box
        self.email_input = ttk.Entry(self.root, width=40, bootstyle="success")
        self.email_input.pack(pady=(20, 15), ipady=4)

        label2 = ttk.Label(self.root, text=('Enter Password'))
        label2.pack()

        # Password Box
        self.password_input = ttk.Entry(self.root, width=40, show="*", bootstyle="success")
        self.password_input.pack(pady=(20, 15), ipady=4)

        # Adding Button to register
        btn1 = ttk.Button(self.root, text="Register", command=self.register_user, bootstyle=PRIMARY)
        btn1.pack()

        # Adding a button to go back to login
        label3 = ttk.Label(self.root, text="Already a member?")
        label3.pack(pady=(20))

        btn2 = ttk.Button(self.root, text="Login", command=self.login_interface, bootstyle=SECONDARY)
        btn2.pack(pady=(15))

    # Method to clear the GUI.
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    # Performing Registration Operations.
    def register_user(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        # Call the insert_user method and get the response
        response = self.obj.insert_user(name, email, password)

        # Check the response and show appropriate messages
        if response == 1:
            ttk.messagebox.showinfo('Success', 'Entry successful')
        elif response == 0:
            ttk.messagebox.showerror('Error', 'Email already exists')
        elif response == "Invalid email format.":
            ttk.messagebox.showerror('Error', 'Invalid email format. Please enter a valid email.')

    # Performing Login Operations.
    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.obj.search(email, password)

        if response:
            self.home_gui()
        else:
            ttk.messagebox.showerror('Error', 'Wrong credentials')

    # Preparation of home GUI.
    def home_gui(self):
        self.clear()

        label = ttk.Label(self.root, text="Welcome to the NLP Application!", bootstyle="info")  # Example Label widget
        label.configure(font=('san serif', 12))
        label.pack(pady=(30, 30))

        btn1 = ttk.Button(self.root, text="Sentiment Analysis", command=self.sentiment_gui, bootstyle=SUCCESS, width=40)
        btn1.pack(pady=(10))

        btn2 = ttk.Button(self.root, text="Name Entity Recognition", command=self.perform_NER, bootstyle=SUCCESS, width=40)
        btn2.pack(pady=(10))

        btn3 = ttk.Button(self.root, text="Headline Generation", command=self.heading_gen, bootstyle=SUCCESS, width=40)
        btn3.pack(pady=(10))

        btn4 = ttk.Button(self.root, text="Logout", command=self.login_interface, bootstyle=SECONDARY, width=40)
        btn4.pack(pady=(10))

    # Preparing heading generator GUI.
    def heading_gen(self):
        self.clear()

        label = ttk.Label(self.root, text="Welcome to the NLP Application!", bootstyle="info")  # Example Label widget
        label.configure(font=('san serif', 12))
        label.pack(pady=(30, 30))

        label1 = ttk.Label(self.root, text="Enter Paragraph")
        label1.pack()

        # Paragraph Box
        self.para_input = ttk.Entry(self.root, width=40, bootstyle="success")
        self.para_input.pack(pady=(20, 15), ipady=6)

        btn5 = ttk.Button(self.root, text="Generate", command=self.Heading_Generate, bootstyle=PRIMARY, width=40)
        btn5.pack(pady=(10))

        self.heading_result = ttk.Label(self.root, text="", bootstyle="info")
        self.heading_result.pack()

        btn6 = ttk.Button(self.root, text="Go Back", command=self.home_gui, bootstyle=SECONDARY)
        btn6.pack(pady=(10))

    # Performing Heading Generator Operations.
    def Heading_Generate(self):
        para = self.para_input.get()

        result = self.obj1.Heading(para)
        self.heading_result.config(text=result)

    # Preparing sentiment analysis GUI.
    def sentiment_gui(self):
        self.clear()

        label = ttk.Label(self.root, text="Welcome to the NLP Application!", bootstyle="info")  # Example Label widget
        label.configure(font=('san serif', 12))
        label.pack(pady=(30, 30))

        label1 = ttk.Label(self.root, text="Enter Paragraph")
        label1.pack()

        # Paragraph Box
        self.para_input = ttk.Entry(self.root, width=40, bootstyle="success")
        self.para_input.pack(pady=(20, 15), ipady=6)

        btn5 = ttk.Button(self.root, text="Generate", command=self.sense_sentiment, bootstyle=PRIMARY, width=40)
        btn5.pack(pady=(10))

        self.heading_result = ttk.Label(self.root, text="", bootstyle="info")
        self.heading_result.pack()

        btn6 = ttk.Button(self.root, text="Go Back", command=self.home_gui, bootstyle=SECONDARY)
        btn6.pack(pady=(10))

    # Performing Sentiment Analysis.
    def sense_sentiment(self):
        txt = self.para_input.get()
        result = self.obj1.sentiment_analysis(txt)
        final = ""

        for i in result['scored_labels']:
            final += i['label'] + ' -> ' + str(i['score']) + '\n'

        self.heading_result.config(text=final)

    # Preparing NER GUI.
    def perform_NER(self):
        self.clear()

        label = ttk.Label(self.root, text="Welcome to the NLP Application!", bootstyle="info")  # Example Label widget
        label.configure(font=('san serif', 12))
        label.pack(pady=(30, 30))

        label1 = ttk.Label(self.root, text="Enter Search Entity")
        label1.pack()

        # Entity Box
        self.search_Entity = ttk.Entry(self.root, width=40, bootstyle="success")
        self.search_Entity.pack(pady=(20, 15), ipady=6)

        label2 = ttk.Label(self.root, text="Enter Paragraph")
        label2.pack()

        # Paragraph Box
        self.para_input = ttk.Entry(self.root, width=40, bootstyle="success")
        self.para_input.pack(pady=(20, 15), ipady=6)

        btn5 = ttk.Button(self.root, text="Generate", command=self.Entity_Recognition, bootstyle=PRIMARY, width=40)
        btn5.pack(pady=(10))

        self.heading_result = ttk.Label(self.root, text="", bootstyle="info")
        self.heading_result.pack()

        btn6 = ttk.Button(self.root, text="Go Back", command=self.home_gui, bootstyle=SECONDARY)
        btn6.pack(pady=(10))

    # Performing NER Operations.
    def Entity_Recognition(self):
        txt = self.para_input.get()
        search_entity = self.search_Entity.get()

        result = self.obj1.entity_recog(txt, search_entity)

        self.heading_result.config(text=result)


obj = NLPApp()