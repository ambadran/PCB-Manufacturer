/* 
 * NEWLY ADDED !!!!!!
  power_supply.h - Opens relays to power up the power supply
  part of grbl

 */


#include "grbl.h"


void power_supply_init() {

  // configuring the power supply enable pin as output and clear it
  POWER_SUPPLY_DDR |= (1 << POWER_SUPPLY_BIT);

  power_supply_set_state(POWER_SUPPLY_DISABLE);

}

void power_supply_set_state(uint8_t state) {

  if (state == POWER_SUPPLY_ENABLE) {

    // setting the power supply enable pin
    POWER_SUPPLY_PORT |= (1 << POWER_SUPPLY_BIT);

  } else {

    // clears the power supply enable pin
    POWER_SUPPLY_PORT &= ~(1 << POWER_SUPPLY_BIT);

  }

}


void power_supply_run(uint8_t state) {

  if (sys.state == STATE_CHECK_MODE) { return; }  // copied from spindle_control.c :)

  protocol_buffer_synchronize(); // Empty planner buffer to ensure spindle is set when programmed.  // copied from spindle_control.c :)

  power_supply_set_state(state);

}
