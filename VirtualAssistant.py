# Carlos Vazquez 4/18/2021
import PySimpleGUI as sg
import wolframalpha
client = wolframalpha.Client("PAEHX3-RV5AJPV9E4") 
import wikipedia
import pyttsx3
engine = pyttsx3.init()



# GUI Setup and Theme
sg.theme('DarkPurple')
layout = [ [sg.Text('Enter command'), sg.InputText()], 
            [sg.Button('Run'), sg.Button('Cancel')] ]

window = sg.Window('Virtual Assistant', layout)






# Display stuff
while True:
    event, values = window.read()
    if event in (None, 'Cancel'): 
        break
    try:
        wikipedia_res = wikipedia.summary(values[0], sentences=2)
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking("Wolfram Result: "+wolfram_res, "Wikipedia Result: "+wikipedia_res)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except:
        wikipedia_res = wikipedia.summary(values[0], sentences=2)
        engine.say(wikipedia_res)
        sg.PopupNonBlocking(wikipedia_res)

    engine.runAndWait()


    
    print(values[0])



window.close()