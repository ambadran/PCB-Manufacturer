/* 
 * NEWLY ADDED !!!!!!
  latch.h - kinematic mount controller
  part of grbl

  praying to god it works ;)

   
 */


#ifndef latch_control_h
#define latch_control_h

// initializes the latch pin
void latch_init();

// sets the state of the latch pin
void latch_set_state(uint8_t state);

// set the wanted state  (like spindle_run)
void latch_run(uint8_t state);

#endif
