# Midi to Bom Converter Scuffed Version 0.1 

This is a temporary tool to convert midi tempo changes to TimingPoints in the .box file.

Written in python because I'm cheap. 

The plan is to include these functionalities in the actual BoomBox Editor. Support for Reaper files in the tool is possible because of the easy to use existing Reaper parsers. 

File converts BPM only but midi notes conversion could be possible in the future.

## HOW TO USE

1. Create a BOM file with the BoomBox Editor (make sure to make a back up)
2. Run MIDI to BOM Converter
3. Press browse .mid/.rpp, make sure to change file type (bottom right) if importing RPP
4. Press browse .bom file
5. Convert BPM :)


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


Beto
