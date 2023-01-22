import random

MOOD_AUDIO_MAP ={
    'happy music': [
        "moods_bg_music/happy/2017-04-14_-_Happy_Dreams_-_David_Fesliyan.mp3",
        "moods_bg_music/happy/Doki Doki Literature Club! OST - Okay, Everyone!.mp3",
        "moods_bg_music/happy/Doki Doki Literature Club! OST - Dreams Of Love and Literature.mp3"
    ],
    'suspenseful music': ["moods_bg_music/suspensful/2019-05-01_-_Undercover_Spy_Agent_-_David_Fesliyan.mp3"],
    'atmospheric music': ["moods_bg_music/atmospheric/Interstellar Main Theme - Extra Extended - Soundtrack by  Hans Zimmer.mp3"],
    'romantic music': ["moods_bg_music/romantic/Persona 5 OST 69 - Sweet.mp3"],
    'comic music': ["moods_bg_music/comic/2018-10-06_-_Silly_Chicken_-_David_Fesliyan.mp3"],
    'action music': ["moods_bg_music/action/2019-05-09_-_Escape_Chase_-_David_Fesliyan.mp3"],
    'horror music': ["moods_bg_music/horror/2019-06-18_-_Creepy_Vibes_-_David_Fesliyan.mp3"],
    'mystery music': ["moods_bg_music/mystery/2023-01-04_-_Witness_Testimony_-_www.FesliyanStudios.com.mp3"],
    'dramatic music': ["moods_bg_music/dramatic/Best Dramatic music ever!!.mp3"],
    'adventure music': ["moods_bg_music/adventure/Nate's Theme 3.0.mp3"],
    'tension music': ["moods_bg_music/tension/Tension - Persona 5.mp3"],
    'tragic music': ["moods_bg_music/tragic/Alleycat - Persona 5.mp3"],
    'comedy music': ["moods_bg_music/comedy/2018-10-06_-_Silly_Chicken_-_David_Fesliyan.mp3"],
}

def pick_mood(mood):
    return random.choice(MOOD_AUDIO_MAP[mood])

if __name__ == "__main__":
    print(pick_mood("tension music"))
    print(pick_mood("happy music"))
    print(pick_mood("happy music"))
    print(pick_mood("happy music"))
    print(pick_mood("tension music"))
    print(pick_mood("tension music"))