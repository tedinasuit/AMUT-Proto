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
prompt_workflow = json.load(open('workflow_AMUT.json'))

# Use this list to set different prompts
prompt_list = [
    "enormous sprawling fantasy castle stretching as far as the eye can see, blue moat around castle, road leading to gates medieval architecture, turrets, flags, banners, intricate, mad king ludwig, anime style, 8k resolution, dynamic lighting, hyperdetailed, unreal 5, volumetric lighting, photorealistic, detailed background, digital matte painting, grassy field, small gate",
    "another prompt here",
    "yet another prompt",
    "and one more prompt"
]

save_image_node = prompt_workflow["27"]

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
