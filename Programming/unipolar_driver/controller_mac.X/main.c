/*
 * File:   main.c
 * Author: AbdulRahman
 *
 * Created on October 30, 2022, 7:31 PM
 */


#include "includes.h"

void main(void) {
    
    // INITs/DEINITs
    coil_init();
    comparator_deinit();
    interrupt_init();
    TMR1_init();
    adc_deinit();
#ifdef ENABLE_SOFT_UART
    soft_uart_init();
#endif
    
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
        
#ifdef ENABLE_SOFT_UART

        soft_uart_send_ALL();
   
        __delay_ms(10);
#endif
        
        
    }
    
    return;
}


void __interrupt() ISR(void) {
    
    if(TMR1IF) {
        TMR1_ISR();
        TMR1IF = 0;
        
    }
    
    
    return;
    
}