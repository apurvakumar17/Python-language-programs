import pygame
import time


names = {
    0: " zero",
    1: " one", 
    2: " two", 
    3: " three", 
    4: " four", 
    5: " five",
    6: " six",
    7: " seven",
    8: " eight",
    9: " nine",
    10: " ten",
    11: " eleven",
    12: " twelve",
    13: " thirteen",
    14: " fourteen",
    15: " fifteen",
    16: " sixteen",
    17: " seventeen",
    18: " eighteen",
    19: " nineteen",
    20: " twenty",
    30: " thirty",
    40: " forty",
    50: " fifty",
    60: " sixty",
    70: " seventy",
    80: " eighty",
    90: " ninety",
    100: " hundred",
    1000: " thousand",
    100000: " lakh",
    10000000: " crore",
    1000000000: " arab",
    100000000000: " kharab",
    10000000000000: " neel"
}

def getWord(n):
    result = "" 
    if (n < 0):
        result = result + "negative" 
        n *= -1 
            
    if (n > 999999999999999):
        return "Please give a number less than 999999999999999" 
    
    if (n >= 10000000000000):
        n1 = n // 10000000000000 
        result = result + getWord(n1) + " neel" 
        n = n % 10000000000000 
        if (n == 0):
            return result 
    
    if (n >= 100000000000):
        n1 = n // 100000000000 
        result = result + getWord(n1) + " kharab" 
        n = n % 100000000000 
        if (n == 0):
            return result 
    
    if (n >= 1000000000):
        n1 = n // 1000000000 
        result = result + getWord(n1) + " arab" 
        n = n % 1000000000 
        if (n == 0):
            return result 
    
    if (n >= 10000000):
        n1 = n // 10000000 
        result = result + getWord(n1) + " crore" 
        n = n % 10000000 
        if (n == 0):
            return result 
    
    if (n >= 100000):
        n1 = n // 100000 
        result = result + getWord(n1) + " lakh" 
        n = n % 100000 
        if (n == 0):
            return result 
    
    if (n >= 1000):
        n2 = n // 1000 
        result = result + getWord(n2) + " thousand" 
        n = n % 1000 
        if (n == 0):
            return result 

    if (n >= 100):
        n3 = n // 100 
        result = result + getWord(n3) + " hundred" 
        n = n % 100 
        if (n == 0):
            return result 

    if (n > 20):
        n4 = n // 10 
        result = result + names.get(n4 * 10) 
        n = n % (n4 * 10) 
        if (n == 0):
            return result 

    if (n <= 20):
        result = result + names.get(n) 
    
    return result 

try:
    num = int(input("Enter the number to covert: ")) 
    word = getWord(num) 
    if (word == None):
        print(num, "Can't Convert!") 
    else:
        print(":->", word) 
except ValueError:
    print("Invalid input! Please enter an integer.")



# Initialize the mixer
pygame.mixer.init()
word = word.lstrip();
playlist2 = word.split(' ');


#songs address list
for i in range(len(playlist2)):
    playlist2[i] = "C:\\Users\\kumar\\Docs n Pics\\Documents\\Github\\Python-language-programs\\Projects\\numbers audio files\\" + playlist2[i] + ".mp3";


# Function to play a song and wait until it finishes
def play_song(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():  # Wait until the song finishes
        time.sleep(1)

# Play each song in sequence
for song in playlist2:
    play_song(song)

print("Audio Playback Completed.")
