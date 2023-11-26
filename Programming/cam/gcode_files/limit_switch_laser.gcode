; This gcode is generated by my specialised python script for my PCB manufacturer project :))

; Machine Initialization Sequence...

G21 ; to set metric units
G90 ; to set absolute mode , G91 for incremental mode
G94 ; To set the active feed rate mode to units per minute mode

M5 ; disabling spindle PWM
C0 ; Choosing the empty tool slot in the multiplexer circuits

B1 ; Turn ON Machine

$H ; Homing :)
G10 P0 L20 X0Y0Z0 ; Force Reset current coordinates after homing


; The following gcode is the PCB trace laser marking gcode

M5 ; Being extra sure it won't light up before activation

; Getting and Activating Tool-1, The Tool.Laser
G00X165Y0Z10.5 ; Go to Tool-1 Home Pos
G00X188 ; Enter Female Kinematic Mount Home Pos
A1 ; Latch on Kinematic Mount
G4 P5 ; Wait for Kinematic Mount to fully attach
G00X92 ; Exit Female Kinematic Mount Home Pos
#TODO X0Y0Z0 ;  ;Add tool offset coordinate
C1 ; Choosing tool 1 in the choose demultiplexer circuits

F600 ; setting default feedrate

G00Z16 ; Moving to correct focal length Z position

S150 ; Setting Laser Power

Number of passes: 1

; Pass number: 0
G01 X20.279Y10.811
M3
G01 X23.071Y13.603
G01 X23.062Y13.641
G01 X23.055Y13.68
G01 X23.049Y13.72
G01 X23.046Y13.76
G01 X23.044Y13.801
G01 X23.045Y13.843
G01 X23.048Y13.886
G01 X23.053Y13.931
G01 X23.061Y13.976
G01 X23.072Y14.022
G01 X23.087Y14.07
G01 X23.106Y14.12
G01 X23.13Y14.172
G01 X23.16Y14.226
G01 X23.199Y14.284
G01 X23.25Y14.347
G01 X23.325Y14.42
G01 X23.538Y14.55
G01 X23.779Y14.608
G01 X23.884Y14.61
G01 X23.965Y14.602
G01 X24.034Y14.588
G01 X24.093Y14.571
G01 X24.147Y14.551
G01 X24.195Y14.53
G01 X24.24Y14.506
G01 X24.281Y14.481
G01 X24.318Y14.455
G01 X24.353Y14.428
G01 X24.386Y14.4
G01 X24.416Y14.37
G01 X24.444Y14.34
G01 X24.47Y14.309
G01 X24.494Y14.277
G01 X24.516Y14.244
G01 X24.537Y14.211
G01 X25.297Y14.211
G01 X25.379Y14.33
G01 X25.462Y14.414
G01 X25.544Y14.478
G01 X25.627Y14.528
G01 X25.709Y14.565
G01 X25.792Y14.591
G01 X25.875Y14.607
G01 X25.958Y14.616
G01 X26.041Y14.614
G01 X26.124Y14.605
G01 X26.207Y14.587
G01 X26.29Y14.558
G01 X26.373Y14.52
G01 X26.457Y14.469
G01 X26.54Y14.4
G01 X26.624Y14.308
G01 X26.707Y14.176
G01 X26.793Y13.822
G01 X26.713Y13.466
G01 X26.631Y13.333
G01 X26.548Y13.24
G01 X26.466Y13.171
G01 X26.383Y13.117
G01 X26.301Y13.078
G01 X26.218Y13.049
G01 X26.135Y13.029
G01 X26.052Y13.018
G01 X25.969Y13.016
G01 X25.886Y13.023
G01 X25.803Y13.039
G01 X25.72Y13.065
G01 X25.637Y13.1
G01 X25.554Y13.147
G01 X25.47Y13.21
G01 X25.387Y13.294
G01 X25.303Y13.411
G01 X24.537Y13.411
G01 X24.529Y13.398
G01 X24.521Y13.384
G01 X24.512Y13.371
G01 X24.503Y13.357
G01 X24.493Y13.343
G01 X24.482Y13.329
G01 X24.471Y13.314
G01 X24.459Y13.299
G01 X24.446Y13.284
G01 X24.431Y13.268
G01 X24.416Y13.251
G01 X24.399Y13.234
G01 X24.379Y13.216
G01 X24.357Y13.197
G01 X24.332Y13.177
G01 X24.3Y13.154
G01 X24.258Y13.127
G01 X24.15Y13.072
G01 X24.035Y13.034
G01 X23.985Y13.024
G01 X23.947Y13.018
G01 X23.914Y13.014
G01 X23.885Y13.012
G01 X23.859Y13.011
G01 X23.835Y13.011
G01 X23.812Y13.012
G01 X23.791Y13.013
G01 X23.771Y13.014
G01 X23.751Y13.016
G01 X23.733Y13.019
G01 X23.716Y13.021
G01 X23.699Y13.024
G01 X23.682Y13.028
G01 X23.666Y13.031
G01 X23.651Y13.035
G01 X23.636Y13.038
G01 X20.609Y10.011
G01 X20.609Y10.011
G01 X11.685Y10.011
G01 X9.998Y11.698
G01 X9.998Y16.024
G01 X12.109Y18.135
G01 X12.077Y18.293
G01 X12.073Y18.423
G01 X12.086Y18.536
G01 X12.111Y18.637
G01 X12.145Y18.728
G01 X12.188Y18.811
G01 X12.238Y18.887
G01 X12.294Y18.956
G01 X12.357Y19.018
G01 X12.427Y19.074
G01 X12.504Y19.123
G01 X12.588Y19.165
G01 X12.681Y19.198
G01 X12.783Y19.222
G01 X12.898Y19.233
G01 X13.03Y19.226
G01 X13.193Y19.189
G01 X13.523Y18.984
G01 X13.728Y18.653
G01 X13.765Y18.49
G01 X13.772Y18.358
G01 X13.76Y18.243
G01 X13.737Y18.141
G01 X13.703Y18.049
G01 X13.662Y17.964
G01 X13.613Y17.888
G01 X13.557Y17.818
G01 X13.494Y17.755
G01 X13.425Y17.698
G01 X13.349Y17.648
G01 X13.266Y17.606
G01 X13.175Y17.571
G01 X13.074Y17.547
G01 X12.961Y17.534
G01 X12.831Y17.538
G01 X12.673Y17.57
G01 X10.798Y15.694
G01 X10.798Y15.694
G01 X10.798Y12.03
G01 X12.017Y10.811
G01 X20.279Y10.811
M5
G01 X23.444Y18.167
M3
G01 X23.444Y18.706
G01 X23.395Y18.737
G01 X23.35Y18.77
G01 X23.307Y18.806
G01 X23.267Y18.845
G01 X23.229Y18.887
G01 X23.195Y18.932
G01 X23.163Y18.979
G01 X23.134Y19.03
G01 X23.109Y19.083
G01 X23.087Y19.14
G01 X23.069Y19.201
G01 X23.055Y19.267
G01 X23.046Y19.337
G01 X23.044Y19.414
G01 X23.05Y19.499
G01 X23.069Y19.597
G01 X23.11Y19.717
G01 X23.278Y19.965
G01 X23.526Y20.133
G01 X23.646Y20.174
G01 X23.744Y20.193
G01 X23.829Y20.199
G01 X23.906Y20.197
G01 X23.976Y20.188
G01 X24.042Y20.174
G01 X24.103Y20.156
G01 X24.16Y20.134
G01 X24.213Y20.109
G01 X24.264Y20.08
G01 X24.311Y20.048
G01 X24.356Y20.014
G01 X24.398Y19.976
G01 X24.437Y19.936
G01 X24.473Y19.893
G01 X24.506Y19.848
G01 X24.537Y19.799
G01 X25.297Y19.799
G01 X25.379Y19.918
G01 X25.462Y20.002
G01 X25.544Y20.066
G01 X25.627Y20.116
G01 X25.709Y20.153
G01 X25.792Y20.179
G01 X25.875Y20.195
G01 X25.958Y20.204
G01 X26.041Y20.202
G01 X26.124Y20.193
G01 X26.207Y20.175
G01 X26.29Y20.146
G01 X26.373Y20.108
G01 X26.457Y20.057
G01 X26.54Y19.988
G01 X26.624Y19.896
G01 X26.707Y19.764
G01 X26.793Y19.41
G01 X26.713Y19.054
G01 X26.631Y18.921
G01 X26.548Y18.828
G01 X26.466Y18.759
G01 X26.383Y18.705
G01 X26.301Y18.666
G01 X26.218Y18.637
G01 X26.135Y18.617
G01 X26.052Y18.606
G01 X25.969Y18.604
G01 X25.886Y18.611
G01 X25.803Y18.627
G01 X25.72Y18.653
G01 X25.637Y18.688
G01 X25.554Y18.735
G01 X25.47Y18.798
G01 X25.387Y18.882
G01 X25.303Y18.999
G01 X24.537Y18.999
G01 X24.534Y18.994
G01 X24.531Y18.989
G01 X24.527Y18.983
G01 X24.524Y18.978
G01 X24.52Y18.972
G01 X24.517Y18.966
G01 X24.513Y18.96
G01 X24.509Y18.954
G01 X24.504Y18.947
G01 X24.499Y18.94
G01 X24.494Y18.933
G01 X24.488Y18.925
G01 X24.482Y18.916
G01 X24.475Y18.907
G01 X24.467Y18.897
G01 X24.457Y18.885
G01 X24.444Y18.869
G01 X24.41Y18.833
G01 X24.374Y18.799
G01 X24.358Y18.786
G01 X24.346Y18.776
G01 X24.336Y18.768
G01 X24.327Y18.761
G01 X24.318Y18.755
G01 X24.31Y18.749
G01 X24.303Y18.744
G01 X24.296Y18.739
G01 X24.289Y18.734
G01 X24.283Y18.73
G01 X24.277Y18.726
G01 X24.271Y18.723
G01 X24.265Y18.719
G01 X24.26Y18.716
G01 X24.254Y18.712
G01 X24.249Y18.709
G01 X24.244Y18.706
G01 X24.244Y17.837
G01 X24.244Y17.837
G01 X17.418Y11.011
G01 X12.099Y11.011
G01 X10.998Y12.112
G01 X10.998Y15.334
G01 X11.907Y16.243
G01 X12.172Y16.243
G01 X12.257Y16.372
G01 X12.342Y16.465
G01 X12.429Y16.535
G01 X12.515Y16.589
G01 X12.603Y16.631
G01 X12.69Y16.661
G01 X12.778Y16.681
G01 X12.866Y16.691
G01 X12.954Y16.693
G01 X13.042Y16.684
G01 X13.131Y16.667
G01 X13.22Y16.639
G01 X13.31Y16.599
G01 X13.399Y16.546
G01 X13.49Y16.476
G01 X13.581Y16.38
G01 X13.673Y16.241
G01 X13.772Y15.867
G01 X13.694Y15.487
G01 X13.61Y15.343
G01 X13.524Y15.243
G01 X13.438Y15.168
G01 X13.351Y15.109
G01 X13.264Y15.065
G01 X13.177Y15.032
G01 X13.089Y15.01
G01 X13.002Y14.997
G01 X12.913Y14.993
G01 X12.825Y14.999
G01 X12.736Y15.014
G01 X12.647Y15.039
G01 X12.558Y15.075
G01 X12.468Y15.124
G01 X12.378Y15.19
G01 X12.287Y15.278
G01 X12.196Y15.402
G01 X11.798Y15.004
G01 X11.798Y15.004
G01 X11.798Y12.444
G01 X12.431Y11.811
G01 X17.088Y11.811
G01 X23.444Y18.167
M5
G01 X16.632Y12.811
M3
G01 X20.539Y16.718
G01 X20.539Y22.247
G01 X23.071Y24.779
G01 X23.062Y24.817
G01 X23.055Y24.856
G01 X23.049Y24.896
G01 X23.046Y24.936
G01 X23.044Y24.977
G01 X23.045Y25.019
G01 X23.048Y25.062
G01 X23.053Y25.107
G01 X23.061Y25.152
G01 X23.072Y25.198
G01 X23.087Y25.246
G01 X23.106Y25.296
G01 X23.13Y25.348
G01 X23.16Y25.402
G01 X23.199Y25.46
G01 X23.25Y25.523
G01 X23.325Y25.596
G01 X23.538Y25.726
G01 X23.779Y25.784
G01 X23.884Y25.786
G01 X23.965Y25.778
G01 X24.034Y25.764
G01 X24.093Y25.747
G01 X24.147Y25.727
G01 X24.195Y25.706
G01 X24.24Y25.682
G01 X24.281Y25.657
G01 X24.318Y25.631
G01 X24.353Y25.604
G01 X24.386Y25.576
G01 X24.416Y25.546
G01 X24.444Y25.516
G01 X24.47Y25.485
G01 X24.494Y25.453
G01 X24.516Y25.42
G01 X24.537Y25.387
G01 X25.297Y25.387
G01 X25.379Y25.506
G01 X25.462Y25.59
G01 X25.544Y25.654
G01 X25.627Y25.704
G01 X25.709Y25.741
G01 X25.792Y25.767
G01 X25.875Y25.783
G01 X25.958Y25.792
G01 X26.041Y25.79
G01 X26.124Y25.781
G01 X26.207Y25.763
G01 X26.29Y25.734
G01 X26.373Y25.696
G01 X26.457Y25.645
G01 X26.54Y25.576
G01 X26.624Y25.484
G01 X26.707Y25.352
G01 X26.793Y24.998
G01 X26.713Y24.642
G01 X26.631Y24.509
G01 X26.548Y24.416
G01 X26.466Y24.347
G01 X26.383Y24.293
G01 X26.301Y24.254
G01 X26.218Y24.225
G01 X26.135Y24.205
G01 X26.052Y24.194
G01 X25.969Y24.192
G01 X25.886Y24.199
G01 X25.803Y24.215
G01 X25.72Y24.241
G01 X25.637Y24.276
G01 X25.554Y24.323
G01 X25.47Y24.386
G01 X25.387Y24.47
G01 X25.303Y24.587
G01 X24.537Y24.587
G01 X24.529Y24.574
G01 X24.521Y24.56
G01 X24.512Y24.547
G01 X24.503Y24.533
G01 X24.493Y24.519
G01 X24.482Y24.505
G01 X24.471Y24.49
G01 X24.459Y24.475
G01 X24.446Y24.46
G01 X24.431Y24.444
G01 X24.416Y24.427
G01 X24.399Y24.41
G01 X24.379Y24.392
G01 X24.357Y24.373
G01 X24.332Y24.353
G01 X24.3Y24.33
G01 X24.258Y24.303
G01 X24.15Y24.248
G01 X24.035Y24.21
G01 X23.985Y24.2
G01 X23.947Y24.194
G01 X23.914Y24.19
G01 X23.885Y24.188
G01 X23.859Y24.187
G01 X23.835Y24.187
G01 X23.812Y24.188
G01 X23.791Y24.189
G01 X23.771Y24.19
G01 X23.751Y24.192
G01 X23.733Y24.195
G01 X23.716Y24.197
G01 X23.699Y24.2
G01 X23.682Y24.204
G01 X23.666Y24.207
G01 X23.651Y24.211
G01 X23.636Y24.214
G01 X21.339Y21.917
G01 X21.339Y21.917
G01 X21.339Y16.388
G01 X16.962Y12.011
G01 X13.648Y12.011
G01 X13.206Y12.453
G01 X12.072Y12.453
G01 X12.072Y14.153
G01 X13.772Y14.153
G01 X13.772Y13.019
G01 X13.98Y12.811
G01 X13.98Y12.811
G01 X16.632Y12.811
M5
G01 X42.663Y12.646
M3
G01 X41.602Y13.707
G01 X41.602Y15.511
G01 X35.061Y22.052
G01 X34.306Y22.052
G01 X34.223Y21.934
G01 X34.14Y21.85
G01 X34.057Y21.787
G01 X33.974Y21.738
G01 X33.891Y21.702
G01 X33.808Y21.676
G01 X33.725Y21.66
G01 X33.642Y21.653
G01 X33.559Y21.654
G01 X33.477Y21.664
G01 X33.394Y21.683
G01 X33.311Y21.711
G01 X33.228Y21.751
G01 X33.145Y21.803
G01 X33.062Y21.872
G01 X32.979Y21.964
G01 X32.896Y22.097
G01 X32.813Y22.452
G01 X32.896Y22.807
G01 X32.979Y22.94
G01 X33.062Y23.032
G01 X33.145Y23.101
G01 X33.228Y23.153
G01 X33.311Y23.193
G01 X33.394Y23.221
G01 X33.477Y23.24
G01 X33.559Y23.25
G01 X33.642Y23.251
G01 X33.725Y23.244
G01 X33.808Y23.228
G01 X33.891Y23.202
G01 X33.974Y23.166
G01 X34.057Y23.117
G01 X34.14Y23.054
G01 X34.223Y22.97
G01 X34.306Y22.852
G01 X35.393Y22.852
G01 X35.393Y22.852
G01 X42.402Y15.843
G01 X42.402Y14.039
G01 X42.995Y13.446
G01 X43.81Y13.446
G01 X45.778Y15.414
G01 X45.659Y15.507
G01 X45.575Y15.599
G01 X45.512Y15.689
G01 X45.465Y15.779
G01 X45.431Y15.869
G01 X45.408Y15.958
G01 X45.395Y16.046
G01 X45.391Y16.134
G01 X45.396Y16.222
G01 X45.411Y16.31
G01 X45.435Y16.397
G01 X45.469Y16.483
G01 X45.515Y16.569
G01 X45.574Y16.654
G01 X45.651Y16.739
G01 X45.753Y16.823
G01 X45.897Y16.904
G01 X46.278Y16.976
G01 X46.65Y16.872
G01 X46.787Y16.778
G01 X46.881Y16.686
G01 X46.95Y16.595
G01 X47.002Y16.505
G01 X47.041Y16.415
G01 X47.067Y16.326
G01 X47.084Y16.238
G01 X47.091Y16.149
G01 X47.088Y16.062
G01 X47.077Y15.974
G01 X47.056Y15.887
G01 X47.026Y15.8
G01 X46.984Y15.714
G01 X46.929Y15.629
G01 X46.859Y15.544
G01 X46.767Y15.46
G01 X46.641Y15.377
G01 X46.641Y15.147
G01 X46.641Y15.147
G01 X44.14Y12.646
G01 X42.663Y12.646
M5
G01 X24.293Y9.011
M3
G01 X11.271Y9.011
G01 X8.998Y11.284
G01 X8.998Y18.834
G01 X12.072Y21.908
G01 X12.072Y23.043
G01 X13.772Y23.043
G01 X13.772Y21.343
G01 X12.638Y21.343
G01 X9.798Y18.504
G01 X9.798Y18.504
G01 X9.798Y11.616
G01 X11.603Y9.811
G01 X23.963Y9.811
G01 X25.22Y11.068
G01 X25.214Y11.094
G01 X25.208Y11.119
G01 X25.204Y11.146
G01 X25.2Y11.173
G01 X25.196Y11.202
G01 X25.194Y11.231
G01 X25.193Y11.261
G01 X25.193Y11.293
G01 X25.195Y11.326
G01 X25.197Y11.36
G01 X25.202Y11.396
G01 X25.209Y11.434
G01 X25.218Y11.475
G01 X25.231Y11.52
G01 X25.248Y11.568
G01 X25.273Y11.624
G01 X25.311Y11.694
G01 X25.427Y11.842
G01 X25.575Y11.958
G01 X25.645Y11.996
G01 X25.701Y12.021
G01 X25.749Y12.038
G01 X25.794Y12.051
G01 X25.834Y12.06
G01 X25.873Y12.067
G01 X25.909Y12.072
G01 X25.943Y12.074
G01 X25.976Y12.076
G01 X26.008Y12.076
G01 X26.038Y12.075
G01 X26.067Y12.073
G01 X26.096Y12.069
G01 X26.123Y12.065
G01 X26.15Y12.061
G01 X26.175Y12.055
G01 X26.201Y12.049
G01 X27.127Y12.975
G01 X27.127Y15.164
G01 X26.2Y16.091
G01 X26.058Y16.067
G01 X25.94Y16.066
G01 X25.836Y16.079
G01 X25.743Y16.104
G01 X25.659Y16.137
G01 X25.582Y16.177
G01 X25.512Y16.225
G01 X25.448Y16.278
G01 X25.391Y16.338
G01 X25.339Y16.403
G01 X25.294Y16.475
G01 X25.255Y16.554
G01 X25.225Y16.641
G01 X25.203Y16.737
G01 X25.193Y16.844
G01 X25.2Y16.968
G01 X25.235Y17.12
G01 X25.427Y17.43
G01 X25.737Y17.622
G01 X25.889Y17.657
G01 X26.013Y17.664
G01 X26.12Y17.654
G01 X26.216Y17.632
G01 X26.303Y17.602
G01 X26.382Y17.563
G01 X26.454Y17.518
G01 X26.519Y17.466
G01 X26.579Y17.409
G01 X26.632Y17.345
G01 X26.68Y17.275
G01 X26.72Y17.198
G01 X26.753Y17.114
G01 X26.777Y17.021
G01 X26.791Y16.917
G01 X26.79Y16.799
G01 X26.766Y16.657
G01 X27.127Y16.296
G01 X27.127Y16.296
G01 X27.127Y20.752
G01 X26.2Y21.679
G01 X26.058Y21.655
G01 X25.94Y21.654
G01 X25.836Y21.668
G01 X25.743Y21.692
G01 X25.659Y21.725
G01 X25.582Y21.765
G01 X25.512Y21.813
G01 X25.448Y21.866
G01 X25.391Y21.926
G01 X25.339Y21.991
G01 X25.294Y22.063
G01 X25.255Y22.142
G01 X25.225Y22.229
G01 X25.203Y22.325
G01 X25.193Y22.432
G01 X25.2Y22.556
G01 X25.235Y22.708
G01 X25.427Y23.018
G01 X25.737Y23.21
G01 X25.889Y23.245
G01 X26.013Y23.252
G01 X26.12Y23.242
G01 X26.216Y23.22
G01 X26.303Y23.19
G01 X26.382Y23.151
G01 X26.454Y23.106
G01 X26.519Y23.054
G01 X26.579Y22.997
G01 X26.632Y22.933
G01 X26.68Y22.863
G01 X26.72Y22.786
G01 X26.753Y22.702
G01 X26.777Y22.609
G01 X26.791Y22.505
G01 X26.79Y22.387
G01 X26.766Y22.245
G01 X27.927Y21.084
G01 X27.927Y21.084
G01 X27.927Y15.33
G01 X27.927Y12.645
G01 X26.766Y11.484
G01 X26.772Y11.458
G01 X26.778Y11.433
G01 X26.782Y11.406
G01 X26.786Y11.379
G01 X26.79Y11.35
G01 X26.792Y11.321
G01 X26.793Y11.291
G01 X26.793Y11.259
G01 X26.791Y11.226
G01 X26.789Y11.192
G01 X26.784Y11.156
G01 X26.777Y11.117
G01 X26.768Y11.077
G01 X26.755Y11.032
G01 X26.738Y10.984
G01 X26.713Y10.928
G01 X26.675Y10.858
G01 X26.559Y10.71
G01 X26.411Y10.594
G01 X26.341Y10.556
G01 X26.285Y10.531
G01 X26.237Y10.514
G01 X26.192Y10.501
G01 X26.151Y10.492
G01 X26.113Y10.485
G01 X26.077Y10.48
G01 X26.043Y10.478
G01 X26.01Y10.476
G01 X25.978Y10.476
G01 X25.948Y10.477
G01 X25.919Y10.479
G01 X25.89Y10.483
G01 X25.863Y10.487
G01 X25.836Y10.491
G01 X25.811Y10.497
G01 X25.785Y10.503
G01 X24.293Y9.011
M5
G01 X15.824Y20.092
M3
G01 X15.824Y24.294
G01 X15.819Y24.297
G01 X15.814Y24.3
G01 X15.808Y24.304
G01 X15.803Y24.307
G01 X15.797Y24.311
G01 X15.791Y24.314
G01 X15.785Y24.318
G01 X15.779Y24.322
G01 X15.772Y24.327
G01 X15.765Y24.332
G01 X15.758Y24.337
G01 X15.75Y24.343
G01 X15.741Y24.349
G01 X15.732Y24.356
G01 X15.722Y24.364
G01 X15.71Y24.374
G01 X15.694Y24.387
G01 X15.658Y24.421
G01 X15.624Y24.457
G01 X15.611Y24.473
G01 X15.601Y24.485
G01 X15.593Y24.495
G01 X15.586Y24.504
G01 X15.58Y24.513
G01 X15.574Y24.521
G01 X15.569Y24.528
G01 X15.564Y24.535
G01 X15.559Y24.542
G01 X15.555Y24.548
G01 X15.551Y24.554
G01 X15.547Y24.56
G01 X15.544Y24.566
G01 X15.541Y24.571
G01 X15.537Y24.577
G01 X15.534Y24.582
G01 X15.531Y24.587
G01 X13.759Y24.587
G01 X13.72Y24.44
G01 X13.668Y24.325
G01 X13.609Y24.232
G01 X13.544Y24.153
G01 X13.474Y24.087
G01 X13.401Y24.031
G01 X13.324Y23.984
G01 X13.244Y23.946
G01 X13.161Y23.917
G01 X13.075Y23.897
G01 X12.985Y23.885
G01 X12.892Y23.884
G01 X12.795Y23.893
G01 X12.693Y23.914
G01 X12.585Y23.953
G01 X12.469Y24.014
G01 X12.337Y24.116
G01 X12.124Y24.439
G01 X12.077Y24.823
G01 X12.111Y24.987
G01 X12.16Y25.109
G01 X12.217Y25.208
G01 X12.28Y25.291
G01 X12.348Y25.36
G01 X12.421Y25.419
G01 X12.496Y25.469
G01 X12.575Y25.509
G01 X12.658Y25.541
G01 X12.743Y25.564
G01 X12.831Y25.578
G01 X12.924Y25.583
G01 X13.019Y25.577
G01 X13.12Y25.56
G01 X13.226Y25.527
G01 X13.339Y25.474
G01 X13.465Y25.387
G01 X15.531Y25.387
G01 X15.562Y25.436
G01 X15.595Y25.481
G01 X15.631Y25.524
G01 X15.67Y25.564
G01 X15.712Y25.602
G01 X15.757Y25.636
G01 X15.804Y25.668
G01 X15.855Y25.697
G01 X15.908Y25.722
G01 X15.965Y25.744
G01 X16.026Y25.762
G01 X16.092Y25.776
G01 X16.162Y25.785
G01 X16.239Y25.787
G01 X16.324Y25.781
G01 X16.422Y25.762
G01 X16.542Y25.721
G01 X16.79Y25.553
G01 X16.958Y25.305
G01 X16.999Y25.185
G01 X17.018Y25.087
G01 X17.024Y25.002
G01 X17.022Y24.925
G01 X17.013Y24.855
G01 X16.999Y24.789
G01 X16.981Y24.728
G01 X16.959Y24.671
G01 X16.934Y24.618
G01 X16.905Y24.567
G01 X16.873Y24.52
G01 X16.839Y24.475
G01 X16.801Y24.433
G01 X16.761Y24.394
G01 X16.718Y24.358
G01 X16.673Y24.325
G01 X16.624Y24.294
G01 X16.624Y20.092
G01 X16.646Y20.079
G01 X16.668Y20.064
G01 X16.691Y20.049
G01 X16.713Y20.032
G01 X16.735Y20.014
G01 X16.757Y19.995
G01 X16.78Y19.975
G01 X16.802Y19.952
G01 X16.824Y19.928
G01 X16.846Y19.902
G01 X16.868Y19.873
G01 X16.891Y19.841
G01 X16.913Y19.806
G01 X16.935Y19.766
G01 X16.957Y19.719
G01 X16.98Y19.662
G01 X17.002Y19.586
G01 X17.024Y19.399
G01 X17.002Y19.212
G01 X16.98Y19.136
G01 X16.957Y19.079
G01 X16.935Y19.032
G01 X16.913Y18.992
G01 X16.891Y18.957
G01 X16.868Y18.925
G01 X16.846Y18.896
G01 X16.824Y18.87
G01 X16.802Y18.846
G01 X16.78Y18.823
G01 X16.757Y18.803
G01 X16.735Y18.784
G01 X16.713Y18.766
G01 X16.691Y18.749
G01 X16.668Y18.734
G01 X16.646Y18.719
G01 X16.624Y18.706
G01 X16.624Y14.504
G01 X16.742Y14.421
G01 X16.826Y14.338
G01 X16.889Y14.255
G01 X16.938Y14.172
G01 X16.974Y14.089
G01 X17.0Y14.006
G01 X17.016Y13.923
G01 X17.023Y13.84
G01 X17.022Y13.757
G01 X17.012Y13.675
G01 X16.993Y13.592
G01 X16.965Y13.509
G01 X16.925Y13.426
G01 X16.873Y13.343
G01 X16.804Y13.26
G01 X16.712Y13.177
G01 X16.579Y13.094
G01 X16.224Y13.011
G01 X15.869Y13.094
G01 X15.736Y13.177
G01 X15.644Y13.26
G01 X15.575Y13.343
G01 X15.523Y13.426
G01 X15.483Y13.509
G01 X15.455Y13.592
G01 X15.436Y13.675
G01 X15.426Y13.757
G01 X15.425Y13.84
G01 X15.432Y13.923
G01 X15.448Y14.006
G01 X15.474Y14.089
G01 X15.51Y14.172
G01 X15.559Y14.255
G01 X15.622Y14.338
G01 X15.706Y14.421
G01 X15.824Y14.504
G01 X15.824Y18.706
G01 X15.824Y18.706
G01 X15.802Y18.719
G01 X15.78Y18.734
G01 X15.757Y18.749
G01 X15.735Y18.766
G01 X15.713Y18.784
G01 X15.691Y18.803
G01 X15.668Y18.823
G01 X15.646Y18.846
G01 X15.624Y18.87
G01 X15.602Y18.896
G01 X15.58Y18.925
G01 X15.557Y18.957
G01 X15.535Y18.992
G01 X15.513Y19.032
G01 X15.491Y19.079
G01 X15.468Y19.136
G01 X15.446Y19.212
G01 X15.424Y19.399
G01 X15.446Y19.586
G01 X15.468Y19.662
G01 X15.491Y19.719
G01 X15.513Y19.766
G01 X15.535Y19.806
G01 X15.557Y19.841
G01 X15.58Y19.873
G01 X15.602Y19.902
G01 X15.624Y19.928
G01 X15.646Y19.952
G01 X15.668Y19.975
G01 X15.691Y19.995
G01 X15.713Y20.014
G01 X15.735Y20.032
G01 X15.757Y20.049
G01 X15.78Y20.064
G01 X15.802Y20.079
G01 X15.824Y20.092
M5
G01 X43.802Y18.706
M3
G01 X43.802Y15.139
G01 X43.92Y15.056
G01 X44.004Y14.973
G01 X44.067Y14.89
G01 X44.116Y14.807
G01 X44.152Y14.724
G01 X44.178Y14.641
G01 X44.194Y14.558
G01 X44.201Y14.475
G01 X44.2Y14.392
G01 X44.19Y14.31
G01 X44.171Y14.227
G01 X44.143Y14.144
G01 X44.103Y14.061
G01 X44.051Y13.978
G01 X43.982Y13.895
G01 X43.89Y13.812
G01 X43.757Y13.729
G01 X43.402Y13.646
G01 X43.047Y13.729
G01 X42.914Y13.812
G01 X42.822Y13.895
G01 X42.753Y13.978
G01 X42.701Y14.061
G01 X42.661Y14.144
G01 X42.633Y14.227
G01 X42.614Y14.31
G01 X42.604Y14.392
G01 X42.603Y14.475
G01 X42.61Y14.558
G01 X42.626Y14.641
G01 X42.652Y14.724
G01 X42.688Y14.807
G01 X42.737Y14.89
G01 X42.8Y14.973
G01 X42.884Y15.056
G01 X43.002Y15.139
G01 X43.002Y18.706
G01 X42.98Y18.719
G01 X42.958Y18.734
G01 X42.935Y18.749
G01 X42.913Y18.766
G01 X42.891Y18.784
G01 X42.869Y18.803
G01 X42.846Y18.823
G01 X42.824Y18.846
G01 X42.802Y18.87
G01 X42.78Y18.896
G01 X42.758Y18.925
G01 X42.735Y18.957
G01 X42.713Y18.992
G01 X42.691Y19.032
G01 X42.669Y19.079
G01 X42.646Y19.136
G01 X42.624Y19.212
G01 X42.602Y19.399
G01 X42.624Y19.586
G01 X42.646Y19.662
G01 X42.669Y19.719
G01 X42.691Y19.766
G01 X42.713Y19.806
G01 X42.735Y19.841
G01 X42.758Y19.873
G01 X42.78Y19.902
G01 X42.802Y19.928
G01 X42.824Y19.952
G01 X42.846Y19.975
G01 X42.869Y19.995
G01 X42.891Y20.014
G01 X42.913Y20.032
G01 X42.935Y20.049
G01 X42.958Y20.064
G01 X42.98Y20.079
G01 X43.002Y20.092
G01 X43.002Y24.294
G01 X42.953Y24.325
G01 X42.908Y24.358
G01 X42.865Y24.394
G01 X42.825Y24.433
G01 X42.787Y24.475
G01 X42.753Y24.52
G01 X42.721Y24.567
G01 X42.692Y24.618
G01 X42.667Y24.671
G01 X42.645Y24.728
G01 X42.627Y24.789
G01 X42.613Y24.855
G01 X42.604Y24.925
G01 X42.602Y25.002
G01 X42.608Y25.087
G01 X42.627Y25.185
G01 X42.668Y25.305
G01 X42.836Y25.553
G01 X43.084Y25.721
G01 X43.204Y25.762
G01 X43.302Y25.781
G01 X43.387Y25.787
G01 X43.464Y25.785
G01 X43.534Y25.776
G01 X43.6Y25.762
G01 X43.661Y25.744
G01 X43.718Y25.722
G01 X43.771Y25.697
G01 X43.822Y25.668
G01 X43.869Y25.636
G01 X43.914Y25.602
G01 X43.956Y25.564
G01 X43.995Y25.524
G01 X44.031Y25.481
G01 X44.064Y25.436
G01 X44.095Y25.387
G01 X45.391Y25.387
G01 X45.391Y25.613
G01 X47.091Y25.613
G01 X47.091Y23.913
G01 X45.391Y23.913
G01 X45.391Y24.587
G01 X44.095Y24.587
G01 X44.092Y24.582
G01 X44.089Y24.577
G01 X44.085Y24.571
G01 X44.082Y24.566
G01 X44.078Y24.56
G01 X44.075Y24.554
G01 X44.071Y24.548
G01 X44.067Y24.542
G01 X44.062Y24.535
G01 X44.057Y24.528
G01 X44.052Y24.521
G01 X44.046Y24.513
G01 X44.04Y24.504
G01 X44.033Y24.495
G01 X44.025Y24.485
G01 X44.015Y24.473
G01 X44.002Y24.457
G01 X43.968Y24.421
G01 X43.932Y24.387
G01 X43.916Y24.374
G01 X43.904Y24.364
G01 X43.894Y24.356
G01 X43.885Y24.349
G01 X43.876Y24.343
G01 X43.868Y24.337
G01 X43.861Y24.332
G01 X43.854Y24.327
G01 X43.847Y24.322
G01 X43.841Y24.318
G01 X43.835Y24.314
G01 X43.829Y24.311
G01 X43.823Y24.307
G01 X43.818Y24.304
G01 X43.812Y24.3
G01 X43.807Y24.297
G01 X43.802Y24.294
G01 X43.802Y20.092
G01 X43.802Y20.092
G01 X43.824Y20.079
G01 X43.846Y20.064
G01 X43.869Y20.049
G01 X43.891Y20.032
G01 X43.913Y20.014
G01 X43.935Y19.995
G01 X43.958Y19.975
G01 X43.98Y19.952
G01 X44.002Y19.928
G01 X44.024Y19.902
G01 X44.046Y19.873
G01 X44.069Y19.841
G01 X44.091Y19.806
G01 X44.113Y19.766
G01 X44.135Y19.719
G01 X44.158Y19.662
G01 X44.18Y19.586
G01 X44.202Y19.399
G01 X44.18Y19.212
G01 X44.158Y19.136
G01 X44.135Y19.079
G01 X44.113Y19.032
G01 X44.091Y18.992
G01 X44.069Y18.957
G01 X44.046Y18.925
G01 X44.024Y18.896
G01 X44.002Y18.87
G01 X43.98Y18.846
G01 X43.958Y18.823
G01 X43.935Y18.803
G01 X43.913Y18.784
G01 X43.891Y18.766
G01 X43.869Y18.749
G01 X43.846Y18.734
G01 X43.824Y18.719
G01 X43.802Y18.706
M5
G01 X37.431Y16.464
M3
G01 X34.306Y16.464
G01 X34.223Y16.346
G01 X34.14Y16.262
G01 X34.057Y16.199
G01 X33.974Y16.15
G01 X33.891Y16.114
G01 X33.808Y16.088
G01 X33.725Y16.072
G01 X33.642Y16.065
G01 X33.559Y16.066
G01 X33.477Y16.076
G01 X33.394Y16.095
G01 X33.311Y16.123
G01 X33.228Y16.163
G01 X33.145Y16.215
G01 X33.062Y16.284
G01 X32.979Y16.376
G01 X32.896Y16.509
G01 X32.813Y16.864
G01 X32.896Y17.219
G01 X32.979Y17.352
G01 X33.062Y17.444
G01 X33.145Y17.513
G01 X33.228Y17.565
G01 X33.311Y17.605
G01 X33.394Y17.633
G01 X33.477Y17.652
G01 X33.559Y17.662
G01 X33.642Y17.663
G01 X33.725Y17.656
G01 X33.808Y17.64
G01 X33.891Y17.614
G01 X33.974Y17.578
G01 X34.057Y17.529
G01 X34.14Y17.466
G01 X34.223Y17.382
G01 X34.306Y17.264
G01 X37.763Y17.264
G01 X37.763Y17.264
G01 X44.558Y10.469
G01 X45.491Y10.469
G01 X45.58Y10.603
G01 X45.669Y10.698
G01 X45.758Y10.768
G01 X45.847Y10.822
G01 X45.935Y10.862
G01 X46.024Y10.891
G01 X46.113Y10.909
G01 X46.202Y10.918
G01 X46.291Y10.918
G01 X46.38Y10.908
G01 X46.469Y10.888
G01 X46.558Y10.858
G01 X46.647Y10.816
G01 X46.735Y10.76
G01 X46.824Y10.687
G01 X46.913Y10.589
G01 X47.002Y10.447
G01 X47.091Y10.069
G01 X47.002Y9.691
G01 X46.913Y9.549
G01 X46.824Y9.451
G01 X46.735Y9.378
G01 X46.647Y9.322
G01 X46.558Y9.28
G01 X46.469Y9.25
G01 X46.38Y9.23
G01 X46.291Y9.22
G01 X46.202Y9.22
G01 X46.113Y9.229
G01 X46.024Y9.247
G01 X45.935Y9.276
G01 X45.847Y9.316
G01 X45.758Y9.37
G01 X45.669Y9.44
G01 X45.58Y9.535
G01 X45.491Y9.669
G01 X44.226Y9.669
G01 X44.226Y9.669
G01 X37.431Y16.464
M5
G01 X34.306Y11.676
M3
G01 X35.393Y11.676
G01 X42.734Y4.335
G01 X45.491Y4.335
G01 X45.58Y4.469
G01 X45.669Y4.564
G01 X45.758Y4.634
G01 X45.847Y4.688
G01 X45.935Y4.728
G01 X46.024Y4.757
G01 X46.113Y4.775
G01 X46.202Y4.784
G01 X46.291Y4.784
G01 X46.38Y4.774
G01 X46.469Y4.754
G01 X46.558Y4.724
G01 X46.647Y4.682
G01 X46.735Y4.626
G01 X46.824Y4.553
G01 X46.913Y4.455
G01 X47.002Y4.313
G01 X47.091Y3.935
G01 X47.002Y3.557
G01 X46.913Y3.415
G01 X46.824Y3.317
G01 X46.735Y3.244
G01 X46.647Y3.188
G01 X46.558Y3.146
G01 X46.469Y3.116
G01 X46.38Y3.096
G01 X46.291Y3.086
G01 X46.202Y3.086
G01 X46.113Y3.095
G01 X46.024Y3.113
G01 X45.935Y3.142
G01 X45.847Y3.182
G01 X45.758Y3.236
G01 X45.669Y3.306
G01 X45.58Y3.401
G01 X45.491Y3.535
G01 X42.402Y3.535
G01 X42.402Y3.535
G01 X35.061Y10.876
G01 X34.306Y10.876
G01 X34.223Y10.758
G01 X34.14Y10.674
G01 X34.057Y10.611
G01 X33.974Y10.562
G01 X33.891Y10.526
G01 X33.808Y10.5
G01 X33.725Y10.484
G01 X33.642Y10.477
G01 X33.559Y10.478
G01 X33.477Y10.488
G01 X33.394Y10.507
G01 X33.311Y10.535
G01 X33.228Y10.575
G01 X33.145Y10.627
G01 X33.062Y10.696
G01 X32.979Y10.788
G01 X32.896Y10.921
G01 X32.813Y11.276
G01 X32.896Y11.631
G01 X32.979Y11.764
G01 X33.062Y11.856
G01 X33.145Y11.925
G01 X33.228Y11.977
G01 X33.311Y12.017
G01 X33.394Y12.045
G01 X33.477Y12.064
G01 X33.559Y12.074
G01 X33.642Y12.075
G01 X33.725Y12.068
G01 X33.808Y12.052
G01 X33.891Y12.026
G01 X33.974Y11.99
G01 X34.057Y11.941
G01 X34.14Y11.878
G01 X34.223Y11.794
G01 X34.306Y11.676
M5
G01 X34.413Y25.392
M3
G01 X35.092Y25.392
G01 X35.176Y25.509
G01 X35.259Y25.593
G01 X35.343Y25.656
G01 X35.426Y25.703
G01 X35.509Y25.738
G01 X35.592Y25.764
G01 X35.675Y25.78
G01 X35.758Y25.787
G01 X35.841Y25.785
G01 X35.924Y25.774
G01 X36.007Y25.754
G01 X36.09Y25.725
G01 X36.172Y25.686
G01 X36.255Y25.632
G01 X36.337Y25.563
G01 X36.42Y25.47
G01 X36.502Y25.337
G01 X36.582Y24.981
G01 X36.496Y24.627
G01 X36.413Y24.495
G01 X36.329Y24.403
G01 X36.246Y24.334
G01 X36.162Y24.283
G01 X36.079Y24.245
G01 X35.996Y24.216
G01 X35.913Y24.198
G01 X35.83Y24.189
G01 X35.747Y24.187
G01 X35.664Y24.196
G01 X35.581Y24.212
G01 X35.498Y24.238
G01 X35.416Y24.275
G01 X35.333Y24.325
G01 X35.251Y24.389
G01 X35.168Y24.473
G01 X35.086Y24.592
G01 X34.413Y24.592
G01 X34.413Y24.192
G01 X32.813Y24.192
G01 X32.813Y25.792
G01 X34.413Y25.792
G01 X34.413Y25.392
M5
G01 X35.086Y19.004
M3
G01 X34.413Y19.004
G01 X34.413Y18.604
G01 X32.813Y18.604
G01 X32.813Y20.204
G01 X34.413Y20.204
G01 X34.413Y19.804
G01 X35.092Y19.804
G01 X35.176Y19.921
G01 X35.259Y20.005
G01 X35.343Y20.068
G01 X35.426Y20.115
G01 X35.509Y20.15
G01 X35.592Y20.176
G01 X35.675Y20.192
G01 X35.758Y20.199
G01 X35.841Y20.197
G01 X35.924Y20.186
G01 X36.007Y20.166
G01 X36.09Y20.137
G01 X36.172Y20.098
G01 X36.255Y20.044
G01 X36.337Y19.975
G01 X36.42Y19.882
G01 X36.502Y19.749
G01 X36.582Y19.393
G01 X36.496Y19.039
G01 X36.413Y18.907
G01 X36.329Y18.815
G01 X36.246Y18.746
G01 X36.162Y18.695
G01 X36.079Y18.657
G01 X35.996Y18.628
G01 X35.913Y18.61
G01 X35.83Y18.601
G01 X35.747Y18.599
G01 X35.664Y18.608
G01 X35.581Y18.624
G01 X35.498Y18.65
G01 X35.416Y18.687
G01 X35.333Y18.737
G01 X35.251Y18.801
G01 X35.168Y18.885
G01 X35.086Y19.004
M5
G01 X34.078Y14.846
M3
G01 X35.089Y14.846
G01 X35.172Y14.964
G01 X35.255Y15.048
G01 X35.338Y15.111
G01 X35.421Y15.16
G01 X35.504Y15.196
G01 X35.587Y15.222
G01 X35.67Y15.238
G01 X35.753Y15.245
G01 X35.836Y15.244
G01 X35.918Y15.234
G01 X36.001Y15.215
G01 X36.084Y15.187
G01 X36.167Y15.147
G01 X36.25Y15.095
G01 X36.333Y15.026
G01 X36.416Y14.934
G01 X36.499Y14.801
G01 X36.582Y14.446
G01 X36.499Y14.091
G01 X36.416Y13.958
G01 X36.333Y13.866
G01 X36.25Y13.797
G01 X36.167Y13.745
G01 X36.084Y13.705
G01 X36.001Y13.677
G01 X35.918Y13.658
G01 X35.836Y13.648
G01 X35.753Y13.647
G01 X35.67Y13.654
G01 X35.587Y13.67
G01 X35.504Y13.696
G01 X35.421Y13.732
G01 X35.338Y13.781
G01 X35.255Y13.844
G01 X35.172Y13.928
G01 X35.089Y14.046
G01 X34.413Y14.046
G01 X34.413Y13.016
G01 X32.813Y13.016
G01 X32.813Y14.616
G01 X33.848Y14.616
G01 X34.078Y14.846
G01 X34.078Y14.846
M5
G01 X45.841Y19.517
M3
G01 X45.841Y21.473
G01 X45.707Y21.562
G01 X45.612Y21.651
G01 X45.542Y21.74
G01 X45.488Y21.829
G01 X45.448Y21.917
G01 X45.419Y22.006
G01 X45.401Y22.095
G01 X45.392Y22.184
G01 X45.392Y22.273
G01 X45.402Y22.362
G01 X45.422Y22.451
G01 X45.452Y22.54
G01 X45.494Y22.629
G01 X45.55Y22.717
G01 X45.623Y22.806
G01 X45.721Y22.895
G01 X45.863Y22.984
G01 X46.241Y23.073
G01 X46.619Y22.984
G01 X46.761Y22.895
G01 X46.859Y22.806
G01 X46.932Y22.717
G01 X46.988Y22.629
G01 X47.03Y22.54
G01 X47.06Y22.451
G01 X47.08Y22.362
G01 X47.09Y22.273
G01 X47.09Y22.184
G01 X47.081Y22.095
G01 X47.063Y22.006
G01 X47.034Y21.917
G01 X46.994Y21.829
G01 X46.94Y21.74
G01 X46.87Y21.651
G01 X46.775Y21.562
G01 X46.641Y21.473
G01 X46.641Y19.517
G01 X47.091Y19.517
G01 X47.091Y18.383
G01 X48.091Y17.383
G01 X48.091Y17.383
G01 X48.091Y13.894
G01 X47.091Y12.894
G01 X47.091Y12.324
G01 X48.091Y11.325
G01 X48.091Y11.325
G01 X48.091Y7.76
G01 X47.091Y6.761
G01 X47.091Y5.625
G01 X45.391Y5.625
G01 X45.391Y7.325
G01 X46.526Y7.325
G01 X47.291Y8.09
G01 X47.291Y8.09
G01 X47.291Y10.993
G01 X46.525Y11.759
G01 X45.391Y11.759
G01 X45.391Y13.459
G01 X46.526Y13.459
G01 X47.291Y14.224
G01 X47.291Y14.224
G01 X47.291Y17.051
G01 X46.525Y17.817
G01 X45.391Y17.817
G01 X45.391Y19.517
G01 X45.841Y19.517
M5
G01 X2.0Y2.0
M3
G01 X56.991Y2.0
G01 X56.991Y26.765
G01 X2.0Y26.765
G01 X2.0Y2.0
M5

M5 ; Disable End-Effector Signal

; Returning the Deactivating Tool-1
C0 ; PWM Tool select demultiplexer to select tool zero which is the empty tool slot in multiplexers
#TODO X0Y0Z0 ;  ;Remove tool offset coordinate
G00X165Y0Z10.5 ; Go to Tool-1 Home Pos
G00X92 ; Enter Female Kinematic Mount Home Pos
A0 ; Latch OFF Kinematic Mount
G4 P5 ; Wait for Kinematic Mount to fully detach
G00X188 ; Exit Female Kinematic Mount Home Pos

; Machine deinitialization Sequence... 

G00X0Y0Z0
B0 ; Turn Machine OFF