# ATTiny-ARSAT

A BEAM solar powered satellite sculpture based on a ATTiny85 microcontroller in honor to [ARSAT satellites](https://en.wikipedia.org/wiki/ARSAT-1).

A sculpture made of a [Freeform Circuit](https://www.digikey.com/en/maker/blogs/2019/freeform-circuit-sculptures) style based on a [Pummer](http://solarbotics.net/library/circuits/bot_pummer.html) with a speaker/buzzer to transmit an image encoded on [SSTV Robot36](https://en.wikipedia.org/wiki/Slow-scan_television).

## Project setup and Code

You will need an image in [SSTV Robot36 format converted into .wav](https://www.vr2woa.com/sstv/)

I recommend you to use [PlatformIO](https://platformio.org/) to setup this project but you can also use Arduino IDE as well.

I am assuming you will be using an Arduino as a programmer.

### Using PlatformIO

- Clone the repo
- Change the **update port** to your Arduino COM in the **platform.ini** file
- Execute the **sstv_to_freq.py** script with a wav file as a parameter

> The script will generate 3 new files: **durations.h**, **frequencies.h** and **spectogram.png**

- **Build** the project, **burn the bootloader** and then **upload** to the microcontroller

Remember to close Arduino IDE before upload the script into the microcontroller, it will make your port bussy.

### Using Arduino IDE

- later...

## Schematic

Using the internal 1MHz oscillator of the ATtiny85.

The SSTV file is saved on Flash Memory due [RAM limitations](https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-2586-AVR-8-bit-Microcontroller-ATtiny25-ATtiny45-ATtiny85_Datasheet.pdf).

> Idea: One file can be loaded on RAM and the other on Flash to distribute the load.

The solarcells are connected in series and fed to the supercapacitor via a reverse current blocking diode.

![image](/res/schematic_01.jpeg)

Spectogram of an SSTV audio file translated into frequencies peaks and durations.

> Note: Currently the script is not saving the entire duration of the spectogram.

![image](/res/spectrogram.png)

Based on this [Mohit Bhoite's wonderful sculpture](https://www.bhoite.com/sculptures/tiny-cube-sat/)
