# Copyright (C)  2022-01-08 WeiRan Hi-Tech

import FreeSimpleGUI as sg
from datetime import *

from dbManager import *
from staffUnitMgr import *
from global_Constants import *
from utility import *


class GlobalPrefs():
    def __init__(self, id, Multi, Single, MaxSol, MaxRunMinutes, MaxWorkHours, CycleGap, SelectStaff, EvenDistLast2Days, CustomizedFormat,
                 OneShiftAllowed, TwoConsecShifts, ThreeConsecShifts, DestFolder, banzu_id, save_time):
        self.id = id
        self.Multi = Multi
        self.Single = Single
        self.MaxSol = MaxSol
        self.MaxRunMinutes = MaxRunMinutes
        self.MaxWorkHours = MaxWorkHours
        self.CycleGap = CycleGap
        self.SelectStaff = SelectStaff
        self.EvenDistLast2Days = EvenDistLast2Days
        self.CustomizedFormat = CustomizedFormat
        self.OneShiftAllowed = OneShiftAllowed
        self.TwoConsecShifts = TwoConsecShifts
        self.ThreeConsecShifts = ThreeConsecShifts
        self.DestFolder = DestFolder
        self.banzu_id = banzu_id
        self.save_time = save_time

    def preferenceGui(self, aBanzuList):
        pList1 = [str(i + 2) for i in range(9)]
        pList2 = [str(i + 1) for i in range(10)] + ['15', '30', '60', '120', '180', '240', '300']
        pList3 = [str(i) for i in range(10)]
        pList4 = ['8','9']  

        defMulti, defSingle = True if self.Multi == 1 else False, True if self.Single == 1 else False
        defMaxsol = self.MaxSol if defMulti else pList3[1]
        disTwoConsecShifts = True if self.OneShiftAllowed else False
        disThreeConsecShifts = True if self.OneShiftAllowed else False

        # Select staffs in record order (Default)
        index0, unitPath = getBanzuNonEmptyParentPathIndex(aBanzuList, False)
        layout = [
            [sg.Text(unitPath, size=(60, 1), justification='center', font=("Helvetica", 13), relief=sg.RELIEF_RIDGE)],
            [sg.Frame(layout=[
                [sg.Radio('Search for multiple solutions', default=defMulti, size=(43, 1), group_id=1, enable_events=True, key='Multi'),
                 sg.Radio('Search for one solution', default=defSingle, group_id=1, enable_events=True, key='Single')],
                [sg.InputCombo(pList1, default_value=defMaxsol, disabled=defSingle, size=(3, 1), key='Maxsol', readonly=True),
                 sg.T(' Max number of solutions')]
            ],
                title='Number of Solution Options', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
            [sg.Text(' ' * 80)],
            [sg.InputCombo(pList2, default_value=self.MaxRunMinutes, size=(3, 1), key='Maxrun', readonly=True),
             sg.T(' Max solver running time (minutes) ', size=(28, 1)),
             sg.InputCombo(pList4, default_value=self.MaxWorkHours, size=(3, 1), key='Maxhour', enable_events=True, readonly=True),
             sg.T(' max number of working hours a day', size=(30, 1))
             ],
            [sg.InputCombo(pList3, default_value=self.CycleGap, size=(3, 1), key='Cyclegap', readonly=True), sg.T(' Cycle gap days ', size=(28, 1)),
             sg.Checkbox(' Manually select staffs for scheduling', size=(31, 1), default=self.SelectStaff, key='Selectstaff'),
             ],
            [sg.Checkbox(' Evenly distribute shifts in last two days', size=(30, 1), default=self.EvenDistLast2Days, key='EvenDistLast2Days'),
             sg.Checkbox(' Use customized format for CSV file', size=(31, 1), default=self.CustomizedFormat, key='CustomizedFormat')],
            [sg.Text(' ' * 80)], # [sg.Text('_' * 80)],
            [sg.Frame(layout=[
                [sg.Checkbox(' One shift is allowed', size=(55, 1), default=self.OneShiftAllowed, enable_events=True,
                             key='OneShiftAllowed')],
                [sg.Checkbox(' Two consecutive shifts should be scheduled on the same day (CZ constraints)', size=(63, 1),
                             default=self.TwoConsecShifts, disabled=disTwoConsecShifts, key='TwoConsecShifts')],
                [sg.Checkbox(' Three consecutive shifts should be scheduled on the same day (CS constraints)', size=(63, 1),
                             default=self.ThreeConsecShifts, disabled=disThreeConsecShifts, key='ThreeConsecShifts')],
            ],
                title='For anyone on any day, if the number of shifts per day is greater than 4', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
            [sg.Text(' ' * 80)],
            [sg.Frame(layout=[
                [sg.Text('Destination Folder ', size=(15, 1), auto_size_text=False, justification='right'),
                 sg.InputText(self.DestFolder, enable_events=True, key='Destfolder', size=(50, 1)), sg.FolderBrowse(key='fBrowse')],
                ],
                title='Choose Schedule File Folder', relief=sg.RELIEF_SUNKEN, tooltip='')],
            [sg.Text(' ' * 80)],
            [sg.Submit(tooltip='Click to submit this window'), sg.Cancel()]
        ]

        window = sg.Window('Schedule Unit Preferences...', layout, default_element_size=(40, 1), grab_anywhere=False)

        retDict = {}
        while True:
            event, values = window.read()
            if event is None or event == 'Cancel':
                break
            if event == 'Multi':
                if values['Multi']:
                    window['Maxsol'].update(disabled=False, set_to_index=1)
            if event == 'Single':
                if values['Single']:
                    window['Maxsol'].update(disabled=True, set_to_index=1)
            if event == 'Destfolder':
                window['Destfolder'].update(values['Destfolder'].replace("/", "\\"))
            if event == 'OneShiftAllowed':
                if values['OneShiftAllowed']:
                    window['TwoConsecShifts'].update(disabled=True)
                    window['ThreeConsecShifts'].update(disabled=True)
                else:
                    if values['Maxhour'] == '8':
                        window['TwoConsecShifts'].update(disabled=False)
                    if values['Maxhour'] == '9':
                        window['ThreeConsecShifts'].update(disabled=False)
            if event == 'Maxhour':
                if values['Maxhour'] == '8' and not values['OneShiftAllowed']:
                    window['TwoConsecShifts'].update(disabled=False)
                    window['ThreeConsecShifts'].update(disabled=True)
                if values['Maxhour'] == '9' and not values['OneShiftAllowed']:
                    window['ThreeConsecShifts'].update(disabled=False)
                    window['TwoConsecShifts'].update(disabled=True)

            if event == 'Submit':
                retDict = values
                break
        window.close()
        return retDict
	
	def editPreferences():
		aBanzuList = showEnSelectScheduleUnits('Pref')
		if len(aBanzuList) == 0:
			loggingAndPrintMsg('No schedule unit selected.')
			return
		aBanzuId = int(aBanzuList[0][0])

		abzPrefIns = self.getBanzuPrefs()
		prefs = abzPrefIns.preferenceGui(aBanzuList[0])

		if prefs:
			newPrefTuple = (abzPrefIns.id,) + tuple(prefs.values())[:-1] + (aBanzuId,) 
			createUpdatePrefs(newPrefTuple)
			createSpecifiedFilePath(abzPrefIns.DestFolder)
			loggingAndPrintMsg('Preferences of the schedule unit are saved!')
		else:
			loggingAndPrintMsg('Schedule unit preferences are not set/changed!')


	def getBanzuPrefs(prefsId=None):
		aBanzuPrefs = findPrefsByBanzuId(self.banzu_id, prefsId)
		if len(aBanzuPrefs) == 0:
			save_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			abzPrefs = (0,) + tuple(DEFAULT_PREFS.values())[:-1] + (self.banzu_id,save_time)
		else:
			abzPrefs = aBanzuPrefs
		return GlobalPrefs(*abzPrefs)


	def getPrefFileFolder(prefsId):
		abzPrefIns = self.getBanzuPrefs(prefsId)
		destFolder = createSpecifiedFilePath(abzPrefIns.DestFolder)
		return destFolder
	


