import pyautogui
import time

#滑鼠移至畫面左上角停止
pyautogui.FAILSAFE = True
#備用調速度
#pyautogui.PAUSE=1

while True:
    war_position = pyautogui.locateOnScreen('war.png')
    watch_position = pyautogui.locateOnScreen('watch.png')
    item_position = pyautogui.locateOnScreen('item.png')
    guildwar_position = pyautogui.locateOnScreen('guildwar.png')
    #魔力是否夠用戰吼
    if war_position != None:
        pyautogui.click(x=war_position[0],y=war_position[1],duration=1)
    else:
        print("Nofound_war")
    #公會戰是否開始
    if guildwar_position != None:
        pyautogui.click(x=guildwar_position[0],y=guildwar_position[1],duration=1)
        time.sleep(3)
        #利用排行榜定位公會戰開始
        guildlist_position = pyautogui.locateOnScreen('guildlist.png')
        pyautogui.click(x=guildlist_position[0]-130,y=guildlist_position[1]+20,duration=1)
        time.sleep(3)
        fight_position = pyautogui.locateOnScreen('fight.png')
        pyautogui.click(x=fight_position[0],y=fight_position[1],duration=1)
        for i in range(200):
            pyautogui.click()
        time.sleep(20)
        pyautogui.click()
        end_position = pyautogui.locateOnScreen('end.png')
        pyautogui.click(x=end_position[0],y=end_position[1],duration=1)   
    else:
        print("Nofound_guildwar")
    #是否看廣告---未完成 
    if watch_position != None:
        pyautogui.click(x=watch_position[0],y=watch_position[1],duration=1)
        #等廣告結束
        time.sleep(40)
        #一律按返回鈕
        return_position = pyautogui.locateOnScreen('return.png')
        pyautogui.click(x=return_position[0],y=return_position[1],duration=1)
        #判斷是否有進廣告
        if pyautogui.locateOnScreen('no.png') == None:
            catch_position = pyautogui.locateOnScreen('catch.png')
            pyautogui.click(x=catch_position[0],y=catch_position[1],duration=1)
        else:
            no_position = pyautogui.locateOnScreen('no.png')
            pyautogui.click(x=no_position[0],y=no_position[1],duration=1.5)            
            catch_position = pyautogui.locateOnScreen('catch.png')
            pyautogui.click(x=catch_position[0],y=catch_position[1],duration=1)
    else:
        print("Nofoundwatch")
    #用item定位公會飛船    
    if item_position != None:
        pyautogui.click(item_position[0]+49,item_position[1]+36)
        
    print("   ")




    
