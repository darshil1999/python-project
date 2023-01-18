# To install pygame module use 
# For windows - pip install pygame
# For linux - pip3 install pygame
import pygame

# Initialise pygame window
pygame.init()
arr1 = ""
arr = []

# define screen dimensions and fonts
screen = pygame.display.set_mode((700,500))
font = pygame.font.SysFont('Ubuntu mono', 20)

run = True

def show_txt(arr):
    # create new screen
    screen.fill((0,0,150,0))
    block = font.render(str(arr), True, (255,255,150))
    # display the array
    screen.blit(block, (20,20))

def draw_rect():
    for i in range(len(arr)):
        pygame.draw.rext(screen, (255,125,0), ((50+i*25,50,20,arr[i]*2)))
        pygame.display.upadte()

def bubble_sort():
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            # compare every element with every other element and switch places
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1] , arr[j]

        arr1 = [str(i) for i in arr]
        arr1 =",".join(arr1)
        show_txt(arr1)
        draw_rect()
        pygame.time.delay(500)
        pygame.display.update()

# initially fill the screen black
screen.fill((0,0,0,0))
block = font.render("Visualization of Bubble Sort", True, (255,0,150))
screen.blit(block, (0,20))

block1 = font.render("Ener Input and press ENTER to visualize", True, (255,255,150))
screen.blit(block1, (0,40))

block2= font.render("Add comma to separate the integers and backspace to pop", True, (255,255,150))
screen.blit(block2, (0,60))

pygame.display.update()

while run == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                arr = arr1.split(",")
                arr = [int(i) for i in arr]
                draw_rect()
                pygame.time.delay(3000)
                bubble_sort()

            elif event.key == pygame.K_BACKSPACE:
                arr1 = arr1[:-1]

            else:

                arr1+=event.unicode
                show_txt(arr1)
                pygame.display.update()

        elif event.type == pygame.QUIT:
            run = False

pygame.quit()