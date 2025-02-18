import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv


def setup_speech_recogniser(filename: str) -> speechsdk.SpeechRecognizer:
    """Return an Azure speech recogniser."""
    key = os.getenv('SPEECH_KEY')
    region = os.getenv('SPEECH_REGION')

    speech_config = speechsdk.SpeechConfig(
        subscription=key,
        region=region,
        speech_recognition_language='en-AU'
    )

    audio_config = speechsdk.audio.AudioConfig(filename=filename)
    return speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        audio_config=audio_config
    )


def recognise_speech_from_file(filename: str):
    """Return recognised text from a given audio file."""
    recogniser = setup_speech_recogniser(filename)
    result = recogniser.recognize_once_async().get()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print(f"No speech recognised: {result.no_match_details}")
    elif result.reason == speechsdk.ResultReason.Canceled:
        details = result.cancellation_details
        print(f"Speech recognition cancelled: {details.reason}")
        if details.reason == speechsdk.CancellationReason.Error:
            print(f"Error details: {details.error_details}")
            print("Please ensure the speech resource key and region are set correctly.")
    return None


def output_text_to_txt(audio_file_path: str, content: str):
    """Output text to a corresponding .txt file in 'text_files'."""
    base_name = os.path.splitext(os.path.basename(audio_file_path))[0]
    text_file = os.path.join(os.getcwd(), 'text_files', f"{base_name}_text.txt")
    with open(text_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed '{audio_file_path}' -> '{text_file}'")


def main():
    """Load environment variables and process all .wav files in 'audio_files'."""
    load_dotenv()

    audio_dir = os.path.join(os.getcwd(), 'audio_files')

    # Process each audio file (assumed all .wav)
    for file_name in os.listdir(audio_dir):
        audio_path = os.path.join(audio_dir, file_name)
        recognised_text = recognise_speech_from_file(audio_path)
        if recognised_text:
            output_text_to_txt(audio_path, recognised_text)
        else:
            print(f"No usable speech recognised from '{file_name}'.")


if __name__ == '__main__':
    main()
