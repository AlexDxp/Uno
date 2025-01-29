import random
import pygame
from pygame import image, MOUSEBUTTONDOWN
import sys


class Players:
  def __init__(self, p):
      self.playername = p
      self.b1 = 'bot1'
      self.b2 = 'bot2'
      self.b3 = 'bot2'
  def getname(self):
      return str(self.playername)
  def getinfo(self):
      return self.playername, self.b1, self.b2, self.b3

class Cards:
  def __init__(self, colour, type):
      self.colour = colour
      self.type = type
  def getinfo(self):
      return f"{self.colour} {self.type}"

class Deck:
  def __init__(self):
      self.cards = self.create_deck()
  def create_deck(self):
      colours = ['R', 'G', 'Y', 'B']
      types = [str(i)for i in range (1, 10)]
      types.append('R',)
      types.append('B')
      types.append('P2')
      noncolourtype = ['Wild', 'P4']
      deck = [Cards(colour, type) for colour in colours for type in types] * 2
      for i in range(4):
          deck.append(Cards(noncolourtype[0],''))
          deck.append(Cards(noncolourtype[1],''))
          deck.append(Cards(colours[i],0))
      random.shuffle(deck)
      return deck

cards = []
game = Deck()
for card in game.create_deck():
  cards.append(card.getinfo())

p = input("What is your name? ").capitalize()
player = Players(p)

phand = []
b1hand = []
b2hand = []
b3hand = []
for i in range (7):
  phand.append(cards[i])
  cards.remove(cards[i])
  b1hand.append(cards[i])
  cards.remove(cards[i])
  b2hand.append(cards[i])
  cards.remove(cards[i])
  b3hand.append(cards[i])
  cards.remove(cards[i])
WIDTH = 1200
HEIGHT = 700

pygame.display.set_caption('UNO')
screen = pygame.display.set_mode((WIDTH, HEIGHT))


card_images = {
  "B 0": image.load("Cards/Colour/Blue/BLUE 0.png"),
  "B 1": image.load("Cards/Colour/Blue/BLUE 1.png"),
  "B 2": image.load("Cards/Colour/Blue/BLUE 2.png"),
  "B 3": image.load("Cards/Colour/Blue/BLUE 3.png"),
  "B 4": image.load("Cards/Colour/Blue/BLUE 4.png"),
  "B 5": image.load("Cards/Colour/Blue/BLUE 5.png"),
  "B 6": image.load("Cards/Colour/Blue/BLUE 6.png"),
  "B 7": image.load("Cards/Colour/Blue/BLUE 7.png"),
  "B 8": image.load("Cards/Colour/Blue/BLUE 8.png"),
  "B 9": image.load("Cards/Colour/Blue/BLUE 9.png"),
  "B B": image.load("Cards/Colour/Blue/BLUE BLOCK.png"),
  "B R": image.load("Cards/Colour/Blue/BLUE REVERSE.png"),
  "B P2": image.load("Cards/Colour/Blue/BLUE +2.png"),
  "G 0": image.load("Cards/Colour/Green/GREEN 0.png"),
  "G 1": image.load("Cards/Colour/Green/GREEN 1.png"),
  "G 2": image.load("Cards/Colour/Green/GREEN 2.png"),
  "G 3": image.load("Cards/Colour/Green/GREEN 3.png"),
  "G 4": image.load("Cards/Colour/Green/GREEN 4.png"),
  "G 5": image.load("Cards/Colour/Green/GREEN 5.png"),
  "G 6": image.load("Cards/Colour/Green/GREEN 6.png"),
  "G 7": image.load("Cards/Colour/Green/GREEN 7.png"),
  "G 8": image.load("Cards/Colour/Green/GREEN 8.png"),
  "G 9": image.load("Cards/Colour/Green/GREEN 9.png"),
  "G B": image.load("Cards/Colour/Green/GREEN BLOCK.png"),
  "G R": image.load("Cards/Colour/Green/GREEN REVERSE.png"),
  "G P2": image.load("Cards/Colour/Green/GREEN +2.png"),
  "R 0": image.load("Cards/Colour/Red/RED 0.png"),
  "R 1": image.load("Cards/Colour/Red/RED 1.png"),
  "R 2": image.load("Cards/Colour/Red/RED 2.png"),
  "R 3": image.load("Cards/Colour/Red/RED 3.png"),
  "R 4": image.load("Cards/Colour/Red/RED 4.png"),
  "R 5": image.load("Cards/Colour/Red/RED 5.png"),
  "R 6": image.load("Cards/Colour/Red/RED 6.png"),
  "R 7": image.load("Cards/Colour/Red/RED 7.png"),
  "R 8": image.load("Cards/Colour/Red/RED 8.png"),
  "R 9": image.load("Cards/Colour/Red/RED 9.png"),
  "R B": image.load("Cards/Colour/Red/RED BLOCK.png"),
  "R R": image.load("Cards/Colour/Red/RED REVERSE.png"),
  "R P2": image.load("Cards/Colour/Red/RED +2.png"),
  "Y 0": image.load("Cards/Colour/Yellow/YELLOW 0.png"),
  "Y 1": image.load("Cards/Colour/Yellow/YELLOW 1.png"),
  "Y 2": image.load("Cards/Colour/Yellow/YELLOW 2.png"),
  "Y 3": image.load("Cards/Colour/Yellow/YELLOW 3.png"),
  "Y 4": image.load("Cards/Colour/Yellow/YELLOW 4.png"),
  "Y 5": image.load("Cards/Colour/Yellow/YELLOW 5.png"),
  "Y 6": image.load("Cards/Colour/Yellow/YELLOW 6.png"),
  "Y 7": image.load("Cards/Colour/Yellow/YELLOW 7.png"),
  "Y 8": image.load("Cards/Colour/Yellow/YELLOW 8.png"),
  "Y 9": image.load("Cards/Colour/Yellow/YELLOW 9.png"),
  "Y B": image.load("Cards/Colour/Yellow/YELLOW BLOCK.png"),
  "Y R": image.load("Cards/Colour/Yellow/YELLOW REVERSE.png"),
  "Y P2": image.load("Cards/Colour/Yellow/YELLOW +2.png"),
  "Wild ": image.load("Cards/Special/WILD.png"),
  "P4 ": image.load("Cards/Special/+4.png"),
}
back = image.load("Cards/Card Back.png")
winscreen = image.load("Win loss/Uno win.png")
lossscreen = image.load("Win loss/Uno lose.png")
turn = 0
selected_card = []
card_positions = [(card, 400 + (i * 50), 450) for i, card in enumerate(phand)]
print(card_positions)
length = len(phand)
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
gamepile = [cards[0]]
center_card = gamepile[0]
print(phand)
running = True
pygame.display.flip()
while running:
    allowed = False
    screen.fill((10, 160, 50))
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 30)
    name = font.render(p, True, (255, 255, 255))
    screen.blit(name, (300, 438))
    destx = 300
    desty = 475
    b1X = 50
    b1Y = 150
    b2X = 400
    b2Y = 25
    b3X = 950
    b3Y = 150

    for card in phand:
        if card in card_images:
            screen.blit(card_images[card], (destx, desty))
            destx += 50
    for card in range(len(b1hand)):
        b1back = pygame.transform.rotate(back, (270))
        screen.blit(b1back, (b1X, b1Y))
        b1Y += 50
    for card in range(len(b2hand)):
        b2back = pygame.transform.rotate(back, (180))
        screen.blit(b2back, (b2X, b2Y))
        b2X += 50
    for card in range(len(b3hand)):
        b3back = pygame.transform.rotate(back, (90))
        screen.blit(b3back, (b3X, b3Y))
        b3Y += 50

    screen.blit(back, (CENTER_X + 135, CENTER_Y - 90))
    screen.blit(back, (CENTER_X + 130, CENTER_Y - 95))
    screen.blit(back, (CENTER_X + 125, CENTER_Y - 100))

    if center_card in card_images:
        screen.blit(card_images[center_card], (CENTER_X - 200, CENTER_Y - 100))
        pygame.display.flip()

    if length == 0:
        while True:
            screen.blit(winscreen, (0, 0))
            pygame.display.flip()
    elif length >= 14:
        while True:
            screen.blit(lossscreen, (0, 0))
            pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(mouse_x, mouse_y)
                print(phand)
                print(length)
                if turn == 0:
                    if 725 <= mouse_x <= 855 and 250 <= mouse_y <= 450:
                        phand.append(cards[0])
                        cards.remove(cards[0])
                        length = len(phand)
                    if length == 0:
                        while True:
                            screen.blit(winscreen, (0, 0))
                            pygame.display.flip()
                    elif length == 1:
                        if 300 <= mouse_x <= 420 and 475 <= mouse_y <= 674:
                            selected_card = phand[0]
                        else:
                            continue
                    elif length == 2:
                        if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                            selected_card = phand[0]
                        elif 350 < mouse_x <= 470 and 475 <= mouse_y <= 674:
                            selected_card = phand[1]
                        else:
                            continue
                    elif length == 3:
                        if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                            selected_card = phand[0]
                        elif 350 < mouse_x <= 400 and 475 <= mouse_y <= 674:
                            selected_card = phand[1]
                        elif 400 < mouse_x <= 520 and 475 <= mouse_y <= 674:
                            selected_card = phand[2]
                        else:
                            continue
                    elif length == 4:
                        if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                            selected_card = phand[0]
                        elif 350 < mouse_x <= 400 and 475 <= mouse_y <= 674:
                            selected_card = phand[1]
                        elif 400 < mouse_x <= 450 and 475 <= mouse_y <= 674:
                            selected_card = phand[2]
                        elif 450 < mouse_x <= 570 and 475 <= mouse_y <= 674:
                            selected_card = phand[3]
                        else:
                            continue
                    elif length == 5:
                        if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                            selected_card = phand[0]
                        elif 350 < mouse_x <= 400 and 475 <= mouse_y <= 674:
                            selected_card = phand[1]
                        elif 400 < mouse_x <= 450 and 475 <= mouse_y <= 674:
                            selected_card = phand[2]
                        elif 450 < mouse_x <= 500 and 475 <= mouse_y <= 674:
                            selected_card = phand[3]
                        elif 500 < mouse_x <= 620 and 475 <= mouse_y <= 674:
                            selected_card = phand[4]
                        else:
                            continue
                    elif length == 6:
                        if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                            selected_card = phand[0]
                        elif 350 < mouse_x <= 400 and 475 <= mouse_y <= 674:
                            selected_card = phand[1]
                        elif 400 < mouse_x <= 450 and 475 <= mouse_y <= 674:
                            selected_card = phand[2]
                        elif 450 < mouse_x <= 500 and 475 <= mouse_y <= 674:
                            selected_card = phand[3]
                        elif 500 < mouse_x <= 550 and 475 <= mouse_y <= 674:
                            selected_card = phand[4]
                        elif 550 < mouse_x <= 670 and 475 <= mouse_y <= 674:
                            selected_card = phand[5]
                        else:
                            continue
                    elif length == 7:
                        if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                            selected_card = phand[0]
                        elif 350 < mouse_x <= 400 and 475 <= mouse_y <= 674:
                            selected_card = phand[1]
                        elif 400 < mouse_x <= 450 and 475 <= mouse_y <= 674:
                            selected_card = phand[2]
                        elif 450 < mouse_x <= 500 and 475 <= mouse_y <= 674:
                            selected_card = phand[3]
                        elif 500 < mouse_x <= 550 and 475 <= mouse_y <= 674:
                            selected_card = phand[4]
                        elif 550 < mouse_x <= 600 and 475 <= mouse_y <= 674:
                            selected_card = phand[5]
                        elif 600 < mouse_x <= 720 and 475 <= mouse_y <= 674:
                            selected_card = phand[6]
                        else:
                            continue
                    elif length == 8:
                        if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                            selected_card = phand[0]
                        elif 350 < mouse_x <= 400 and 475 <= mouse_y <= 674:
                            selected_card = phand[1]
                        elif 400 < mouse_x <= 450 and 475 <= mouse_y <= 674:
                            selected_card = phand[2]
                        elif 450 < mouse_x <= 500 and 475 <= mouse_y <= 674:
                            selected_card = phand[3]
                        elif 500 < mouse_x <= 550 and 475 <= mouse_y <= 674:
                            selected_card = phand[4]
                        elif 550 < mouse_x <= 600 and 475 <= mouse_y <= 674:
                            selected_card = phand[5]
                        elif 600 < mouse_x <= 650 and 475 <= mouse_y <= 674:
                            selected_card = phand[6]
                        elif 650 < mouse_x <= 770 and 475 <= mouse_y <= 674:
                            selected_card = phand[7]
                        else:
                            continue
                    elif length == 9:
                        if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                            selected_card = phand[0]
                        elif 350 < mouse_x <= 400 and 475 <= mouse_y <= 674:
                            selected_card = phand[1]
                        elif 400 < mouse_x <= 450 and 475 <= mouse_y <= 674:
                            selected_card = phand[2]
                        elif 450 < mouse_x <= 500 and 475 <= mouse_y <= 674:
                            selected_card = phand[3]
                        elif 500 < mouse_x <= 550 and 475 <= mouse_y <= 674:
                            selected_card = phand[4]
                        elif 550 < mouse_x <= 600 and 475 <= mouse_y <= 674:
                            selected_card = phand[5]
                        elif 600 < mouse_x <= 650 and 475 <= mouse_y <= 674:
                            selected_card = phand[6]
                        elif 650 < mouse_x <= 700 and 475 <= mouse_y <= 674:
                            selected_card = phand[7]
                        elif 700 < mouse_x <= 820 and 475 <= mouse_y <= 674:
                            selected_card = phand[8]
                        else:
                            continue
                    elif length == 10:
                        if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                            selected_card = phand[0]
                        elif 350 < mouse_x <= 400 and 475 <= mouse_y <= 674:
                            selected_card = phand[1]
                        elif 400 < mouse_x <= 450 and 475 <= mouse_y <= 674:
                            selected_card = phand[2]
                        elif 450 < mouse_x <= 500 and 475 <= mouse_y <= 674:
                            selected_card = phand[3]
                        elif 500 < mouse_x <= 550 and 475 <= mouse_y <= 674:
                            selected_card = phand[4]
                        elif 550 < mouse_x <= 600 and 475 <= mouse_y <= 674:
                            selected_card = phand[5]
                        elif 600 < mouse_x <= 650 and 475 <= mouse_y <= 674:
                            selected_card = phand[6]
                        elif 650 < mouse_x <= 700 and 475 <= mouse_y <= 674:
                            selected_card = phand[7]
                        elif 700 < mouse_x <= 750 and 475 <= mouse_y <= 674:
                            selected_card = phand[8]
                        elif 750 < mouse_x <= 870 and 475 <= mouse_y <= 674:
                            selected_card = phand[9]
                        else:
                            continue
                    elif length == 11:
                        if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                            selected_card = phand[0]
                        elif 350 < mouse_x <= 400 and 475 <= mouse_y <= 674:
                            selected_card = phand[1]
                        elif 400 < mouse_x <= 450 and 475 <= mouse_y <= 674:
                            selected_card = phand[2]
                        elif 450 < mouse_x <= 500 and 475 <= mouse_y <= 674:
                            selected_card = phand[3]
                        elif 500 < mouse_x <= 550 and 475 <= mouse_y <= 674:
                            selected_card = phand[4]
                        elif 550 < mouse_x <= 600 and 475 <= mouse_y <= 674:
                            selected_card = phand[5]
                        elif 600 < mouse_x <= 650 and 475 <= mouse_y <= 674:
                            selected_card = phand[6]
                        elif 650 < mouse_x <= 700 and 475 <= mouse_y <= 674:
                            selected_card = phand[7]
                        elif 700 < mouse_x <= 750 and 475 <= mouse_y <= 674:
                            selected_card = phand[8]
                        elif 750 < mouse_x <= 800 and 475 <= mouse_y <= 674:
                            selected_card = phand[9]
                        elif 800 < mouse_x <= 920 and 475 <= mouse_y <= 674:
                            selected_card = phand[10]
                        else:
                            continue
                    elif length == 12:
                        if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                            selected_card = phand[0]
                        elif 350 < mouse_x <= 400 and 475 <= mouse_y <= 674:
                            selected_card = phand[1]
                        elif 400 < mouse_x <= 450 and 475 <= mouse_y <= 674:
                            selected_card = phand[2]
                        elif 450 < mouse_x <= 500 and 475 <= mouse_y <= 674:
                            selected_card = phand[3]
                        elif 500 < mouse_x <= 550 and 475 <= mouse_y <= 674:
                            selected_card = phand[4]
                        elif 550 < mouse_x <= 600 and 475 <= mouse_y <= 674:
                            selected_card = phand[5]
                        elif 600 < mouse_x <= 650 and 475 <= mouse_y <= 674:
                            selected_card = phand[6]
                        elif 650 < mouse_x <= 700 and 475 <= mouse_y <= 674:
                            selected_card = phand[7]
                        elif 700 < mouse_x <= 750 and 475 <= mouse_y <= 674:
                            selected_card = phand[8]
                        elif 750 < mouse_x <= 800 and 475 <= mouse_y <= 674:
                            selected_card = phand[9]
                        elif 800 < mouse_x <= 850 and 475 <= mouse_y <= 674:
                            selected_card = phand[10]
                        elif 850 < mouse_x <= 970 and 475 <= mouse_y <= 674:
                            selected_card = phand[11]
                        else:
                            continue
                    elif length == 13:
                        if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                            selected_card = phand[0]
                        elif 350 < mouse_x <= 400 and 475 <= mouse_y <= 674:
                            selected_card = phand[1]
                        elif 400 < mouse_x <= 450 and 475 <= mouse_y <= 674:
                            selected_card = phand[2]
                        elif 450 < mouse_x <= 500 and 475 <= mouse_y <= 674:
                            selected_card = phand[3]
                        elif 500 < mouse_x <= 550 and 475 <= mouse_y <= 674:
                            selected_card = phand[4]
                        elif 550 < mouse_x <= 600 and 475 <= mouse_y <= 674:
                            selected_card = phand[5]
                        elif 600 < mouse_x <= 650 and 475 <= mouse_y <= 674:
                            selected_card = phand[6]
                        elif 650 < mouse_x <= 700 and 475 <= mouse_y <= 674:
                            selected_card = phand[7]
                        elif 700 < mouse_x <= 750 and 475 <= mouse_y <= 674:
                            selected_card = phand[8]
                        elif 750 < mouse_x <= 800 and 475 <= mouse_y <= 674:
                            selected_card = phand[9]
                        elif 800 < mouse_x <= 850 and 475 <= mouse_y <= 674:
                            selected_card = phand[10]
                        elif 850 < mouse_x <= 900 and 475 <= mouse_y <= 674:
                            selected_card = phand[11]
                        elif 900 < mouse_x <= 1020 and 475 <= mouse_y <= 674:
                            selected_card = phand[12]
                        else:
                            continue
                    elif length >= 14:
                        while True:
                            screen.blit(lossscreen, (0, 0))
                            pygame.display.flip()


                    print(selected_card)
                    selected = selected_card.split()
                    center = center_card.split()
                    sc = selected[0]
                    cc = center[0]
                    if len(selected) <= 1 or len(center) <= 1:
                        continue
                    else:
                        scard = selected[1]
                        ccard = center[1]
                    print(sc)
                    print(cc)
                    if sc == 'P4' or sc == 'Wild' or sc == cc:
                        allowed = True
                    elif scard == ccard:
                        allowed = True
                    else:
                        allowed = False

                    if allowed:
                        if length == 0:
                            while True:
                                screen.blit(winscreen, (0, 0))
                                pygame.display.flip()
                        elif length == 1:
                            if 300 <= mouse_x <= 420 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(0)
                            else:
                                continue
                        elif length == 2:
                            if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(0)
                            elif 350 < mouse_x <= 470 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(1)
                            else:
                                continue
                        elif length == 3:
                            if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(0)
                            elif 350 < mouse_x <= 400 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(1)
                            elif 400 < mouse_x <= 520 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(2)
                            else:
                                continue
                        elif length == 4:
                            if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(0)
                            elif 350 < mouse_x <= 400 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(1)
                            elif 400 < mouse_x <= 450 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(2)
                            elif 450 < mouse_x <= 570 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(3)
                            else:
                                continue
                        elif length == 5:
                            if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(0)
                            elif 350 < mouse_x <= 400 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(1)
                            elif 400 < mouse_x <= 450 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(2)
                            elif 450 < mouse_x <= 500 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(3)
                            elif 500 < mouse_x <= 620 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(4)
                            else:
                                continue
                        elif length == 6:
                            if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(0)
                            elif 350 < mouse_x <= 400 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(1)
                            elif 400 < mouse_x <= 450 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(2)
                            elif 450 < mouse_x <= 500 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(3)
                            elif 500 < mouse_x <= 550 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(4)
                            elif 550 < mouse_x <= 670 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(5)
                            else:
                                continue
                        elif length == 7:
                            if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(0)
                            elif 350 < mouse_x <= 400 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(1)
                            elif 400 < mouse_x <= 450 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(2)
                            elif 450 < mouse_x <= 500 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(3)
                            elif 500 < mouse_x <= 550 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(4)
                            elif 550 < mouse_x <= 600 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(5)
                            elif 600 < mouse_x <= 720 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(6)
                            else:
                                continue
                        elif length == 8:
                            if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(0)
                            elif 350 < mouse_x <= 400 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(1)
                            elif 400 < mouse_x <= 450 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(2)
                            elif 450 < mouse_x <= 500 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(3)
                            elif 500 < mouse_x <= 550 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(4)
                            elif 550 < mouse_x <= 600 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(5)
                            elif 600 < mouse_x <= 650 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(6)
                            elif 650 < mouse_x <= 770 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(7)
                            else:
                                continue
                        elif length == 9:
                            if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(0)
                            elif 350 < mouse_x <= 400 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(1)
                            elif 400 < mouse_x <= 450 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(2)
                            elif 450 < mouse_x <= 500 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(3)
                            elif 500 < mouse_x <= 550 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(4)
                            elif 550 < mouse_x <= 600 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(5)
                            elif 600 < mouse_x <= 650 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(6)
                            elif 650 < mouse_x <= 700 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(7)
                            elif 700 < mouse_x <= 820 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(8)
                            else:
                                continue
                        elif length == 10:
                            if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(0)
                            elif 350 < mouse_x <= 400 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(1)
                            elif 400 < mouse_x <= 450 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(2)
                            elif 450 < mouse_x <= 500 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(3)
                            elif 500 < mouse_x <= 550 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(4)
                            elif 550 < mouse_x <= 600 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(5)
                            elif 600 < mouse_x <= 650 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(6)
                            elif 650 < mouse_x <= 700 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(7)
                            elif 700 < mouse_x <= 750 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(8)
                            elif 750 < mouse_x <= 870 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(9)
                            else:
                                continue
                        elif length == 11:
                            if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(0)
                            elif 350 < mouse_x <= 400 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(1)
                            elif 400 < mouse_x <= 450 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(2)
                            elif 450 < mouse_x <= 500 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(3)
                            elif 500 < mouse_x <= 550 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(4)
                            elif 550 < mouse_x <= 600 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(5)
                            elif 600 < mouse_x <= 650 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(6)
                            elif 650 < mouse_x <= 700 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(7)
                            elif 700 < mouse_x <= 750 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(8)
                            elif 750 < mouse_x <= 800 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(9)
                            elif 800 < mouse_x <= 920 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(10)
                            else:
                                continue
                        elif length == 12:
                            if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(0)
                            elif 350 < mouse_x <= 400 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(1)
                            elif 400 < mouse_x <= 450 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(2)
                            elif 450 < mouse_x <= 500 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(3)
                            elif 500 < mouse_x <= 550 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(4)
                            elif 550 < mouse_x <= 600 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(5)
                            elif 600 < mouse_x <= 650 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(6)
                            elif 650 < mouse_x <= 700 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(7)
                            elif 700 < mouse_x <= 750 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(8)
                            elif 750 < mouse_x <= 800 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(9)
                            elif 800 < mouse_x <= 850 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(10)
                            elif 850 < mouse_x <= 970 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(11)
                            else:
                                continue
                        elif length == 13:
                            if 300 <= mouse_x <= 350 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(0)
                            elif 350 < mouse_x <= 400 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(1)
                            elif 400 < mouse_x <= 450 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(2)
                            elif 450 < mouse_x <= 500 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(3)
                            elif 500 < mouse_x <= 550 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(4)
                            elif 550 < mouse_x <= 600 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(5)
                            elif 600 < mouse_x <= 650 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(6)
                            elif 650 < mouse_x <= 700 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(7)
                            elif 700 < mouse_x <= 750 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(8)
                            elif 750 < mouse_x <= 800 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(9)
                            elif 800 < mouse_x <= 850 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(10)
                            elif 850 < mouse_x <= 900 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(11)
                            elif 900 < mouse_x <= 1020 and 475 <= mouse_y <= 674:
                                selected_card = phand.pop(12)
                            else:
                                continue
                        elif length >= 14:
                            while True:
                                screen.blit(lossscreen, (0, 0))
                                pygame.display.flip()
                        turn = 1
                        length = len(phand)
                        gamepile.append(selected_card)
                        center_card = selected_card
                    elif not allowed:
                        continue






