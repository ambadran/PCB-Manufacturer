
#ifndef CONFIG_H
#define CONFIG_H


// User Definned Configs
//#define DEBUG_MODE
//#define CONSTANT_STEPS
#define ENABLE_SOFT_UART  // comment to enable usage of GPIO5 as debug pin

#if(defined(ENABLE_SOFT_UART) && defined(DEBUG_MODE))
#error  // Can't enable software uart and enable debug pin in the same time
#endif


// micro controller specific defs
#define _XTAL_FREQ 4000000

#endif