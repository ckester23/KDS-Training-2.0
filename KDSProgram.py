"""
Author: Cheyanne Kester
File: Karate-Do Shotokai Belt Test Training

This file contains functionality to facilitate a Shotokai belt test as
    a training exercise.

All terms and grading are based off of the "Commonly Used Terms" poster
    and "Adult Belt Grading Standards" info-sheet. These can
    be found on the American Karate-Do Shotokai website:
        shotokai.org

The [Color]Practice functions only contain the *newest* techniques
    needed for the specified belt, in addition to the
    5 basic stances.

If you wish to do a full training exercise by working on all the
    techniques you have learned so far, start with the Red belt
    exercise, then work your way up.

All the techniques are sorted into these categories:
    Tachikata - Stances
    Tsuki-te  - Hand Techniques / Strikes
    Geri      - Kicks
    Uke       - Blocks
    General   - Other commonly used terms
    Kata      - Kata

This file requires the use of the mp3's in the sound_files folder
"""
from playsound import *
import random
import time


# Defining and sorting all the Terms and mp3 files
# Some terms may not have an mp3 file yet

# Tachikata - Stances
Seiza = "Seiza.mp3"
Hachiji_dachi = "Hachiji_dachi.mp3"
Kiba_dachi = "Kiba_dachi.mp3"
Zenkutsu_dachi = "Zenkutsu.mp3"
Kokutsu_dachi = "Kokutsu_dachi.mp3"
Fudo_dachi = "Fudo_dachi.mp3"

stances = [Seiza, Hachiji_dachi, Kiba_dachi, Zenkutsu_dachi, Kokutsu_dachi, Fudo_dachi]

# Tsuki-te - Hand Techniques
Oi_tsuki = "Oi_tsuki.mp3"
Mae_te_tsuki = "Mae_te_tsuki.mp3"
Gyaku_tsuki = "Gyaku_tsuki.mp3"
Uraken = "Uraken"
Empi = "Empi"
Shomen_uchi = "Shomen Uchi"
Yokomen_uchi = "Yokomen Uchi"
Tetsui = "Tetsui"
Morote_tsuki = "Morote Tsuki"
Yama_tsuki = "Yama Tsuki"

hand_techniques = [Oi_tsuki, Mae_te_tsuki, Gyaku_tsuki, Uraken, Empi, Shomen_uchi,
                   Yokomen_uchi, Tetsui, Morote_tsuki, Yama_tsuki]

# Geri - Kicks
Mae_geri = "Mae_geri.mp3"
Yoko_geri_kekomi = "Yoko_geri_kekomi.mp3"
Yoko_geri_keage = "Keage"
Fumikomi = "Fumi_komi.mp3"
Mawashi_geri = "Mawashi"
Mikazuki_geri = "Mikazuki"
Aori_geri = "Aori"
Nami_gaeshi = "Nami Gaeshi"
Hiza_tsuchi = "Hiza Tsuchi"
Nidan_geri = "Nidan"

kicks = [Mae_geri, Yoko_geri_kekomi, Yoko_geri_keage, Fumikomi, Mawashi_geri, Aori_geri,
         Nami_gaeshi, Hiza_tsuchi, Nidan_geri]

# Uke - Blocks
Gedan_barai = "Gedan_barai.mp3"
Teisho_barai = "teisho_barai.mp3"
Udi_uke = "Udi_uke.mp3"
Uchikomi = "Uchikomi.mp3"
Age_uke = "Age_uke.mp3"
Shuto_uke = "Shuto Uke"
Shuto_barai = "Shuto Barai"
Morote_uke = "Morote Uke"

blocks = [Gedan_barai, Teisho_barai, Udi_uke, Uchikomi, Age_uke, Shuto_uke, Shuto_barai,
          Morote_uke]

# KATA

# Taikyoku
T_Shodan = "Taikyoku_Shodan.mp3"
T_Nidan = "Taikyoku_Nidan.mp3"
T_Sandan = "Taikyoku_Sandan.mp3"



# Heian
H_Shodan = "Heian_Shodan.mp3"
H_Nidan = "Heian_Nidan.mp3"
H_Sandan = "Heian_Sandan.mp3"

# Tekki
Te_Shodan = "Tekki_Shodan.mp3"


# General Training Terms
Tate_tsuki = "Tate_tsuki"
Seiken = "Seiken"
Hiki_te = "Hiki_te.mp3"
Gedan = "Gedan"
Chudan = "Chudan"
Jodan = "Jodan"
Irimi = "Irimi.mp3"
general = [Tate_tsuki, Seiken, Hiki_te, Gedan, Chudan, Jodan]


# Define Based on Belt system (Based on what to train for the Color Belt Testing)

# Red Belt Training
RedStances = [Seiza, Kiba_dachi, Zenkutsu_dachi, Kokutsu_dachi, Fudo_dachi]
RedHands = [Oi_tsuki]
RedKicks = [Mae_geri]
RedBlocks = [Gedan_barai, Udi_uke]
RedGeneral = [Hiki_te]
RedKata = [T_Shodan, T_Nidan, T_Sandan, H_Shodan]
RedOther = []

# Orange Belt Training
OrangeStances = [Seiza, Kiba_dachi, Zenkutsu_dachi, Kokutsu_dachi, Fudo_dachi]
OrangeHands = [Gyaku_tsuki]
OrangeKicks = [Fumikomi, Yoko_geri_kekomi]
OrangeBlocks = [Teisho_barai, Age_uke, Uchikomi]
OrangeGeneral = [Irimi]
OrangeKata = [H_Nidan, H_Sandan, Te_Shodan]


def getRandItem(i_list):
    """ Get a random item from the list """
    n = len(i_list)
    my_ind = random.randint(0, n-1)

    return i_list[my_ind]


def playMP3(mp_str):
    """ Play the mp3 file associated with the string """
    #sound = "sound_files/" + mp_str
    sound = mp_str
    playsound(sound)

    return mp_str


def removeItem(lst, item):
    """ Function to remove an item from the list """
    new_lst = lst
    new_lst.remove(item)
    return new_lst


def StanceExercise(belt):
    """
    Exercise sequence that will go through all the Stances for the specified belt,
    in a random order, and each stance gets exactly one call.
    """

    print("Stances...")
    #playMP3("stances/tachikata.mp3")
    playMP3("tachikata.mp3")

    item = None
    s = None
    if belt == "red":
        s = RedStances
    elif belt == "orange":
        s = OrangeStances

    lst = s
    for i in range(len(s)):
        item = getRandItem(lst)
        lst = removeItem(lst, item)
        #item = "stances/" + item

        if i == 0:
            print(item, "i =", i)
            playMP3(item)
        else:
            time.sleep(2)
            print(item, "i =", i)
            playMP3(item)

    return True


def HandExercise(belt):
    """
    Exercise sequence that will go through all the Strikes for the specified belt,
    in a random order, and each Strike gets exactly one call.
    """

    print("Hand Techniques...")
    #playMP3("hands/tsuki_te.mp3")
    playMP3("tsuki_te.mp3")

    item = None
    h = None
    if belt == "red":
        h = RedHands
    elif belt == "orange":
        h = OrangeHands

    lst = h
    for i in range(len(h)):
        item = getRandItem(lst)
        lst = removeItem(lst, item)
        #item = "hands/" + item

        if i == 0:
            print(item, "i =", i)
            playMP3(item)
        else:
            time.sleep(2)
            print(item, "i =", i)
            playMP3(item)

    return True


def KickExercise(belt):
    """
    Exercise sequence that will go through all the Kicks for the specified belt,
    in a random order, and each kick gets exactly one call.
    """

    print("Kicks...")
    #playMP3("kicks/geri.mp3")
    playMP3("geri.mp3")

    item = None
    k = None
    if belt == "red":
        k = RedKicks
    elif belt == "orange":
        k = OrangeKicks

    lst = k
    for i in range(len(k)):
        item = getRandItem(lst)
        lst = removeItem(lst, item)
        #item = "kicks/" + item

        if i == 0:
            print(item, "i =", i)
            playMP3(item)
        else:
            time.sleep(2)
            print(item, "i =", i)
            playMP3(item)

    return True


def BlockExercise(belt):
    """
    Exercise sequence that will go through all the Blocks for the specified belt,
    in a random order, and each block gets exactly one call.
    """
    print("Blocks...")
    #playMP3("blocks/uke.mp3")
    playMP3("uke.mp3")

    item = None
    b = None
    if belt == "red":
        b = RedBlocks
    elif belt == "orange":
        b = OrangeBlocks

    lst = b
    for i in range(len(b)):
        item = getRandItem(lst)
        lst = removeItem(lst, item)
        #item = "blocks/" + item

        if i == 0:
            print(item, "i =", i)
            playMP3(item)
        else:
            time.sleep(2)
            print(item, "i =", i)
            playMP3(item)

    return True


def GeneralExercise(belt):
    """
    Exercise sequence that will go through all the General terms for the specified belt,
    in a random order, and each term gets exactly one call.
    """

    print("General...")
    #playMP3("general/general.mp3")
    playMP3("general.mp3")

    item = None
    g = None
    if belt == "red":
        g = RedGeneral
    elif belt == "orange":
        g = OrangeGeneral

    lst = g
    for i in range(len(g)):
        item = getRandItem(lst)
        lst = removeItem(lst, item)
        #item = "general/" + item

        if i == 0:
            print(item, "i =", i)
            playMP3(item)
        else:
            time.sleep(2)
            print(item, "i =", i)
            playMP3(item)
    return True


def KataExercise(belt):
    """
    Exercise sequence for the Kata.
    Because of the structured nature of kata, we will not
    perform them in a random order.
    """

    print("Kata...")
    #playMP3("kata/kata.mp3")
    playMP3("kata.mp3")

    item = None
    delay = 0.5
    k = None
    if belt == "red":
        k = RedKata
    elif belt == "orange":
        k = OrangeKata

    for i in range(len(k)):
        item = k[i]
        #item = "kata/" + item

        if i != 0:
            delay = 2

        time.sleep(delay)
        print(item, "i =", i)
        playMP3(item)

    return True


def RedPractice():
    """ Entire Red Belt Training Exercise """

    print("Beginning Red Belt Exercise...")
    #playMP3("other/red.mp3")
    playMP3("red.mp3")

    StanceExercise("red")
    time.sleep(1)
    HandExercise("red")
    time.sleep(1)
    KickExercise("red")
    time.sleep(1)
    BlockExercise("red")
    time.sleep(1)
    GeneralExercise("red")
    time.sleep(1)
    KataExercise("red")
    time.sleep(1)

    print("Exercise Complete, well done")
    #playMP3("other/complete.mp3")
    playMP3("complete.mp3")


def OrangePractice():
    """ Entire Orange Belt Training Exercise """

    print("Beginning Orange Belt Exercise...")
    #playMP3("other/orange.mp3")
    playMP3("orange.mp3")

    StanceExercise("orange")
    time.sleep(1)
    HandExercise("orange")
    time.sleep(1)
    KickExercise("orange")
    time.sleep(1)
    BlockExercise("orange")
    time.sleep(1)
    GeneralExercise("orange")
    time.sleep(1)
    KataExercise("orange")
    time.sleep(1)

    print("Exercise Complete, well done")
    #playMP3("other/complete.mp3")
    playMP3("complete.mp3")


def main():
    print("Please enter the belt color you are training for: ")
    #playMP3("other/input_prompt.mp3")
    playMP3("input_prompt.mp3")
    practice = str(input())

    if practice == "red" or practice == "Red":
        RedPractice()
    elif practice == "orange" or practice == "Orange":
        OrangePractice()

    print("Do you wish to continue?")
    #playMP3("other/wish_continue.mp3")
    playMP3("wish_continue.mp3")
    c_bool = str(input())

    if c_bool == "yes" or c_bool == "Yes":
        main()

    elif c_bool == "no" or c_bool == "No":
        print("Very well, great work today!")
        #playMP3("other/end.mp3")
        playMP3("end.mp3")

    return True


if __name__ == "__main__":
    main()

