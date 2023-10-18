
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
    for(uint8_t i=0; i<8; i++) {

        S_UART_TX = (value>>i) & 0b1;

        __delay_us(one_bit_delay);
    }

    // stop condition
    S_UART_TX = 1;
    __delay_us(one_bit_delay);
    __delay_us(one_bit_delay);
        
}

unsigned divu10(unsigned n) {
    unsigned q, r;
    q = (n >> 1) + (n >> 2);
    q = q + (q >> 4);
    q = q + (q >> 8);
//    q = q + (q >> 16);  // it doesn't support 16bits anyway
    q = q >> 3;
    r = n - (((q << 2) + q) << 1);
    return q + (r > 9);
}

void soft_uart_send_int_AS_IS(int value) {
        // start condition
    S_UART_TX = 0;
    __delay_us(one_bit_delay);

    // data frame 1
    uint8_t i;
    for(i=8; i<16; i++) {

        S_UART_TX = (value>>i) & 0b1;

        __delay_us(one_bit_delay);
    }

    // stop condition
    S_UART_TX = 1;
    __delay_us(one_bit_delay);
    __delay_us(one_bit_delay);
    
            // start condition
    S_UART_TX = 0;
    __delay_us(one_bit_delay);

    // data frame 1
    for(i=0; i<8; i++) {

        S_UART_TX = (value>>i) & 0b1;

        __delay_us(one_bit_delay);
    }

    // stop condition
    S_UART_TX = 1;
    __delay_us(one_bit_delay);
    __delay_us(one_bit_delay);
}

void soft_uart_send_int(int value){

    // should implement a while loop (value!=0)
    // and a dynamic array expanding with every new digit from the int
    uint8_t third_digit = intToASCII(value%10);
    value = divu10(value);
    uint8_t second_digit = intToASCII(value%10);
    value = divu10(value);
    uint8_t first_digit = intToASCII(value%10);
    
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

void soft_uart_send_ALL() {
    // because the RAM is sooo freakin tiny, I couldn't even sprintf two characters at once ;)
//        sprintf(message, "OF_num_TMR1: %d\ntarget_OF_num: %d\ncurrent_position: %d\n", OF_num_TMR1, target_OF_num, current_position);
//        sprintf(message, "0%d", OF_num_TMR1);
//        soft_uart_send_string(message);

    soft_uart_send_string("OF_num_TMR1: ");
    soft_uart_send_int(OF_num_TMR1);
    soft_uart_send_string("\n");

    soft_uart_send_string("target_OF_num: ");
    soft_uart_send_int(target_OF_num);
    soft_uart_send_string("\n");

    soft_uart_send_string("current_position: ");
    soft_uart_send_int(current_position);
    soft_uart_send_string("\n");

}

#endif






















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
    
    
//    uint8_t first_digit = (value!=0)?0:intToASCII(value%10);
//    value *= 0.1;
//    uint8_t second_digit = (value!=0)?0:intToASCII(value%10);
//    value *= 0.1;
//    uint8_t third_digit = (value!=0)?0:intToASCII(value%10);
    
//    soft_uart_send_uint8_t((value!=0) ? intToASCII(value%10) : 0);
//    soft_uart_send_uint8_t(value);
//    value *= 0.1;
//    soft_uart_send_uint8_t((value!=0) ? intToASCII(value%10) : 0);
//    soft_uart_send_uint8_t(value);
//    value *= 0.1;
//    soft_uart_send_uint8_t((value!=0) ? intToASCII(value%10) : 0);
//    soft_uart_send_uint8_t(value%10);
