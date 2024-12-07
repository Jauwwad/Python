import pyautogui as py
import time

message = input("enter a sentence :")
count = 1 
n=int(input("Enter number of repeation:"))
time.sleep(0.1)

for i in range (n):
    py.typewrite(message + " " + str(count))
    py.press("Enter")
    count = count + 1

    print("ok")