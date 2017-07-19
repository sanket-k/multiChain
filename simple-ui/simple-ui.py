
# coding: utf-8

# # Multichain-simpleUI
# 
#     import tkinter for python GUI
#     import os for system file location

# In[49]:


from tkinter import *
import os


# # Working
#     
#     1. locate file in system(here the files are in the same directory as the python file)
#     2. create a simple UI with three buttons
#     3. button1 ==> creates a new chain named "chain1" through a .bat file(code : multichain-ulti)
#     4. button2 ==> launches the newly created chain1 through a .bat file(code : multichaind chain1 -daemon)
#     5. button3 ==> exits the chain through a .bat file(code : /cmd c exit) 

# In[65]:


class application(Frame):
    def openFileCreate(self):
        # change file location as per reqirement
        os.system(r'""C:\\Users\\zero\\Desktop\\int\\create-chain.bat""')
        
    def openFileLaunch(self):
        os.system(r'""C:\\Users\\zero\\Desktop\\int\\launch-chain.bat""')
        
    def openFileExit(self):
        os.system(r'""C:\\Users\\zero\\Desktop\\int\\exit-chain.bat""')
        
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        #create chain
        self.create_button = Button(self,command = self.openFileCreate,text="create chain")
        self.create_button.grid(row = 0,column = 1,columnspan = 1,sticky = W)
        
        #launch chain
        self.launch_button = Button(self,command = self.openFileLaunch,text="launch chain")
        self.launch_button.grid(row = 2,column = 2,columnspan = 2,sticky = W)
        
        #exit chain
        self.exit_button = Button(self,command = self.openFileExit,text="exit chain")
        self.exit_button.grid(row = 3,column = 2,columnspan = 2, sticky = W)
        
        
root = Tk()
root.title("Multichain-Launcher")
root.geometry("200x100")
app = application(root)
root.mainloop()


# In[ ]:




