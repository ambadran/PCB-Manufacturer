
#ifndef SOFTWARE_UART_H
#define SOFTWARE_UART_H

#define baudrate 1200
//#define one_bit_delay (1000000/baudrate)  // 1/baudrate * 10^6, ready to be put in delay_us
#define one_bit_delay 905  // as measured from oscilloscope, output from raspberry pi pico 1200 baudrate

void soft_uart_init();

void soft_uart_send(uint8_t value);

void soft_uart_send_16bit(int value);

#endif