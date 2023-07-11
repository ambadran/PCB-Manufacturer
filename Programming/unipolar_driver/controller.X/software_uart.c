
#include "includes.h"


#ifdef ENABLE_SOFT_UART

uint8_t intToASCII(uint8_t num) {
    return '0' + num;
}

void soft_uart_init() {
    
    // GPIO5 as tx
    SOFT_UART_TX_TRIS = 0;
    S_UART_TX = 1;  // idle state
    
}

void soft_uart_send_uint8_t(uint8_t value) {
        
    // start condition
    S_UART_TX = 0;
    __delay_us(one_bit_delay);

    // data frame 1
    for(uint8_t bit_counter=0; bit_counter<8; bit_counter++) {

        S_UART_TX = (value>>bit_counter) & 0b1;

        __delay_us(one_bit_delay);
    }

    // stop condition
    S_UART_TX = 1;
    __delay_us(one_bit_delay);
    __delay_us(one_bit_delay);
        
}

void soft_uart_send_int(int value) {

#define MAXDIGITS 3  // i don't think i will be sending more than 3 digits
    uint8_t mod;
    uint8_t* nums[MAXDIGITS] = {0, 0, 0};  
    uint8_t index = MAXDIGITS-1;
    while (value != 0) {

        mod = value%10;
        
        nums[index] = intToASCII(mod);
        index--;
        
        value /= 10;
    }
    
    for(index=0; index<MAXDIGITS; index++) {
        soft_uart_send_uint8_t(nums[index]);
    }
    
}

void soft_uart_send_string(char* string) {
    
    uint8_t i = 0;
    while (string[i] != '\0') {
        // getting ASCII value of character by casting it into an integer
        soft_uart_send_uint8_t((uint8_t)string[i]);
        i++;
    }
}

#endif