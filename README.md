# PCB-Manufacturer

###  Intro
A cnc machine with a kinematic mounting mechanism and specialised code to change head as wanted so as to have access to all the
tools to create a PCB without any human intervention.

### Mechanics
This is a 3 Axis CNC machine made of both metal and 3D printed Parts.
The main driving mechanism is a V-wheel on 2020 profile system with a GT-2 belt driving.
Nema17 Motors was used. The machine was designed for maximal repeatability. 

A 3D printed Kinematic Mounting System was developed to enable the CNC machine to detach and attach to different tool heads on command. The current tool heads are a laser head, a spindle, a Pen marker. The machine automatically attaches to the wanted tool heads without any human intervention.

I also developed an auto-clamping system that clamps the PCB in the bed automatically.

#### Photos
[![Overview](https://github.com/ambadran/PCB-Manufacturer/blob/main/Mechanics/Media/EB5CB823-7A3D-43ED-BADD-CD01FB9BCF4A.JPG)]()

[![Male Kinematic Mount](https://github.com/ambadran/PCB-Manufacturer/blob/main/Mechanics/Media/IMG_1377.JPG)]()

[![Female Kinematic Mount](https://github.com/ambadran/PCB-Manufacturer/blob/main/Mechanics/Media/IMG_1376.JPG)]()

### Electronics
The Main MCU is an Arduino Mega. A Custom GRBL firmware created by me is running on it.

To add a screen monitoring functionality and control the main MCU wirelessly through WiFi, I added a raspberry pi 4 with a 7 inch screen, running mainly UGS Software to monitor the CNC machine.

The Stepper drivers are powerful TB6600 drivers, The end-stops have their own opto-coupler circuit. 
There are 3 power supplies for the CNC machine. one 5v for the main MCU only, one 5v for the raspberry pi. and the third 24v is for the rest of the CNC machine.

This main 24v power supply is switched on using a relay that is controled by the Main MCU. A special G-Code was coded in the firmware to control the main power supply. This adds an important safety layer as the machine is intended to be run remotely.

To relieve the Main MCU from doing everything in the project. I took the liberity to make different circuits for different functions needed for this machine.

I developed a circuit that takes in a 3-bit binary code and the spindle PWM signal from the Main MCU. Then it decodes the 3-bit binary code to allow the PWM to exit through one of the 8 channels that this CNC machine controls. Meaning, the machine can control 8 different end-effectors with PWM, depending on the current 3-bit binary that the MCU outputs.

Another circuit worth mentioning was the stand alone circuit to control the latching mechanism of the kinematic mounting system, where the input to the circuit is just a HIGH/LOW signal from the main MCU triggered by a G-code command `A1` or `A0`. The local MCU does controls the unipolar stepper to latch ON or OFF to the Female kinematic mounts on command and does all the necessary closed-loop logic locally.

[![Electronics](https://github.com/ambadran/PCB-Manufacturer/blob/main/Mechanics/Media/EAF457E6-06F3-4282-9E6C-934CC6FC3E58.JPG)]()


### Programming
I customized the GRBL firmware from: https://github.com/gnea/grbl 
To accomodate for all the new functionality needed for this CNC machine.
I put in my own G-code commands like `A<x>`, `B<x>` or `C<x>`, that outputs the necessary logic on the Main MCU GPIOs, with no compromise to the original code.

I also developed (from scratch) a complete CAM solution that takes in the gerber files and gives out the G-code ready for my machine. However, due to me deciding to develop from scratch and not use geometry-manipulating libraries like `shapely`. There is alot of corner cases that this version can't handle. 
However, I developed V2 of my all-in-one CAM solution for my CNC machine here: https://github.com/ambadran/PCB-CAM

This version is much much more reliable as to it not being built from scratch.



