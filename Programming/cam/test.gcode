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
G01 X33.861Y26.53
M3
G01 X34.965Y27.634
G01 X34.965Y31.334
G01 X33.414Y32.885
G01 X11.055Y32.885
G01 X8.86Y30.69
G01 X8.86Y30.055
G01 X8.985Y30.055
G01 X8.985Y28.555
G01 X8.86Y28.555
G01 X8.86Y27.34
G01 X8.86Y27.34
G01 X7.811Y26.291
G01 X7.818Y26.257
G01 X7.824Y26.221
G01 X7.828Y26.186
G01 X7.83Y26.149
G01 X7.83Y26.112
G01 X7.828Y26.073
G01 X7.824Y26.034
G01 X7.819Y25.994
G01 X7.81Y25.953
G01 X7.799Y25.911
G01 X7.784Y25.868
G01 X7.766Y25.823
G01 X7.744Y25.776
G01 X7.715Y25.727
G01 X7.679Y25.674
G01 X7.632Y25.617
G01 X7.562Y25.55
G01 X7.367Y25.432
G01 X7.146Y25.378
G01 X7.05Y25.376
G01 X6.976Y25.382
G01 X6.913Y25.394
G01 X6.858Y25.409
G01 X6.809Y25.426
G01 X6.764Y25.445
G01 X6.723Y25.465
G01 X6.686Y25.487
G01 X6.651Y25.51
G01 X6.618Y25.534
G01 X6.588Y25.559
G01 X6.56Y25.585
G01 X6.533Y25.611
G01 X6.509Y25.639
G01 X6.486Y25.667
G01 X6.465Y25.696
G01 X6.446Y25.725
G01 X5.23Y25.725
G01 X5.146Y25.608
G01 X5.063Y25.524
G01 X4.979Y25.461
G01 X4.896Y25.414
G01 X4.813Y25.379
G01 X4.73Y25.353
G01 X4.647Y25.337
G01 X4.564Y25.33
G01 X4.481Y25.332
G01 X4.398Y25.343
G01 X4.315Y25.363
G01 X4.232Y25.392
G01 X4.15Y25.431
G01 X4.067Y25.485
G01 X3.985Y25.554
G01 X3.902Y25.647
G01 X3.82Y25.78
G01 X3.74Y26.136
G01 X3.826Y26.49
G01 X3.909Y26.622
G01 X3.993Y26.714
G01 X4.076Y26.783
G01 X4.16Y26.834
G01 X4.243Y26.872
G01 X4.326Y26.901
G01 X4.409Y26.919
G01 X4.492Y26.928
G01 X4.575Y26.93
G01 X4.658Y26.921
G01 X4.741Y26.905
G01 X4.824Y26.879
G01 X4.906Y26.842
G01 X4.989Y26.792
G01 X5.071Y26.728
G01 X5.154Y26.644
G01 X5.236Y26.525
G01 X6.446Y26.525
G01 X6.453Y26.536
G01 X6.461Y26.548
G01 X6.469Y26.559
G01 X6.477Y26.571
G01 X6.486Y26.583
G01 X6.496Y26.596
G01 X6.506Y26.608
G01 X6.518Y26.621
G01 X6.529Y26.634
G01 X6.542Y26.648
G01 X6.557Y26.662
G01 X6.572Y26.677
G01 X6.589Y26.692
G01 X6.609Y26.709
G01 X6.632Y26.726
G01 X6.66Y26.746
G01 X6.698Y26.77
G01 X6.793Y26.818
G01 X6.895Y26.852
G01 X6.938Y26.861
G01 X6.972Y26.867
G01 X7.001Y26.871
G01 X7.026Y26.873
G01 X7.05Y26.874
G01 X7.071Y26.875
G01 X7.091Y26.875
G01 X7.11Y26.874
G01 X7.128Y26.873
G01 X7.144Y26.872
G01 X7.161Y26.871
G01 X7.176Y26.869
G01 X7.191Y26.867
G01 X7.206Y26.864
G01 X7.22Y26.862
G01 X7.233Y26.859
G01 X7.246Y26.856
G01 X8.06Y27.67
G01 X8.06Y27.67
G01 X8.06Y28.555
G01 X7.935Y28.555
G01 X7.935Y30.055
G01 X8.06Y30.055
G01 X8.06Y31.02
G01 X8.06Y31.02
G01 X10.725Y33.685
G01 X33.58Y33.685
G01 X40.631Y33.685
G01 X44.961Y29.355
G01 X45.254Y29.457
G01 X45.472Y29.484
G01 X45.656Y29.477
G01 X45.818Y29.448
G01 X45.963Y29.402
G01 X46.095Y29.342
G01 X46.215Y29.271
G01 X46.324Y29.188
G01 X46.422Y29.095
G01 X46.51Y28.992
G01 X46.587Y28.878
G01 X46.653Y28.753
G01 X46.706Y28.614
G01 X46.744Y28.462
G01 X46.764Y28.29
G01 X46.757Y28.091
G01 X46.703Y27.847
G01 X46.399Y27.351
G01 X45.903Y27.047
G01 X45.659Y26.993
G01 X45.46Y26.986
G01 X45.288Y27.006
G01 X45.136Y27.044
G01 X44.997Y27.097
G01 X44.872Y27.163
G01 X44.758Y27.24
G01 X44.655Y27.328
G01 X44.562Y27.426
G01 X44.479Y27.535
G01 X44.408Y27.655
G01 X44.348Y27.787
G01 X44.302Y27.932
G01 X44.273Y28.094
G01 X44.266Y28.278
G01 X44.293Y28.496
G01 X44.395Y28.789
G01 X40.299Y32.885
G01 X40.299Y32.885
G01 X34.546Y32.885
G01 X35.765Y31.666
G01 X35.765Y27.304
G01 X34.191Y25.73
G01 X29.674Y25.73
G01 X28.289Y27.115
G01 X27.996Y27.013
G01 X27.778Y26.986
G01 X27.594Y26.993
G01 X27.432Y27.022
G01 X27.287Y27.068
G01 X27.155Y27.128
G01 X27.035Y27.199
G01 X26.926Y27.282
G01 X26.828Y27.375
G01 X26.74Y27.478
G01 X26.663Y27.592
G01 X26.597Y27.717
G01 X26.544Y27.856
G01 X26.506Y28.008
G01 X26.486Y28.18
G01 X26.493Y28.379
G01 X26.547Y28.623
G01 X26.851Y29.119
G01 X27.347Y29.423
G01 X27.591Y29.477
G01 X27.79Y29.484
G01 X27.962Y29.464
G01 X28.114Y29.426
G01 X28.253Y29.373
G01 X28.378Y29.307
G01 X28.492Y29.23
G01 X28.595Y29.142
G01 X28.688Y29.044
G01 X28.771Y28.935
G01 X28.842Y28.815
G01 X28.902Y28.683
G01 X28.948Y28.538
G01 X28.977Y28.376
G01 X28.984Y28.192
G01 X28.957Y27.974
G01 X28.855Y27.681
G01 X30.006Y26.53
G01 X30.006Y26.53
G01 X33.861Y26.53
M5
G01 X12.395Y10.724
M3
G01 X12.395Y15.169
G01 X9.827Y17.737
G01 X9.685Y17.713
G01 X9.567Y17.712
G01 X9.463Y17.726
G01 X9.37Y17.75
G01 X9.286Y17.783
G01 X9.209Y17.823
G01 X9.139Y17.871
G01 X9.075Y17.924
G01 X9.018Y17.984
G01 X8.966Y18.049
G01 X8.921Y18.121
G01 X8.882Y18.2
G01 X8.852Y18.287
G01 X8.83Y18.383
G01 X8.82Y18.49
G01 X8.827Y18.614
G01 X8.862Y18.766
G01 X9.054Y19.076
G01 X9.364Y19.268
G01 X9.516Y19.303
G01 X9.64Y19.31
G01 X9.747Y19.3
G01 X9.843Y19.278
G01 X9.93Y19.248
G01 X10.009Y19.209
G01 X10.081Y19.164
G01 X10.146Y19.112
G01 X10.206Y19.055
G01 X10.259Y18.991
G01 X10.307Y18.921
G01 X10.347Y18.844
G01 X10.38Y18.76
G01 X10.405Y18.667
G01 X10.418Y18.563
G01 X10.417Y18.445
G01 X10.393Y18.303
G01 X13.195Y15.501
G01 X13.195Y15.501
G01 X13.195Y11.056
G01 X15.11Y9.141
G01 X15.11Y7.805
G01 X15.244Y7.716
G01 X15.339Y7.627
G01 X15.409Y7.538
G01 X15.463Y7.449
G01 X15.503Y7.361
G01 X15.532Y7.272
G01 X15.55Y7.183
G01 X15.559Y7.094
G01 X15.559Y7.005
G01 X15.549Y6.916
G01 X15.529Y6.827
G01 X15.499Y6.738
G01 X15.457Y6.649
G01 X15.401Y6.561
G01 X15.328Y6.472
G01 X15.23Y6.383
G01 X15.088Y6.294
G01 X14.71Y6.205
G01 X14.332Y6.294
G01 X14.19Y6.383
G01 X14.092Y6.472
G01 X14.019Y6.561
G01 X13.963Y6.649
G01 X13.921Y6.738
G01 X13.891Y6.827
G01 X13.871Y6.916
G01 X13.861Y7.005
G01 X13.861Y7.094
G01 X13.87Y7.183
G01 X13.888Y7.272
G01 X13.917Y7.361
G01 X13.957Y7.449
G01 X14.011Y7.538
G01 X14.081Y7.627
G01 X14.176Y7.716
G01 X14.31Y7.805
G01 X14.31Y8.809
G01 X14.31Y8.809
G01 X12.395Y10.724
M5
G01 X11.42Y6.655
M3
G01 X10.38Y6.655
G01 X10.348Y6.6
G01 X10.313Y6.549
G01 X10.275Y6.501
G01 X10.234Y6.457
G01 X10.189Y6.415
G01 X10.142Y6.376
G01 X10.091Y6.341
G01 X10.037Y6.309
G01 X9.979Y6.28
G01 X9.918Y6.255
G01 X9.852Y6.234
G01 X9.782Y6.219
G01 X9.706Y6.208
G01 X9.623Y6.205
G01 X9.531Y6.211
G01 X9.425Y6.23
G01 X9.296Y6.274
G01 X9.029Y6.454
G01 X8.849Y6.721
G01 X8.805Y6.85
G01 X8.786Y6.956
G01 X8.78Y7.048
G01 X8.783Y7.131
G01 X8.794Y7.207
G01 X8.809Y7.277
G01 X8.83Y7.343
G01 X8.855Y7.404
G01 X8.884Y7.462
G01 X8.916Y7.516
G01 X8.951Y7.566
G01 X8.99Y7.614
G01 X9.031Y7.659
G01 X9.076Y7.7
G01 X9.124Y7.738
G01 X9.175Y7.773
G01 X9.23Y7.805
G01 X9.23Y9.546
G01 X9.194Y9.565
G01 X9.16Y9.587
G01 X9.126Y9.611
G01 X9.092Y9.637
G01 X9.06Y9.665
G01 X9.029Y9.695
G01 X8.999Y9.727
G01 X8.969Y9.763
G01 X8.941Y9.801
G01 X8.915Y9.842
G01 X8.89Y9.887
G01 X8.866Y9.937
G01 X8.845Y9.991
G01 X8.826Y10.052
G01 X8.811Y10.122
G01 X8.802Y10.205
G01 X8.802Y10.312
G01 X8.86Y10.56
G01 X8.993Y10.776
G01 X9.068Y10.853
G01 X9.134Y10.905
G01 X9.193Y10.944
G01 X9.25Y10.974
G01 X9.303Y10.998
G01 X9.354Y11.016
G01 X9.404Y11.031
G01 X9.452Y11.041
G01 X9.499Y11.049
G01 X9.544Y11.053
G01 X9.589Y11.055
G01 X9.632Y11.054
G01 X9.675Y11.051
G01 X9.717Y11.046
G01 X9.757Y11.039
G01 X9.797Y11.03
G01 X9.837Y11.019
G01 X10.585Y11.801
G01 X10.585Y11.801
G01 X10.585Y14.007
G01 X10.467Y14.09
G01 X10.383Y14.173
G01 X10.32Y14.256
G01 X10.271Y14.339
G01 X10.235Y14.422
G01 X10.209Y14.505
G01 X10.193Y14.588
G01 X10.186Y14.671
G01 X10.187Y14.754
G01 X10.197Y14.836
G01 X10.216Y14.919
G01 X10.244Y15.002
G01 X10.284Y15.085
G01 X10.336Y15.168
G01 X10.405Y15.251
G01 X10.497Y15.334
G01 X10.63Y15.417
G01 X10.985Y15.5
G01 X11.34Y15.417
G01 X11.473Y15.334
G01 X11.565Y15.251
G01 X11.634Y15.168
G01 X11.686Y15.085
G01 X11.726Y15.002
G01 X11.754Y14.919
G01 X11.773Y14.836
G01 X11.783Y14.754
G01 X11.784Y14.671
G01 X11.777Y14.588
G01 X11.761Y14.505
G01 X11.735Y14.422
G01 X11.699Y14.339
G01 X11.65Y14.256
G01 X11.587Y14.173
G01 X11.503Y14.09
G01 X11.385Y14.007
G01 X11.385Y11.479
G01 X11.385Y11.479
G01 X10.381Y10.43
G01 X10.384Y10.416
G01 X10.386Y10.402
G01 X10.389Y10.387
G01 X10.391Y10.372
G01 X10.394Y10.356
G01 X10.396Y10.34
G01 X10.397Y10.322
G01 X10.398Y10.304
G01 X10.399Y10.286
G01 X10.4Y10.266
G01 X10.4Y10.244
G01 X10.399Y10.222
G01 X10.398Y10.197
G01 X10.395Y10.17
G01 X10.392Y10.14
G01 X10.386Y10.104
G01 X10.375Y10.058
G01 X10.34Y9.95
G01 X10.289Y9.848
G01 X10.264Y9.808
G01 X10.243Y9.779
G01 X10.224Y9.754
G01 X10.207Y9.733
G01 X10.19Y9.715
G01 X10.175Y9.699
G01 X10.16Y9.684
G01 X10.145Y9.67
G01 X10.131Y9.657
G01 X10.118Y9.645
G01 X10.105Y9.634
G01 X10.092Y9.624
G01 X10.079Y9.614
G01 X10.066Y9.605
G01 X10.054Y9.596
G01 X10.042Y9.588
G01 X10.03Y9.58
G01 X10.03Y7.805
G01 X10.036Y7.802
G01 X10.043Y7.798
G01 X10.049Y7.794
G01 X10.056Y7.791
G01 X10.063Y7.786
G01 X10.07Y7.782
G01 X10.078Y7.778
G01 X10.085Y7.773
G01 X10.094Y7.768
G01 X10.102Y7.762
G01 X10.111Y7.756
G01 X10.12Y7.749
G01 X10.131Y7.742
G01 X10.142Y7.734
G01 X10.154Y7.724
G01 X10.169Y7.712
G01 X10.187Y7.697
G01 X10.231Y7.656
G01 X10.272Y7.612
G01 X10.287Y7.594
G01 X10.299Y7.579
G01 X10.309Y7.567
G01 X10.317Y7.556
G01 X10.324Y7.545
G01 X10.331Y7.536
G01 X10.337Y7.527
G01 X10.342Y7.519
G01 X10.348Y7.51
G01 X10.353Y7.503
G01 X10.357Y7.495
G01 X10.361Y7.488
G01 X10.366Y7.481
G01 X10.369Y7.474
G01 X10.373Y7.468
G01 X10.377Y7.461
G01 X10.38Y7.455
G01 X11.42Y7.455
G01 X11.441Y7.492
G01 X11.464Y7.529
G01 X11.49Y7.565
G01 X11.517Y7.599
G01 X11.547Y7.633
G01 X11.579Y7.666
G01 X11.614Y7.698
G01 X11.651Y7.728
G01 X11.692Y7.758
G01 X11.736Y7.786
G01 X11.783Y7.812
G01 X11.836Y7.837
G01 X11.893Y7.859
G01 X11.958Y7.878
G01 X12.032Y7.894
G01 X12.12Y7.904
G01 X12.233Y7.903
G01 X12.495Y7.84
G01 X12.724Y7.699
G01 X12.805Y7.62
G01 X12.861Y7.551
G01 X12.902Y7.487
G01 X12.934Y7.428
G01 X12.959Y7.372
G01 X12.979Y7.317
G01 X12.994Y7.265
G01 X13.005Y7.214
G01 X13.013Y7.165
G01 X13.018Y7.116
G01 X13.02Y7.069
G01 X13.019Y7.023
G01 X13.017Y6.979
G01 X13.011Y6.935
G01 X13.004Y6.891
G01 X12.995Y6.849
G01 X12.983Y6.808
G01 X14.216Y5.575
G01 X14.216Y5.575
G01 X16.44Y5.575
G01 X18.11Y7.245
G01 X18.11Y20.884
G01 X13.264Y25.73
G01 X12.853Y25.73
G01 X12.822Y25.681
G01 X12.789Y25.636
G01 X12.753Y25.593
G01 X12.714Y25.553
G01 X12.672Y25.515
G01 X12.627Y25.481
G01 X12.58Y25.449
G01 X12.529Y25.42
G01 X12.476Y25.395
G01 X12.419Y25.373
G01 X12.358Y25.355
G01 X12.292Y25.341
G01 X12.222Y25.332
G01 X12.145Y25.33
G01 X12.06Y25.336
G01 X11.962Y25.355
G01 X11.842Y25.396
G01 X11.594Y25.564
G01 X11.426Y25.812
G01 X11.385Y25.932
G01 X11.366Y26.03
G01 X11.36Y26.115
G01 X11.362Y26.192
G01 X11.371Y26.262
G01 X11.385Y26.328
G01 X11.403Y26.389
G01 X11.425Y26.446
G01 X11.45Y26.499
G01 X11.479Y26.55
G01 X11.511Y26.597
G01 X11.545Y26.642
G01 X11.583Y26.684
G01 X11.623Y26.723
G01 X11.666Y26.759
G01 X11.711Y26.792
G01 X11.76Y26.823
G01 X11.76Y27.979
G01 X11.76Y27.979
G01 X11.184Y28.555
G01 X10.475Y28.555
G01 X10.475Y30.055
G01 X11.525Y30.055
G01 X11.525Y29.346
G01 X12.56Y28.311
G01 X12.56Y28.311
G01 X12.56Y26.823
G01 X12.565Y26.82
G01 X12.57Y26.817
G01 X12.576Y26.813
G01 X12.581Y26.81
G01 X12.587Y26.806
G01 X12.593Y26.803
G01 X12.599Y26.799
G01 X12.605Y26.795
G01 X12.612Y26.79
G01 X12.619Y26.785
G01 X12.626Y26.78
G01 X12.634Y26.774
G01 X12.643Y26.768
G01 X12.652Y26.761
G01 X12.662Y26.753
G01 X12.674Y26.743
G01 X12.69Y26.73
G01 X12.726Y26.696
G01 X12.76Y26.66
G01 X12.773Y26.644
G01 X12.783Y26.632
G01 X12.791Y26.622
G01 X12.798Y26.613
G01 X12.804Y26.604
G01 X12.81Y26.596
G01 X12.815Y26.589
G01 X12.82Y26.582
G01 X12.825Y26.575
G01 X12.829Y26.569
G01 X12.833Y26.563
G01 X12.836Y26.557
G01 X12.84Y26.551
G01 X12.843Y26.546
G01 X12.847Y26.54
G01 X12.85Y26.535
G01 X12.853Y26.53
G01 X13.596Y26.53
G01 X13.596Y26.53
G01 X18.91Y21.216
G01 X18.91Y6.915
G01 X16.77Y4.775
G01 X13.884Y4.775
G01 X12.417Y6.242
G01 X12.401Y6.237
G01 X12.384Y6.232
G01 X12.366Y6.228
G01 X12.348Y6.224
G01 X12.329Y6.22
G01 X12.31Y6.217
G01 X12.289Y6.213
G01 X12.268Y6.211
G01 X12.245Y6.208
G01 X12.222Y6.207
G01 X12.196Y6.205
G01 X12.169Y6.205
G01 X12.14Y6.206
G01 X12.107Y6.207
G01 X12.071Y6.211
G01 X12.028Y6.217
G01 X11.973Y6.228
G01 X11.845Y6.27
G01 X11.724Y6.331
G01 X11.678Y6.362
G01 X11.643Y6.388
G01 X11.615Y6.412
G01 X11.591Y6.433
G01 X11.569Y6.454
G01 X11.551Y6.473
G01 X11.533Y6.492
G01 X11.518Y6.51
G01 X11.504Y6.527
G01 X11.49Y6.544
G01 X11.478Y6.561
G01 X11.467Y6.577
G01 X11.456Y6.593
G01 X11.446Y6.609
G01 X11.437Y6.625
G01 X11.428Y6.64
G01 X11.42Y6.655
M5
G01 X10.408Y4.305
M3
G01 X16.584Y4.305
G01 X19.11Y6.831
G01 X19.11Y24.294
G01 X16.289Y27.115
G01 X16.189Y27.063
G01 X16.089Y27.044
G01 X15.988Y27.009
G01 X15.888Y26.99
G01 X15.788Y26.989
G01 X15.688Y26.987
G01 X15.587Y27.002
G01 X15.487Y27.017
G01 X15.387Y27.032
G01 X15.287Y27.063
G01 X15.186Y27.112
G01 X15.086Y27.16
G01 X14.986Y27.242
G01 X14.886Y27.323
G01 X14.785Y27.422
G01 X14.685Y27.554
G01 X14.585Y27.753
G01 X14.485Y28.236
G01 X14.586Y28.722
G01 X14.686Y28.908
G01 X14.786Y29.043
G01 X14.887Y29.146
G01 X14.987Y29.231
G01 X15.087Y29.3
G01 X15.188Y29.352
G01 X15.288Y29.404
G01 X15.388Y29.439
G01 X15.489Y29.457
G01 X15.589Y29.476
G01 X15.689Y29.478
G01 X15.789Y29.479
G01 X15.89Y29.481
G01 X15.99Y29.466
G01 X16.09Y29.435
G01 X16.19Y29.403
G01 X16.291Y29.355
G01 X19.62Y32.685
G01 X19.62Y32.685
G01 X29.631Y32.685
G01 X32.961Y29.355
G01 X33.254Y29.457
G01 X33.472Y29.484
G01 X33.656Y29.477
G01 X33.818Y29.448
G01 X33.963Y29.402
G01 X34.095Y29.342
G01 X34.215Y29.271
G01 X34.324Y29.188
G01 X34.422Y29.095
G01 X34.51Y28.992
G01 X34.587Y28.878
G01 X34.653Y28.753
G01 X34.706Y28.614
G01 X34.744Y28.462
G01 X34.764Y28.29
G01 X34.757Y28.091
G01 X34.703Y27.847
G01 X34.399Y27.351
G01 X33.903Y27.047
G01 X33.659Y26.993
G01 X33.46Y26.986
G01 X33.288Y27.006
G01 X33.136Y27.044
G01 X32.997Y27.097
G01 X32.872Y27.163
G01 X32.758Y27.24
G01 X32.655Y27.328
G01 X32.562Y27.426
G01 X32.479Y27.535
G01 X32.408Y27.655
G01 X32.348Y27.787
G01 X32.302Y27.932
G01 X32.273Y28.094
G01 X32.266Y28.278
G01 X32.293Y28.496
G01 X32.395Y28.789
G01 X29.299Y31.885
G01 X29.299Y31.885
G01 X19.95Y31.885
G01 X16.855Y28.79
G01 X16.862Y28.775
G01 X16.869Y28.76
G01 X16.877Y28.744
G01 X16.884Y28.727
G01 X16.891Y28.71
G01 X16.898Y28.692
G01 X16.906Y28.674
G01 X16.913Y28.654
G01 X16.92Y28.633
G01 X16.927Y28.611
G01 X16.934Y28.587
G01 X16.942Y28.561
G01 X16.949Y28.533
G01 X16.956Y28.502
G01 X16.963Y28.467
G01 X16.971Y28.425
G01 X16.978Y28.369
G01 X16.985Y28.235
G01 X16.978Y28.101
G01 X16.971Y28.045
G01 X16.963Y28.003
G01 X16.956Y27.968
G01 X16.949Y27.937
G01 X16.942Y27.909
G01 X16.934Y27.883
G01 X16.927Y27.859
G01 X16.92Y27.837
G01 X16.913Y27.816
G01 X16.906Y27.796
G01 X16.898Y27.778
G01 X16.891Y27.76
G01 X16.884Y27.743
G01 X16.877Y27.726
G01 X16.869Y27.71
G01 X16.862Y27.695
G01 X16.855Y27.68
G01 X19.91Y24.626
G01 X19.91Y24.626
G01 X19.91Y6.501
G01 X16.914Y3.505
G01 X10.071Y3.505
G01 X7.419Y6.205
G01 X6.24Y6.205
G01 X6.24Y7.905
G01 X6.7Y7.905
G01 X6.7Y9.562
G01 X6.687Y9.57
G01 X6.673Y9.578
G01 X6.66Y9.587
G01 X6.646Y9.596
G01 X6.632Y9.606
G01 X6.618Y9.617
G01 X6.603Y9.628
G01 X6.588Y9.64
G01 X6.573Y9.653
G01 X6.557Y9.668
G01 X6.541Y9.683
G01 X6.524Y9.7
G01 X6.506Y9.72
G01 X6.487Y9.741
G01 X6.466Y9.767
G01 X6.443Y9.798
G01 X6.416Y9.841
G01 X6.361Y9.949
G01 X6.323Y10.064
G01 X6.313Y10.113
G01 X6.307Y10.152
G01 X6.303Y10.184
G01 X6.301Y10.213
G01 X6.3Y10.239
G01 X6.3Y10.264
G01 X6.301Y10.286
G01 X6.302Y10.307
G01 X6.303Y10.328
G01 X6.305Y10.347
G01 X6.308Y10.365
G01 X6.31Y10.383
G01 X6.313Y10.4
G01 X6.316Y10.416
G01 X6.32Y10.432
G01 X6.323Y10.447
G01 X6.327Y10.462
G01 X4.847Y11.942
G01 X4.67Y11.924
G01 X4.53Y11.934
G01 X4.411Y11.961
G01 X4.306Y11.999
G01 X4.213Y12.047
G01 X4.13Y12.102
G01 X4.055Y12.164
G01 X3.989Y12.232
G01 X3.931Y12.307
G01 X3.88Y12.387
G01 X3.838Y12.474
G01 X3.804Y12.568
G01 X3.78Y12.67
G01 X3.768Y12.781
G01 X3.77Y12.903
G01 X3.794Y13.042
G01 X3.854Y13.209
G01 X4.111Y13.532
G01 X4.486Y13.706
G01 X4.663Y13.724
G01 X4.803Y13.714
G01 X4.922Y13.687
G01 X5.027Y13.649
G01 X5.12Y13.602
G01 X5.203Y13.547
G01 X5.278Y13.485
G01 X5.344Y13.417
G01 X5.403Y13.342
G01 X5.454Y13.261
G01 X5.496Y13.174
G01 X5.53Y13.08
G01 X5.554Y12.979
G01 X5.566Y12.868
G01 X5.564Y12.746
G01 X5.54Y12.607
G01 X5.481Y12.44
G01 X6.893Y11.028
G01 X6.905Y11.031
G01 X6.917Y11.034
G01 X6.931Y11.037
G01 X6.946Y11.04
G01 X6.962Y11.043
G01 X6.981Y11.046
G01 X7.003Y11.049
G01 X7.032Y11.052
G01 X7.1Y11.083
G01 X7.168Y11.052
G01 X7.197Y11.049
G01 X7.22Y11.046
G01 X7.238Y11.043
G01 X7.255Y11.04
G01 X7.269Y11.037
G01 X7.283Y11.034
G01 X7.295Y11.031
G01 X7.307Y11.028
G01 X8.585Y12.305
G01 X8.585Y12.305
G01 X8.585Y13.9
G01 X8.185Y13.9
G01 X8.185Y15.5
G01 X8.585Y15.5
G01 X8.585Y16.434
G01 X8.585Y16.434
G01 X7.264Y17.755
G01 X6.33Y17.755
G01 X6.33Y19.255
G01 X7.83Y19.255
G01 X7.83Y18.321
G01 X9.385Y16.766
G01 X9.385Y16.766
G01 X9.385Y15.5
G01 X9.785Y15.5
G01 X9.785Y13.9
G01 X9.385Y13.9
G01 X9.385Y11.975
G01 X9.385Y11.975
G01 X7.873Y10.463
G01 X7.876Y10.448
G01 X7.88Y10.433
G01 X7.883Y10.417
G01 X7.887Y10.4
G01 X7.89Y10.384
G01 X7.892Y10.366
G01 X7.895Y10.348
G01 X7.897Y10.328
G01 X7.898Y10.308
G01 X7.899Y10.287
G01 X7.9Y10.264
G01 X7.9Y10.24
G01 X7.899Y10.214
G01 X7.897Y10.185
G01 X7.893Y10.152
G01 X7.887Y10.114
G01 X7.877Y10.065
G01 X7.839Y9.949
G01 X7.784Y9.841
G01 X7.757Y9.798
G01 X7.734Y9.767
G01 X7.713Y9.742
G01 X7.694Y9.72
G01 X7.677Y9.7
G01 X7.66Y9.683
G01 X7.643Y9.668
G01 X7.627Y9.653
G01 X7.612Y9.64
G01 X7.597Y9.628
G01 X7.582Y9.617
G01 X7.568Y9.606
G01 X7.554Y9.596
G01 X7.54Y9.587
G01 X7.527Y9.578
G01 X7.513Y9.57
G01 X7.5Y9.562
G01 X7.5Y7.905
G01 X7.94Y7.905
G01 X7.94Y6.817
G01 X10.408Y4.305
G01 X10.408Y4.305
M5
G01 X40.914Y29.796
M3
G01 X48.715Y21.995
G01 X48.715Y5.11
G01 X46.85Y3.245
G01 X35.89Y3.245
G01 X34.139Y4.996
G01 X33.873Y4.95
G01 X33.651Y4.948
G01 X33.457Y4.974
G01 X33.282Y5.02
G01 X33.124Y5.082
G01 X32.98Y5.157
G01 X32.849Y5.246
G01 X32.729Y5.346
G01 X32.621Y5.458
G01 X32.524Y5.581
G01 X32.439Y5.716
G01 X32.367Y5.864
G01 X32.31Y6.026
G01 X32.269Y6.206
G01 X32.25Y6.407
G01 X32.263Y6.639
G01 X32.329Y6.925
G01 X32.689Y7.506
G01 X33.27Y7.866
G01 X33.556Y7.932
G01 X33.788Y7.945
G01 X33.989Y7.926
G01 X34.169Y7.885
G01 X34.331Y7.828
G01 X34.479Y7.756
G01 X34.614Y7.671
G01 X34.737Y7.574
G01 X34.849Y7.466
G01 X34.949Y7.346
G01 X35.038Y7.215
G01 X35.113Y7.071
G01 X35.175Y6.913
G01 X35.221Y6.738
G01 X35.247Y6.544
G01 X35.245Y6.322
G01 X35.199Y6.056
G01 X36.51Y4.745
G01 X36.51Y4.745
G01 X46.23Y4.745
G01 X47.215Y5.73
G01 X47.215Y21.375
G01 X39.854Y28.736
G01 X39.588Y28.69
G01 X39.366Y28.688
G01 X39.172Y28.714
G01 X38.997Y28.76
G01 X38.839Y28.822
G01 X38.695Y28.897
G01 X38.564Y28.986
G01 X38.444Y29.086
G01 X38.336Y29.198
G01 X38.239Y29.321
G01 X38.154Y29.456
G01 X38.082Y29.604
G01 X38.025Y29.766
G01 X37.984Y29.946
G01 X37.965Y30.147
G01 X37.978Y30.379
G01 X38.044Y30.665
G01 X38.404Y31.246
G01 X38.985Y31.606
G01 X39.271Y31.672
G01 X39.503Y31.685
G01 X39.704Y31.666
G01 X39.884Y31.625
G01 X40.046Y31.568
G01 X40.194Y31.496
G01 X40.329Y31.411
G01 X40.452Y31.314
G01 X40.564Y31.206
G01 X40.664Y31.086
G01 X40.753Y30.955
G01 X40.828Y30.811
G01 X40.89Y30.653
G01 X40.936Y30.478
G01 X40.962Y30.284
G01 X40.96Y30.062
G01 X40.914Y29.796
M5
G01 X22.435Y28.886
M3
G01 X22.435Y13.74
G01 X28.23Y7.945
G01 X30.17Y7.945
G01 X30.17Y4.945
G01 X27.17Y4.945
G01 X27.17Y6.885
G01 X20.935Y13.12
G01 X20.935Y13.12
G01 X20.935Y28.886
G01 X20.714Y29.041
G01 X20.556Y29.197
G01 X20.437Y29.352
G01 X20.346Y29.508
G01 X20.279Y29.663
G01 X20.23Y29.819
G01 X20.2Y29.974
G01 X20.186Y30.13
G01 X20.188Y30.285
G01 X20.207Y30.441
G01 X20.243Y30.596
G01 X20.296Y30.752
G01 X20.37Y30.907
G01 X20.469Y31.063
G01 X20.598Y31.218
G01 X20.77Y31.374
G01 X21.02Y31.529
G01 X21.685Y31.685
G01 X22.35Y31.529
G01 X22.6Y31.374
G01 X22.772Y31.218
G01 X22.901Y31.063
G01 X23.0Y30.907
G01 X23.074Y30.752
G01 X23.127Y30.596
G01 X23.163Y30.441
G01 X23.182Y30.285
G01 X23.184Y30.13
G01 X23.17Y29.974
G01 X23.14Y29.819
G01 X23.091Y29.663
G01 X23.024Y29.508
G01 X22.933Y29.352
G01 X22.814Y29.197
G01 X22.656Y29.041
G01 X22.435Y28.886
M5
G01 X46.265Y14.736
M3
G01 X46.265Y7.105
G01 X46.045Y6.885
G01 X46.045Y4.945
G01 X43.045Y4.945
G01 X43.045Y7.945
G01 X44.765Y7.945
G01 X44.765Y14.736
G01 X44.765Y14.736
G01 X44.544Y14.891
G01 X44.386Y15.047
G01 X44.267Y15.202
G01 X44.176Y15.358
G01 X44.109Y15.513
G01 X44.06Y15.669
G01 X44.03Y15.824
G01 X44.016Y15.98
G01 X44.018Y16.135
G01 X44.037Y16.291
G01 X44.073Y16.446
G01 X44.126Y16.602
G01 X44.2Y16.757
G01 X44.299Y16.913
G01 X44.428Y17.068
G01 X44.6Y17.224
G01 X44.85Y17.379
G01 X45.515Y17.535
G01 X46.18Y17.379
G01 X46.43Y17.224
G01 X46.602Y17.068
G01 X46.731Y16.913
G01 X46.83Y16.757
G01 X46.904Y16.602
G01 X46.957Y16.446
G01 X46.993Y16.291
G01 X47.012Y16.135
G01 X47.014Y15.98
G01 X47.0Y15.824
G01 X46.97Y15.669
G01 X46.921Y15.513
G01 X46.854Y15.358
G01 X46.763Y15.202
G01 X46.644Y15.047
G01 X46.486Y14.891
G01 X46.265Y14.736
M5
G01 X29.565Y15.285
M3
G01 X29.034Y15.285
G01 X28.879Y15.064
G01 X28.723Y14.906
G01 X28.568Y14.787
G01 X28.412Y14.696
G01 X28.257Y14.629
G01 X28.101Y14.58
G01 X27.946Y14.55
G01 X27.79Y14.536
G01 X27.635Y14.538
G01 X27.479Y14.557
G01 X27.324Y14.593
G01 X27.168Y14.646
G01 X27.013Y14.72
G01 X26.857Y14.819
G01 X26.702Y14.948
G01 X26.546Y15.12
G01 X26.391Y15.37
G01 X26.235Y16.035
G01 X26.391Y16.7
G01 X26.546Y16.95
G01 X26.702Y17.122
G01 X26.857Y17.251
G01 X27.013Y17.35
G01 X27.168Y17.424
G01 X27.324Y17.477
G01 X27.479Y17.513
G01 X27.635Y17.532
G01 X27.79Y17.534
G01 X27.946Y17.52
G01 X28.101Y17.49
G01 X28.257Y17.441
G01 X28.412Y17.374
G01 X28.568Y17.283
G01 X28.723Y17.164
G01 X28.879Y17.006
G01 X29.034Y16.785
G01 X30.185Y16.785
G01 X30.185Y16.785
G01 X39.076Y7.894
G01 X39.342Y7.94
G01 X39.564Y7.942
G01 X39.758Y7.916
G01 X39.933Y7.87
G01 X40.091Y7.808
G01 X40.235Y7.733
G01 X40.366Y7.644
G01 X40.486Y7.544
G01 X40.594Y7.432
G01 X40.691Y7.309
G01 X40.776Y7.174
G01 X40.848Y7.026
G01 X40.905Y6.864
G01 X40.946Y6.684
G01 X40.965Y6.483
G01 X40.952Y6.251
G01 X40.886Y5.965
G01 X40.526Y5.384
G01 X39.945Y5.024
G01 X39.659Y4.958
G01 X39.427Y4.945
G01 X39.226Y4.964
G01 X39.046Y5.005
G01 X38.884Y5.062
G01 X38.736Y5.134
G01 X38.601Y5.219
G01 X38.478Y5.316
G01 X38.366Y5.424
G01 X38.266Y5.544
G01 X38.177Y5.675
G01 X38.102Y5.819
G01 X38.04Y5.977
G01 X37.994Y6.152
G01 X37.968Y6.346
G01 X37.97Y6.568
G01 X38.016Y6.834
G01 X29.565Y15.285
G01 X29.565Y15.285
M5
G01 X4.94Y17.817
M3
G01 X4.94Y16.264
G01 X5.567Y16.264
G01 X5.567Y14.464
G01 X3.767Y14.464
G01 X3.767Y16.264
G01 X4.14Y16.264
G01 X4.14Y17.817
G01 X4.022Y17.9
G01 X3.938Y17.983
G01 X3.875Y18.066
G01 X3.826Y18.149
G01 X3.79Y18.232
G01 X3.764Y18.315
G01 X3.748Y18.398
G01 X3.741Y18.481
G01 X3.742Y18.564
G01 X3.752Y18.646
G01 X3.771Y18.729
G01 X3.799Y18.812
G01 X3.839Y18.895
G01 X3.891Y18.978
G01 X3.96Y19.061
G01 X4.052Y19.144
G01 X4.185Y19.227
G01 X4.54Y19.31
G01 X4.895Y19.227
G01 X5.028Y19.144
G01 X5.12Y19.061
G01 X5.189Y18.978
G01 X5.241Y18.895
G01 X5.281Y18.812
G01 X5.309Y18.729
G01 X5.328Y18.646
G01 X5.338Y18.564
G01 X5.339Y18.481
G01 X5.332Y18.398
G01 X5.316Y18.315
G01 X5.29Y18.232
G01 X5.254Y18.149
G01 X5.205Y18.066
G01 X5.142Y17.983
G01 X5.058Y17.9
G01 X4.94Y17.817
M5
G01 X12.56Y23.756
M3
G01 X12.56Y19.203
G01 X12.678Y19.12
G01 X12.762Y19.037
G01 X12.825Y18.954
G01 X12.874Y18.871
G01 X12.91Y18.788
G01 X12.936Y18.705
G01 X12.952Y18.622
G01 X12.959Y18.539
G01 X12.958Y18.456
G01 X12.948Y18.374
G01 X12.929Y18.291
G01 X12.901Y18.208
G01 X12.861Y18.125
G01 X12.809Y18.042
G01 X12.74Y17.959
G01 X12.648Y17.876
G01 X12.515Y17.793
G01 X12.16Y17.71
G01 X11.805Y17.793
G01 X11.672Y17.876
G01 X11.58Y17.959
G01 X11.511Y18.042
G01 X11.459Y18.125
G01 X11.419Y18.208
G01 X11.391Y18.291
G01 X11.372Y18.374
G01 X11.362Y18.456
G01 X11.361Y18.539
G01 X11.368Y18.622
G01 X11.384Y18.705
G01 X11.41Y18.788
G01 X11.446Y18.871
G01 X11.495Y18.954
G01 X11.558Y19.037
G01 X11.642Y19.12
G01 X11.76Y19.203
G01 X11.76Y23.424
G01 X11.76Y23.424
G01 X9.827Y25.357
G01 X9.789Y25.348
G01 X9.75Y25.341
G01 X9.71Y25.335
G01 X9.67Y25.332
G01 X9.629Y25.33
G01 X9.587Y25.331
G01 X9.544Y25.334
G01 X9.5Y25.339
G01 X9.455Y25.347
G01 X9.408Y25.359
G01 X9.36Y25.373
G01 X9.31Y25.392
G01 X9.259Y25.416
G01 X9.204Y25.446
G01 X9.147Y25.485
G01 X9.083Y25.537
G01 X9.011Y25.612
G01 X8.881Y25.824
G01 X8.823Y26.066
G01 X8.821Y26.17
G01 X8.829Y26.252
G01 X8.843Y26.32
G01 X8.86Y26.38
G01 X8.88Y26.433
G01 X8.901Y26.481
G01 X8.925Y26.526
G01 X8.95Y26.567
G01 X8.976Y26.604
G01 X9.003Y26.639
G01 X9.032Y26.672
G01 X9.061Y26.702
G01 X9.091Y26.73
G01 X9.122Y26.756
G01 X9.154Y26.78
G01 X9.187Y26.802
G01 X9.22Y26.823
G01 X9.22Y28.555
G01 X9.205Y28.555
G01 X9.205Y30.055
G01 X10.255Y30.055
G01 X10.255Y28.555
G01 X10.02Y28.555
G01 X10.02Y26.823
G01 X10.033Y26.815
G01 X10.046Y26.807
G01 X10.06Y26.798
G01 X10.074Y26.789
G01 X10.088Y26.779
G01 X10.102Y26.768
G01 X10.117Y26.757
G01 X10.132Y26.745
G01 X10.147Y26.732
G01 X10.163Y26.717
G01 X10.179Y26.702
G01 X10.197Y26.685
G01 X10.214Y26.665
G01 X10.233Y26.644
G01 X10.254Y26.618
G01 X10.277Y26.587
G01 X10.304Y26.544
G01 X10.359Y26.436
G01 X10.397Y26.321
G01 X10.407Y26.272
G01 X10.413Y26.233
G01 X10.417Y26.201
G01 X10.419Y26.172
G01 X10.42Y26.146
G01 X10.42Y26.121
G01 X10.419Y26.099
G01 X10.418Y26.078
G01 X10.417Y26.057
G01 X10.415Y26.038
G01 X10.412Y26.02
G01 X10.41Y26.002
G01 X10.407Y25.985
G01 X10.404Y25.969
G01 X10.4Y25.953
G01 X10.397Y25.938
G01 X10.393Y25.923
G01 X12.56Y23.756
G01 X12.56Y23.756
M5
G01 X31.965Y15.985
M3
G01 X32.048Y16.478
G01 X32.132Y16.672
G01 X32.215Y16.814
G01 X32.298Y16.928
G01 X32.382Y17.023
G01 X32.465Y17.103
G01 X32.548Y17.172
G01 X32.632Y17.232
G01 X32.715Y17.284
G01 X32.798Y17.329
G01 X32.882Y17.367
G01 X32.965Y17.399
G01 X33.048Y17.426
G01 X33.132Y17.448
G01 X33.215Y17.464
G01 X33.298Y17.476
G01 X33.382Y17.483
G01 X33.548Y17.483
G01 X33.632Y17.476
G01 X33.715Y17.464
G01 X33.798Y17.448
G01 X33.882Y17.426
G01 X33.965Y17.399
G01 X34.048Y17.367
G01 X34.132Y17.329
G01 X34.215Y17.284
G01 X34.298Y17.232
G01 X34.382Y17.172
G01 X34.465Y17.103
G01 X34.548Y17.023
G01 X34.632Y16.928
G01 X34.715Y16.814
G01 X34.798Y16.672
G01 X34.882Y16.478
G01 X34.965Y15.985
G01 X34.882Y15.492
G01 X34.798Y15.298
G01 X34.715Y15.156
G01 X34.632Y15.042
G01 X34.548Y14.947
G01 X34.465Y14.867
G01 X34.382Y14.798
G01 X34.298Y14.738
G01 X34.215Y14.686
G01 X34.132Y14.641
G01 X34.048Y14.603
G01 X33.965Y14.571
G01 X33.882Y14.544
G01 X33.798Y14.523
G01 X33.715Y14.506
G01 X33.632Y14.494
G01 X33.548Y14.487
G01 X33.382Y14.487
G01 X33.298Y14.494
G01 X33.215Y14.506
G01 X33.132Y14.523
G01 X33.048Y14.544
G01 X32.965Y14.571
G01 X32.882Y14.603
G01 X32.798Y14.641
G01 X32.715Y14.686
G01 X32.632Y14.738
G01 X32.548Y14.798
G01 X32.465Y14.867
G01 X32.382Y14.947
G01 X32.298Y15.042
G01 X32.215Y15.156
G01 X32.132Y15.298
G01 X32.048Y15.492
G01 X31.965Y15.985
G01 X31.965Y15.985
M5
G01 X14.185Y15.985
M3
G01 X14.268Y16.478
G01 X14.352Y16.672
G01 X14.435Y16.814
G01 X14.518Y16.928
G01 X14.602Y17.023
G01 X14.685Y17.103
G01 X14.768Y17.172
G01 X14.852Y17.232
G01 X14.935Y17.284
G01 X15.018Y17.329
G01 X15.102Y17.367
G01 X15.185Y17.399
G01 X15.268Y17.426
G01 X15.352Y17.448
G01 X15.435Y17.464
G01 X15.518Y17.476
G01 X15.602Y17.483
G01 X15.768Y17.483
G01 X15.852Y17.476
G01 X15.935Y17.464
G01 X16.018Y17.448
G01 X16.102Y17.426
G01 X16.185Y17.399
G01 X16.268Y17.367
G01 X16.352Y17.329
G01 X16.435Y17.284
G01 X16.518Y17.232
G01 X16.602Y17.172
G01 X16.685Y17.103
G01 X16.768Y17.023
G01 X16.852Y16.928
G01 X16.935Y16.814
G01 X17.018Y16.672
G01 X17.102Y16.478
G01 X17.185Y15.985
G01 X17.102Y15.492
G01 X17.018Y15.298
G01 X16.935Y15.156
G01 X16.852Y15.042
G01 X16.768Y14.947
G01 X16.685Y14.867
G01 X16.602Y14.798
G01 X16.518Y14.738
G01 X16.435Y14.686
G01 X16.352Y14.641
G01 X16.268Y14.603
G01 X16.185Y14.571
G01 X16.102Y14.544
G01 X16.018Y14.523
G01 X15.935Y14.506
G01 X15.852Y14.494
G01 X15.768Y14.487
G01 X15.602Y14.487
G01 X15.518Y14.494
G01 X15.435Y14.506
G01 X15.352Y14.523
G01 X15.268Y14.544
G01 X15.185Y14.571
G01 X15.102Y14.603
G01 X15.018Y14.641
G01 X14.935Y14.686
G01 X14.852Y14.738
G01 X14.768Y14.798
G01 X14.685Y14.867
G01 X14.602Y14.947
G01 X14.518Y15.042
G01 X14.435Y15.156
G01 X14.352Y15.298
G01 X14.268Y15.492
G01 X14.185Y15.985
G01 X14.185Y15.985
M5
G01 X2.0Y2.0
M3
G01 X49.625Y2.0
G01 X49.625Y34.385
G01 X2.0Y34.385
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
