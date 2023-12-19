import tkinter
from mainmenu import menu

#variables
root=None
userbox=None
passbox=None
topframe=None
bottomframe=None
frame3=None
login=None

# called on submit 
def GET():
    global userbox,passbox,error
    login_username=userbox.get()
    login_password=passbox.get()
    # if(login_username=='admin' and login_password=='admin'):
    if True:
        error=tkinter.Label(bottomframe,text="Success",fg="Green",font="bold")
        error.pack()
        menu()
    else:   
        error=tkinter.Label(bottomframe,text="Wrong Id / Password \n TRY AGAIN",fg="red",font="bold")
        error.pack()

        
def Entry():
    global userbox,passbox,login,topframe,bottomframe,image_1
    root = tkinter.Tk()
    root.geometry("500x500")
    topframe = tkinter.Frame(root)
    topframe.pack()
    bottomframe=tkinter.Frame(root)
    bottomframe.pack()
    heading = tkinter.Label(topframe, text="WELCOME TO SOMAIYA HOSPITAL",height=1,bg='white',fg='orange',font='Consolas')
    username=tkinter.Label(topframe,text="USERNAME")
    userbox = tkinter.Entry(topframe)
    password=tkinter.Label(bottomframe,text="PASSWORD")
    passbox = tkinter.Entry(bottomframe,show="*")
    login = tkinter.Button(bottomframe, text="LOGIN", command=GET,font="Consolas")
    heading.pack()
    username.pack()
    userbox.pack()
    password.pack()
    passbox.pack()
    login.pack()
    root.title("ADMIN LOGIN")
    root.mainloop()


# call main menu on file run
# Entry of project
Entry()

