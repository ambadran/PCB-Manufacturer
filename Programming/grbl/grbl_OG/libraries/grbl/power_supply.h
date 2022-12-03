/* 
 * NEWLY ADDED !!!!!!
  power_supply.h - Opens relays to power up the power supply
  part of grbl

 */

#ifndef POWER_SUPPLY_H
#define POWER_SUPPLY_H

// initializes the power supply enable pin
void power_supply_init();

// sets the state of the power supply enable pin
void power_supply_set_state(uint8_t state);

// runs the pin after waiting for buffer
void power_supply_run(uint8_t state);

#endif
