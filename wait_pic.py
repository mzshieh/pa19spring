import snp, pyautogui

def wait_pic(name,region=None):
    loc = snp.locateOnScreen(name,region=region)
    while loc == None:
        loc = snp.locateOnScreen(name,region=region)
    return loc
        
loc = wait_pic('box.png')
print(loc)
pyautogui.click(pyautogui.center(loc))

loc = wait_pic('box.png',region=(1,700,1250,80))
print(loc)
pyautogui.click(pyautogui.center(loc))