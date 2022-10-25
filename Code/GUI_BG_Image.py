# Copyright (C)  2022-08-08 WeiRan Hi-Tech

import PySimpleGUI as sg

sg.Window._move_all_windows = True


def title_bar(title, text_color, background_color):
    bc = background_color
    tc = text_color
    font = 'Helvetica 12'

    return [sg.Col([[sg.T(title, text_color=tc, background_color=bc, font=font, grab=True)]], pad=(0, 0), background_color=bc),
            sg.Col([[sg.Text('❎', text_color=tc, background_color=bc, font=font, enable_events=True, key='Exit')]], element_justification='r',
                   key='-C-', grab=True, pad=(0, 0), background_color=bc)]


def loginWithBackgroundImage():
    background_layout = [title_bar('System Login', sg.theme_text_color(), sg.theme_background_color()), [sg.Image(r"./resources/Open_Space.png")]]
    window_background = sg.Window('Background', background_layout, no_titlebar=True, finalize=True, margins=(0, 0), element_padding=(0, 0),
                                  right_click_menu=[[''], ['Exit', ]])

    window_background['-C-'].expand(True, False, False) 

    Title = '   Intelligent Shift Scheduling'
    Label = 'Password:'
    layout = [
        [sg.Text(Title, text_color='Green', font=("Helvetica", 30))],
        [sg.T("")],
        [sg.T("")],
        [sg.Text('               '), sg.Text('User Name:', text_color='Black'),
         sg.InputText('', key='username', size=(20, 1))],
        [sg.Text('               '), sg.Text('  ' + Label, text_color='Black'),
         sg.InputText('', key='password', password_char='*', size=(20, 1))],
        [sg.Button('Submit', visible=False, bind_return_key=True)],
        [sg.Text('                                    '), sg.Button('OK'), sg.Cancel('Cancel')],
        [sg.T("")]
    ]

    top_window = sg.Window('System login', layout, finalize=True, keep_on_top=True, grab_anywhere=False,
                           transparent_color=sg.theme_background_color(), no_titlebar=True)
    while True:
        window, event, values = sg.read_all_windows()
        if event == 'Exit' or event == 'Cancel':
            top_window.close()
            window_background.close()
            return '',''
        else:
            top_window.close()
            window_background.close()
            return values['username'], values['password']
