import yfinance
import pyautogui
import pyperclip
import time
import datetime

def waitingTime(time):
    time.sleep(time)
    waitingTime()

getClient = input("Digite seu nome: ")
getEmail = input("Digite o email para enviar o relatório: ")
getTicker = input("Digite o ticker da empresa baseado no Yahoo Finance: ")
dateTicker = yfinance.Ticker(getTicker).history("6mo")
gettingClose = dateTicker.Close

maxClose = gettingClose.max()
minClose = gettingClose.min()
currentClose = gettingClose[-1]
today = datetime.date.today()

time.sleep(3)
pyautogui.hotkey("ctrl","t")
pyperclip.copy("www.gmail.com")
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("enter")
time.sleep(10)
pyautogui.click(x=72, y=201)
timE.sleep(5)
pyperclip.copy(getEmail)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")
time.sleep(5)
pyperclip.copy(f"Análise das ações diárias da empresa {getTicker}")
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")
time.sleep(5)
pyperclip.copy(f"""
Bom dia {getClient}!

Segue as análises da empresa {getTicker}!

Atualmente a cotação da empresa no dia {today} é de R${round(currentClose, 2)}

O fechamento mínimo foi de: R${round(minClose, 2)}

O fechamento máximo foi de: R${round(maxClose, 2)}

Para qualquer dúvida sobre nosso sistema de análises, basta enviar um email para nosso suporte!

Atenciosamente,
Matheus Siqueira!
""")
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")


