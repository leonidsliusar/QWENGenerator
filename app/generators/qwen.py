import os
import torch
from PIL import Image
from diffusers import QwenImageEditPlusPipeline
import gc
gc.collect()
torch.cuda.empty_cache()

pipeline = QwenImageEditPlusPipeline.from_pretrained("Qwen/Qwen-Image-Edit-2509", device_map="balanced", torch_dtype=torch.float16, cache_dir="../../models")
print("pipeline loaded")

pipeline.to('cpu')

pipeline.set_progress_bar_config(disable=None)
image1 = Image.open("girl_7_20_1.png")
# image2 = Image.open("input2.png")
prompt = "Check every part of humans at the image and fixe all low quality or unrealistic parts"
inputs = {
    "image": [image1],
    "prompt": prompt,
    "generator": torch.manual_seed(0),
    "true_cfg_scale": 4.0,
    "negative_prompt": " ",
    "num_inference_steps": 10,
    "guidance_scale": 1,
    "num_images_per_prompt": 1,
}
with torch.inference_mode():
    output = pipeline(**inputs)
    output_image = output.images[0]
    output_image.save("girl_7_20_1_fixed.png")
    print("image saved at", os.path.abspath("output_image_edit_plus.png"))
