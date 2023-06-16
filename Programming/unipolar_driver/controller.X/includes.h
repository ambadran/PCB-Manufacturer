
#ifndef UNIPOLAR_DRIVER_H
#define UNIPOLAR_DRIVER_H

#include <xc.h>
#include <stdint.h>
#include <stdbool.h>
//#include <string.h>
//#include <stdio.h>

#include "config.h"
#include "fuses.h"
#include "cpu_map.h"
#include "adc_module.h"
#include "coil_control.h"
#include "comparator_module.h"
#include "interrupts.h"
#include "tmr1_module.h"

#ifdef ENABLE_SOFT_UART
#include "software_uart.h"
#endif

#endif