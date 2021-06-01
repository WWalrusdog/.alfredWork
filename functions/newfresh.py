#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from pydub import AudioSegment

path = "/Users/scottmolloy/Desktop/Projects/audio projects/Re2016/July/"
pods = """15 2016 GIST And We Never Looked at Music the Same Way Again.mp3
15 Jul 2016.mp3""".split("\n")

july2 = AudioSegment.from_mp3(f"{path}{pods[0]}")
july3 = AudioSegment.from_mp3(f"{path}{pods[1]}")
july = july2+july3
july.export(f"{path}trial.mp3", format="mp3")


 


