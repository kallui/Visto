import replicate
import os
import uuid
import urllib
import ssl
from rembg import remove
ssl._create_default_https_context = ssl._create_unverified_context

model = replicate.models.get("stability-ai/stable-diffusion")
version = model.versions.get("f178fa7a1ae43a9a9af01b833b9d2ecf97b1bcb0acfd2dc5dd04895e042863f1")

def generate_bg_sd(prompt, negative_prompt):
    images = version.predict(prompt=prompt, negative_prompt=negative_prompt, width=1024, height=768)
    return images[0]

def generate_char_sd(prompt):
    images = version.predict(prompt=prompt, width=768, height=768, num_inference_steps=100)
    return images[0]

def save_to_path(url):
    file_name = str(uuid.uuid4())+'.png'
    file_path = os.path.join("generated_images", file_name)
    urllib.request.urlretrieve(url, file_path)
    return file_path

def bg_prompt(prompt):
    return f"""studio ghibli's style, {prompt}"""

def character_prompt(prompt):
    return f"""studio ghibli's style, head to waist, transparent background, {prompt}"""



def rembg_char(file_path):
    file_name = str(uuid.uuid4())+'.png'
    output_path = os.path.join("generated_images", file_name)
    with open(file_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            output = remove(input)
            o.write(output)
    return output_path

def generate_image(prompt, ctype):
    if ctype == 'bg':
        return save_to_path(generate_bg_sd(bg_prompt(prompt), 'animal, people'))
    elif ctype == 'char':
        return rembg_char(save_to_path(generate_char_sd(character_prompt(prompt))))

if __name__ == "__main__":
    p = "The story takes place in a dark, dense forest with tall trees and thick foliage. The ground is littered with crunchy leaves and twigs, and the air is filled with the sounds of chirping birds and buzzing insects. The path twists and turns, and is dotted with small puddles. A bramble bush sits off to the side, with its thorns ready to snag any unsuspecting traveler."
    c = "Little Red Riding Hood was a small girl with long, curly red hair and bright blue eyes. She was wearing a red cape with a hood, a white dress, and a basket of food in her hands."
    c2= "The Big Bad Wolf is a tall, dark figure with sharp eyes and teeth. He is menacing and intimidating, but his voice has a deep, booming tone."
    print(generate_image(c, 'char'))
    print(generate_image(c2, 'char'))