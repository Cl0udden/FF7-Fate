#William Caravello
import PySimpleGUI as sg
import pygame

timer_running = True
counter = 0
Text_size = 20
loop = 0
sg.theme('SystemDefault')
layout = [[sg.Image('ffvii-banner1.png')],
          [sg.Text(size=(10, 1), font=('Helvetica', 100), justification='center', key='_OUTPUT_')],
          [sg.Button('▶/⏸', focus=True, font=("Helvetica", Text_size)),
           sg.Button('⟲', focus=True, font=("Helvetica", Text_size))],
          [sg.Slider(range=(1, 20), key='_TimeLim_', orientation='h', size=(40, 40), default_value=8),
           sg.Text('Time incounter Limit' + '\n' + 'in minites', font=('Helvetica', Text_size - 10))],
          [sg.Checkbox('Loop Music?', font=("Helvetica", Text_size), size=(50, 1), default=False, key='loop')],
          [sg.Button('Stop Music', font=("Helvetica", Text_size)),
           sg.Button('Battle music', font=("Helvetica", Text_size)),
           sg.Button('Battle won', font=("Helvetica", Text_size)),
           sg.Quit(font=("Helvetica", Text_size))]]

window = sg.Window('Final Fantisy IIV', layout)
pygame.mixer.init()
while True:
    event, values = window.read(timeout=10)

    if timer_running:
        counter += 1
        if ((counter // 100) % 60) % 2:  # Turns the timer red and black everyother second
            color = 'Red'
        else:
            color = 'Black'

        window['_OUTPUT_'].update(
            '{:02d}:{:02d}.{:02d}'.format((counter // 100) // 60, (counter // 100) % 60, counter % 100),
            text_color=color)

        if ((counter // 100) // 60) >= values['_TimeLim_'] and ((counter // 100) % 60) >= 5:
            pygame.mixer.music.load('20-fight-on.mp3')
            pygame.mixer.music.play(loop)
            counter = 0

    if values['loop'] is True:
        loop = -1
    else:
        loop = 0

    if event in (None, 'Quit'):
        pygame.mixer.music.stop()
        break

    if event == 'Stop Music':
        pygame.mixer.music.stop()

    if event == 'Battle won':
        pygame.mixer.music.load('11-fanfare.mp3')
        pygame.mixer.music.play(loop)

    if event == 'Battle music':
        pygame.mixer.music.load('20-fight-on.mp3')
        pygame.mixer.music.play(loop)

    if event == '▶/⏸':
        timer_running = not timer_running

    if event == '⟲':
        counter = 0
