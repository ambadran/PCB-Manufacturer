
; The following gcode is the PCB trace laser marking gcode

M5 ; Being extra sure it won't light up before activation

; Getting and Activating Tool-1, The Tool.Laser
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
G01 X7.825Y26.213
G01 X7.83Y26.13
G01 X7.826Y26.044
G01 X7.81Y25.953
G01 X7.78Y25.857
G01 X7.73Y25.751
G01 X7.645Y25.632
G01 X7.367Y25.432
G01 X7.03Y25.377
G01 X6.885Y25.401
G01 X6.775Y25.44
G01 X6.686Y25.487
G01 X6.61Y25.54
G01 X6.546Y25.598
G01 X6.492Y25.66
G01 X6.446Y25.725
G01 X5.23Y25.725
G01 X5.042Y25.507
G01 X4.854Y25.394
G01 X4.667Y25.34
G01 X4.481Y25.332
G01 X4.294Y25.369
G01 X4.108Y25.456
G01 X3.923Y25.62
G01 X3.74Y26.136
G01 X3.93Y26.648
G01 X4.118Y26.809
G01 X4.305Y26.894
G01 X4.492Y26.928
G01 X4.679Y26.917
G01 X4.865Y26.861
G01 X5.051Y26.746
G01 X5.236Y26.525
G01 X6.446Y26.525
G01 X6.462Y26.551
G01 X6.482Y26.577
G01 X6.504Y26.605
G01 X6.529Y26.634
G01 X6.56Y26.666
G01 X6.599Y26.7
G01 X6.652Y26.741
G01 X6.793Y26.818
G01 X6.947Y26.863
G01 X7.014Y26.872
G01 X7.066Y26.875
G01 X7.11Y26.874
G01 X7.149Y26.872
G01 X7.184Y26.868
G01 X7.216Y26.863
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
G01 X45.521Y29.485
G01 X45.893Y29.427
G01 X46.186Y29.29
G01 X46.422Y29.095
G01 X46.605Y28.848
G01 X46.727Y28.54
G01 X46.762Y28.144
G01 X46.399Y27.351
G01 X45.606Y26.988
G01 X45.21Y27.023
G01 X44.902Y27.145
G01 X44.655Y27.328
G01 X44.46Y27.564
G01 X44.323Y27.857
G01 X44.265Y28.229
G01 X44.395Y28.789
G01 X40.299Y32.885
G01 X40.299Y32.885
G01 X34.546Y32.885
G01 X35.765Y31.666
G01 X35.765Y27.304
G01 X34.191Y25.73
G01 X29.674Y25.73
G01 X28.289Y27.115
G01 X27.729Y26.985
G01 X27.357Y27.043
G01 X27.064Y27.18
G01 X26.828Y27.375
G01 X26.645Y27.622
G01 X26.523Y27.93
G01 X26.488Y28.326
G01 X26.851Y29.119
G01 X27.644Y29.482
G01 X28.04Y29.447
G01 X28.348Y29.325
G01 X28.595Y29.142
G01 X28.79Y28.906
G01 X28.927Y28.613
G01 X28.985Y28.241
G01 X28.855Y27.681
G01 X30.006Y26.53
G01 X30.006Y26.53
M5
G01 X12.395Y10.724
M3
G01 X12.395Y15.169
G01 X9.827Y17.737
G01 X9.54Y17.714
G01 X9.327Y17.765
G01 X9.156Y17.858
G01 X9.018Y17.984
G01 X8.911Y18.14
G01 X8.84Y18.333
G01 X8.823Y18.581
G01 X9.054Y19.076
G01 X9.549Y19.307
G01 X9.797Y19.29
G01 X9.99Y19.219
G01 X10.146Y19.112
G01 X10.272Y18.974
G01 X10.365Y18.803
G01 X10.416Y18.59
G01 X10.393Y18.303
G01 X13.195Y15.501
G01 X13.195Y15.501
G01 X13.195Y11.056
G01 X15.11Y9.141
G01 X15.11Y7.805
G01 X15.358Y7.605
G01 X15.485Y7.405
G01 X15.547Y7.205
G01 X15.559Y7.005
G01 X15.522Y6.805
G01 X15.431Y6.605
G01 X15.258Y6.405
G01 X14.71Y6.205
G01 X14.162Y6.405
G01 X13.989Y6.605
G01 X13.898Y6.805
G01 X13.861Y7.005
G01 X13.873Y7.205
G01 X13.935Y7.405
G01 X14.062Y7.605
G01 X14.31Y7.805
G01 X14.31Y8.809
G01 X14.31Y8.809
M5
G01 X11.42Y6.655
M3
G01 X10.38Y6.655
G01 X10.304Y6.537
G01 X10.212Y6.435
G01 X10.104Y6.349
G01 X9.979Y6.28
G01 X9.835Y6.23
G01 X9.665Y6.206
G01 X9.453Y6.224
G01 X9.029Y6.454
G01 X8.799Y6.878
G01 X8.781Y7.09
G01 X8.805Y7.26
G01 X8.855Y7.404
G01 X8.924Y7.529
G01 X9.01Y7.637
G01 X9.112Y7.729
G01 X9.23Y7.805
G01 X9.23Y9.546
G01 X9.151Y9.593
G01 X9.076Y9.65
G01 X9.006Y9.719
G01 X8.941Y9.801
G01 X8.884Y9.899
G01 X8.835Y10.021
G01 X8.803Y10.182
G01 X8.86Y10.56
G01 X9.085Y10.868
G01 X9.222Y10.96
G01 X9.342Y11.012
G01 X9.452Y11.041
G01 X9.556Y11.054
G01 X9.654Y11.053
G01 X9.747Y11.041
G01 X9.837Y11.019
G01 X10.585Y11.801
G01 X10.585Y11.801
G01 X10.585Y14.007
G01 X10.366Y14.194
G01 X10.252Y14.38
G01 X10.196Y14.567
G01 X10.187Y14.754
G01 X10.222Y14.94
G01 X10.308Y15.127
G01 X10.471Y15.313
G01 X10.985Y15.5
G01 X11.499Y15.313
G01 X11.662Y15.127
G01 X11.748Y14.94
G01 X11.783Y14.754
G01 X11.774Y14.567
G01 X11.718Y14.38
G01 X11.604Y14.194
G01 X11.385Y14.007
G01 X11.385Y11.479
G01 X11.385Y11.479
G01 X10.381Y10.43
G01 X10.387Y10.398
G01 X10.393Y10.364
G01 X10.397Y10.327
G01 X10.399Y10.286
G01 X10.4Y10.239
G01 X10.397Y10.184
G01 X10.387Y10.114
G01 X10.34Y9.95
G01 X10.258Y9.8
G01 X10.215Y9.744
G01 X10.179Y9.703
G01 X10.145Y9.67
G01 X10.115Y9.642
G01 X10.085Y9.619
G01 X10.057Y9.598
G01 X10.03Y9.58
G01 X10.03Y7.805
G01 X10.044Y7.797
G01 X10.06Y7.788
G01 X10.076Y7.779
G01 X10.094Y7.767
G01 X10.113Y7.754
G01 X10.136Y7.738
G01 X10.165Y7.715
G01 X10.231Y7.656
G01 X10.29Y7.59
G01 X10.313Y7.561
G01 X10.329Y7.538
G01 X10.342Y7.519
G01 X10.354Y7.501
G01 X10.363Y7.485
G01 X10.372Y7.469
G01 X10.38Y7.455
G01 X11.42Y7.455
G01 X11.47Y7.538
G01 X11.532Y7.616
G01 X11.605Y7.69
G01 X11.692Y7.758
G01 X11.796Y7.818
G01 X11.925Y7.869
G01 X12.096Y7.902
G01 X12.495Y7.84
G01 X12.821Y7.602
G01 X12.919Y7.457
G01 X12.974Y7.331
G01 X13.005Y7.214
G01 X13.019Y7.105
G01 X13.018Y7.001
G01 X13.006Y6.902
G01 X12.983Y6.808
G01 X14.216Y5.575
G01 X14.216Y5.575
G01 X16.44Y5.575
G01 X18.11Y7.245
G01 X18.11Y20.884
G01 X13.264Y25.73
G01 X12.853Y25.73
G01 X12.78Y25.625
G01 X12.693Y25.534
G01 X12.592Y25.457
G01 X12.476Y25.395
G01 X12.342Y25.351
G01 X12.184Y25.33
G01 X11.988Y25.349
G01 X11.594Y25.564
G01 X11.379Y25.958
G01 X11.36Y26.154
G01 X11.381Y26.312
G01 X11.425Y26.446
G01 X11.487Y26.562
G01 X11.564Y26.663
G01 X11.655Y26.75
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
G01 X12.572Y26.816
G01 X12.584Y26.808
G01 X12.598Y26.8
G01 X12.612Y26.79
G01 X12.628Y26.779
G01 X12.647Y26.765
G01 X12.671Y26.745
G01 X12.726Y26.696
G01 X12.775Y26.641
G01 X12.795Y26.617
G01 X12.809Y26.598
G01 X12.82Y26.582
G01 X12.83Y26.568
G01 X12.838Y26.554
G01 X12.846Y26.542
G01 X12.853Y26.53
G01 X13.596Y26.53
G01 X13.596Y26.53
G01 X18.91Y21.216
G01 X18.91Y6.915
G01 X16.77Y4.775
G01 X13.884Y4.775
G01 X12.417Y6.242
G01 X12.38Y6.231
G01 X12.339Y6.222
G01 X12.294Y6.214
G01 X12.245Y6.208
G01 X12.19Y6.205
G01 X12.124Y6.206
G01 X12.04Y6.215
G01 X11.845Y6.27
G01 X11.668Y6.369
G01 X11.602Y6.423
G01 X11.555Y6.468
G01 X11.518Y6.51
G01 X11.487Y6.549
G01 X11.461Y6.586
G01 X11.439Y6.621
M5
G01 X10.408Y4.305
M3
G01 X16.584Y4.305
G01 X19.11Y6.831
G01 X19.11Y24.294
G01 X16.289Y27.115
G01 X16.064Y27.027
G01 X15.838Y26.99
G01 X15.612Y26.986
G01 X15.387Y27.032
G01 X15.161Y27.128
G01 X14.936Y27.274
G01 X14.71Y27.521
G01 X14.485Y28.236
G01 X14.711Y28.959
G01 X14.937Y29.197
G01 X15.163Y29.351
G01 X15.388Y29.439
G01 X15.614Y29.476
G01 X15.84Y29.48
G01 X16.065Y29.434
G01 X16.291Y29.355
G01 X19.62Y32.685
G01 X19.62Y32.685
G01 X29.631Y32.685
G01 X32.961Y29.355
G01 X33.521Y29.485
G01 X33.893Y29.427
G01 X34.186Y29.29
G01 X34.422Y29.095
G01 X34.605Y28.848
G01 X34.727Y28.54
G01 X34.762Y28.144
G01 X34.399Y27.351
G01 X33.606Y26.988
G01 X33.21Y27.023
G01 X32.902Y27.145
G01 X32.655Y27.328
G01 X32.46Y27.564
G01 X32.323Y27.857
G01 X32.265Y28.229
G01 X32.395Y28.789
G01 X29.299Y31.885
G01 X29.299Y31.885
G01 X19.95Y31.885
G01 X16.855Y28.79
G01 X16.871Y28.756
G01 X16.888Y28.719
G01 X16.904Y28.678
G01 X16.92Y28.633
G01 X16.936Y28.581
G01 X16.953Y28.518
G01 X16.969Y28.436
G01 X16.985Y28.235
G01 X16.969Y28.034
G01 X16.953Y27.952
G01 X16.936Y27.889
G01 X16.92Y27.837
G01 X16.904Y27.792
G01 X16.888Y27.751
G01 X16.871Y27.714
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
G01 X6.67Y9.58
G01 X6.639Y9.601
G01 X6.607Y9.625
G01 X6.573Y9.653
G01 X6.536Y9.687
G01 X6.496Y9.73
G01 X6.449Y9.79
G01 X6.361Y9.949
G01 X6.311Y10.124
G01 X6.302Y10.199
G01 X6.3Y10.258
G01 X6.302Y10.307
G01 X6.306Y10.351
G01 X6.312Y10.391
G01 X6.319Y10.428
G01 X6.327Y10.462
G01 X4.847Y11.942
G01 X4.499Y11.94
G01 X4.258Y12.022
G01 X4.073Y12.148
G01 X3.931Y12.306
G01 X3.828Y12.497
G01 X3.773Y12.724
G01 X3.785Y13.005
G01 X4.111Y13.532
G01 X4.7Y13.723
G01 X4.976Y13.669
G01 X5.184Y13.561
G01 X5.344Y13.416
G01 X5.465Y13.24
G01 X5.543Y13.031
G01 X5.566Y12.778
G01 X5.481Y12.44
G01 X6.893Y11.028
G01 X6.921Y11.035
G01 X6.954Y11.041
G01 X6.997Y11.048
G01 X7.1Y11.083
G01 X7.203Y11.048
G01 X7.247Y11.041
G01 X7.279Y11.035
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
G01 X7.881Y10.429
G01 X7.888Y10.392
G01 X7.894Y10.352
G01 X7.898Y10.308
G01 X7.9Y10.258
G01 X7.898Y10.2
G01 X7.889Y10.124
G01 X7.839Y9.949
G01 X7.751Y9.79
G01 X7.704Y9.73
G01 X7.664Y9.687
G01 X7.627Y9.653
G01 X7.593Y9.625
G01 X7.561Y9.601
G01 X7.53Y9.58
G01 X7.5Y9.562
G01 X7.5Y7.905
G01 X7.94Y7.905
G01 X7.94Y7.905
G01 X7.94Y6.817
G01 X10.408Y4.305
M5
G01 X40.914Y29.796
M3
G01 X48.715Y21.995
G01 X48.715Y5.11
G01 X46.85Y3.245
G01 X35.89Y3.245
G01 X34.139Y4.996
G01 X33.6Y4.952
G01 X33.202Y5.049
G01 X32.881Y5.223
G01 X32.621Y5.458
G01 X32.42Y5.752
G01 X32.287Y6.114
G01 X32.256Y6.577
G01 X32.689Y7.506
G01 X33.618Y7.939
G01 X34.081Y7.908
G01 X34.443Y7.775
G01 X34.737Y7.574
G01 X34.972Y7.314
G01 X35.146Y6.993
G01 X35.242Y6.595
G01 X35.199Y6.056
G01 X36.51Y4.745
G01 X36.51Y4.745
G01 X46.23Y4.745
G01 X47.215Y5.73
G01 X47.215Y21.375
G01 X39.854Y28.736
G01 X39.315Y28.692
G01 X38.917Y28.789
G01 X38.596Y28.963
G01 X38.336Y29.198
G01 X38.135Y29.492
G01 X38.002Y29.854
G01 X37.971Y30.317
G01 X38.404Y31.246
G01 X39.333Y31.679
G01 X39.796Y31.648
G01 X40.158Y31.515
G01 X40.452Y31.314
G01 X40.687Y31.054
G01 X40.861Y30.733
G01 X40.958Y30.335
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
G01 X20.523Y29.236
G01 X20.31Y29.586
G01 X20.206Y29.936
G01 X20.188Y30.285
G01 X20.254Y30.635
G01 X20.416Y30.985
G01 X20.722Y31.335
G01 X21.685Y31.685
G01 X22.648Y31.335
G01 X22.954Y30.985
G01 X23.116Y30.635
G01 X23.182Y30.285
G01 X23.164Y29.936
G01 X23.06Y29.586
G01 X22.847Y29.236
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
G01 X44.353Y15.086
G01 X44.14Y15.436
G01 X44.036Y15.786
G01 X44.018Y16.135
G01 X44.084Y16.485
G01 X44.246Y16.835
G01 X44.552Y17.185
G01 X45.515Y17.535
G01 X46.478Y17.185
G01 X46.784Y16.835
G01 X46.946Y16.485
G01 X47.012Y16.135
G01 X46.994Y15.786
G01 X46.89Y15.436
G01 X46.677Y15.086
M5
G01 X29.565Y15.285
M3
G01 X29.034Y15.285
G01 X28.684Y14.873
G01 X28.334Y14.66
G01 X27.984Y14.556
G01 X27.635Y14.538
G01 X27.285Y14.604
G01 X26.935Y14.766
G01 X26.585Y15.072
G01 X26.235Y16.035
G01 X26.585Y16.998
G01 X26.935Y17.304
G01 X27.285Y17.466
G01 X27.635Y17.532
G01 X27.984Y17.514
G01 X28.334Y17.41
G01 X28.684Y17.197
G01 X29.034Y16.785
G01 X30.185Y16.785
G01 X30.185Y16.785
G01 X39.076Y7.894
G01 X39.615Y7.938
G01 X40.013Y7.841
G01 X40.334Y7.667
G01 X40.594Y7.432
G01 X40.795Y7.138
G01 X40.928Y6.776
G01 X40.959Y6.313
G01 X40.526Y5.384
G01 X39.597Y4.951
G01 X39.134Y4.982
G01 X38.772Y5.115
G01 X38.478Y5.316
G01 X38.243Y5.576
G01 X38.069Y5.897
G01 X37.972Y6.295
G01 X38.016Y6.834
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
G01 X3.921Y18.004
G01 X3.807Y18.19
G01 X3.751Y18.377
G01 X3.742Y18.564
G01 X3.777Y18.75
G01 X3.863Y18.937
G01 X4.026Y19.123
G01 X4.54Y19.31
G01 X5.054Y19.123
G01 X5.217Y18.937
G01 X5.303Y18.75
G01 X5.338Y18.564
G01 X5.329Y18.377
G01 X5.273Y18.19
G01 X5.159Y18.004
M5
G01 X12.56Y23.756
M3
G01 X12.56Y19.203
G01 X12.779Y19.016
G01 X12.893Y18.83
G01 X12.949Y18.643
G01 X12.958Y18.456
G01 X12.923Y18.27
G01 X12.837Y18.083
G01 X12.674Y17.897
G01 X12.16Y17.71
G01 X11.646Y17.897
G01 X11.483Y18.083
G01 X11.397Y18.27
G01 X11.362Y18.456
G01 X11.371Y18.643
G01 X11.427Y18.83
G01 X11.541Y19.016
G01 X11.76Y19.203
G01 X11.76Y23.424
G01 X11.76Y23.424
G01 X9.827Y25.357
G01 X9.74Y25.339
G01 X9.65Y25.331
G01 X9.555Y25.333
G01 X9.455Y25.347
G01 X9.348Y25.378
G01 X9.232Y25.43
G01 X9.1Y25.522
G01 X8.881Y25.824
G01 X8.822Y26.192
G01 X8.851Y26.351
G01 X8.896Y26.47
G01 X8.95Y26.567
G01 X9.01Y26.648
G01 X9.076Y26.716
G01 X9.146Y26.774
G01 X9.22Y26.823
G01 X9.22Y28.555
G01 X9.205Y28.555
G01 X9.205Y30.055
G01 X10.255Y30.055
G01 X10.255Y28.555
G01 X10.02Y28.555
G01 X10.02Y26.823
G01 X10.05Y26.805
G01 X10.081Y26.784
G01 X10.113Y26.76
G01 X10.147Y26.732
G01 X10.184Y26.698
G01 X10.224Y26.655
G01 X10.271Y26.595
G01 X10.359Y26.436
G01 X10.409Y26.261
G01 X10.418Y26.186
G01 X10.42Y26.127
G01 X10.418Y26.078
G01 X10.414Y26.034
G01 X10.408Y25.994
G01 X10.401Y25.957
G01 X10.393Y25.923
G01 X12.56Y23.756
M5
G01 X31.965Y15.985
M3
G01 X32.153Y16.711
G01 X32.34Y16.977
G01 X32.528Y17.156
G01 X32.715Y17.284
G01 X32.903Y17.376
G01 X33.09Y17.437
G01 X33.278Y17.473
G01 X33.653Y17.473
G01 X33.84Y17.437
G01 X34.028Y17.376
G01 X34.215Y17.284
G01 X34.403Y17.156
G01 X34.59Y16.977
G01 X34.778Y16.711
G01 X34.965Y15.985
G01 X34.778Y15.259
G01 X34.59Y14.993
G01 X34.403Y14.814
G01 X34.215Y14.686
G01 X34.028Y14.594
G01 X33.84Y14.533
G01 X33.653Y14.497
G01 X33.278Y14.497
G01 X33.09Y14.533
G01 X32.903Y14.594
G01 X32.715Y14.686
G01 X32.528Y14.814
G01 X32.34Y14.993
G01 X32.153Y15.259
G01 X31.965Y15.985
M5
G01 X14.185Y15.985
M3
G01 X14.373Y16.711
G01 X14.56Y16.977
G01 X14.748Y17.156
G01 X14.935Y17.284
G01 X15.123Y17.376
G01 X15.31Y17.437
G01 X15.498Y17.473
G01 X15.873Y17.473
G01 X16.06Y17.437
G01 X16.247Y17.376
G01 X16.435Y17.284
G01 X16.622Y17.156
G01 X16.81Y16.977
G01 X16.997Y16.711
G01 X17.185Y15.985
G01 X16.997Y15.259
G01 X16.81Y14.993
G01 X16.622Y14.814
G01 X16.435Y14.686
G01 X16.247Y14.594
G01 X16.06Y14.533
G01 X15.873Y14.497
G01 X15.498Y14.497
G01 X15.31Y14.533
G01 X15.123Y14.594
G01 X14.935Y14.686
G01 X14.748Y14.814
G01 X14.56Y14.993
G01 X14.373Y15.259
G01 X14.185Y15.985
M5

M5 ; Disable End-Effector Signal

; Returning the Deactivating Tool-1
C0 ; PWM Tool select demultiplexer to select tool zero which is the empty tool slot in multiplexers
#TODO X0Y0Z0 ;  ;Remove tool offset coordinate
G01 X165Y0Z11 ; Go to Tool-1 Home Pos
G01 X92 ; Enter Female Kinematic Mount Home Pos
A0 ; Latch OFF Kinematic Mount
G4 P5 ; Wait for Kinematic Mount to fully detach
G01 X188 ; Exit Female Kinematic Mount Home Pos

