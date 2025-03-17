from diffusers import StableDiffusionPipeline
import torch

# Load the Stable Diffusion model
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")  # Requires an NVIDIA GPU

# Ask the user for a text prompt
prompt = input("Enter a text prompt for the video: ")

# Generate an image from the text prompt
image = pipe(prompt).images[0]

# Save the generated image
image.save("generated_image.png")
print("Image saved as generated_image.png")
