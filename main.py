import pygame   # 导入pygame模块

FPS = 60  # 设置帧率
WIDTH = 500
HEIGHT = 600

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

pygame.init()  # 初始化pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # 创建一个窗口
pygame.display.set_caption("打飞机")  # 设置窗口标题
clock = pygame.time.Clock()  # 创建一个时钟对象

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200
    
    def update(self):
        self.rect.x += 2
        if self.rect.left > WIDTH:
            self.rect.right = 0

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True

# 游戏循环
while running:
    clock.tick(FPS)  # 设置帧率
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新游戏
    all_sprites.update()
    
    # 画面显示
    screen.fill(WHITE)  # 填充背景色
    all_sprites.draw(screen)  # 绘制精灵组
    pygame.display.update()


pygame.quit()  # 退出pygame