import os


from azure.cognitiveservices.speech.audio import AudioOutputConfig
import azure.cognitiveservices.speech as speechsdk

class TextToSpeech:
    @staticmethod
    def synthesize_speech(text: str, signo: str):
        speech_key = "67048847fcb9464cb8123bca34efd37e"
        service_region = "brazilsouth"
        speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
        speech_config.speech_synthesis_voice_name = "pt-BR-BrendaNeural"
        audio_config = AudioOutputConfig(filename="Audios/"+signo + ".wav")
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        result = speech_synthesizer.speak_text(text)
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized for text [{}] and saved to {}.wav".format(text, signo))
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))


    @staticmethod
    def folder(folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                # Read the contents of the text file
                with open(os.path.join(folder_path, filename), "r") as f:
                    text = f.read()

                # Remove the file extension from the filename
                signo = os.path.splitext(filename)[0]

                # Call the synthesize_speech method with the text and filename as arguments
                TextToSpeech.synthesize_speech(text, signo)

