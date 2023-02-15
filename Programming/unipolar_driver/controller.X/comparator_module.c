
#include "unipolar_driver.h"

void comparator_deinit() {
    CMCONbits.CM = 0b111;  // all pins digital
}