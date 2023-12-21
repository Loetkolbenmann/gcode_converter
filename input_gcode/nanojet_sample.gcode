;Fusion 360 CAM 2.0.17954
; Posts processor: Marlin.cps
; Gcode generated: Thursday, December 21, 2023 4:31:30 PM GMT
; Document: s line test v1
; Setup: Setup2
; 
; Ranges Table:
;   X: Min=9.85 Max=29.95 Size=20.1
;   Y: Min=10.5 Max=29.55 Size=19.05
;   Z: Min=4 Max=16 Size=12
; 
; Tools Table:
;  T1 D=0 CR=0 - ZMIN=4 - laser cutter 
; 
; Feedrate and Scaling Properties:
;   Feed: Travel speed X/Y = 2500
;   Feed: Travel Speed Z = 300
;   Feed: Enforce Feedrate = true
;   Feed: Scale Feedrate = false
;   Feed: Max XY Cut Speed = 900
;   Feed: Max Z Cut Speed = 180
;   Feed: Max Toolpath Speed = 1000
; 
; G1->G0 Mapping Properties:
;   Map: First G1 -> G0 Rapid = false
;   Map: G1s -> G0 Rapids = false
;   Map: SafeZ Mode = Retract : default = 15
;   Map: Allow Rapid Z = false
; 
; *** START begin ***
;   Set Absolute Positioning
;   Units = mm
;   Disable stepper timeout
;   Set current position to 0,0,0
G90
G21
M84 S0
G92 X0 Y0 Z0
; *** START end ***
; 
; *** SECTION begin ***
;   X Min: 9.85 - X Max: 29.95
;   Y Min: 10.5 - Y Max: 29.55
;   Z Min: 4 - Z Max: 16
; 2D Profile1, Laser/Plasma Cutting mode: auto, jetMode: Through, power: 80
; COMMAND_START_SPINDLE
; COMMAND_SPINDLE_COUNTERCLOCKWISE
; COMMAND_COOLANT_ON
M117  2D Profile1
G0 Z16 F300
G0 X9.85 Y10.5 F2500
G0 Z4 F300
; >>> LASER Power ON
M106 S204
; COMMAND_POWER_ON
; MOVEMENT_LEAD_IN
G1 X9.95 F400
; MOVEMENT_CUTTING
G1 Y29.5 F400
G2 X10 Y29.55 I0.05 F400
G1 X20 F400
G2 X20.05 Y29.5 J-0.05 F400
G1 Y10.55 F400
G1 X29.95 F400
G1 Y29.5 F400
; >>> LASER Power OFF
M107
; COMMAND_POWER_OFF
; MOVEMENT_RAPID
G0 Z16 F300
; *** SECTION end ***
;
; *** STOP begin ***
M400
; COMMAND_COOLANT_OFF
G0 X0 Y0 F2500
; COMMAND_STOP_SPINDLE
M117 Job end
; *** STOP end ***
