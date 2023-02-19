
#include "includes.h"

void interrupt_init() {
    GIE = 1;  // enable global interrupt bit
    PEIE = 1;  // enable peripheral interrupt bit
    TMR0IE = 0;  // FUCK YOU TMR0 ;) 
    TMR1IE = 1;  // enable TMR1 interrupt enable bit
}