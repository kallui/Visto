import openai
import re

MOODS=['suspenseful music', 'atmospheric music', 'romantic music','comic music','action music','horror music','mystery music','dramatic music','adventure music','tension music','tragic music','comedy music','happy music']
lob=[
    """At one end of Long-Lost Wood, where the Wise Owl watched out for wolves, there
lived a little girl. Whenever the wind whistled she wore a warm, scarlet cloak, so
the animals called her Little Red Riding Hood.
One breezy day her mother said, “You must take this basket of sweet cherry pies
to Grandma’s house. Follow the twisty path, jump the puddles and NEVER speak to
 the Big Bad Wolf.”
    """,
    """
    Little Red Riding Hood skipped away. She followed the twisty path and jumped over the puddles until
she came to a bramble bush. Oh no! A thorn spiked her scarlet cloak and held her tight.
“Keep still, my dear,” boomed a deep voice. “I’ll soon set you free.” Sure enough, the thorn snapped,
the cloak flapped and Little Red Riding Hood swung around.
“Thank you,” she cried, but all she could see was a tall dark shape, standing in the shadows.
“Where are you walking to, all alone?” it asked, in its deep, booming voice. Little Red Riding Hood
thought she caught a glimpse of big eyes and sharp teeth.
“To Grandma’s house,” answered Little Red Riding Hood nervously. “She lives at the other end
of Long-Lost Wood, in the cottage with a green door.” At that moment an owl hooted and the dark
shape was gone, melting into the trees. Little Red Riding Hood didn’t know she had just met the Big
Bad Wolf, so she just wandered along happily, singing tunes to herself.
    """,
    """
    Meanwhile, the hungry wolf raced to Grandma’s house and knocked on her green door. “Let me in,
Grandma,” he said in his squeakiest voice. “I have brought you a basket of sweet cherry pies.”
But did Grandma put on her two pointy shoes and let him in? I’m afraid that she did! Poor
Grandma. And poor Little Red Riding Hood, who reached the cottage far too late.
 “Let me in, Grandma,” she called merrily. “I have brought you a basket of sweet cherry pies.”
“Let yourself in, my dear,” replied a croaky voice. “I am in bed with a nasty cold.” 
    """,
    """
    Little Red Riding Hood lifted the latch and stepped inside. Someone was tucked up in bed wearing
Grandma’s favourite nightcap. The room was dark, so Little Red Riding Hood crept closer.
 “Grandma”, she whispered. “What big eyes you’ve got.”
“All the better to SEE you with,” said the voice. With a sneeze, their nightcap fell off!
    """,

    """
    “Grandma”, gasped Little Red Riding Hood. “What big ears you’ve got.”
“All the better to HEAR you with,” growled the voice.
“Grandma,” gulped Little Red Riding Hood. “What big teeth you’ve got.”
“All the better to EAT you with,” roared the voice.
 “Wait! You’re not my grandma!’ shrieked Little Red Riding Hood.
 The wolf sprang out of the bed, its sharp teeth flashing in the dark. “And that’s why you should
NEVER stop and speak to the Big Bad Wolf!” 
    """,

    """
    Now Little Red Riding Hood saw his fat tummy and she screamed, “Help, help! The Big Bad Wolf has
eaten my Grandma, and he wants to eat me too!”
Luckily, the Wise Owl had already sent for the Storyland Vets. They burst through the green door
with their magic medicine, and in no time the wolf was fast asleep. Inside his tummy, I’m pleased to
say, they found Grandma safe and well, but when they sewed him up again – they ACCIDENTALLY left
her two pointy shoes inside! So now, whenever the Big Bad Wolf feels hungry, those two shoes DANCE and PRANCE until he howls
– and that is why he never even DREAMS of eating a grandma again.
    """
]

def generate_text(prompt, temperature=0.7, max_tokens=500):
    completion = openai.Completion.create(engine="text-davinci-003", temperature=temperature, prompt=prompt, max_tokens=max_tokens)
    return completion.choices[0].text

# prompt: block of text, characters: ['mario', 'luigo', 'cassie']
def dialogue_prompt(prompt, characters):
    character_string=""
    for i, character in enumerate(characters):
        if i != 0:
            character_string += f"    {str(i + 1)}) {character}\n"
        else:
            character_string += f"{str(i + 1)}) {character}\n"
    return f"""Story:

    {prompt}

    Characters:
    Include Characters only if they are mentioned in the story:
    {character_string}

    extract the scene of the story as a dialogues of characters and narrator.
    """

def background_prompt(prompt):
    return f"""
    Story:

    {prompt}

    give a short physical description with no living beings of the general location of where the Story takes place
    """

# prompt: block of text, characters: ['mario', 'luigo', 'cassie']
def characters_prompt(prompt, characters):
    character_string=""
    for i, character in enumerate(characters):
        if i != 0:
            character_string += f"    {str(i + 1)}. {character}\n"
        else:
            character_string += f"{str(i + 1)}. {character}\n"

    return f"""Story:

    {prompt}

    describe these characters' physical description:
    {character_string}"""

def mood_prompt(prompt):
    mood_string=""
    for mood in MOODS:
        mood_string += f'-{mood}\n'
    return f"""Story:

    {prompt}

    From the following list of tones:
    {mood_string}

    Fit the story in on of them:
    """

def standardize(text):
  return text #re.sub('\s+(a|an|and|the)(\s+)', '\2', text.lower())


def extract_words(string):
    pattern = re.compile(r'\n(.*?):')
    matches = pattern.finditer(string)
    words = [match.group(1).strip() for match in matches]
    return words

# Extract characterr names
def extract_characters(raw_dialogues, character_list):
    character_list += list(set(extract_words(raw_dialogues)))
    return character_list

# Extract char descriptions
def extract_characters_desc(raw_character_description, character_map):
    splitted = raw_character_description.split(":")
    for i, line in enumerate(splitted[0:-1]):
        character_map[standardize(line.split(". ")[-1])] = splitted[i+1].split("\n")[0]
    return character_map

def extract_script(raw_dialogues, script):
    splitted = raw_dialogues.split("\n")

    for line in splitted:
        if line != '':
            script.append((line.split(":")[0], line.split(":")[-1].strip()))
    return script

def extract_mood(raw_mood, script):
    simple_mood = raw_mood.strip().lower()
    for mood in MOODS:
        if mood in simple_mood:
            script.append(('mood', mood))
            return script
    script.append('mood', 'generic music')
    return script

def generate_script_and_character_map(lob):
    script = []
    character_map = {}
    character_list = []
    for block in lob:
        raw_bg = generate_text(background_prompt(block))
        script.append(('bg', raw_bg.strip()))
        raw_mood  = generate_text(mood_prompt(block))
        script = extract_mood(raw_mood, script)

        raw_dialogues = generate_text(dialogue_prompt(block, character_list))
        character_list = list(set(extract_characters(raw_dialogues, character_list)))
        if "Narrator" in character_list:
            character_list.remove('Narrator')
        # sets the character description of existsing characters to the very last description
        raw_character_description = generate_text(characters_prompt(block, list(character_list)))
        character_map = extract_characters_desc(raw_character_description, character_map)

        script = extract_script(raw_dialogues, script)
    return script, character_map




if __name__ == "__main__":
    script, character_map = generate_script_and_character_map(lob)
    for line in script:
        print(line)
    print("\n\n8=======================================3\n\n")
    for line2 in character_map:
        print(f"{line2} => {character_map[line2].strip()}")