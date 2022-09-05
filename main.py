import webbrowser
import pyautogui as pt
from pyautogui import *
from pyperclip import *
import pyperclip as pc

# certain caractèrer ne sont pas pris en compte
# si on utilise la syntaxe pyautogui.write.
def _work_write(text):
    pc.copy(text)
    pt.hotkey('ctrl', 'v')
    pc.copy('')


# vérifie l'image a 80% 'confidence=.8' .
def nav_to_imgage(image, clicks, off_x=0, off_y=0):
    # localise ce qui ressemble a l'image qu'on lui fourni
    position = pt.locateCenterOnScreen(image, confidence=.8)
    if position is None:
        print(f"{image} not found ...")
        return 0
    else:
        # va au centre de l'image et clique
        pt.moveTo(position, duration=.1)
        pt.moveRel(off_x, off_y, duration=.1)
        pt.click(clicks=clicks, interval=.3)

# vérifie l'image a 90% 'confidence=.9' .
def more_precise(image, clicks, off_x=0, off_y=0):
    # localise ce qui ressemble a l'image qu'on lui fourni
    position = pt.locateCenterOnScreen(image, confidence=.9)
    if position is None:
        print(f"{image} not found ...")
        return 0
    else:
        # va au centre de l'image et clique
        pt.moveTo(position, duration=.1)
        pt.moveRel(off_x, off_y, duration=.1)
        pt.click(clicks=clicks, interval=.3)


def question():
    global webbrowser, identifiant, mdp
    webbrowser = input("what is your webbrowser ? : ")
    identifiant = input("what is your login name ? : ")
    mdp = input("what is your password ? : ")


def main():
    question()
    site = "https://login.unice.fr/login?service=https://ent.unice.fr/uPortal/Login"

    pt.press("winleft")
    sleep(.5)
    _work_write(webbrowser)
    pt.press("enter")
    sleep(1)
    nav_to_imgage("Images/nouvelle-fenetre.png", 1)
    nav_to_imgage("Images/barre-de-recherche.png", 1)
    _work_write(site)
    pt.press("enter")
    sleep(1)

    nav_to_imgage("Images/identifiant.png", 1)
    _work_write(identifiant)
    nav_to_imgage("Images/mot-de-passe.png", 1)
    _work_write(mdp)
    nav_to_imgage("Images/connect-button.png", 1)
    # le temps d'attente peut être modifier si votre connexion est trop lente ou plus rapide
    sleep(4)
    more_precise("Images/mes-infos.png", 1)
    # le temps d'attente peut être modifier si votre connexion est trop lente ou plus rapide
    sleep(3)

    nav_to_imgage("Images/planning.png", 1)
    sleep(1)
    nav_to_imgage("Images/gpu.png", 1)
    sleep(0.5)
    nav_to_imgage("Images/emplois-du-temps.png", 1)
    sleep(0.5)
    nav_to_imgage("Images/edp-etudiant.png", 1)


if __name__ == '__main__':
    main()
