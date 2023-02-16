
#ifndef CPU_MAP_H
#define CPU_MAP_H

// Pin definitions
#define INPUT_TRIS TRISIO3
#define COIL1_TRIS TRISIO0
#define COIL2_TRIS TRISIO1
#define COIL3_TRIS TRISIO2
#define COIL4_TRIS TRISIO4

#ifndef ENABLE_SOFT_UART
#define debug_pin_tris TRISIO5
#else
#define SOFT_UART_TX_TRIS TRISIO5
#endif

#define INPUT GPIO3
#define COIL1 GPIO0
#define COIL2 GPIO1
#define COIL3 GPIO2
#define COIL4 GPIO4

#ifndef ENABLE_SOFT_UART
#define debug_pin GPIO5
#else
#define S_UART_TX GPIO5
#endif


#endif