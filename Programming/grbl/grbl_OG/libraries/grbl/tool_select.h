/* 
 * NEWLY ADDED !!!!!!
  tool_select.h - feeds to a demultiplexer to choose which 
                  end effector gets the PWM signal
  part of grbl

 */

#ifndef TOOL_SELECT_H
#define TOOL_SELECT_H

void tool_select_init();

void tool_select_set_state(uint8_t state);

void tool_select_run(uint8_t state);

#endif
