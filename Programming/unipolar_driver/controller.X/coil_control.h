
#ifndef COIL_CONTROL_H
#define COIL_CONTROL_H

void coil_init();

void even_pins_set_clear();

void even_pins_clear_set();

void odd_pins_set_clear();

void odd_pins_clear_set();

void reset_all_pins();

void (*func_ptr[2][2][2])();

#endif