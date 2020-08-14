import pyaudio
import math
import struct
import wave
import time
import os

#recognize.py
import requests
import json

import simpleaudio as sa
import random 

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import PatternMatchingEventHandler


# Wit speech API endpoint
API_ENDPOINT = 'https://api.wit.ai/speech'

# Wit.ai api access token
wit_access_token = 'VXKDLST6NDRASUJ4PZFZTF332563FBNY'

owd = os.getcwd()

global PAUSED
PAUSED = False


class MyHandler(PatternMatchingEventHandler):
    patterns = ["*.wav", "*/test.txt"]

    store = ""
    III_A_count = 0
    III_B_count = 0
    III_C_count = 0
    III_D_count = 0
    III_E_count = 0
    III_F_count = 0

    def __init__(self, patterns=None, ignore_patterns=None,
                ignore_directories=True, case_sensitive=False):
        super(PatternMatchingEventHandler, self).__init__()

        self._patterns = patterns
        self._ignore_patterns = ignore_patterns
        self._ignore_directories = ignore_directories
        self._case_sensitive = case_sensitive

    def read_audio(self, WAVE_FILENAME):
        # function to read audio(wav) file
        with open(WAVE_FILENAME, 'rb') as f:
            audio = f.read()
        return audio
        
    def on_modified(self, event):
        
        try:
            print(f'event type: {event.event_type}  path : {event.src_path}\n')
            
            # get a sample of the audio that we recorded before. 
            audio = self.read_audio(os.path.join(owd,'Audio','filename.wav'))

            # defining headers for HTTP request
            headers = {'authorization': 'Bearer ' + wit_access_token,
                       'Content-Type': 'audio/wav'}

            #Send the request as post request and the audio as data
            resp = requests.post(API_ENDPOINT, headers = headers,
                                     data = audio)

            #Get the text
            wit_response = json.loads(resp.content)
            print(wit_response)

            
            if wit_response:
                # if there is SOMETHING picked up by wit.ai
                if 'intents' in wit_response: 

                    if wit_response['intents'] and wit_response['intents'][0]['confidence']:

                        if wit_response['intents'][0]['confidence']>0.6:

                            # V_smalltalk

                            if wit_response['intents'][0]['name'] == 'welcome':
                                
                                if 'welcome_who:welcome_who' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','V_smalltalk','V-A','V-A_2'))), os.path.join(owd,'ba_timemachine_audio','V_smalltalk','V-A','V-A_2'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','V_smalltalk','V-A','V-A_2'))), os.path.join(owd,'ba_timemachine_text','V_smalltalk','V-A','V-A_2'))
                                else:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','V_smalltalk','V-A','V-A_1'))), os.path.join(owd,'ba_timemachine_audio','V_smalltalk','V-A','V-A_1'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','V_smalltalk','V-A','V-A_1'))), os.path.join(owd,'ba_timemachine_text','V_smalltalk','V-A','V-A_1'))


                            elif wit_response['intents'][0]['name'] == 'current_mood':                            
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','V_smalltalk','V-B','V-B_1'))), os.path.join(owd,'ba_timemachine_audio','V_smalltalk','V-B','V-B_1'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','V_smalltalk','V-B','V-B_1'))), os.path.join(owd,'ba_timemachine_text','V_smalltalk','V-B','V-B_1'))

                            elif wit_response['intents'][0]['name'] == 'goodbye':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','V_smalltalk','V-C','V-C_1'))), os.path.join(owd,'ba_timemachine_audio','V_smalltalk','V-C','V-C_1'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','V_smalltalk','V-C','V-C_1'))), os.path.join(owd,'ba_timemachine_text','V_smalltalk','V-C','V-C_1'))

                            elif wit_response['intents'][0]['name'] == 'alligator':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','V_smalltalk','V-D','V-D_1'))), os.path.join(owd,'ba_timemachine_audio','V_smalltalk','V-D','V-D_1'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','V_smalltalk','V-D','V-D_1'))), os.path.join(owd,'ba_timemachine_text','V_smalltalk','V-D','V-D_1'))

                            elif wit_response['intents'][0]['name'] == 'current_date':
                                
                                if 'current_date:current_year' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','V_smalltalk','V-E','V-E_1'))), os.path.join(owd,'ba_timemachine_audio','V_smalltalk','V-E','V-E_1'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','V_smalltalk','V-E','V-E_1'))), os.path.join(owd,'ba_timemachine_text','V_smalltalk','V-E','V-E_1'))
                                elif 'current_date:current_day' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','V_smalltalk','V-E','V-E_2'))), os.path.join(owd,'ba_timemachine_audio','V_smalltalk','V-E','V-E_2'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','V_smalltalk','V-E','V-E_2'))), os.path.join(owd,'ba_timemachine_text','V_smalltalk','V-E','V-E_2'))
                                elif 'current_date:exact_date' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','V_smalltalk','V-E','V-E_3'))), os.path.join(owd,'ba_timemachine_audio','V_smalltalk','V-E','V-E_3'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','V_smalltalk','V-E','V-E_3'))), os.path.join(owd,'ba_timemachine_text','V_smalltalk','V-E','V-E_3'))

                            # II_hardfacts
                                
                            elif wit_response['intents'][0]['name'] == 'own_name':
                                
                                if 'own_name:own_name_only' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-A','II-A_1'))), os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-A','II-A_1'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-A','II-A_1'))), os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-A','II-A_1'))
                                elif 'own_name:own_surname' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-A','II-A_2'))), os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-A','II-A_2'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-A','II-A_2'))), os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-A','II-A_2'))
                                elif 'own_name:whole_name' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-A','II-A_3'))), os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-A','II-A_3'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-A','II-A_3'))), os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-A','II-A_3'))
                                else:
                                    # not sure about the role
                                    # play a random file from own_name
                                    own_name_folder = random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-A')))

                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-A',own_name_folder))), os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-A',own_name_folder))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-A',own_name_folder))), os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-A',own_name_folder))

                            elif wit_response['intents'][0]['name'] == 'age_of_person':

                                if 'age_of_person:birthdate' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-B','II-B_1'))), os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-B','II-B_1'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-B','II-B_1'))), os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-B','II-B_1'))
                                elif 'age_of_person:age' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-B','II-B_2'))), os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-B','II-B_2'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-B','II-B_2'))), os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-B','II-B_2'))
                                else:
                                    age_of_person_folder = random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-B')))

                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-B',age_of_person_folder))), os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-B',age_of_person_folder))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-B',age_of_person_folder))), os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-B',age_of_person_folder))

                            elif wit_response['intents'][0]['name'] == 'own_gender':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-C'))), os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-C'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-C'))), os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-C'))

                            elif wit_response['intents'][0]['name'] == 'own_birthplace':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-D'))), os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-D'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-D'))), os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-D'))

                            elif wit_response['intents'][0]['name'] == 'residence_of_person':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-E'))), os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-E'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-E'))), os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-E'))

                            elif wit_response['intents'][0]['name'] == 'own_religion':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-F'))), os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-F'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-F'))), os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-F'))

                            elif wit_response['intents'][0]['name'] == 'school_visited':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-G'))), os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-G'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-G'))), os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-G'))

                            elif wit_response['intents'][0]['name'] == 'education_youth':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-H'))), os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-H'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-H'))), os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-H'))

                            elif wit_response['intents'][0]['name'] == 'own_parents':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-I'))), os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-I'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-I'))), os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-I'))

                            elif wit_response['intents'][0]['name'] == 'father_occup':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-J'))), os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-J'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-J'))), os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-J'))

                            elif wit_response['intents'][0]['name'] == 'mother_occup':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-L'))), os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-L'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-L'))), os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-L'))

                            elif wit_response['intents'][0]['name'] == 'own_siblings':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-N'))), os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-N'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-N'))), os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-N'))

                            elif wit_response['intents'][0]['name'] == 'siblings_occup':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-O'))), os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-O'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-O'))), os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-O'))

                            elif wit_response['intents'][0]['name'] == 'wealth_youth':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-P'))), os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-P'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-P'))), os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-P'))

                            elif wit_response['intents'][0]['name'] == 'friends_youth':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-Q'))), os.path.join(owd,'ba_timemachine_audio','II_hardfacts','II-Q'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-Q'))), os.path.join(owd,'ba_timemachine_text','II_hardfacts','II-Q'))

                            # semi-fluid facts
                            
                            elif wit_response['intents'][0]['name'] == 'political_mind':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','VI_semifluidfacts','VI-A'))), os.path.join(owd,'ba_timemachine_audio','VI_semifluidfacts','VI-A'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','VI_semifluidfacts','VI-A'))), os.path.join(owd,'ba_timemachine_text','VI_semifluidfacts','VI-A'))

                            elif wit_response['intents'][0]['name'] == 'religious_mind':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','VI_semifluidfacts','VI-B'))), os.path.join(owd,'ba_timemachine_audio','VI_semifluidfacts','VI-B'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','VI_semifluidfacts','VI-B'))), os.path.join(owd,'ba_timemachine_text','VI_semifluidfacts','VI-B'))

                            elif wit_response['intents'][0]['name'] == 'economic_mind':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','VI_semifluidfacts','VI-C'))), os.path.join(owd,'ba_timemachine_audio','VI_semifluidfacts','VI-C'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','VI_semifluidfacts','VI-C'))), os.path.join(owd,'ba_timemachine_text','VI_semifluidfacts','VI-C'))
                            


                            # IV_wisdom

                            elif wit_response['intents'][0]['name'] == 'wis_general':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-A'))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-A'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-A'))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-A'))

                            elif wit_response['intents'][0]['name'] == 'wis_finance':                               

                                if 'wis_fi_longlife:wis_fi_longlife' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-B','IV-B_1'))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-B','IV-B_1'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-B','IV-B_1'))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-B','IV-B_1'))
                                elif 'wis_fi_earn:wis_fi_earn' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-B','IV-B_2'))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-B','IV-B_2'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-B','IV-B_2'))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-B','IV-B_2'))
                                elif 'wis_fi_gender:wis_fi_gender' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-B','IV-B_3'))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-B','IV-B_3'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-B','IV-B_3'))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-B','IV-B_3'))
                                else:
                                    wis_finance_folder = random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-B')))

                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-B',wis_finance_folder))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-B',wis_finance_folder))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-B',wis_finance_folder))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-B',wis_finance_folder))

                            elif wit_response['intents'][0]['name'] == 'wis_work':

                                if 'wis_wo_fun:wis_wo_fun' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-C','IV-C_1'))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-C','IV-C_1'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-C','IV-C_1'))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-C','IV-C_1'))
                                elif 'wis_wo_flex:wis_wo_flex' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-C','IV-C_2'))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-C','IV-C_2'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-C','IV-C_2'))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-C','IV-C_2'))
                                elif 'wis_wo_skills:wis_wo_skills' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-C','IV-C_3'))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-C','IV-C_3'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-C','IV-C_3'))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-C','IV-C_3'))
                                elif 'wis_wo_new:wis_wo_new' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-C','IV-C_4'))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-C','IV-C_4'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-C','IV-C_4'))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-C','IV-C_4'))
                                elif 'wis_wo_soft:wis_wo_soft' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-C','IV-C_5'))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-C','IV-C_5'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-C','IV-C_5'))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-C','IV-C_5'))
                                else:
                                    wis_work_folder = random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-C')))

                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-C',wis_work_folder))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-C',wis_work_folder))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-C',wis_work_folder))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-C',wis_work_folder))                                 

                            elif wit_response['intents'][0]['name'] == 'wis_learning':

                                if 'wis_le_refresh:wis_le_refresh' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-D','IV-D_1'))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-D','IV-D_1'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-D','IV-D_1'))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-D','IV-D_1'))
                                elif 'wis_le_newstart:wis_le_newstart' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-D','IV-D_2'))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-D','IV-D_2'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-D','IV-D_2'))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-D','IV-D_2'))
                                elif 'wis_le_active:wis_le_active' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-D','IV-D_3'))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-D','IV-D_3'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-D','IV-D_3'))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-D','IV-D_3'))
                                elif 'wis_le_agemix:wis_le_agemix' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-D','IV-D_4'))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-D','IV-D_4'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-D','IV-D_4'))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-D','IV-D_4'))
                                else:
                                    wis_learning_folder = random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-D')))

                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-D',wis_learning_folder))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-D',wis_learning_folder))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-D',wis_learning_folder))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-D',wis_learning_folder))

                            elif wit_response['intents'][0]['name'] == 'wis_relations':

                                if 'wis_re_longfriends:wis_re_longfriends' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-E','IV-E_1'))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-E','IV-E_1'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-E','IV-E_1'))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-E','IV-E_1'))
                                elif 'wis_re_multigen:wis_re_multigen' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-E','IV-E_2'))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-E','IV-E_2'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-E','IV-E_2'))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-E','IV-E_2'))
                                else:
                                    wis_relations_folder = random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-E')))

                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-E',wis_relations_folder))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-E',wis_relations_folder))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-E',wis_relations_folder))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-E',wis_relations_folder))

                            elif wit_response['intents'][0]['name'] == 'wis_family':

                                if 'wis_fa_childs:wis_fa_childs' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-F','IV-F_1'))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-F','IV-F_1'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-F','IV-F_1'))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-F','IV-F_1'))
                                elif 'wis_fa_balance:wis_fa_balance' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-F','IV-F_2'))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-F','IV-F_2'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-F','IV-F_2'))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-F','IV-F_2'))
                                elif 'wis_fa_eyelevel:wis_fa_eyelevel' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-F','IV-F_3'))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-F','IV-F_3'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-F','IV-F_3'))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-F','IV-F_3'))
                                elif 'wis_fa_marriage:wis_fa_marriage' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-F','IV-F_4'))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-F','IV-F_4'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-F','IV-F_4'))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-F','IV-F_4'))
                                elif 'wis_fa_support:wis_fa_support' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-F','IV-F_5'))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-F','IV-F_5'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-F','IV-F_5'))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-F','IV-F_5'))
                                else:
                                    wis_family_folder = random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-F')))

                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-F',wis_family_folder))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-F',wis_family_folder))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-F',wis_family_folder))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-F',wis_family_folder))

                            elif wit_response['intents'][0]['name'] == 'wis_recreate':

                                if 'w_re_general:w_re_general' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-G','IV-G_1'))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-G','IV-G_1'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-G','IV-G_1'))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-G','IV-G_1'))
                                elif 'w_re_importance:w_re_importance' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-G','IV-G_2'))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-G','IV-G_2'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-G','IV-G_2'))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-G','IV-G_2'))
                                else:
                                    wis_recreate_folder = random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-G')))

                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-G',wis_recreate_folder))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-G',wis_recreate_folder))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-G',wis_recreate_folder))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-G',wis_recreate_folder))

                            ## wis_health?

                            elif wit_response['intents'][0]['name'] == 'wis_owning':

                                if 'wis_own_change:wis_own_change' in wit_response['entities']:
                                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-I','IV-I_1'))), os.path.join(owd,'ba_timemachine_audio','IV_wisdom','IV-I','IV-I_1'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-I','IV-I_1'))), os.path.join(owd,'ba_timemachine_text','IV_wisdom','IV-I','IV-I_1'))
                            
                            
                            # I_general

                            elif wit_response['intents'][0]['name'] == 'agreement':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-A'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-A'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-A'))), os.path.join(owd,'ba_timemachine_text','I_general','I-A'))

                            elif wit_response['intents'][0]['name'] == 'disagreement':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-B'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-B'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-B'))), os.path.join(owd,'ba_timemachine_text','I_general','I-B'))

                            elif wit_response['intents'][0]['name'] == 'oos_general':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-C'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-C'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-C'))), os.path.join(owd,'ba_timemachine_text','I_general','I-C'))

                            elif wit_response['intents'][0]['name'] == 'oos_ridiculous':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-D'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-D'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-D'))), os.path.join(owd,'ba_timemachine_text','I_general','I-D'))

                            elif wit_response['intents'][0]['name'] == 'version_confusion':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-H'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-H'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-H'))), os.path.join(owd,'ba_timemachine_text','I_general','I-H'))

                            elif wit_response['intents'][0]['name'] == 'your_range':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-I'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-I'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-I'))), os.path.join(owd,'ba_timemachine_text','I_general','I-I'))
                            
                            elif wit_response['intents'][0]['name'] == 'interested_feedback':                            
                                print("Because ...")

                                

                                
                            # III_fluidfacts

                            elif wit_response['intents'][0]['name'] == 'life_20-26':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-E'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-E'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-E'))), os.path.join(owd,'ba_timemachine_text','I_general','I-E'))

                                MyHandler.store = 'III_A'

                            elif wit_response['intents'][0]['name'] == 'life_27-33':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-E'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-E'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-E'))), os.path.join(owd,'ba_timemachine_text','I_general','I-E'))

                                MyHandler.store = 'III_B'

                            elif wit_response['intents'][0]['name'] == 'life_34-40':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-E'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-E'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-E'))), os.path.join(owd,'ba_timemachine_text','I_general','I-E'))

                                MyHandler.store = 'III_C'

                            elif wit_response['intents'][0]['name'] == 'life_41-46':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-E'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-E'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-E'))), os.path.join(owd,'ba_timemachine_text','I_general','I-E'))

                                MyHandler.store = 'III_D'

                            elif wit_response['intents'][0]['name'] == 'life_47-59':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-E'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-E'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-E'))), os.path.join(owd,'ba_timemachine_text','I_general','I-E'))

                                MyHandler.store = 'III_E'

                            elif wit_response['intents'][0]['name'] == 'life_60plus':
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-E'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-E'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-E'))), os.path.join(owd,'ba_timemachine_text','I_general','I-E'))

                                MyHandler.store = 'III_F'
                            

                            # III_fluidfacts long version        
                            elif wit_response['intents'][0]['name'] == 'long_please':

                                if MyHandler.store == 'III_A':

                                    if MyHandler.III_A_count == 0:

                                        self.III_A_version_a = random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-A",'III-A_1','III-A_1_a')))
                                        
                                        
                                        #self.speak(self.III_A_version_a, os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-A",'III-A_1','III-A_1_a'))
                                        self.read(self.III_A_version_a, os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-A",'III-A_1','III-A_1_a'))

                                        MyHandler.III_A_count = MyHandler.III_A_count + 1
                                        print(MyHandler.III_A_count)

                                    else:
                                        #self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))
                                        self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-G'))), os.path.join(owd,'ba_timemachine_text','I_general','I-G'))

                                elif MyHandler.store == 'III_B':

                                    if MyHandler.III_B_count == 0:

                                        self.III_B_version_a = random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-B",'III-B_1','III-B_1_a')))
                                        
                                        
                                        #self.speak(self.III_B_version_a, os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-B",'III-B_1','III-B_1_a'))
                                        self.read(self.III_B_version_a, os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-B",'III-B_1','III-B_1_a'))

                                        MyHandler.III_B_count = MyHandler.III_B_count + 1
                                        print(MyHandler.III_B_count)

                                    else:
                                        #self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))
                                        self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-G'))), os.path.join(owd,'ba_timemachine_text','I_general','I-G'))

                                elif MyHandler.store == 'III_C':

                                    if MyHandler.III_C_count == 0:

                                        self.III_C_version_a = random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-C",'III-C_1','III-C_1_a')))
                                        
                                        
                                        #self.speak(self.III_C_version_a, os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-C",'III-C_1','III-C_1_a'))
                                        self.read(self.III_C_version_a, os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-C",'III-C_1','III-C_1_a'))

                                        MyHandler.III_C_count = MyHandler.III_C_count + 1
                                        print(MyHandler.III_C_count)

                                    else:
                                        #self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))
                                        self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-G'))), os.path.join(owd,'ba_timemachine_text','I_general','I-G'))

                                elif MyHandler.store == 'III_D':

                                    if MyHandler.III_D_count == 0:

                                        self.III_D_version_a = random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-D",'III-D_1','III-D_1_a')))
                                        
                                        
                                        #self.speak(self.III_D_version_a, os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-D",'III-D_1','III-D_1_a'))
                                        self.read(self.III_D_version_a, os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-D",'III-D_1','III-D_1_a'))

                                        MyHandler.III_D_count = MyHandler.III_D_count + 1
                                        print(MyHandler.III_D_count)

                                    else:
                                        #self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))
                                        self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-G'))), os.path.join(owd,'ba_timemachine_text','I_general','I-G'))

                                elif MyHandler.store == 'III_E':

                                    if MyHandler.III_E_count == 0:

                                        self.III_E_version_a = random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-E",'III-E_1','III-E_1_a')))
                                        
                                        
                                        #self.speak(self.III_E_version_a, os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-E",'III-E_1','III-E_1_a'))
                                        self.read(self.III_E_version_a, os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-E",'III-E_1','III-E_1_a'))

                                        MyHandler.III_E_count = MyHandler.III_E_count + 1
                                        print(MyHandler.III_E_count)

                                    else:
                                        #self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))
                                        self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-G'))), os.path.join(owd,'ba_timemachine_text','I_general','I-G'))

                                elif MyHandler.store == 'III_F':

                                    if MyHandler.III_F_count == 0:

                                        self.III_F_version_a = random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-F",'III-F_1','III-F_1_a')))
                                        
                                        
                                        #self.speak(self.III_F_version_a, os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-F",'III-F_1','III-F_1_a'))
                                        self.read(self.III_F_version_a, os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-F",'III-F_1','III-F_1_a'))

                                        MyHandler.III_F_count = MyHandler.III_F_count + 1
                                        print(MyHandler.III_F_count)

                                    else:
                                        #self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))
                                        self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-G'))), os.path.join(owd,'ba_timemachine_text','I_general','I-G'))



                            # III_fluidfacts long version cont.
                            elif wit_response['intents'][0]['name'] == 'go_further':


                                # A
                                if MyHandler.store == 'III_A':
                                    
                                    if MyHandler.III_A_count == 1:

                                        self.III_A_version_b = self.III_A_version_a[:-5] + "b" + '.txt'
                                    
                                        #self.speak(self.III_A_version_b, os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-A",'III-A_1'))
                                        self.read(self.III_A_version_b, os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-A",'III-A_1'))

                                        MyHandler.III_A_count = MyHandler.III_A_count + 1
                                        print(MyHandler.III_A_count)

                                    elif MyHandler.III_A_count == 2:

                                        self.III_A_version_c = self.III_A_version_a[:-5] + "c" + '.txt'
                                    
                                        #self.speak(self.III_A_version_c, os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-A",'III-A_1'))
                                        self.read(self.III_A_version_c, os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-A",'III-A_1'))

                                        MyHandler.III_A_count = 0
                                        print(MyHandler.III_A_count)

                                # B
                                elif MyHandler.store == 'III_B':
                                    if MyHandler.III_B_count == 1:

                                        self.III_B_version_b = self.III_B_version_a[:-5] + "b" + '.txt'
                                    
                                        #self.speak(self.III_B_version_b, os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-B",'III-B_1'))
                                        self.read(self.III_B_version_b, os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-B",'III-B_1'))

                                        MyHandler.III_B_count = MyHandler.III_B_count + 1
                                        print(MyHandler.III_B_count)

                                    elif MyHandler.III_B_count == 2:

                                        self.III_B_version_c = self.III_B_version_a[:-5] + "c" + '.txt'
                                    
                                        #self.speak(self.III_B_version_c, os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-B",'III-B_1'))
                                        self.read(self.III_B_version_c, os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-B",'III-B_1'))

                                        MyHandler.III_B_count = 0
                                        print(MyHandler.III_B_count)

                                #C
                                elif MyHandler.store == 'III_C':
                                    if MyHandler.III_C_count == 1:

                                        self.III_C_version_b = self.III_C_version_a[:-5] + "b" + '.txt'
                                    
                                        #self.speak(self.III_C_version_b, os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-C",'III-C_1'))
                                        self.read(self.III_C_version_b, os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-C",'III-C_1'))

                                        MyHandler.III_C_count = MyHandler.III_C_count + 1
                                        print(MyHandler.III_C_count)

                                    elif MyHandler.III_C_count == 2:

                                        self.III_C_version_c = self.III_C_version_a[:-5] + "c" + '.txt'
                                    
                                        #self.speak(self.III_C_version_c, os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-C",'III-C_1'))
                                        self.read(self.III_C_version_c, os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-C",'III-C_1'))

                                        MyHandler.III_C_count = 0
                                        print(MyHandler.III_C_count)

                                # D
                                elif MyHandler.store == 'III_D':
                                    if MyHandler.III_D_count == 1:

                                        self.III_D_version_b = self.III_D_version_a[:-5] + "b" + '.txt'
                                    
                                        #self.speak(self.III_D_version_b, os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-D",'III-D_1'))
                                        self.read(self.III_D_version_b, os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-D",'III-D_1'))

                                        MyHandler.III_D_count = MyHandler.III_D_count + 1
                                        print(MyHandler.III_D_count)

                                    elif MyHandler.III_D_count == 2:

                                        self.III_D_version_c = self.III_D_version_a[:-5] + "c" + '.txt'
                                    
                                        #self.speak(self.III_D_version_c, os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-D",'III-D_1'))
                                        self.read(self.III_D_version_c, os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-D",'III-D_1'))

                                    MyHandler.III_D_count = 0
                                    print(MyHandler.III_D_count)

                                # E
                                elif MyHandler.store == 'III_E':
                                    if MyHandler.III_E_count == 1:

                                        self.III_E_version_b = self.III_E_version_a[:-5] + "b" + '.txt'
                                    
                                        #self.speak(self.III_E_version_b, os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-E",'III-E_1'))
                                        self.read(self.III_E_version_b, os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-E",'III-E_1'))

                                        MyHandler.III_E_count = MyHandler.III_E_count + 1
                                        print(MyHandler.III_E_count)

                                    elif MyHandler.III_E_count == 2:

                                        self.III_E_version_c = self.III_E_version_a[:-5] + "c" + '.txt'
                                    
                                        #self.speak(self.III_E_version_c, os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-E",'III-E_1'))
                                        self.read(self.III_E_version_c, os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-E",'III-E_1'))

                                        MyHandler.III_E_count = 0
                                        print(MyHandler.III_E_count)
                                        
                                else:
                                    #self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-G'))), os.path.join(owd,'ba_timemachine_text','I_general','I-G'))

                            elif wit_response['intents'][0]['name'] == 'stop_this':

                                # agreement
                                #self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-A'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-A'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-A'))), os.path.join(owd,'ba_timemachine_text','I_general','I-A'))
                                
                                MyHandler.store == ''
                                MyHandler.III_A_count = 0
                                MyHandler.III_B_count = 0
                                MyHandler.III_C_count = 0
                                MyHandler.III_D_count = 0
                                MyHandler.III_E_count = 0
                                MyHandler.III_F_count = 0

                                

                            # III_fluidfacts short version                                
                            elif wit_response['intents'][0]['name'] == 'short_please':

                                if MyHandler.store == 'III_A':
                                    #self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-A",'III-A_2'))), os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-A",'III-A_2'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-A",'III-A_2'))), os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-A",'III-A_2'))

                                elif MyHandler.store == 'III_B':
                                    #self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-B",'III-B_2'))), os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-B",'III-B_2'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-B",'III-B_2'))), os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-B",'III-B_2'))

                                elif MyHandler.store == 'III_C':
                                    #self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-C",'III-C_2'))), os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-C",'III-C_2'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-C",'III-C_2'))), os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-C",'III-C_2'))

                                elif MyHandler.store == 'III_D':
                                    #self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-D",'III-D_2'))), os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-D",'III-D_2'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-D",'III-D_2'))), os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-D",'III-D_2'))

                                elif MyHandler.store == 'III_E':
                                    #self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-E",'III-E_2'))), os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-E",'III-E_2'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-E",'III-E_2'))), os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-E",'III-E_2'))

                                elif MyHandler.store == 'III_E':
                                    #self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-F",'III-F_2'))), os.path.join(owd,'ba_timemachine_audio','III_fluidfacts',"III-F",'III-F_2'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-F",'III-F_2'))), os.path.join(owd,'ba_timemachine_text','III_fluidfacts',"III-F",'III-F_2'))

                                else:
                                    # we don't know which fluid fact is being referred to
                                    print("Which life event would you like to hear from?")
                                    #self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))
                                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-G'))), os.path.join(owd,'ba_timemachine_text','I_general','I-G'))
     
                                

                            else:
                                # not in our list of intents
                                self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))
                                self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-G'))), os.path.join(owd,'ba_timemachine_text','I_general','I-G'))
                                
                        else:
                            # confidence level not high enough
                            self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))
                            self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-G'))), os.path.join(owd,'ba_timemachine_text','I_general','I-G'))

                    else:
                        print("I hear something but I don't get your intent")
                        self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))
                        self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-G'))), os.path.join(owd,'ba_timemachine_text','I_general','I-G'))

                else:
                    # didn't sense an intent
                    print("I didn't get your intent")
                    
                    if random.randint(1,10) > 6:
                        # repeat question
                        self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))
                        self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-G'))), os.path.join(owd,'ba_timemachine_text','I_general','I-G'))
                    else:
                        # fillers
                        self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-F'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-F'))
                        self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-F'))), os.path.join(owd,'ba_timemachine_text','I_general','I-F'))


            else:
                print("Did you say something?")


                if random.randint(1,10) > 6:
                    # repeat question
                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))
                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-G'))), os.path.join(owd,'ba_timemachine_text','I_general','I-G'))
                else:
                    # fillers
                    self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-F'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-F'))
                    self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-F'))), os.path.join(owd,'ba_timemachine_text','I_general','I-F'))
                


        #except:
            #print("Something went wrong")

            # repeat question
            #self.speak(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))), os.path.join(owd,'ba_timemachine_audio','I_general','I-G'))
            #self.read(random.choice(os.listdir(os.path.join(owd,'ba_timemachine_text','I_general','I-G'))), os.path.join(owd,'ba_timemachine_text','I_general','I-G'))
        finally:
            print('Returning to listening...')


    def read(self, file, dir):
        try:
            print("Reading...")
            os.chdir(dir)
            f = open(file, 'r')
            file_contents = f.read()
            print(file_contents)
            f.close()
        finally:
            os.chdir(owd)
        
    def speak(self, file, dir):
        
        global PAUSED
        if PAUSED is True:
            print("Pause")
            return
            
        try:            
            print("Speaking...")
            os.chdir(dir)
            wave_obj = sa.WaveObject.from_wave_file(file)
            play_obj = wave_obj.play()
            play_obj.wait_done()

            PAUSED = True
            
        finally:
            os.chdir(owd)
            PAUSED = False


    
if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=os.path.join(owd,'Audio'), recursive=False)
    observer.start()


    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()





