from tkinter import *
from googletrans import Translator
from tkinter import ttk
import os
import pyperclip
from gtts import gTTS
import pyttsx3
import playsound
import pyglet
from pyglet.gl import *

win = Tk()
win.geometry("350x350")
win.title('LANGUAGE CONVERTER')


def open_help():
    os.system(r'ENTER YOUR FILE PATH')
    # label4 = Label(win2, text="'af': 'afrikaans',
    """'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',, font="Courier 13 bold").grid(row=0,column=0)
    win2.mainloop()"""


def translate(user_input, user_language):
    translator = Translator()
    translated = translator.translate(user_input, dest=user_language)
    return translated.text


def display_text():
    label1 = Label(win, text="Your answer is ", font="Courier 13 bold")
    label1.grid(row=5, column=10)
    global entry, user_language
    global entry1, string1
    user_language = entry1.get()
    string = entry.get()
    string1 = translate(string, user_language)
    label.configure(text=string1)


def copy1():
    pyperclip.copy(string1)


def speak():
    output = gTTS(text=string1, lang=user_language, slow=False)
    output.save("output.mp3")
    # playsound.playsound('output.mp3', False)
    # os.system("start output.mp3")
    # print(string1)
    # engine = pyttsx3.init()
    # engine.say(string1)
    # engine.runAndWait()
    pyglet.options['audio'] = ('openal', 'directsound', 'silent')
    music = pyglet.resource.media('output.mp3')
    music.play()
    pyglet.app.run()


# ans label
label = Label(win, text="", font="Courier 22 bold")
label.grid(row=6, column=10)
# label 2
label2 = Label(win, text="Please enter a language below", font="Courier 13 bold")
label2.grid(row=0, column=10)
# label 3
label3 = Label(win, text="Please enter text below", font="Courier 13 bold")
label3.grid(row=2, column=10)

# data entry from user
entry = Entry(win, width=40, borderwidth=5)
entry.focus_set()
entry.grid(row=3, column=10)
# data entry 2
entry1 = Entry(win, width=40, borderwidth=5)
entry1.focus_set()
entry1.grid(row=1, column=10)

# Create a Button to validate Entry Widget
ttk.Button(win, text="Enter", width=5, style='W.TButton', command=display_text).grid(row=4, column=10)
ttk.Button(win, text="Help", width=5, style='W.TButton', command=open_help).grid(row=1, column=11)
ttk.Button(win, text="copy", width=5, style='W.TButton', command=copy1).grid(row=6, column=11)
ttk.Button(win, text="speak", width=5, style='W.TButton', command=speak).grid(row=7, column=11)
win.mainloop()
0