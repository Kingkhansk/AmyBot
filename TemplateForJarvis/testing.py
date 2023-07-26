# import pygame
# import sys
# import random

# pygame.init()

# # Screen dimensions
# SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

# # Eye position
# eye_x, eye_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3

# # Initialize Pygame window
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Cute Voice Assistant with Blinking Eyes")

# # Load eye images
# eye_open_image = pygame.image.load("eyeopen.png")
# eye_closed_image = pygame.image.load("eyeclose.png")

# # Blinking animation variables
# BLINK_INTERVAL_MIN, BLINK_INTERVAL_MAX = 1000, 5000  # Milliseconds
# next_blink_time = pygame.time.get_ticks() + random.randint(BLINK_INTERVAL_MIN, BLINK_INTERVAL_MAX)
# is_eye_open = True

# def draw_eyes(x, y):
#     eye_offset_x = 30
#     eye_offset_y = 50

#     # Draw left eye
#     screen.blit(eye_open_image if is_eye_open else eye_closed_image, (x - eye_offset_x, y - eye_offset_y))

#     # Draw right eye
#     screen.blit(eye_open_image if is_eye_open else eye_closed_image, (x + eye_offset_x - eye_open_image.get_width(), y - eye_offset_y))

# # Main loop
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_UP]:
#         eye_y = max(eye_y - 5, 0)
#     if keys[pygame.K_DOWN]:
#         eye_y = min(eye_y + 5, SCREEN_HEIGHT)
#     if keys[pygame.K_LEFT]:
#         eye_x = max(eye_x - 5, 0)
#     if keys[pygame.K_RIGHT]:
#         eye_x = min(eye_x + 5, SCREEN_WIDTH)

#     # Check for blinking
#     current_time = pygame.time.get_ticks()
#     if current_time >= next_blink_time:
#         is_eye_open = False
#         # Set the time for the next blink
#         next_blink_time = current_time + random.randint(BLINK_INTERVAL_MIN, BLINK_INTERVAL_MAX)
#     elif current_time >= next_blink_time - 100:  # Eye closing time
#         is_eye_open = False
#     else:
#         is_eye_open = True

#     # Clear the screen
#     screen.fill((255, 255, 255))

#     # Draw eyes
#     draw_eyes(eye_x, eye_y)

#     # Update the display
#     pygame.display.update()
