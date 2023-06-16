
#include "includes.h"


#ifdef ENABLE_SOFT_UART

uint8_t intToASCII(uint8_t num) {
    return '0' + num;
//    return num;
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
    for(uint8_t i=0; i<8; i++) {

        S_UART_TX = (value>>i) & 0b1;

        __delay_us(one_bit_delay);
    }

    // stop condition
    S_UART_TX = 1;
    __delay_us(one_bit_delay);
    __delay_us(one_bit_delay);
        
}

void soft_uart_send_int(int value) {

//    uint8_t index = MAXDIGITS-1;
//    uint8_t* nums[MAXDIGITS];
//    while (value != 0) {
//
//        nums[index] = intToASCII(value%10);
////        nums[index] = value%10;
//        index--;
//                
////        value = (int)(value*0.1);
////        value = value*0.1;
//        value *= 0.1;
//    }
    
//    for(index=0; index<MAXDIGITS; index++) {
//        soft_uart_send_uint8_t(nums[index]);
//    }
    
    
    uint8_t first_digit = (value!=0)?0:intToASCII(value%10);
    value *= 0.1;
    uint8_t second_digit = (value!=0)?0:intToASCII(value%10);
    value *= 0.1;
    uint8_t third_digit = (value!=0)?0:intToASCII(value%10);
    
    soft_uart_send_uint8_t(first_digit);
    soft_uart_send_uint8_t(second_digit);
    soft_uart_send_uint8_t(third_digit);
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