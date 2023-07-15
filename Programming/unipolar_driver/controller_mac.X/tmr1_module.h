
#ifndef TMR1_MODULE_H
#define TMR1_MODULE_H

#define TMR1_PRELOADING_VALUE 59582

// Global Variables
int OF_num_TMR1 = 00;
int target_OF_num = 1;
int current_position;

uint8_t CW_CCW_select = 0;  // defaulted to clockwise rotation
bool pair_select = false;  // whether we will flip 0&2 or 1&3
bool set_clear_sequence = false;  // decide whether we will set,clear or clear,set
bool tmp_set_clear_sequence = false; // a buffer to let set_sequence increment every 2 cycles

#ifdef CONSTANT_STEPS
#define num_steps 790
#else
int num_steps[2] = {570, 780};  // anti-clockwise has more steps than clock-wise
                                // this is because closing needs more torque
                                // and to gaurantee it reaches the end (even if it
                                // skips a couple of steps when it reaches the end)
#endif


void TMR1_init(void);

void start_timer(void);

void stop_timer(void);

void retrieve_current_position(void);

void update_current_position(int value);

void TMR1_ISR(void);

#endif