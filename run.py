from scriptmaker import generate_script_and_character_map
from schemamaker import create_schema
from compositor import write_to_script
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
if __name__ == "__main__":
    script, character_map = generate_script_and_character_map(lob)
    schema = create_schema(script, character_map)
    write_to_script(schema, "jobs/test")

