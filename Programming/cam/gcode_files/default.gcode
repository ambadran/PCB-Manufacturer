
; The following gcode is the PCB trace laser marking gcode

M5 ; Being extra sure it won't light up before activation; Getting and Activating Tool-1, The Tool.Laser
G01 X165Y0Z11 ; Go to Tool-1 Home Pos
G01 X188 ; Enter Female Kinematic Mount Home Pos
A1 ; Latch on Kinematic Mount
G4 P5 ; Wait for Kinematic Mount to fully attach
G01 X92 ; Exit Female Kinematic Mount Home Pos
#TODO X0Y0Z0 ;  ;Add tool offset coordinate
C1 ; Choosing tool 1 in the choose demultiplexer circuits

F600 ; setting default feedrate

G00Z16 ; Moving to correct focal length Z position

S150 ; Setting Laser Power


M5 ; Disable End-Effector Signal

; Returning the Deactivating Tool-1
C0 ; PWM Tool select demultiplexer to select tool zero which is the empty tool slot in multiplexers
#TODO X0Y0Z0 ;  ;Remove tool offset coordinate
G01 X165Y0Z11 ; Go to Tool-1 Home Pos
G01 X92 ; Enter Female Kinematic Mount Home Pos
A0 ; Latch OFF Kinematic Mount
G4 P5 ; Wait for Kinematic Mount to fully detach
G01 X188 ; Exit Female Kinematic Mount Home Pos

G00X0Y0Z0
B0 ; Turn Machine OFF
