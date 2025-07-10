import pygame
import random
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# === Init Pygame ===
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Letter Shooter")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# === Game state ===
def reset_game():
    global score, time_left, target_letter, falling_objects, bullets, game_over
    score = 0
    time_left = 60
    target_letter = random.choice("abcdefghijklmnopqrstuvwxyz")
    falling_objects = []
    bullets = []
    game_over = False

# === Object list ===
object_data = [
    {"name": "abacus", "image": "assets/abacus.png"},
    {"name": "aeroplane", "image": "assets/aeroplane.png"},
    {"name": "ant", "image": "assets/ant.png"},
    {"name": "apple", "image": "assets/apple.png"},
    {"name": "aquarium", "image": "assets/aquarium.png"},
    {"name": "arrow", "image": "assets/arrow.png"},
    {"name": "award", "image": "assets/award.png"},
    {"name": "axe", "image": "assets/axe.png"},
    {"name": "baby", "image": "assets/baby.png"},
    {"name": "ball", "image": "assets/ball.png"},
    {"name": "bike", "image": "assets/bike.png"},
    {"name": "book", "image": "assets/book.png"},
    {"name": "butterfly", "image": "assets/butterfly.png"},
    {"name": "cake", "image": "assets/cake.png"},
    {"name": "car", "image": "assets/car.png"},
    {"name": "carrot", "image": "assets/carrot.png"},
    {"name": "cat", "image": "assets/cat.png"},
    {"name": "coat", "image": "assets/coat.png"},
    {"name": "cow", "image": "assets/cow.png"},
    {"name": "diamond", "image": "assets/diamond.png"},
    {"name": "dice", "image": "assets/dice.png"},
    {"name": "dog", "image": "assets/dog.png"},
    {"name": "doll", "image": "assets/doll.png"},
    {"name": "door", "image": "assets/door.png"},
    {"name": "duck", "image": "assets/duck.png"},
    {"name": "earth", "image": "assets/earth.png"},
    {"name": "egg", "image": "assets/egg.png"},
    {"name": "elephant", "image": "assets/elephant.png"},
    {"name": "eraser", "image": "assets/eraser.png"},
    {"name": "eye", "image": "assets/eye.png"},
    {"name": "fan", "image": "assets/fan.png"},
    {"name": "fish", "image": "assets/fish.png"},
    {"name": "flower", "image": "assets/flower.png"},
    {"name": "fox", "image": "assets/fox.png"},
    {"name": "frog", "image": "assets/frog.png"},
    {"name": "ghost", "image": "assets/ghost.png"},
    {"name": "giraffe", "image": "assets/giraffe.png"},
    {"name": "goat", "image": "assets/goat.png"},
    {"name": "grass", "image": "assets/grass.png"},
    {"name": "guitar", "image": "assets/guitar.png"},
    {"name": "gun", "image": "assets/gun.png"},
    {"name": "hammer", "image": "assets/hammer.png"},
    {"name": "hat", "image": "assets/hat.png"},
    {"name": "heart", "image": "assets/heart.png"},
    {"name": "horse", "image": "assets/horse.png"},
    {"name": "house", "image": "assets/house.png"},
    {"name": "ice", "image": "assets/ice.png"},
    {"name": "icecream", "image": "assets/icecream.png"},
    {"name": "igloo", "image": "assets/igloo.png"},
    {"name": "ink", "image": "assets/ink.png"},
    {"name": "iron", "image": "assets/iron.png"},
    {"name": "jacket", "image": "assets/jacket.png"},
    {"name": "jeep", "image": "assets/jeep.png"},
    {"name": "jellyfish", "image": "assets/jellyfish.png"},
    {"name": "jet", "image": "assets/jet.png"},
    {"name": "jug", "image": "assets/jug.png"},
    {"name": "juice", "image": "assets/juice.png"},
    {"name": "kangaroo", "image": "assets/kangaroo.png"},
    {"name": "key", "image": "assets/key.png"},
    {"name": "king", "image": "assets/king.png"},
    {"name": "kite", "image": "assets/kite.png"},
    {"name": "knife", "image": "assets/knife.png"},
    {"name": "laptop", "image": "assets/laptop.png"},
    {"name": "leaf", "image": "assets/leaf.png"},
    {"name": "lemon", "image": "assets/lemon.png"},
    {"name": "lion", "image": "assets/lion.png"},
    {"name": "lolipop", "image": "assets/lolipop.png"},
    {"name": "mango", "image": "assets/mango.png"},
    {"name": "milk", "image": "assets/milk.png"},
    {"name": "mirror", "image": "assets/mirror.png"},
    {"name": "monkey", "image": "assets/monkey.png"},
    {"name": "moon", "image": "assets/moon.png"},
    {"name": "mouse", "image": "assets/mouse.png"},
    {"name": "nail", "image": "assets/nail.png"},
    {"name": "necklace", "image": "assets/necklace.png"},
    {"name": "nest", "image": "assets/nest.png"},
    {"name": "newspaper", "image": "assets/newspaper.png"},
    {"name": "nut", "image": "assets/nut.png"},
    {"name": "octopus", "image": "assets/octopus.png"},
    {"name": "oil", "image": "assets/oil.png"},
    {"name": "onion", "image": "assets/onion.png"},
    {"name": "orange", "image": "assets/orange.png"},
    {"name": "owl", "image": "assets/owl.png"},
    {"name": "parrot", "image": "assets/parrot.png"},
    {"name": "pen", "image": "assets/pen.png"},
    {"name": "pencil", "image": "assets/pencil.png"},
    {"name": "pizza", "image": "assets/pizza.png"},
    {"name": "potato", "image": "assets/potato.png"},
    {"name": "question", "image": "assets/question.png"},
    {"name": "rabbit", "image": "assets/rabbit.png"},
    {"name": "rainbow", "image": "assets/rainbow.png"},
    {"name": "robot", "image": "assets/robot.png"},
    {"name": "rocket", "image": "assets/rocket.png"},
    {"name": "sheep", "image": "assets/sheep.png"},
    {"name": "snake", "image": "assets/snake.png"},
    {"name": "soap", "image": "assets/soap.png"},
    {"name": "star", "image": "assets/star.png"},
    {"name": "sun", "image": "assets/sun.png"},
    {"name": "table", "image": "assets/table.png"},
    {"name": "tiger", "image": "assets/tiger.png"},
    {"name": "tomato", "image": "assets/tomato.png"},
    {"name": "tree", "image": "assets/tree.png"},
    {"name": "turtle", "image": "assets/turtle.png"},
    {"name": "ufo", "image": "assets/ufo.png"},
    {"name": "umbrella", "image": "assets/umbrella.png"},
    {"name": "unicorn", "image": "assets/unicorn.png"},
    {"name": "vampire", "image": "assets/vampire.png"},
    {"name": "van", "image": "assets/van.png"},
    {"name": "violin", "image": "assets/violin.png"},
    {"name": "volcano", "image": "assets/volcano.png"},
    {"name": "wallet", "image": "assets/wallet.png"},
    {"name": "watch", "image": "assets/watch.png"},
    {"name": "watermelon", "image": "assets/watermelon.png"},
    {"name": "whale", "image": "assets/whale.png"},
    {"name": "xylophone", "image": "assets/xylophone.png"},
    {"name": "yoga", "image": "assets/yoga.png"},
    {"name": "yoyo", "image": "assets/yoyo.png"},
    {"name": "zebra", "image": "assets/zebra.png"},
    {"name": "zoo", "image": "assets/zoo.png"},
]

# === Load all images ===
for obj in object_data:
    try:
        img_path = resource_path(obj["image"])
        img = pygame.image.load(img_path).convert_alpha()
        obj["img"] = pygame.transform.scale(img, (75, 75))
    except Exception as e:
        print(f"Failed to load {obj['image']}: {e}")
        obj["img"] = pygame.Surface((75, 75))
        obj["img"].fill((255, 0, 0))

# === Timer events ===
TIMER_EVENT = pygame.USEREVENT + 1
SPAWN_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(TIMER_EVENT, 1000)
pygame.time.set_timer(SPAWN_EVENT, 800)

# === Game classes ===
class FallingObject:
    def __init__(self, obj):
        self.name = obj["name"]
        self.image = obj["img"]
        self.x = random.randint(0, WIDTH - 50)
        self.y = -50
        self.speed = random.randint(1, 3)
        self.rect = pygame.Rect(self.x, self.y, 50, 50)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y
        screen.blit(self.image, (self.x, self.y))

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 8
        self.rect = pygame.Rect(self.x, self.y, 10, 20)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y
        pygame.draw.rect(screen, (255, 255, 0), self.rect)

class Shooter:
    def __init__(self):
        self.width = 60
        self.height = 20
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - self.height - 10
        self.speed = 6
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, direction):
        if direction == "left":
            self.x = max(0, self.x - self.speed)
        elif direction == "right":
            self.x = min(WIDTH - self.width, self.x + self.speed)
        self.rect.x = self.x

    def draw(self):
        pygame.draw.rect(screen, (255, 128, 130), self.rect)

def draw_text(text, x, y, color=(255, 255, 255)):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def choose_weighted_object(letter):
    matches = [obj for obj in object_data if obj["name"].startswith(letter)]
    non_matches = [obj for obj in object_data if not obj["name"].startswith(letter)]
    return random.choice(matches) if random.random() < 0.5 and matches else random.choice(non_matches or matches)

# === Initialize state ===
shooter = Shooter()
reset_game()

# === Game loop ===
running = True
while running:
    if not game_over:
        screen.fill((138, 183, 255))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: shooter.move("left")
        if keys[pygame.K_RIGHT]: shooter.move("right")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bullets.append(Bullet(shooter.x + shooter.width // 2 - 5, shooter.y))
            elif event.type == TIMER_EVENT:
                time_left -= 1
                if time_left <= 0:
                    game_over = True
            elif event.type == SPAWN_EVENT:
                falling_objects.append(FallingObject(choose_weighted_object(target_letter)))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for obj in falling_objects[:]:
                    if obj.rect.collidepoint((mx, my)):
                        if obj.name.startswith(target_letter):
                            score += 1
                        else:
                            score -= 1
                        falling_objects.remove(obj)
                        break

        # Bullet logic
        for bullet in bullets[:]:
            bullet.update()
            if bullet.y < 0:
                bullets.remove(bullet)
                continue
            for obj in falling_objects[:]:
                if bullet.rect.colliderect(obj.rect):
                    if obj.name.startswith(target_letter):
                        score += 1
                    else:
                        score -= 1
                    falling_objects.remove(obj)
                    bullets.remove(bullet)
                    break

        # Falling object update
        for obj in falling_objects[:]:
            obj.update()
            if obj.y > HEIGHT:
                falling_objects.remove(obj)

        # Draw everything
        shooter.draw()
        for bullet in bullets: bullet.update()
        for obj in falling_objects: obj.update()
        draw_text(f"Target Letter: {target_letter.upper()}", 10, 10)
        draw_text(f"Score: {score}", 10, 50)
        draw_text(f"Time Left: {time_left}", 10, 90)

    else:
        screen.fill((0, 0, 0))
        draw_text("Game Over", WIDTH // 2 - 100, HEIGHT // 2 - 30)
        draw_text(f"Final Score: {score}", WIDTH // 2 - 100, HEIGHT // 2 + 10)
        draw_text("Press R to Restart or Q to Quit", WIDTH // 2 - 150, HEIGHT // 2 + 50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_r:
                    reset_game()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
