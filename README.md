# DJPY


Fork of omriharel's [deej](https://github.com/omriharel/deej): An Arduino project for controlling audio volume for separate Windows processes using physical sliders (like a DJ!)

**But now it's back in Python!** *Cue Applause*

# How it works
## Software

- The PC runs a Python script [`deej.py`](./deej.py) that listens to [`the python window`](./PYDJwindow.py) and detects changes in slider values and sets volume of equivalent audio sessions accordingly.


## Slider mapping (configuration)
`DJPY` uses an external YAML-formatted configuration file named [`config.yaml`](./config.yaml).

The config file determines which applications are mapped to which sliders, ~~and which COM port/baud rate to use for the connection to the Arduino board.~~ ***No longer applies with DJPY***

**This file auto-reloads when its contents are changed, so you can change application mappings on-the-fly without restarting `DJPY`.**

It looks something like this:

```yaml
slider_mapping:
  0: master
  1: chrome.exe
  2: spotify.exe
  3:
    - pathofexile_x64.exe
    - rocketleague.exe
  4: discord.exe

# recommend to leave this setting at its default value
process_refresh_frequency: 5
```
- Process names aren't case-sensitive
- You can use a list of process names to either:
    - define a group that is controlled simultaneously
    - choose whichever process in the group is currently running (in this example, one slider is for different games that may be running)
- `master` is a special option for controlling master volume of the system.
- `mic` is a special option for controlling the default microphone of the system.
- The `process_refresh_frequency` option limits how often `deej` may look for new processes if their appropriate slider moves. This allows you to leave `deej` running in background and open/close processes normally - the sliders will #justwork
# How to run

Well, it's not ready for release yet, but when it is, you'll be able to download an executable from the Releases page.

### Requirements

- Python 3 (with venv & pip)

### Installation

- Download the repository by either cloning it or downloading its archive.
- In the repo's directory, run:
    - `virtualenv venv`
    - `venv\Scripts\activate.bat`
    - `pip install -r requirements.txt`


## Missing stuff

- Better logging and error handling
- ***Concurrent processing. Whoops...***
