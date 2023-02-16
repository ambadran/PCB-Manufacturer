
#ifndef SOFTWARE_UART_H
#define SOFTWARE_UART_H

#define baudrate 1200
#define one_bit_delay (1000000/baudrate)  // 1/baudrate * 10^6, ready to be put in delay_us

void soft_uart_init();

void soft_uart_send(uint8_t value);

#endif