#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install yfinance')


# In[7]:


get_ipython().system('pip install pyautogui')


# In[9]:


get_ipython().system('pip install pyperClip')


# In[ ]:


import yfinance
import pyautogui
import pyperclip
import time

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

time.sleep(3)
pyautogui.hotkey("ctrl","t")
pyperclip.copy("www.gmail.com")
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("enter")

time.sleep(20)
pyautogui.click(x=72, y=201)

pyautogui.copy(getEmail)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

pyautogui.copy(f"Análise das ações diárias da empresa {getTicker}")
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")



# In[ ]:


import time
import pyautogui

time.sleep(5)
pyautogui.position()


# In[ ]:





# In[ ]:




