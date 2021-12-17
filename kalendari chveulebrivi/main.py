import calendar
from colorama import init, Fore, Back, Style
print(Back.CYAN)
year = int(input('chawere weli: '))
print(Back.LIGHTRED_EX)
print(calendar.prcal(year))
init(autoreset=True)
input()