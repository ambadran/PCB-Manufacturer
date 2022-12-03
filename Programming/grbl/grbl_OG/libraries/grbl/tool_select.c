/* 
 * NEWLY ADDED !!!!!!
 *  tool_select.c - feeds to a demultiplexer to choose which 
                  end effector gets the PWM signal
  part of grbl

 */


#include "grbl.h"

void tool_select_init() {

  // Turning on the last 3 bits
  TOOL_SELECT_DDR |= 0b00000111;

  tool_select_set_state(TOOL0);

}

void tool_select_set_state(uint8_t state) {

  // state is a 3-bit value aka 0-7 
  if (state > 7) {
    //ERROR, don't want to play with other unaccounted for port bits
    return;  
  }
  
  // First clear the lowest 3-bits of the TOOL_SELECT_PORT
  TOOL_SELECT_PORT &= 0b11111000;

  // Then setting it with the new value
  TOOL_SELECT_PORT |= state;


}

void tool_select_run(uint8_t state) {

  if (sys.state == STATE_CHECK_MODE) { return; }  // copied from spindle_control.c :)

  // I think this will ensure this command will get executed in the right time after the previous commands
  protocol_buffer_synchronize(); // Empty planner buffer to ensure spindle is set when programmed.  // copied from spindle_control.c :)

  tool_select_set_state(state);

}

