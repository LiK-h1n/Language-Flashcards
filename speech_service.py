import azure.cognitiveservices.speech as speechsdk

key = "72e9084a5a5b4eaca34aed453ee526ad"
location = "centralindia"


def get_speech(language_code, word):
    speech_config = speechsdk.SpeechConfig(subscription=key, region=location)
    speech_config.speech_synthesis_voice_name = language_code
    file_name = "outputaudio.wav"
    file_config = speechsdk.audio.AudioOutputConfig(filename=file_name)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=file_config)
    audio = speech_synthesizer.speak_text_async(word).get()
    return audio


if __name__ == "__main__":
    from supported_languages import get_language_codes
    from word import get_random_word
    from translator import translate

    language_code = get_language_codes()["Malayalam"]
    word = get_random_word()
    translation = translate(language_code[1], word)
    print(word, translation)

    get_speech(language_code[0], translation)
