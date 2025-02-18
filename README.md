# Azure Speech to Text

---

## Project Overview
This script automatically converts your audio recordings into written text using Azure's speech service. Simply place your `.wav` files in the `audio_files` folder, and the script will process them for you. Transcribed text files will then appear in the `text_files` folder, making it easy to review and share the results. The audio files have been sourced from [this link](https://www.cs.uic.edu/~i101/SoundFiles/).

---

## Azure Setup
The following is a guide on how to set up the required resource(s) for creating speech enabled apps.

### Create Resource
First create the resource by searching for **Speech services**, then **Create**.
<img width="1591" alt="Screenshot 2025-02-18 at 9 41 39 AM" src="https://github.com/user-attachments/assets/5dd95c73-0646-4cd8-83a9-e3e5f40a912b" />

Then, configure your resource to exist in a **Region** of your choice, using a **Pricing tier** set to **Free F0**. Once done, select **Review + Create**.

<img width="666" alt="Screenshot 2025-02-18 at 9 44 14 AM" src="https://github.com/user-attachments/assets/3b8a49a8-bd25-4017-8161-28e5e0c27e98" />

Then select **Create**. This will begin the deployment process of the resource to the resource group.

<img width="566" alt="Screenshot 2025-02-18 at 9 47 43 AM" src="https://github.com/user-attachments/assets/2eac0a1f-c04e-4a37-ab44-e89b289f47b1" />

### Explore resource
Navigate to the newly deployed resource. We will need the **Keys and endpoint** section for later when using the SDK.

<img width="1250" alt="Screenshot 2025-02-18 at 9 56 14 AM" src="https://github.com/user-attachments/assets/1364789e-f4c1-4a09-a5d0-995d7171dac4" />

---

## Code Steup

Create and activate new virtual environment for the project to install the correct libraries seamlessly.

```bash
python3 -m venv speech_env
```
```bash
source speech_env/bin/activate
```

Now install the required libraries by pasting in the terminal:
```bash
pip install azure-cognitiveservices-speech python-dotenv
```

Lastly, configure the `.env` file in the following way:
```
SPEECH_KEY=your_speech_key
SPEECH_REGION=your_speech_region
```

## Run the Program
Run the program by running
```bash
python3 speech_to_text.py
```

---

## Resources
* [The `SpeechConfig` class](https://learn.microsoft.com/en-us/python/api/azure-cognitiveservices-speech/azure.cognitiveservices.speech.speechconfig?view=azure-python)
