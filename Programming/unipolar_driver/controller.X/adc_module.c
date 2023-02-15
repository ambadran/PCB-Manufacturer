
#include "unipolar_driver.h"

void adc_deinit() {
    ADON = 0;  // no power to ADC module
    ANSELbits.ANS = 0b0000;  // all pins are digital pins
}