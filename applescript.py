# Credit to https://leancrew.com/all-this/2013/03/combining-python-and-applescript/
import subprocess

def asrun(ascript):
    osa = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    return osa.communicate(ascript)[0]

def asquote(astr):
    astr = astr.replace('"', '" & quote & "')
    return '"{}"'.format(astr)
