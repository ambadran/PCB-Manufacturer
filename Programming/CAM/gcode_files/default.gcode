; This gcode is generated by my python script specially for my PCB manufacturer project :))

G21 ; to set metric units
G90 ; to set absolute mode , G91 for incremental mode
G94 ; To set the active feed rate mode to units per minute mode

F700 ; setting default feedrate

M5 ; disabling spindle PWM
C0 ; Choosing the empty tool slot in the multiplexer circuits

B1 ; Turn ON Machine

$H ; Homing :)
G10 P0 L20 X0 Y0 Z0 ; Force Reset current coordinates after homing

; Getting and Activating Tool-2
G01 X0Y0Z0 ; Go to Tool-2 Home Pos
G01 X5 ; Enter Female Kinematic Mount Home Pos
A1 ; Latch on Kinematic Mount
G4 P5000 ; Wait for Kinematic Mount to fully attach
G01 X0Y0Z0 ; Exit Female Kinematic Mount Home Pos
C2 ; Choosing tool 2 in the choose demultiplexer circuits

S230 ; sets pwm speed when we enable it
G01 Z20F10

M3 ; Turn Motor ON
G4 P2000 ; dwell for 2 seconds so motor reaches full RPM

G01 X44.545Y26.125F700
G01 Z25F10
G01 Z20F10
G01 X44.545Y18.505F700
G01 Z25F10
G01 Z20F10
G01 X23.89Y28.235F700
G01 Z25F10
G01 Z20F10
G01 X29.94Y30.185F700
G01 Z25F10
G01 Z20F10
G01 X43.165424Y29.305F700
G01 Z25F10
G01 Z20F10
G01 X41.895424Y29.305F700
G01 Z25F10
G01 Z20F10
G01 X40.625424Y29.305F700
G01 Z25F10
G01 Z20F10
G01 X36.915Y7.055F700
G01 Z25F10
G01 Z20F10
G01 X39.455Y7.055F700
G01 Z25F10
G01 Z20F10
G01 X41.995Y7.055F700
G01 Z25F10
G01 Z20F10
G01 X44.535Y7.055F700
G01 Z25F10
G01 Z20F10
G01 X7.08Y6.445F700
G01 Z25F10
G01 Z20F10
G01 X42.005Y18.51F700
G01 Z25F10
G01 Z20F10
G01 X42.005Y26.13F700
G01 Z25F10
G01 Z20F10
G01 X42.025Y10.255F700
G01 Z25F10
G01 Z20F10
G01 X44.525Y10.255F700
G01 Z25F10
G01 Z20F10
G01 X40.64Y14.7F700
G01 Z25F10
G01 Z20F10
G01 X42.64Y14.7F700
G01 Z25F10
G01 Z20F10
G01 X46.958Y12.824F700
G01 Z25F10
G01 Z20F10
G01 X46.958Y15.364F700
G01 Z25F10
G01 Z20F10

M5 ; Turn Motor OFF

; Returning the Deactivating Tool-2G01 X0Y0Z0 ; Go to Tool-2 Home Pos
G01 X5 ; Enter Female Kinematic Mount Home Pos
A0 ; Latch OFF Kinematic Mount
G4 P5000 ; Wait for Kinematic Mount to fully detach
G01 X0Y0Z0 ; Exit Female Kinematic Mount Home Pos
C0 ; PWM Tool select demultiplexer to select tool zero which is the empty tool slot in multiplexers

