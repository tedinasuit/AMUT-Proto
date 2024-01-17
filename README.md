# AMUT Prototype

## Introduction

The AMUT (Advanced Marketing User Testing) prototype is a web application that utilizes ComfyUI and the SDXL Turbo model for automatically generating new iterations based on user feedback.

## Hardware Requirements

AMUT requires an Nvidia RTX series GPU. Older Nvidia GPUs from the GTX series work, but far from optimally.

- Minimum: RTX 2060
- Recommended: RTX 3080
- Optimal: RTX 4080
- Free space required: 15 GB

## Installation

To run the prototype, follow these steps:

1. **Download the latest AMUT-Proto release:**
   - Donwload the [latest AMUT Prototype release here.](https://github.com/tedinasuit/AMUT-Proto/releases/tag/Latest)

3. **Download ComfyUI:**
   - Download the ComfyUI repository from [here](https://github.com/comfyanonymous/ComfyUI/releases/tag/latest).

4. **Place ComfyUI in the AMUT-Proto folder:**
   - Extract the ComfyUI repository.
   - Move the extracted `ComfyUI_windows_portable` folder into the `AMUT-Proto` folder.

5. **Download SDXL Turbo Checkpoint:**
   - Download the SDXL Turbo checkpoint file "sd_xl_turbo_1.0_fp16.safetensors" from [this link](https://huggingface.co/stabilityai/sdxl-turbo/blob/main/sd_xl_turbo_1.0_fp16.safetensors).
   - Place the downloaded checkpoint file in the `AMUT-Proto\ComfyUI_windows_portable\ComfyUI\models\checkpoints` folder.

6. **Set Up Python Environment:**
   - Make sure you have Python installed on your system.
   - If you are not sure on whether you have it installed, [you can download it from the Microsoft Store here.](https://apps.microsoft.com/detail/9P7QFQMJRFP7?hl=en-us&gl=US)

## Usage (Nvidia GPU)

1. **Run the 'Launch_AMUT' batch file:**
   - Navigate to the `AMUT-Proto` folder in your terminal.
   - Find the 'Launch_AMUT.bat' file and run it.

2. **Access the Prototype:**
   - Use the "Start" button to begin generating images based on prompts.
   - Click on images to add prompts and see the newest generated image.

3. **Reset and Clear Files:**
   - Use the "Reset" button to stop image generation and clear the output folder.

![image](https://github.com/tedinasuit/AMUT-Proto/assets/73829267/f3e74094-6251-475d-9f4a-ef74d1e32727)


## Troubleshooting

- If you encounter any issues, make sure you have followed the installation steps correctly and that the required files are in their designated locations.

## Acknowledgments

- This prototype utilizes ComfyUI and the SDXL Turbo model. Special thanks to the respective authors and contributors of these projects.
