import sys
import time

def jalanin_lyrics():
    lirik = [
        ("I'll never let you go again like I did Oh, I used to say", 0.1),
        ("I would never fall in love again until I found her", 0.1),
        ("I said, 'I would never fall unless it's you I fall into'", 0.1),
        ("I was lost within the darkness, but then I found her", 0.1),
        ("I found you", 0.1),
        ("I would never fall in love again until I found her", 0.1),
        ("I said, 'I would never fall unless it's you I fall into'", 0.1),
        ("I was lost within the darkness, but then I found her", 0.1),
        ("I found you", 0.1),8
    ]
    
    delay_list = [2.4, 2.6 , 2.3, 1.7, 21, 2, 2, 2, 1.8 ]

    print("\nUntil I Found You\n")
    time.sleep(1.5)

    for i, (line, char_delay) in enumerate(lirik):
        for karakter in line:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(char_delay)  
        
        time.sleep(delay_list[i])  
        print('')

    print()

jalanin_lyrics()