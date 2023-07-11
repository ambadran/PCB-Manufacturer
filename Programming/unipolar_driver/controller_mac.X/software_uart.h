
#ifndef SOFTWARE_UART_H
#define SOFTWARE_UART_H

//#define MAXDIGITS 3  // i don't think i will be sending more than 3 digits

#define baudrate 1200
//#define one_bit_delay (1000000/baudrate)  // 1/baudrate * 10^6, ready to be put in delay_us
#define one_bit_delay 905  // as measured from oscilloscope, output from raspberry pi pico 1200 baudrate

//char message[MAXDIGITS]; // no enough memory for it ;;;)

uint8_t intToASCII(uint8_t num);

unsigned divu10(unsigned n);

void soft_uart_init(void);

void soft_uart_send_uint8_t(uint8_t value);

void soft_uart_send_int_AS_IS(int value);

void soft_uart_send_int(int value);  //decided to do the calculations outside the send to not interfere with bit delays on sending
// then i redecided to implement it again because after thinking it through
// the calculations is done between the stop and start bits so it doesn't really matter

void soft_uart_send_string(char* string);

void soft_uart_send_ALL(void);

#endif