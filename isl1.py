from nltk.parse.stanford import StanfordDependencyParser
import numpy as np
import cv2
import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.editor import VideoFileClip, concatenate_videoclips

import nltk

import os
import sys
try:
	os.remove("my_concatenation.mp4")
except:
	pass
print(sys.path)
name=""

for each in range(1,len(sys.argv)):
    name+=sys.argv[each]
    name+=" "

input_text=name

text = nltk.word_tokenize(input_text)

result=nltk.pos_tag(text)

for each in result:
    print(each)

dict={}
dict["NN"]="noun"
arg_array=[]

for text in result:
    arg_array.append(VideoFileClip(text[0]+"_"+dict[text[1]]+".mp4"))
    print(text[0]+"_"+dict[text[1]]+".mp4")
print(arg_array[0])
        
final_clip = concatenate_videoclips(arg_array)
final_clip.write_videofile("my_concatenation.mp4")