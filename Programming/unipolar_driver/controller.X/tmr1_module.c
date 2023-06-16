
#include "includes.h"

void TMR1_init() {
    TMR1GE = 0;  // external TMR1 enable pin disabled, TMR1 always on
    T1CONbits.T1CKPS = 0b00;  // Prescalar value = 1
    T1OSCEN = 0;  // not sure exactly what this pin does
//    T1SYNC = ;  // this bit is ignored
    TMR1CS = 0;  // TMR1 Clock Source is system clock (Fosc/4)
    TMR1ON = 0;  // TMR1 is on when needed
    TMR1 = TMR1_PRELOADING_VALUE;  // Pre-loading
}

void start_timer() {
    
    if (CW_CCW_select) { // clockwise motion - shaft locking
        // updating current position
        update_current_position(current_position - OF_num_TMR1);
        
        // set new target overflow number
#ifdef CONSTANT_STEPS
        target_OF_num = num_steps - current_position;
#else
        target_OF_num = num_steps[1] - current_position;
#endif
        
    } else {  // anti-clockwise motion - shaft unlocking
        // updating current position
        update_current_position(current_position + OF_num_TMR1);
        
        // set new target overflow number
#ifdef CONSTANT_STEPS
        target_OF_num = current_position;
#else
        if (current_position > num_steps[0]) {
            target_OF_num = num_steps[0];
        } else {
            target_OF_num = current_position;
        }
#endif
    }
    
    // zero out current overflow number with every new start
    OF_num_TMR1 = 0;
    
    // start timer if it's not already started
    TMR1ON = 1;
}

void stop_timer() {
    TMR1ON = 0;
}

void retrieve_current_position() {
    //TODO: read EEPROM to get it
    current_position = 0;
}

void update_current_position(int value) {
    //TODO: write value to EEPROM
    current_position = value;
}

void TMR1_ISR() {
        
#ifdef DEBUG_MODE
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

//        soft_uart_send_16bit(OF_num_TMR1);
        
        if (OF_num_TMR1 == target_OF_num) {
            TMR1ON = 0; // stops once number of steps is achieved
            reset_all_pins();
            
        }
        
#ifdef DEBUG_MODE
        GPIO5 = 0;  // for calculating end time
        GPIO5 = !GPIO5;  // for debugging
#endif
}