
#ifndef SOFTWARE_UART_H
#define SOFTWARE_UART_H

#define baudrate 1200
//#define one_bit_delay (1000000/baudrate)  // 1/baudrate * 10^6, ready to be put in delay_us
#define one_bit_delay 905  // as measured from oscilloscope, output from raspberry pi pico 1200 baudrate

char message[2]; // no enough memory for it ;;;)
//char tmp_char;

uint8_t intToASCII(uint8_t num);

void soft_uart_init();

void soft_uart_send_uint8_t(uint8_t value);

void soft_uart_send_int(int value);

void soft_uart_send_string(char* string);

#endif