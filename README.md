# Midi to Bom Converter Scuffed Version 0.1 

This is a temporary tool to convert midi tempo changes to TimingPoints in the .box file. It also supports Reaper files (.rpp)

Written in python because I'm cheap. 

The plan is to include these functionalities in the actual BoomBox Editor. Support for Reaper files in the tool is possible because of the easy to use existing Reaper parsers for python. 

File converts BPM only but midi notes conversion could be possible in the future.

## CREDITS 

These are the python libraries used:

MIDO
https://github.com/mido/mido

    Copyright (c) Ole Martin Bjørndalen


RPP
https://github.com/Perlence/rpp

    Copyright 2015 Sviatoslav Abakumov

https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element

## OTHER

The Python Imaging Library (PIL) is

    Copyright © 1997-2011 by Secret Labs AB
    Copyright © 1995-2011 by Fredrik Lundh

Pillow is the friendly PIL fork. It is

    Copyright © 2010-2021 by Alex Clark and contributors
---

## DOWNLOAD

https://drive.google.com/file/d/1VmHSMC-BFp_srPHQ3nUdbdiHxyQxxHQp/view?usp=sharing

## HOW TO USE

1. Create a BOM file with the BoomBox Editor (make sure to make a back up if you are using an old map)

![Step1](gifs/midi01.gif)

2. Run MIDI to BOM Converter, load midi/rpp and bom files. Convert!

![Step2](gifs/midi02.gif)

3. Open BOM file back in the editor


![Step3](gifs/midi03.gif)




Beto
