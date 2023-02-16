
#include "includes.h"

void soft_uart_init() {
    
    // GPIO5 as tx
    SOFT_UART_TX_TRIS = 0;
    S_UART_TX = 1;  // idle state
    
}

void soft_uart_send(uint8_t value) {
    
    // start condition
    S_UART_TX = 0;
    __delay_us(one_bit_delay);
    
    // data frame
    for(uint8_t bit_counter=0; bit_counter<8; bit_counter++) {
        
        S_UART_TX = (value>>bit_counter) & 0b1;
        
        __delay_us(one_bit_delay);
    }
    
    // stop condition
    S_UART_TX = 1;
    __delay_us(one_bit_delay);
    
}