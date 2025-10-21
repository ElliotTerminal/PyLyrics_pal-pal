import time
import sys

def print_lyrics():
    lyrics = [
        "Mein ab kyun hosh may aata nahi?",
        "Sukoon yeh dil kyun paata nahi?",
        "Kyun torrun khud se jo thay waadey",
        "Ke an yeh ishq nibhana nahi?",
        "Main morrun tum se jo yeh chehra",
        "Dobara nazar milana nahi",
        "Yeh duniya jane mera dard",
        "Tujhe yeh nazar kyun aata nahi?"
    ]

    delays = [
        0.3, 0.3, 0.4, 0.3, 0.3, 0.3, 0.8,
    ]

    print("I remember YoU : \n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.8)
    
print_lyrics()