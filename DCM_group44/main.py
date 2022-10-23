from tkinter import *
from PIL import ImageTk, Image
import login
import registration
from data import createDB

background = 'white'
class WelcomePage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('450x500')
        self.width = 400
        self.height = 450
        self.window.minsize(self.width+30, self.height+40)
        self.window.iconbitmap("images\logo.ico")
        self.window.title("Pacemaker")

        connectionChecker=False
        if(connectionChecker==False):
            connectionBanner=Label(self.window,text="Not connected - ", fg= 'red', font=("Helvetica",12), padx=10)
            connectionBanner.grid(row=0,column=0, sticky=W)
        else:
            connectionBanner=Label(self.window,text="Connected - ",fg="green", font=("Helvetica",12), padx=10)
            connectionBanner.grid(row=0,column=0, sticky=W)

        newDeviceChecker=True
        if(newDeviceChecker==False):
            deviceBanner = Label(self.window,text="No new device",fg='black', font=("Helvetica", 12), padx=10)
            deviceBanner.grid(row=0,column=2, sticky=E)
        else:
            deviceBanner = Label(self.window,text="New device detected", fg="black", font=("Helvetica",12), padx=10)
            deviceBanner.grid(row=0,column=2, sticky=E)

        def openLoginWin():
            self.welcome_frame.destroy()
            login.launchLogin(self.window)


        def openRegisterWin():
            self.welcome_frame.destroy()
            registration.launchRegistration(self.window)

        # ========= Welcome Frame =========
        self.welcome_frame = Frame(
            self.window,
            bg = background,
            width = self.width,
            height= self.height,
        )
        self.welcome_frame.place(anchor="c", relx=0.5, rely=0.5)
        self.welcome_frame.grid_propagate(False)

        # set weight of grid
        self.welcome_frame.columnconfigure(0,weight=1)
        self.welcome_frame.columnconfigure(1,weight=3)

        # ========= Welcome Text =========
        self.header_text = "Welcome"
        self.header = Label(self.welcome_frame, text = self.header_text, font=('Arial', 24, 'bold'), bg = background, fg='black')
        self.header.grid(row=0, column=0, columnspan=2, pady=(50,10))

        # ========= Welcome Logo =========
        self.logo_image = ImageTk.PhotoImage(Image.open("images/welcomeLogo.png"))
        self.logo = Label(self.welcome_frame, image = self.logo_image, bg=background)
        self.logo.image = self.logo_image
        self.logo.grid(row=1,column=0,columnspan=2,pady=10)

        # ========= Welcome Entry =========
        self.login_button = Button(self.welcome_frame, text="Login", width = 30, bg=background, command=openLoginWin)
        self.register_button = Button(self.welcome_frame, text="Register", width = 30, bg=background, command=openRegisterWin)

        # formatting entries
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)
        self.register_button.grid(row=3, column=0, columnspan=2)

        

def launchApp():
    createDB()
    window = Tk()
    WelcomePage(window)
    window.mainloop()

if __name__ == '__main__':
    launchApp()