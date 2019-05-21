#!/usr/bin/env python
# coding: utf-8

# In[3]:


# import speech_recognition as sr
# import pyaudio

from gtts import gTTS
import os

test = 'Hello. This is a test'

speech = gTTS(text = test, lang = 'en')
speech.save('tts.mp3')


# In[ ]:





# In[ ]:




