import PySimpleGUI as sg


layout = [[sg.Text('Some text on Row 1')],
          [sg.Text('Enter something on Row 2'), sg.InputText()],
          [sg.OK(), sg.Cancel()]]


window = sg.Window('Window Title', layout)

while True:
    event, values = window.Read()
    if event in (None, 'Cancel'):
        break

window.Close()
