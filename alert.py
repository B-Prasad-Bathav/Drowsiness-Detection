import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load the sound file (mp3 or wav)
alarm_sound = 'alert.mp3'
pygame.mixer.music.load(alarm_sound)

# Play the sound in a loop (-1 for infinite loop)
pygame.mixer.music.play(loops=-1)

# Wait for the user to stop the sound
input("Press Enter to stop the alarm...")

# Stop the alarm
pygame.mixer.music.stop()