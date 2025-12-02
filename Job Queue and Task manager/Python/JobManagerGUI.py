import sys
import tkinter
from tkinter import *
from Python.JobList import JobList
from Python.Job import Job

job_list = JobList()

root = Tk()
root.title("JobQueueTaskManager")
root.geometry("400x400")

menu_frame = Frame(root)
menu_frame.pack()
intro = Label(menu_frame, text = "What would you like to do?", justify="center" )
intro.grid(column=5, row=0)

create_frame = Frame(root)
create_frame.pack()

delete_frame = Frame(root)
delete_frame.pack()

edit_frame = Frame(root)
edit_frame.pack()

edit_logic_frame = Frame(root)
edit_logic_frame.pack()

view_frame = Frame(root)
view_frame.pack()

view_all_frame = Frame(root)
view_all_frame.pack()

def go_to_main_menu():
    create_frame.forget()
    delete_frame.forget()
    edit_frame.forget()
    edit_logic_frame.forget()
    view_frame.forget()
    view_all_frame.forget()

    menu_frame.pack()


menu_bar = Menu(root)
menu = Menu(menu_bar, tearoff=0)
menu_bar.add_command(label="Menu", command = go_to_main_menu)

name_not_found_warning = Label(edit_frame, text="", fg="red")

def create_job_button_click():
    menu_frame.pack_forget()
    create_frame.pack()

    job_name_label = Label(create_frame, text="Job Name: ")
    job_name_label.grid(column=0, row=0, sticky="W", pady=10)
    job_name_entry = Entry(create_frame, width=20, justify="center")
    job_name_entry.grid(column=1, row=0, pady=10)

    job_type_label = Label(create_frame, text="Job Type: ")
    job_type_label.grid(column=0, row=1, sticky="W", pady=10)
    job_type_entry = Entry(create_frame, width=20, justify="center")
    job_type_entry.grid(column=1, row=1, pady=10)

    job_scheduled_run_time_label = Label(create_frame, text="Scheduled\nRun Time: ")
    job_scheduled_run_time_label.grid(column=0, row=2, sticky="W", pady=2)
    job_scheduled_run_time_entry = Entry(create_frame, width=20, justify="center")
    job_scheduled_run_time_entry.grid(column=1, row=2, pady=2)

    create_button = Button(create_frame, text = "Create", command=lambda: create_job_logic(job_name_entry.get().strip(), job_type_entry.get().strip(), job_scheduled_run_time_entry.get().strip()))
    create_button.grid(column=1, row=3)


def create_job_logic(job_name, job_type, job_date):
    if job_name != "" and job_type != "" and job_date != "":
        job_list.add_job(Job(job_name, job_type, job_date))
        create_frame.pack_forget()
        intro.config(text=f'Added "{job_name}" to Job List', justify="center")
        menu_frame.pack()

def delete_job_button_click():
    if check_job_list_size():
        menu_frame.pack_forget()
        delete_frame.pack()

        delete_job_label = Label(delete_frame, text = "Job Name to delete: ")
        delete_job_label.grid(column=0, row=0, sticky="W", pady=2)
        delete_job_entry = Entry(delete_frame, width=20, justify="center")
        delete_job_entry.grid(column=1, row=0, pady=2)

        delete_button = Button(delete_frame, text = "Delete", command= lambda:
            display_edit_warning(f"{delete_job_entry.get()} not found", 2, 0) if delete_job_logic(delete_job_entry.get().lower().strip()) is False else True)
        delete_button.grid(column=1, row=3, sticky="W", pady=10)

def delete_job_logic(job_name):
    #find the job
    #If it's not in the list, then print out a red text warning
    #If it is, then remove the job form the job_list and then move back to the main menu
    job_to_delete = job_list.find_job(job_name)
    if job_to_delete is False:
        return False
    job_list.remove_job(job_to_delete)
    return True


def edit_job_button_click():
    if check_job_list_size():
        menu_frame.pack_forget()
        edit_frame.pack()

        edit_job_label = Label(edit_frame, text = "Job Name to edit: ")
        edit_job_label.grid(column=0, row=0, sticky="W", pady=2)
        edit_job_entry = Entry(edit_frame, width=20, justify="center")
        edit_job_entry.grid(column=1, row=0, pady=2)

        edit_button = Button(edit_frame, text = "Edit", command=lambda:
            display_edit_warning(f"{edit_job_entry.get()} not found", 2, 0) if edit_job_logic(edit_job_entry.get().lower().strip())
                                                                         is False else name_not_found_warning.grid_remove())
        edit_button.grid(column=1, row=3, sticky="W", pady=10)

def edit_job_logic(job_name):
    #check if that job is in the jobList
    #if it's not, return false
    #if it is, keep going
    job_to_edit = job_list.find_job(job_name)
    if job_to_edit is False:
        return False

    edit_frame.pack_forget()

    edit_name_label = Label(edit_logic_frame, text="Job Name: ", justify="center")
    edit_name_label.grid(column=0, row=0, sticky="w", pady=2)
    edit_name_entry = Entry(edit_logic_frame, width=20, justify="center")
    edit_name_entry.grid(column=1, row=0, pady=2)

    edit_type_label = Label(edit_logic_frame, text="Job Type: ", justify="center")
    edit_type_label.grid(column=0, row=1, sticky="w", pady=2)
    edit_type_entry = Entry(edit_logic_frame, width=20, justify="center")
    edit_type_entry.grid(column=1, row=1, pady=2)

    edit_date_label = Label(edit_logic_frame, text="Scheduled\nRun Time: ", justify="center")
    edit_date_label.grid(column=0, row=2, sticky="w", pady=2)
    edit_date_entry = Entry(edit_logic_frame, width=20, justify="center")
    edit_date_entry.grid(column=1, row=2, pady=2)

    save_button = Button(edit_logic_frame, text="Save", command=lambda:
        display_edit_warning(f"Can't have blank fields", 2, 3) if save_edit_logic(job_to_edit, edit_name_entry.get().strip(),
                                                             edit_type_entry.get().strip(),
                                                             edit_date_entry.get().strip()) else name_not_found_warning.grid_remove())
    save_button.grid(column=1, row=3, sticky="W", pady=10)
    return True

def save_edit_logic(job, new_name, new_type, new_date):
    if new_name == "" or new_type == "" or new_date == "":
        return False
    else:
        job.set_job_name(new_name)
        job.set_job_type(new_type)
        job.set_scheduled_run_time(new_date)
        edit_frame.pack_forget()
        edit_logic_frame.pack_forget()
        intro.config(text=f'Edited "{new_name}" in Job List', justify="center")
        menu_frame.pack()
        return True



def view_job_button_click():
    if check_job_list_size():
        menu_frame.pack_forget()
        view_frame.pack()

        view_job_label = Label(view_frame, text="Job Name to view: ")
        view_job_label.grid(column=0, row=0, sticky="W", pady=2)
        view_job_entry = Entry(view_frame, width=20, justify="center")
        view_job_entry.grid(column=1, row=0, pady=2)

        view_button = Button(view_frame, text="View", command=lambda :display_edit_warning(f"{view_job_entry.get()} not found", 2, 0)
            if view_job_logic(view_job_entry.get().lower().strip()) is False else True)
        view_button.grid(column=1, row=3, sticky="W", pady=10)

def view_job_logic(job_name):
    job_to_view = job_list.find_job(job_name)
    if job_to_view is False:
        return False
    else:
        job_info_label = Label(view_frame, text=job_to_view.__str__(), justify="left")
        job_info_label.grid(column=0, row=4, columnspan=2, pady=10)

        menu_button = Button(view_frame, text="Menu", command=go_to_main_menu)
        menu_button.grid(column=1, row=5, sticky="W", pady=10)
        return True

def view_all_job_button_click():
    if check_job_list_size():
        menu_frame.pack_forget()
        job_info_text = Text(view_all_frame, height=50, width=45)
        v = Scrollbar(view_all_frame, orient="vertical", command=job_info_text.yview)
        v.pack(side=RIGHT, fill=Y)
        #iterate through each entry and print out the info
        #Add a scroll to be able to scroll to the bottom of the list
        for jobs in job_list.get_job_list():
            job_info_text.pack(anchor="w", pady=5)
            job_info_text.insert(tkinter.END, jobs.__str__() + "\n")
        v.config(command=job_info_text.yview)

        menu_button = Button(view_frame, text="Menu", command=go_to_main_menu)
        menu_button.grid(column=1, row=0, sticky="W")


def display_edit_warning(warning_text, column, row):
    name_not_found_warning.config(text=warning_text)
    name_not_found_warning.grid(column=column, row=row, pady=2)

def check_job_list_size():
    if job_list.get_job_size() == 0:
        intro.config(text=f"There are no jobs in the job list.", justify="center")
        go_to_main_menu()
        return False
    else:
        return True

def quit_button_click():
    sys.exit()




create_job_btn = Button(menu_frame, text = "Create Job", width=10,command = create_job_button_click)
create_job_btn.grid(column = 5, row = 1)

delete_job_btn = Button(menu_frame, text = "Delete Job", width=10, command = delete_job_button_click)
delete_job_btn.grid(column = 5, row = 2)

edit_job_btn = Button(menu_frame, text = "Edit Job", width=10, command = edit_job_button_click)
edit_job_btn.grid(column = 5, row = 3)

view_job_btn = Button(menu_frame, text = "View Job", width=10, command = view_job_button_click)
view_job_btn.grid(column = 5, row = 4)

view_all_job_btn = Button(menu_frame, text = "View All Jobs", width=10, command = view_all_job_button_click)
view_all_job_btn.grid(column = 5, row = 5)

quit_btn = Button(menu_frame, text = "Quit", width=10, command = quit_button_click)
quit_btn.grid(column = 5, row = 6)

root.config(menu = menu_bar)
root.mainloop()