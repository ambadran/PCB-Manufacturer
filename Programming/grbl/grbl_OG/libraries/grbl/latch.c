/* 
 * NEWLY ADDED !!!!!!
  latch.c - kinematic mount controller
  part of grbl

  praying to god it works ;)

   
 */

#include "grbl.h"

void latch_init() {

  // configures the latch pin output and let it be LOW
  LATCH_DDR |= (1<<LATCH_BIT); // Configure as latch output pin.

  latch_set_state(LATCH_CLOSE);

}

void latch_set_state(uint8_t state) {

  if (state == LATCH_OPEN) {

  // sets the latch pin
  LATCH_PORT |= (1<<LATCH_BIT);

  } else {

  // clears the latch pin
  LATCH_PORT &= ~(1<<LATCH_BIT);

  }

}

void latch_run(uint8_t state) {

  if (sys.state == STATE_CHECK_MODE) { return; }  // copied from spindle_control.c :)

  // I think this will ensure this command will get executed in the right time after the previous commands
  protocol_buffer_synchronize(); // Empty planner buffer to ensure spindle is set when programmed.  // copied from spindle_control.c :)

  latch_set_state(state);

}


