
#include "unipolar_driver.h"

// array of array of array of function address pointer
// the first array is an array of clock-wise/anti-clock-wise 2-d array
// the rows are even/odd, the columns are set_clear/clear_set for clock-wise
// the rows are odd/even, the columns are clear_set/set_clear for anti-clock-wise
void (*func_ptr[2][2][2])() = {
                                    {
                                        {even_pins_set_clear, even_pins_clear_set},
                                        {odd_pins_set_clear, odd_pins_clear_set}
                                    },
                                
                                    {
                                        {odd_pins_clear_set, odd_pins_set_clear},
                                        {even_pins_clear_set, even_pins_set_clear}
                                    }
                               };


void coil_init() {
    
    INPUT_TRIS = 1;
    COIL1_TRIS = 0;
    COIL2_TRIS = 0;
    COIL3_TRIS = 0;
    COIL4_TRIS = 0;
    
    debug_pin_tris = 0;
    debug_pin = 0;   
}

void even_pins_set_clear() {
    COIL2 = 1;
    COIL4 = 0;
}

void even_pins_clear_set() {
    COIL2 = 0;
    COIL4 = 1;
}

void odd_pins_set_clear() {
    COIL1 = 1;
    COIL3 = 0;
}

void odd_pins_clear_set() {
    COIL1 = 0;
    COIL3 = 1;
}

void reset_all_pins() {
    COIL1 = 0;
    COIL2 = 0;
    COIL3 = 0;
    COIL4 = 0;
}
