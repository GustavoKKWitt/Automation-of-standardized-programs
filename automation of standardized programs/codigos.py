import pyautogui
import time
import pandas

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
tabela = pandas.read_csv("produtos.csv")

#entrar no chrome
pyautogui.PAUSE = 0.5 #internet pode demorar para carregar
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

#no site
time.sleep(3)
pyautogui.click(x=744,y=372)
pyautogui.write("cagueinascalças@gmail.com")
pyautogui.press("tab")
pyautogui.write("xixiecoco")
pyautogui.press("tab")
pyautogui.press("enter")

#colocar os produtos
time.sleep(3)

for linha in tabela.index:
    pyautogui.click(x=790,y=255)
    
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    #marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)
    #tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)
    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)
    #preco
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco)
    #custo
    custo= str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)
    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)