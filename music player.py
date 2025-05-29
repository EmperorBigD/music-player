import pygame


def match_case(action):
    match action:
        case 'p' : pause_audio()
        case 'u' : unpause_audio()
        case 'r' : restart_audio()
        case 's' : stop_audio()


def play_audio(file_location):

    pygame.mixer.init() # You need to intiate mixer.
    pygame.mixer.music.load(file_location) # Song file should be in same folder as code or full location must be typed.
    pygame.mixer.music.play(-1) # -1 endless loop.

    # NOTE - Initially faced error coz terminal should, keep on runing the program for music to play.

    x = input('enter the action you want to take "p" for pause or "r" for rewind or "s" for stop - ').lower()
    match_case(x)


def pause_audio():

    pygame.mixer.music.pause()

    print("----music paused----")

    x = input('enter the action you want to take "u" for unpause or "r" for rewind or "s" for stop - ').lower()
    match_case(x)


def unpause_audio():

    pygame.mixer.music.unpause()

    print("----music unpaused----")

    x = input('enter the action you want to take "p" for pause or "r" for rewind or "s" for stop - ').lower()
    match_case(x)


def restart_audio():

    pygame.mixer.music.rewind()

    print("----music rewinded----")

    x = input('enter the action you want to take "p" for pause or "u" for unpause or "s" for stop - ').lower()
    match_case(x)


def stop_audio():

    pygame.mixer.music.stop()

    print("----END----")


# Initiate program.


music_file = input('enter file location - ') # Song file should be in same folder as code or full location must be typed.
play_audio(music_file)