import os
import shutil

SCHEMA = [{'characters': [{'name': 'Narrator', 'dialogue': 'At one end of Long-Lost Wood, where the Wise Owl watched out for wolves, there lived a little girl. Whenever the wind whistled she wore a warm, scarlet cloak, so the animals called her Little Red Riding Hood.'}, {'name': 'Mother', 'dialogue': 'You must take this basket of sweet cherry pies to Grandma’s house. Follow the twisty path, jump the puddles and NEVER speak to the Big Bad Wolf.', 'image': 'generated_images/8949705d-36f3-40a2-aecf-16058c8b34e0.png'}, {'name': 'Little Red Riding Hood', 'dialogue': 'Yes, mother.', 'image': 'generated_images/ad09fe3d-5813-41f8-bacc-161ba02f16b7.png'}], 'bg': 'generated_images/c41ba971-7f78-43f9-bf08-bb065786602d.png', 'tone': 'moods_bg_music/dramatic/Best Dramatic music ever!!.mp3'}, {'characters': [{'name': 'Narrator', 'dialogue': 'Little Red Riding Hood skipped away. She followed the twisty path and jumped over the puddles until she came to a bramble bush.'}, {'name': 'Little Red Riding Hood', 'dialogue': 'Oh no!', 'image': 'generated_images/ad09fe3d-5813-41f8-bacc-161ba02f16b7.png'}, {'name': 'Narrator', 'dialogue': 'A thorn spiked her scarlet cloak and held her tight.'}, {'name': 'Big Bad Wolf', 'dialogue': "Keep still, my dear. I'll soon set you free.", 'image': 'generated_images/fb08dd89-eafe-473a-b1a6-8fdc05295c18.png'}, {'name': 'Narrator', 'dialogue': 'Sure enough, the thorn snapped, the cloak flapped and Little Red Riding Hood swung around.'}, {'name': 'Little Red Riding Hood', 'dialogue': 'Thank you!', 'image': 'generated_images/ad09fe3d-5813-41f8-bacc-161ba02f16b7.png'}, {'name': 'Narrator', 'dialogue': 'All she could see was a tall dark shape, standing in the shadows.'}, {'name': 'Big Bad Wolf', 'dialogue': 'Where are you walking to, all alone?', 'image': 'generated_images/fb08dd89-eafe-473a-b1a6-8fdc05295c18.png'}, {'name': 'Little Red Riding Hood', 'dialogue': "To Grandma's house. She lives at the other end of Long-Lost Wood, in the cottage with a green door.", 'image': 'generated_images/ad09fe3d-5813-41f8-bacc-161ba02f16b7.png'}, {'name': 'Narrator', 'dialogue': "At that moment an owl hooted and the dark shape was gone, melting into the trees. Little Red Riding Hood didn't know she had just met the Big Bad Wolf, so she just wandered along happily, singing tunes to herself."}], 'bg': 'generated_images/19126d62-8f16-4741-997c-a7ae0e652909.png', 'tone': 'moods_bg_music/suspensful/2019-05-01_-_Undercover_Spy_Agent_-_David_Fesliyan.mp3'}, {'characters': [{'name': 'Narrator', 'dialogue': 'Meanwhile, the hungry wolf raced to Grandma’s house and knocked on her green door.'}, {'name': 'Big Bad Wolf', 'dialogue': '“Let me in, Grandma,” he said in his squeakiest voice. “I have brought you a basket of sweet cherry pies.”', 'image': 'generated_images/fb08dd89-eafe-473a-b1a6-8fdc05295c18.png'}, {'name': 'Narrator', 'dialogue': 'But did Grandma put on her two pointy shoes and let him in? I’m afraid that she did! Poor Grandma. And poor Little Red Riding Hood, who reached the cottage far too late.'}, {'name': 'Little Red Riding Hood', 'dialogue': '“Let me in, Grandma,” she called merrily. “I have brought you a basket of sweet cherry pies.”', 'image': 'generated_images/ad09fe3d-5813-41f8-bacc-161ba02f16b7.png'}, {'name': 'Grandma', 'dialogue': '“Let yourself in, my dear,” replied a croaky voice. “I am in bed with a nasty cold.”', 'image': 'generated_images/d140f5ee-eb0c-46f1-b39f-c1570deb729f.png'}], 'bg': 'generated_images/b1b6f5b1-ccf9-4131-a7c3-858bc195acad.png', 'tone': 'moods_bg_music/mystery/2023-01-04_-_Witness_Testimony_-_www.FesliyanStudios.com.mp3'}, {'characters': [{'name': 'Narrator', 'dialogue': 'Little Red Riding Hood lifted the latch and stepped inside. Someone was tucked up in bed wearing Grandma’s favourite nightcap. The room was dark, so Little Red Riding Hood crept closer.'}, {'name': 'Little Red Riding Hood', 'dialogue': '“Grandma”, she whispered. “What big eyes you’ve got.”', 'image': 'generated_images/ad09fe3d-5813-41f8-bacc-161ba02f16b7.png'}, {'name': 'Grandma', 'dialogue': '“All the better to SEE you with,” said the voice.', 'image': 'generated_images/d140f5ee-eb0c-46f1-b39f-c1570deb729f.png'}, {'name': 'Narrator', 'dialogue': 'With a sneeze, their nightcap fell off!'}], 'bg': 'generated_images/86a25c1e-2db0-4e74-a1cd-7e53a918a662.png', 'tone': 'moods_bg_music/suspensful/2019-05-01_-_Undercover_Spy_Agent_-_David_Fesliyan.mp3'}, {'characters': [{'name': 'Narrator', 'dialogue': '"Grandma," gasped Little Red Riding Hood. "What big ears you\'ve got."'}, {'name': 'Little Red Riding Hood', 'dialogue': '"Grandma, what big teeth you\'ve got."', 'image': 'generated_images/ad09fe3d-5813-41f8-bacc-161ba02f16b7.png'}, {'name': 'Big Bad Wolf', 'dialogue': '"All the better to HEAR you with," growled the voice. "All the better to EAT you with," roared the voice.', 'image': 'generated_images/fb08dd89-eafe-473a-b1a6-8fdc05295c18.png'}, {'name': 'Little Red Riding Hood', 'dialogue': '"Wait! You\'re not my Grandma!"', 'image': 'generated_images/ad09fe3d-5813-41f8-bacc-161ba02f16b7.png'}, {'name': 'Narrator', 'dialogue': 'The wolf sprang out of the bed, its sharp teeth flashing in the dark. "And that\'s why you should NEVER stop and speak to the Big Bad Wolf!"'}], 'bg': 'generated_images/cf9ac2fd-1138-4a0b-816b-de3bb0b2bf18.png', 'tone': 'moods_bg_music/horror/2019-06-18_-_Creepy_Vibes_-_David_Fesliyan.mp3'}, {'characters': [{'name': 'Narrator', 'dialogue': 'Now Little Red Riding Hood saw his fat tummy and she screamed, “Help, help! The Big Bad Wolf has eaten my Grandma, and he wants to eat me too!”'}, {'name': 'Little Red Riding Hood', 'dialogue': 'Help, help! The Big Bad Wolf has eaten my Grandma, and he wants to eat me too!', 'image': 'generated_images/ad09fe3d-5813-41f8-bacc-161ba02f16b7.png'}, {'name': 'Narrator', 'dialogue': 'Luckily, the Wise Owl had already sent for the Storyland Vets. They burst through the green door with their magic medicine, and in no time the wolf was fast asleep.'}, {'name': 'Narrator', 'dialogue': 'Inside his tummy, I’m pleased to say, they found Grandma safe and well, but when they sewed him up again – they ACCIDENTALLY left her two pointy shoes inside!'}, {'name': 'Mother', 'dialogue': 'Thank goodness Grandma is safe!', 'image': 'generated_images/8949705d-36f3-40a2-aecf-16058c8b34e0.png'}, {'name': 'Narrator', 'dialogue': 'So now, whenever the Big Bad Wolf feels hungry, those two shoes DANCE and PRANCE until he howls – and that is why he never even DREAMS of eating a grandma again.'}], 'bg': 'generated_images/92b365ee-2ed0-4d4a-83f6-7dee83815e6e.png', 'tone': "moods_bg_music/adventure/Nate's Theme 3.0.mp3"}]

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
        bg_path = get_bg(videoschema, i)
        bg_name = get_bg_name(bg_path)
        shutil.copyfile(bg_path, f"assets/Visto/game/images/{bg_name}")

        music_path = get_tone(videoschema, i)
        music_name = get_tone_name(music_path)
        shutil.copyfile(music_path, f"assets/Visto/game/audio/{music_name}")

        characters = get_characters(videoschema, i)

        data += f'''     scene {bg_name.split('.')[0]}:\n'''
        data += f'''        xzoom 2.0\n'''
        data += f'''        yzoom 1.5\n'''
        data += f'''     play music \"audio/{music_name}\"\n'''

        curr_chars = [] # keep track of who is in the scene so that we can hide later
                        # aiming to keep 2 chars in the scene per "round"
        for i in range(len(characters)):
            #get char image, name and dialog (free of quotation marks)
            char_name = characters[i]["name"].replace('"', '')
            char_dialog = characters[i]["dialogue"].replace('"', '')
            if(char_name == "Narrator"):
                data += f'''     \"{char_dialog}\"\n'''
                continue
            file = characters[i]["image"].split("/")[-1]
            # fromv = characters[i]["image"]
            # werks = characters[i]["name"]
            # print(f"{i}) {werks}: {fromv} => assets/Visto/game/images/{file}")
            shutil.copyfile(characters[i]["image"], f"assets/Visto/game/images/{file}")

            if(len(curr_chars) == 0):
                curr_chars.append(char_name)
            if(len(curr_chars) == 1):
                curr_chars.append(char_name)

            if(i % 2 == 0):
                if(len(curr_chars) == 2):
                    if(char_name not in curr_chars):
                        data += f'''     hide {curr_chars[0]}\n'''
                        curr_chars[0] = char_name
                data += f'''     show {characters[i]["image"].split('/')[-1].split('.')[0]} at left\n'''
            else:
                if(len(curr_chars) == 2):
                    if(char_name not in curr_chars):
                        data += f'''     hide {curr_chars[1]}\n'''
                        curr_chars[1] = char_name
                data += f'''     show {characters[i]["image"].split('/')[-1].split('.')[0]} at right\n'''

            data += f'''     \"{char_name}\" \"{char_dialog}\"\n'''

        # clean up to prepare for next scene
        data += f'''     hide {curr_chars[0]}\n'''
        data += f'''     hide {curr_chars[1]}\n'''
        curr_chars = []

        # clean up sound
        data += f'''     stop music\n'''

    data += '''     return'''

    return data

def write_to_script(videoschema, output_path):
    #f = open(f'{os.path.abspath(os.getcwd())}/script.rpy', "w")
    with open('assets/Visto/game/script.rpy', 'w') as the_file:
        the_file.write(main(videoschema))
    shutil.make_archive(output_path+"/game", 'zip', 'assets')
    return output_path


if __name__ == '__main__':
    write_to_script(SCHEMA, "public/test")