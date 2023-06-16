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
        
        // because the RAM is sooo freakin tiny, I couldn't even sprintf two characters at once ;)
//        sprintf(message, "OF_num_TMR1: %d\ntarget_OF_num: %d\ncurrent_position: %d\n", OF_num_TMR1, target_OF_num, current_position);
//        sprintf(message, "0%d", OF_num_TMR1);
//        soft_uart_send_string(message);

//        soft_uart_send_string("OF_num_TMR1: ");
//        soft_uart_send_int(OF_num_TMR1);
//        soft_uart_send_string(" \n");
        
        soft_uart_send_string("target_OF_num: ");
        soft_uart_send_int(target_OF_num);
        soft_uart_send_string(" \n");
        
//        soft_uart_send_string("current_position: ");
//        soft_uart_send_int(current_position);
//        soft_uart_send_string(" \n");
   
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