import pyautogui
import time

#abrir o chrome
pyautogui.click(546, 733, 1, 3, 'left')

# clicar no zyro
time.sleep(2)
pyautogui.click(286, 81)

# clicar em importar imagem.
time.sleep(3)
pyautogui.click(631, 442)

# clique na imagem na pasta
time.sleep(3)
pyautogui.click(283,188, 2, 0, 'left')

#baixamo imagem
time.sleep(10)
pyautogui.click(535, 629)

#clicamo em importar nova imagem
pyautogui.click(967, 460, 1, 0,'left')

#deletar a 1 imagem
time.sleep(3)
pyautogui.click(283,188, 1, 0, 'left')
pyautogui.click(283,188,1, 0,'right')
pyautogui.click(360,647,1, 0,'left')

#clicar na imagem 1
time.sleep(3)
pyautogui.click(283,188, 2, 0, 'left')
#baixar imagem 2
time.sleep(10)
pyautogui.click(535, 629)

# clicar em importar imagem.
time.sleep(3)
pyautogui.click(631, 442)

# clique na imagem na pasta
time.sleep(3)
pyautogui.click(283,188, 2, 0, 'left')

#baixamo imagem
time.sleep(10)
pyautogui.click(535, 629)

#clicamo em importar nova imagem
pyautogui.click(967, 460, 1, 0,'left')
# clique na imagem na pasta
time.sleep(3)
pyautogui.click(283,188, 2, 0, 'left')

#baixamo imagem
time.sleep(10)
pyautogui.click(535, 629)

#clicamo em importar nova imagem
pyautogui.click(967, 460, 1, 0,'left')