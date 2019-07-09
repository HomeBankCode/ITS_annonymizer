# GUI builder for .its anonymizer app
# Created by: Sarah MacEwan
# Last Updated: July 9, 2019

import sys
import os

if sys.version_info[0] == 2:
    import Tkinter as tk
    import tkFileDialog
    from tkMessageBox import showwarning, askyesno, showinfo, showerror
else:
    import tkinter as tk
    from tkinter import PhotoImage
    from tkinter import filedialog as tkFileDialog
    from tkinter.messagebox import showwarning, askyesno, showinfo, showerror
    
import webbrowser
import its_anonymizer


class Anonymizer(object):
    
    def __init__(self, master):
        self.root = master
        self.root.resizable(width=True, height=True)
        self.root.title('ITS Anonymizer')
        self.root.protocol('WM_DELETE_WINDOW')# add function to register pressing the x button as event and call the corresponding function

        program_path = os.getcwd()
        self.frame = tk.Frame(root)
        self.frame.grid(row=0, column=0, sticky='wns', padx=(30, 30), pady=30)

        # Menu window
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.submenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='Menu', menu=self.submenu)
        self.submenu.add_command(label = 'run standard anonymization...', command=self.anonymize_its_files_full)
        readme_link = 'https://github.com/BLLManitoba/ITS_anonymizer/blob/master/README.md'
        self.submenu.add_command(label='Help', command=lambda: webbrowser.open_new(readme_link))

        # Input/Output Selection Buttons
        self.input_dir_button = tk.Button(
            self.frame,
            text = 'Select input files', 
            command = self.select_input_its,
            height = 1,
            width = 20,
            relief=tk.GROOVE).grid(row=0, column=0, padx=20, pady=5)

        self.output_dir_button = tk.Button(
            self.frame,
            text = 'Select output location',
            command = self.select_output_dir,
            height = 1,
            width = 20,
            relief = tk.GROOVE).grid(row = 1, column = 0, padx=20, pady=5)
            
        # Type of info to anonymize checkbuttons
        self.primaryChild_checkbox = tk.Checkbutton(
            self.frame,
            text = 'Primary Child Data',
            onvalue=True,
            offvalue=False).grid(row=0, column = 1, padx=5, pady=5, sticky='NW')
        self.its_checkbox = tk.Checkbutton(
            self.frame,
            text = 'ITS file data',
            onvalue=True,
            offvalue=False).grid(row=1, column = 1, padx=5, pady=5, sticky='NW')
        self.transfer_checkbox = tk.Checkbutton(
            self.frame,
            text = 'File transfer data',
            onvalue=True,
            offvalue=False).grid(row=2, column = 1, padx=5, pady=5, sticky='NW')
        self.childInfo_checkbox = tk.Checkbutton(
            self.frame,
            text = 'Child birthdate and gender',
            onvalue=True,
            offvalue=False).grid(row=3, column = 1, padx=5, pady=5, sticky='NW')
        self.clocktime_checkbox = tk.Checkbutton(
            self.frame,
            text = 'Clock start/stop',
            onvalue=True,
            offvalue=False).grid(row=4, column = 1, padx=5, pady=5, sticky='NW')
            
            
        # TODO:
            # Add buttons to select directory of its files
            # Add a set of checkboxes to list off the things that they want anonymized
            # Add a "save anonymized files as..." button so they can save the files in a specified location
            # Add a big old "anonymize" button :D
            
    def select_input_its(self):
        print('selecting inputs...')
        input_dir = tkFileDialog.askdirectory()
        return input_dir
        # TODO: pull up a filechooser to select the directory of its files you want anonymized
        #set that directory as your input directory
        
    def select_output_dir(self):
        print('selecting output dir...')
        output_dir = tkFileDialog.askdirectory(title='Select where to save your output files')
        return output_dir
        # TODO: pull up a filechooser to select where you want to save your anon'd files
        # let them name the directory and then set that as the output dir
        
    def anonymize_its_files_full(self):
        print("anonymizing your its files the old fashioned way :P")
        # TDOD: add functionality to this function -> call an anonymizer object to anonymize the files???
        #self.its_anonymizer.main()
        
    def select_type_anonymize(self):
        print('select the kinds of things you want to anonymize')
        #TODO: add funcionality to select the certain data to anonymize
        # returns a list of things to anonymize
        
    def anonymize_its_files(self, anon_list):
        print('anonymizing files...')
        #TODO: this function will take into account the list of things to anonymize and only blank out that stuff!


if __name__ == '__main__':
    root = tk.Tk()
    x = Anonymizer(root)
    root.mainloop()