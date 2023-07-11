
#include "includes.h"


void TMR0_init() {
    T0CS = 0;  // clock source: internal clock
    PSA = 1;  // pre-scalar value assigned to watchdog instead of TMR0
              // so that prescalar is 1
//    OPTION_REGbits.PS = 0b000;  // pre-scalar value is 2
}