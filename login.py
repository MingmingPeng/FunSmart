from tkinter import* # allows us to work with grapics
import os           # allos us to work with files
import Methods # custome methods module
from tkmacosx import Button
import Home 

root = Tk()
root.title("FunSmart Login Screen")
text=Label(root, text="FunSmart")
text.pack()


def checkLogin():
    #---------------------------------------------------------------
    #   Open up the username_profile.txt and verify the user credentials
    #       if the credentials match what is in file, upload user progress
    #        from file and go to main home screen
    #
    #---------------------------------------------------------------
    profileName = loginUsernameEntry.get() +"_profile.txt"
    #Check if the username profile exist
    if os.path.isfile(profileName):
        existingProfile = Methods.fileSplitter(profileName)        
        searchedUsername = existingProfile[2]
        searchedPassword = existingProfile[3]
        #Check if the username and passwrod match
        if(searchedUsername == loginUsernameEntry.get() and searchedPassword == loginPasswordEntry.get()):
            # Send user to homePage
            Label(frame,text="Successful Login").grid(row=3,column=2)
            #Go to the home Screen module
            Home.main(root, frame)
        else:
            Label(frame,text="incorrect password/username").grid(row=3,column=2)
    else:
        Label(frame,text="incorrect password/username").grid(row=4,column=2) # remove the hard code

createProfileWindow = None
proErrorInput = None    
def submitProfile():
    #--------------------------------------------------------------------------------
    #   When user submits their profile, create a profile with the username_profile.txt
    #       store all of the acquired data in the profile
    #------------------------------------------------------------------------
    profileContent=[]
    profileContent.append(FnameEntry.get())
    profileContent.append(LnameEntry.get())
    profileContent.append(usernameEntry.get())
    profileContent.append(passwordEntry.get())
    profileContent.append(confirmPasswordEntry.get())
    profileContent.append(securityQuestion1Entry.get())
    profileContent.append(securityQuestion2Entry.get())
    #Check for completed fields
    submitNow = True
    for field in profileContent:
        if(Methods.isEmpty(field) == True):
            submitNow = False
            error = proErrorInput + "*"
            Label(createProfileWindow, text=error).grid(row=11, column=2)
            break
    #check if user profile does not exist
    if(submitNow ):
        saveProfile = usernameEntry.get() + "_profile.txt" 
        if(os.path.isfile(saveProfile) == False):
            with open(saveProfile,"w") as file:
                for content in profileContent:
                    file.write(content + ",")
            #close profile window
            createProfileWindow.destroy()

def createProfile():
    #Lets function know you are using the global defined values
    global createProfileWindow
    global proErrorInput 
    
    #------------------------------------------------------------------------
    #   If user does not already have an account, then have user create a profile
    #       If profile already exist for the user, allow the user to reset his
    #       password
    #------------------------------------------------------------------------
    profileMaker = Methods.fileSplitter("profileMaker.txt")
    #Strip all the profile components from the profilemaker
    profTitle = profileMaker[0]
    profHeader = profileMaker[1]
    profFname = profileMaker[2]
    profLname = profileMaker[3]
    profUsername = profileMaker[4]
    profPassword = profileMaker[5]
    profConfirmPassword = profileMaker[6]
    profSecurityQuestionHeader = profileMaker[7]
    profSecurityQuestion1 = profileMaker[8]
    profSecurityQuestion2 = profileMaker[9]
    profSubmit = profileMaker[10]
    proErrorInput = profileMaker[11]
    
    createProfileWindow = Toplevel(root)
    createProfileWindow.title(profTitle)
    createProfileWindow.geometry("600x600")

    #Headers
    h1 = Label(createProfileWindow,text = profHeader)
    h1.grid(row=1,column=1)

    h2 =Label(createProfileWindow,text = profSecurityQuestionHeader)
    h2.grid(row=8,column=1)

    #Profile component label and entry
    Fname = Label(createProfileWindow, text=profFname)
    Fname.grid(row=3,column=0)
    Lname = Label(createProfileWindow, text=profLname).grid(row=4,column=0)
    username = Label(createProfileWindow, text=profUsername).grid(row=5,column=0)
    password = Label(createProfileWindow, text=profPassword).grid(row=6,column=0)
    confirmPassword = Label(createProfileWindow, text=profConfirmPassword).grid(row=7,column=0)
    securityQuestion1 = Label(createProfileWindow, text=profSecurityQuestion1).grid(row=9,column=0)
    securityQuestion2 = Label(createProfileWindow, text=profSecurityQuestion2).grid(row=10,column=0)

    Entry(createProfileWindow, textvariable=FnameEntry,width=20).grid(row=3,column=1)
    Entry(createProfileWindow, textvariable = LnameEntry, width=20).grid(row=4,column=1)
    Entry(createProfileWindow, textvariable = usernameEntry, width=20).grid(row=5,column=1)
    Entry(createProfileWindow, textvariable = passwordEntry, width=20,show="*").grid(row=6,column=1)
    Entry(createProfileWindow,textvariable = confirmPasswordEntry, width=20,show="*").grid(row=7,column=1)
    Entry(createProfileWindow, textvariable = securityQuestion1Entry, width=20).grid(row=9,column=1)
    Entry(createProfileWindow, textvariable = securityQuestion2Entry, width=20).grid(row=10,column=1)

    btn = Button(createProfileWindow,text= profSubmit, background="lightgreen",command = submitProfile)
    btn.grid(row=11,column=1)

#Exterior canvas
canvas = Canvas(root, height = 600, width = 600, bg = "#263D42")
canvas.pack()

frame = Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

photo=PhotoImage(file="funsmart.png")
# photo1=PhotoImage(file="funsmart1.png")
text=Label(frame, image=photo).grid(row=0,columnspan=3)
# text=Label(frame, image=photo)
# text1=Label(frame, image=photo1).grid(row=0, column=0,)


#Username label and entry
loginUsernameLable = Label(frame, text="Username",font=("Arial CE", 14))
loginUsernameLable.grid(row=1,column=0,pady=20)

loginUsernameEntry = Entry(frame, width=20)
loginUsernameEntry.grid(row=1,column=1,pady=20)

#Password label and entry
loginPasswordLable = Label(frame, text="Password",font=("Arial CE", 14,))
loginPasswordLable.grid(row=2,column=0,pady=10)

loginPasswordEntry = Entry(frame, width=20, show="*")
loginPasswordEntry.grid(row=2,column=1,pady=10)

#Login button
login = Button(frame, text="Login", bg="#82E0AA", command= checkLogin)
login.grid(row=4,column=0,pady=20)

#Global profile variable
var_name = StringVar()
FnameEntry = StringVar()
LnameEntry = StringVar()
usernameEntry = StringVar()
passwordEntry = StringVar()
confirmPasswordEntry =StringVar()
securityQuestion1Entry = StringVar()
securityQuestion2Entry = StringVar()

#signUp button
signUp = Button(frame, text="Sign Up", bg="#82E0AA", command = createProfile)
signUp.grid(row=4,column=1,pady=20)

photo1=PhotoImage(file="bottom.png")
# photo1=PhotoImage(file="funsmart1.png")
text1=Label(frame, image=photo1).grid(row=7,columnspan=3,pady=160)

root.mainloop()