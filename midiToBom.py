
from mido import MidiFile
from mido import tempo2bpm
import json
import os

from pathlib import Path
from zipfile import ZipFile

import rpp


def GetBPM_FromRPP(rppFileName):    
    """ returns list of (bpm, pos) tuplets """
    
    with open(rppFileName, "r") as file:
        r = rpp.loads(file.read())    
    
    elements = r.findall("TEMPOENVEX")[0]
    
    bpms = [[ float(e[2]), round(float(e[1]) * 1000, 5) ] for e in elements if "PT" in str(e)]

    return bpms


def GetBPM_FromMIDI(midiFileName):    
    """ returns list of [bpm, pos] floats """
    
    mid = MidiFile(midiFileName, clip = True)
        
    bpms = [[round(tempo2bpm(msg.tempo), 2), msg.time] for msg in mid.tracks[0] if msg.type == "set_tempo"]

    # this one replicates the extra bpm added in the box files
    #bpms.append([120,mid.length])
    
    return Convert_DeltaTimeTicks_ToTimeMilliSeconds(bpms, mid.ticks_per_beat) 


def AddTimingPoints_toBOX(boxFileName, bpms):
    """ appends the data to the json """
    
    with open(boxFileName) as json_file:
        data = json.load(json_file)
    
    # Resets
    data["TimingPoints"] = []
    
    print("Bpms saved:")
    for i in bpms:
        print(i)
        data["TimingPoints"].append(
            {"Bpm" : i[0],
            "Offset": i[1]})
        
            
    with open(boxFileName, "w") as json_file_write:
        json.dump(data, json_file_write)


def Convert_DeltaTimeTicks_ToTimeMilliSeconds(bpms, midiResolution):
    """ gets the list with delta times in ticks from mido and returns the same list in milliseconds"""
    totalTime, previousBPM = 0, 120
    
    for i in bpms:
        # converts to milliseconds
        deltaTime = round((i[1] / midiResolution) * (60 / previousBPM) * 1000, 5)
        # Saves values
        previousBPM = i[0]
        totalTime += deltaTime 
        # This is the good one
        i[1] = totalTime

    return bpms


def Open_Bom(file, bpms, dr):
    """ reads zip, finds the boxes"""
        
    
    with ZipFile(file, 'r') as bomFile:
        nameList = bomFile.namelist()
        bomFile.extractall()
    
    boxes = [i for i in nameList if ".box" in i]
    
    for boxFileName in boxes:
        print(boxFileName)
        AddTimingPoints_toBOX(boxFileName, bpms)


    # WRITE ALL FILES BACK INTO THE BOM :D
    with ZipFile(file, "w") as bomFile:
        
        for fileName in nameList:        
            bomFile.write(fileName)
            
            
    # Remove once zip back up is done
    for fileName in nameList:
        os.remove(fileName)
                
    return boxes


        
def RunFromFiles_MIDI(midiFileName, bom):
    root = Path.cwd()
    
    bpms = GetBPM_FromMIDI(midiFileName)
    
    Open_Bom(bom, bpms, root)
            
    
def RunFromFiles_RPP(midiFileName, bom):
    root = Path.cwd()
    
    bpms = GetBPM_FromRPP(midiFileName)
    
    Open_Bom(bom, bpms, root)



