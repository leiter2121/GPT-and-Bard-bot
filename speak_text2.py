import boto3
import pygame
import tempfile

# Set your Amazon Polly credentials
polly = boto3.client(
    "polly",
    region_name="YOUR AWS REGION",
    aws_access_key_id="YOUR AWS ACCESS ID",
    aws_secret_access_key="RYOUR AWS SECRET ACCESS KEY"
)

# Define function to speak text using Amazon Polly
def speak_text2(text):
    response = polly.synthesize_speech(
        Text=text,
        Engine='neural',
        OutputFormat='mp3',
        VoiceId='Joanna'
    )
    with tempfile.TemporaryFile() as temp_file:
        temp_file.write(response["AudioStream"].read())
        temp_file.flush()
        temp_file.seek(0)
        pygame.mixer.init()
        pygame.mixer.music.load(temp_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue