# droid3scrambler

A patch randomizer for the [Abildgard Droid-3 synthesizer](https://www.droid3.com/).

## Requirements

Requires Python 3 (written and tested on Python 3.10 only, YMMV).  Also requires the ['mido' package](https://mido.readthedocs.io/en/latest/).

## License

Whatever you wanna do with it.  [WTFPL](http://www.wtfpl.net/about/).

## Non-techy installation instructions (Windows)

If you know what you're doing, feel free to ignore this section.  I don't have a Mac, so unfortunately you're on your own there.  I assume Linux/BSD/other OS users know what they're doing.

- Fetch the latest Python 3 installer from [the Python website](https://www.python.org/downloads/windows/) and install it.  Be sure to tick the 'Add python to PATH' option at the end of the installer prompt.

- Open a command prompt (Start -> Command Prompt), and type `pip install mido` into it, and press enter.

- Make a folder somewhere on your machine, named whatever you'd like.

- Download the droid3scrambler.py file from this repository (using the 'raw' link) into that folder.  (You don't need the .leo file, or this README.md file.)

## Non-techy usage instructions (Windows)

Same as the previous section -- feel free to ignore this if you know what you're doing.

- Open the folder you placed the droid3scrambler.py file into.

- Right click on that .py file, and select Edit with IDLE.  That should open the script up in a window.

- In the IDLE window, select Run -> Run Module (or just hit F5).  You'll see the script output, which looks like this (as a patch sheet):

```
Instrument ID: 5035550078
BIT: 01101001 (105)
TYP: 01110100 (116)
CUT: 218
WID: 0
ARP: Pb2
STP: 1
=== DCO1 ===
DCO1WAV: En2
DCO1OCT: 1
DCO1PW: 20
DCO1OFF: 11
DCO1AMP: 84
DCO1FRQ: DC2
=== DCO2 ===
DCO2WAV: KF2
DCO2OCT: 15
DCO2PW: 67
DCO2OFF: Vel
DCO2AMP: Gat
DCO2FRQ: KF2
=== EN1 ===
EN1A: 46
EN1LV: 82
EN1D: 222
EN1S: 86
EN1R: 57
EN1OFF: DC2
=== EN2 ===
EN2A: 253
EN2LV: 236
EN2D: 139
EN2S: 27
EN2R: 181
EN2OFF: Pb2
Instrument saved as: 5035550078.mid
```

- In the folder where you saved the script, you should now have a new .mid (MIDI) file, named as the output indicated (in this example, `5035550078.mid`).  Send that to your Droid-3 (perhaps use MIDIBar from the [MIDI-OX project](http://www.midiox.com/)) and you're running the new randomized patch!

