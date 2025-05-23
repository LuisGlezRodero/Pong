import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 200, 0)

# Configuración de las paletas y la pelota
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_RADIUS = 10
paddle_speed = 6
ball_speed = [4, 4]

# Posiciones iniciales
left_paddle = pygame.Rect(10, (HEIGHT // 2) - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 20, (HEIGHT // 2) - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Puntuaciones
left_score = 0
right_score = 0
font = pygame.font.Font(None, 74)

# Función para dibujar los elementos en la pantalla
def draw():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Mostrar puntuaciones
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (WIDTH // 4, 20))
    screen.blit(right_text, (WIDTH - WIDTH // 4, 20))

    pygame.display.flip()

# Función para manejar la lógica de la pelota
def move_ball():
    global ball_speed, left_score, right_score

    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Rebote en la parte superior e inferior
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Rebote en las paletas
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed[0] = -ball_speed[0]

    # Puntos para los jugadores
    if ball.left <= 0:
        right_score += 1
        reset_ball()
    if ball.right >= WIDTH:
        left_score += 1
        reset_ball()

# Función para reiniciar la pelota
def reset_ball():
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed[0] = -ball_speed[0]

# Función principal del juego
def main():
    global left_paddle, right_paddle

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Controles de las paletas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle.top > 0:
            left_paddle.y -= paddle_speed
        if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
            left_paddle.y += paddle_speed
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= paddle_speed
        if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
            right_paddle.y += paddle_speed

        # Mover la pelota
        move_ball()

        # Dibujar todo
        draw()

        # Controlar la velocidad del juego
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()