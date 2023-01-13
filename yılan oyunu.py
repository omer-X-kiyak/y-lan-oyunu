import pygame
import random

# Oyun ekranının boyutlarını ayarlayın
WIDTH = 600
HEIGHT = 600

# Yılanın başlangıç pozisyonunu ve hızını ayarlayın
x = WIDTH / 2
y = HEIGHT / 2
speed = 5

# Yiyecekleri rastgele pozisyonlara yerleştirin
food_x = random.randint(0, WIDTH)
food_y = random.randint(0, HEIGHT)

# Pygame modülünü başlatın
pygame.init()

# Oyun ekranını oluşturun
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Yılanın rengini ayarlayın
color = (255, 255, 0)

# Oyun döngüsü
while True:
    # Olayları dinleyin
    for event in pygame.event.get():
        # Oyun kapatılırsa döngüyü kırın
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Yılanı yön tuşları ile yönlendirin
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Eğer yılan yiyecekleri yerse, yiyecekleri tekrar rastgele pozisyonlara yerleştirin ve puanı arttırın
    if x == food_x and y == food_y:
        food_x = random.randint(0, WIDTH)
        food_y = random.randint(0, HEIGHT)
        score += 1

    # Eğer yılan ekranın dışına çıkarsa,
