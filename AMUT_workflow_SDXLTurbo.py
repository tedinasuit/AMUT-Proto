import json
from urllib import request

# This function sends a prompt workflow to the specified URL 
# (http://127.0.0.1:8188/prompt) and queues it on the ComfyUI server
# running at that address.
def queue_prompt(prompt_workflow):
    p = {"prompt": prompt_workflow}
    data = json.dumps(p).encode('utf-8')
    req = request.Request("http://127.0.0.1:8188/prompt", data=data)
    request.urlopen(req)

# Read workflow api data from file and convert it into a dictionary 
# Assign it to the variable prompt_workflow
prompt_workflow = {
    "5": {
        "inputs": {
            "width": 512,
            "height": 512,
            "batch_size": 1
        },
        "class_type": "EmptyLatentImage"
    },
    "6": {
        "inputs": {
            "text": "",  # Placeholder for dynamic text
            "clip": [
                "20",
                1
            ]
        },
        "class_type": "CLIPTextEncode"
    },
    "7": {
        "inputs": {
            "text": "text, watermark",
            "clip": [
                "20",
                1
            ]
        },
        "class_type": "CLIPTextEncode"
    },
    "8": {
        "inputs": {
            "samples": [
                "13",
                0
            ],
            "vae": [
                "20",
                2
            ]
        },
        "class_type": "VAEDecode"
    },
    "13": {
        "inputs": {
            "add_noise": True,
            "noise_seed": 0,
            "cfg": 1,
            "model": [
                "20",
                0
            ],
            "positive": [
                "6",
                0
            ],
            "negative": [
                "7",
                0
            ],
            "sampler": [
                "14",
                0
            ],
            "sigmas": [
                "22",
                0
            ],
            "latent_image": [
                "5",
                0
            ]
        },
        "class_type": "SamplerCustom"
    },
    "14": {
        "inputs": {
            "sampler_name": "euler_ancestral"
        },
        "class_type": "KSamplerSelect"
    },
    "20": {
        "inputs": {
            "ckpt_name": "sd_xl_turbo_1.0_fp16.safetensors"
        },
        "class_type": "CheckpointLoaderSimple"
    },
    "22": {
        "inputs": {
            "steps": 1,
            "model": [
                "20",
                0
            ]
        },
        "class_type": "SDTurboScheduler"
    },
    "25": {
        "inputs": {
            "images": [
                "8",
                0
            ]
        },
        "class_type": "PreviewImage"
    }
}

# Use this list to set different prompts
prompt_list = [
    "enormous sprawling fantasy castle stretching as far as the eye can see, blue moat around castle, road leading to gates medieval architecture, turrets, flags, banners, intricate, mad king ludwig, anime style, 8k resolution, dynamic lighting, hyperdetailed, unreal 5, volumetric lighting, photorealistic, detailed background, digital matte painting, grassy field, small gate",
    "another prompt here",
    "yet another prompt",
    "and one more prompt"
]

# Update the prompt in the workflow and queue it
for index, prompt_text in enumerate(prompt_list):
    # Set the text prompt for positive CLIPTextEncode node
    prompt_workflow["6"]["inputs"]["text"] = prompt_text

    # Set filename prefix to be the same as prompt (truncate to first 100 chars if necessary)
    file_prefix = prompt_text[:100]

    # Update the filename prefix in the SaveImage node
    prompt_workflow["25"]["inputs"]["filename_prefix"] = file_prefix

    # Everything set, add the entire workflow to the queue
    queue_prompt(prompt_workflow)
