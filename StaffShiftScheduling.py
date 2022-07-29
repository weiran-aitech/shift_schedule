# Copyright (C)  2022 WeiRan Hi-Tech

from Staff_Shift_Scheduling.util.preferences import editPreferences
from Staff_Shift_Scheduling.scheduleEngine.scheduleCreate import *
from Staff_Shift_Scheduling.scheduleEngine.scheduleMerge import mergeScheduels
from Staff_Shift_Scheduling.scheduleEngine.scheduleRepair import *
from Staff_Shift_Scheduling.manager.staffUnitMgr import *
from Staff_Shift_Scheduling.util.utility import *


# @jit(nopython=True)
def main():
    setLogFile()

    userList = ['sys', 'ryp']
    user, pwd = loginUserPassword()
    login_password_hash = '41d58364911d2323247cc5c71c0307f1be1e6ca3'
    if (user in userList) and pwd and PasswordMatches(pwd, login_password_hash):
        pass
    else:
        sg.popup_error('Incorrect user name and password. Scheduler will quit now!')
        exit()

    loggingAndPrintMsg(datetime.now().strftime("%Y-%m-%d"))

    sg.ChangeLookAndFeel('LightGreen')
    sg.SetOptions(element_padding=(0, 0))

    menu_def = [['File', ['New', ['Schedule Unit', 'Employee'], 'Open', 'Preference', 'Print', 'Exit']],
                ['Edit', ['Copy', 'Delete', 'Paste', 'Undo']],
                ['Schedule', ['Create New Schedule', 'Review Schedule', 'Revise Schedule', 'Merge Schedules']],
                ['Schedule_Unit', ['Create a schedule unit', 'Edit a schedule unit', 'View schedule units', ['Detail', 'Structure']]],
                ['Employee', ['Create an employee', 'Edit an employee', 'Import employee data', 'View employee data']],
                ['Database', ['Initialization', 'Backup', 'Restore']],
                ['Help', 'About...']]

    layout0 = [
        [sg.Menu(menu_def, )],  
        [sg.Output(size=(120, 45),expand_x=True, expand_y=True)]  
    ]

    window = sg.Window(title="Intelligent Shift Scheduler", layout=layout0,
                       default_element_size=(12, 1), auto_size_text=True, auto_size_buttons=True,
                       default_button_element_size=(12, 1), font=("Helvetica", 10), resizable=True)
    try:
        while True:
            event, values = window.read()
            logAndPrintSeparator('-', 60)
            loggingAndPrintMsg('Select action = %s' %event)
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            # ------ Process menu choices ------ #
            if event == 'About...':
                sg.popup('About this program', 'Version 1.0', 'PySimpleGUI rocks...')
            elif event == 'Preference':
                editPreferences()
            elif event == 'Import employee data':
                importEmployeeData()
            elif event == 'Employee' or event == 'Create an employee':
                addEmployee()
            elif event == 'Edit an employee':
                editEmployee()
            elif event == 'Structure':
                PopupUnitTree2()
            elif event == 'Detail':
                showEnSelectScheduleUnits('')
            elif event == 'Schedule Unit' or event == 'Create a schedule unit':
                addScheduleUnit()
            elif event == 'Edit a schedule unit':
                editScheduleUnit()
            elif event == 'Backup':
                createBackup()
            elif event == 'Initialization':
                initializeScheduleTables()
            elif event == 'Create New Schedule':
                createSchedules()
            elif event == 'Review Schedule':
                openExistingSchedule()
            elif event == 'Revise Schedule':
                reviseExistingSchedule()
            elif event == 'Merge Schedules':
                mergeScheduels()
    except Exception as e:
            logging.critical(e, exc_info=True)



if __name__ == '__main__':
    main()
