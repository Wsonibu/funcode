from time import sleep
import sys

def print_lyrics():
    lines = [
        ("Gave me brain, was so insane ", 0.06),
        ("That I made her my header", 0.04),
        ("If she ever call my phone ", 0.05),
        ("You know I gotta dead her", 0.05),
        ("But I like that girl too much, I wish I never met her", 0.05),
        ("I know it hurts sometimes", 0.07),
        ("But", 0.1),
        ("You'll get over it", 0.07),
        ("You'll find another life to live", 0.06),
        ("I know that you'll get over it", 0.07)
    ]

    delays = [0.06, 0.5, 0.3, 0.1, 0.5, 0.7, 0.5, 1.0, 1.7]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        sleep(delays[i % len(delays)])
        print("")

print_lyrics()
