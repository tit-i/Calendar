import calendar
from colorama import init, Fore, Back, Style
print(Back.CYAN)
print(">>>>>>>>>> nakiani wlis kalendari <<<<<<<<<<")
y1 = int(input('chawere pirveli weli: '))
y2 = int(input('chawere meore weli: '))
print(Back.LIGHTRED_EX)
leaps = calendar.leapdays(y1, y2)
print('nakiani wlebis raodenoba am wlidan', y1, ',', y2, 'am wlamde aris: ', leaps, 'weli')
init(autoreset=True)
input()