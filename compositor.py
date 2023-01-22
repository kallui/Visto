import os

videoschema = [
    {
        "bg": "assets/bgcave1.jpg",
        "tone": "assets/swallows.mp3",
        "characters": [
            {
                "name": "Trevor",
                "dialogue": "blah blah blah"
            },
            {
                "name": "Lex",
                "dialogue": "blah blah blah 2"
            }
        ]
    },
    # {
    #     "bg": "pathtoimage",
    #     "tone": "pathtoaudio",
    #     "characters": [
    #         {
    #             "name": "Trevor2",
    #             "dialogue": "blah blah blah"
    #         },
    #         {
    #             "name": "Lex2",
    #             "dialogue": "blah blah blah 2"
    #         }
    #     ]
    # },
]

# Helper functions to get information from specific scene
def get_bg(videoschema, sceneNumber):
    return videoschema[sceneNumber]["bg"]

def get_bg_name(bg_path):
    bg_name = bg_path.split('/')
    return bg_name[len(bg_name) - 1]

def get_tone(videoschema, sceneNumber):
    return videoschema[sceneNumber]["tone"]

def get_tone_name(tone_path):
    tone_name = tone_path.split('/')
    return tone_name[len(tone_name) - 1]

def get_characters(videoschema, sceneNumber):
    return videoschema[sceneNumber]["characters"]

# Main function -> assemble all the scenes into a .rpy script
# returns data -> string containing indentation to paste into .rpy file
def main(videoschema):
    data = '''label start:\n'''

    for i in range(len(videoschema)):
        print(os.path.abspath(os.getcwd()))
        bg_path = get_bg(videoschema, i)
        bg_name = get_bg_name(bg_path)
        os.rename(bg_path, f"assets/Visto/game/images/{bg_name}")
        music_path = get_tone(videoschema, i)
        music_name = get_tone_name(music_path)
        os.rename(music_path, f"assets/Visto/game/audio/{music_name}")
        characters = get_characters(videoschema, i)

        data += f'''     scene {bg_name.split('.')[0]}\n'''
        data += f'''     play music \"audio/{music_name}\"\n'''

        curr_chars = [] # keep track of who is in the scene so that we can hide later
                        # aiming to keep 2 chars in the scene per "round"
        for i in range(len(characters)):
            char_name = characters[i]["name"]
            char_dialog = characters[i]["dialogue"]
            if(i == 0):
                curr_chars.append(char_name)
            if(i == 1):
                curr_chars.append(char_name)
                    
            if(i % 2 == 0):
                if(len(curr_chars) == 2):
                    if(char_name not in curr_chars):
                        data += f'''     hide {curr_chars[0]}\n'''
                        curr_chars[0] = char_name
                data += f'''     show {char_name} at left\n'''
            else:
                if(len(curr_chars) == 2):
                    if(char_name not in curr_chars):
                        data += f'''     hide {curr_chars[1]}\n'''
                        curr_chars[1] = char_name
                data += f'''     show {char_name} at right\n'''
            
            data += f'''     \"{char_name}\" \"{char_dialog}\"\n'''
        
        # clean up to prepare for next scene
        data += f'''     hide {curr_chars[0]}\n'''
        data += f'''     hide {curr_chars[1]}\n'''
        curr_chars = []

        # clean up sound 
        data += f'''     stop music\n'''

    data += '''     return'''

    return data

def write_to_script():
    #f = open(f'{os.path.abspath(os.getcwd())}/script.rpy', "w")
    with open('assets/Visto/game/script.rpy', 'w') as the_file:
        the_file.write(main(videoschema))

write_to_script()

#print(main(videoschema))