
#ifndef COIL_CONTROL_H
#define COIL_CONTROL_H

void coil_init(void);

void even_pins_set_clear(void);

void even_pins_clear_set(void);

void odd_pins_set_clear(void);

void odd_pins_clear_set(void);

void reset_all_pins(void);

void (*func_ptr[2][2][2])(void);

#endif