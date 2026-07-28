import math
import pygame

def Distance(A, B):
    return math.sqrt((A.rect.center[0] - B.rect.center[0])**2 + (A.rect.center[1] - B.rect.center[1])**2)

def Angle(A, B, look):
    # A-lvo, B-não alvo, look = o angulo para olhar para o alvo, ou para persegui-lo
    # retorna Radians
    try:
        if look:
            return math.atan2((A.rect.center[0]) - (B.rect.center[0]), (A.rect.center[1]) - (B.rect.center[1]))
        else:
            return math.atan2((A.rect.center[1]) - (B.rect.center[1]), (A.rect.center[0]) - (B.rect.center[0]))
    except:
        return 0

def Colide(A, B):
    if pygame.Rect.colliderect(A, B): # (Erro!) Rect sendo atualizado
        return True
    else:
        return False

def Touch(A, B, At, Bt): # R-ectangle, S-ector
    if At == 'R' and Bt == 'S':
        if Distance(A, B[0]) <= B[1]:
            a = Angle(A, B[0], True) + math.pi
            l1 = B[2][0]
            l2 = B[2][1]
            if a >= l1 and a <= l2:
                return True
    return False


def Escrever(texto, tam, pos, gameDisplay):
    largeText = pygame.font.Font('freesansbold.ttf', tam)
    TextSurf = largeText.render(texto, True, (0, 0, 0))
    TextRect = TextSurf.get_rect()
    TextRect.center = ((pos[0], pos[1]))
    gameDisplay.blit(TextSurf, TextRect)

def EscreverCanto(texto, tam, pos, gameDisplay, color = (0, 0, 0)):
    largeText = pygame.font.Font('freesansbold.ttf', tam)
    TextSurf = largeText.render(texto, True, color)
    gameDisplay.blit(TextSurf, pos)

def Closest(A, B): # A is you, B is list of others
    dm = 10000
    om = None
    for b in B:
        d = Distance(A, b)
        if d < dm:
            dm = d
            om = b
    return om

def Farthest(A, B): # A is you, B is list of others
    dm = 0
    om = None
    for b in B:
        d = Distance(A, b)
        if d > dm:
            dm = d
            om = b
    return om

def Inside(x, y, R):
    if x < R[0]:
        return False
    if x > R[0]+R[2]:
        return False
    
    if y < R[1]:
        return False
    if y > R[1]+R[3]:
        return False

    return True