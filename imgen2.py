# pip install diffusers torch transformers pipe accelerate

import string
import random
import torch
from diffusers import DiffusionPipeline

pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-base").to('cpu')

def generate_image(prompt, ctype):
    preimg = diffuse(prompt)
    filename = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
    if ctype == 'bg':
        post_img = change_ratio(img)
        post_img.save(f"generated_imgs/{filename}.png")
    elif ctype == 'char':
        post_img = remove_bg(img)
        post_img.save(f"generated_imgs/{filename}.png")
    return  f"generated_imgs/{filename}.png"

def diffuse(prompt):
    img = pipe(prompt).images[0]
    # filename = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
    # image.save(f"generated_imgs/{filename}.png")
    # return f"generated_imgs/{filename}.png"
    return img

# remove background
def remove_bg(img):
    pass

# expand image for background
def change_ratio(img):
import replicate
model = replicate.models.get("stability-ai/stable-diffusion")
version = model.versions.get("27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478")
version.predict(prompt="a 19th century portrait of a wombat gentleman")
['https://replicate.com/api/models/stability-ai/stable-diffusion/files/50fcac81-865d-499e-81ac-49de0cb79264/out-0.png']   



if __name__ == "__main__":
    generate_image("studio ghibli's style, The story takes place in a dark, dense forest with tall trees and thick foliage. The ground is littered with crunchy leaves and twigs, and the air is filled with the sounds of chirping birds and buzzing insects. The path twists and turns, and is dotted with small puddles.", "bg")