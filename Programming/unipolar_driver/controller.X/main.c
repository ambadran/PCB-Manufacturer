/*
 * File:   main.c
 * Author: AbdulRahman
 *
 * Created on October 30, 2022, 7:31 PM
 */


#include <xc.h>
#include <stdint.h>
#include <stdbool.h>
#include "config.h"

// Pin definitions
#define INPUT GPIO3
#define COIL1 GPIO0
#define COIL2 GPIO1
#define COIL3 GPIO2
#define COIL4 GPIO4

#define TMR1_PRELOADING_VALUE 59582



// Global Variables
int OF_num_TMR1 = 00;
int target_OF_num = 1;
int current_position;

bool CW_CCW_select = false;  // defaulted to clockwise rotation
bool pair_select = false;  // whether we will flip 0&2 or 1&3
bool set_clear_sequence = false;  // decide whether we will set,clear or clear,set
bool tmp_set_clear_sequence = false; // a buffer to let set_sequence increment every 2 cycles

#if CONSTANT_STEPS
#define num_steps 790
#else
int num_steps[2] = {780, 805};  // anti-clockwise has more steps than clock-wise
                                // this is because closing needs more torque
                                // and to gaurantee it reaches the end (even if it
                                // skips a couple of steps when it reaches the end)
#endif


// Function Definitions

void retrieve_current_position() {
    //TODO: read EEPROM to get it
    current_position = 0;
}

void update_current_position(int value) {
    //TODO: write value to EEPROM
    current_position = value;
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
                                

void start_timer() {
    
    if (CW_CCW_select) {
        // updating current position
        update_current_position(current_position - OF_num_TMR1);
        // set new target overflow number
        target_OF_num = num_steps - current_position;
    
    } else {
        // updating current position
        update_current_position(current_position + OF_num_TMR1);
        // set new target overflow number
        target_OF_num = current_position;
    
    }
    
    // zero out current overflow number with every new start
    OF_num_TMR1 = 0;
    
    // start timer if it's not already started
    TMR1ON = 1;
}

void stop_timer() {
    TMR1ON = 0;
}

void reset_all_pins() {
    COIL1 = 0;
    COIL2 = 0;
    COIL3 = 0;
    COIL4 = 0;
}


void main(void) {
    
    // TRIS registers
    TRISIO0 = 0;
    TRISIO1 = 0;
    TRISIO2 = 0;
    TRISIO3 = 1;
    TRISIO4 = 0;
    
    
    TRISIO5 = 0;
    GPIO5 = 0;
    
    // Comparator Module
    CMCONbits.CM = 0b111;  // all pins digital
    
    // ADC module
    ADON = 0;  // no power to ADC module
    ANSELbits.ANS = 0b0000;  // all pins are digital pins
    
    // TMR1 module
    TMR1GE = 0;  // external TMR1 enable pin disabled, TMR1 always on
    T1CONbits.T1CKPS = 0b00;  // Prescalar value = 1
    T1OSCEN = 0;  // not sure exactly what this pin does
//    T1SYNC = ;  // this bit is ignored
    TMR1CS = 0;  // TMR1 Clock Source is system clock (Fosc/4)
    TMR1ON = 0;  // TMR1 is on when needed
    TMR1 = TMR1_PRELOADING_VALUE;  // Pre-loading
    
    // Interrupt bits
    GIE = 1;  // enable global interrupt bit
    PEIE = 1;  // enable peripheral interrupt bit
    TMR1IE = 1;  // enable TMR1 interrupt enable bit
    
    // Initial Pin Setup
    reset_all_pins();
    
    // Initial delay
    __delay_ms(2000); // waiting for voltage to stabilize
    retrieve_current_position();
    
    // Main Routine
    while(1) {
        
        if(INPUT != CW_CCW_select) {
            CW_CCW_select = INPUT;
            start_timer();
        }
        
    }
    
    return;
}


void __interrupt() ISR(void) {
    
    if(TMR1IF) {
        
#if DEBUG_MODE
        GPIO5 = 1;  // for calculating start time
#endif
        
        TMR1 = TMR1_PRELOADING_VALUE; // pre-loading  -> frequency without pre-loading=9.0843Hz
        
        OF_num_TMR1++; // incrementing Overflow counter
        
        // setting motor pins

        pair_select = !pair_select;  // pair_select changes every cycle
        
        set_clear_sequence ^= tmp_set_clear_sequence;  // set_clear sequence changes every two cycles
        tmp_set_clear_sequence = !tmp_set_clear_sequence; // thus a dumy bit is combined with the
                                                          // original bit to change every 2 cycles
        
        (*func_ptr[CW_CCW_select][pair_select][set_clear_sequence])();  // executing correct motor sequence

        
        if (OF_num_TMR1 == target_OF_num) {
            TMR1ON = 0; // stops once number of steps is achieved
            reset_all_pins();
            
            // cycle finished at CW then it's at maximum position
            // cycle finished at CCW then it's at minimum position
//            if (CW_CCW_select) {
//                update_current_position(num_steps);
//            } else {
//                update_current_position(0);
//            }
            
//            OF_num_TMR1 = 0;
        }
        
        
        TMR1IF = 0;
        
#if DEBUG_MODE
        GPIO5 = 0;  // for calculating end time
        GPIO5 = !GPIO5;  // for debugging
#endif
    }
    
    return;
    
}