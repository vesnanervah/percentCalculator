import PySimpleGUI as sg

layout = [
[sg.Text("The biggest number bellow:")],
[sg.Input(key = '-biggestNum-')],
[sg.Text("The smallest number bellow:")],
[sg.Input(key='-smallNum-')],
[sg.Button('Calculate the %')],
[sg.Text("The answer is: "), sg.Text('?', key='-OUTPUT-')]
]
window = sg.Window("% calculator", layout)

while(True):
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Calculate the %' :
       a = int(values['-biggestNum-'])
       b = int(values['-smallNum-'])
       output = b*100/a
       window['-OUTPUT-'].update(output)
