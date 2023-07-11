#include <stdio.h>
#include <stdint.h>

void main() {

  uint8_t state = 3;

  uint8_t TOOL_SELECT_PORT = 0b10101000;

  TOOL_SELECT_PORT &= 0b11111000;
  TOOL_SELECT_PORT |= state;

  printf("%d\n", TOOL_SELECT_PORT);

  state = 4;

  TOOL_SELECT_PORT &= 0b11111000;
  TOOL_SELECT_PORT |= state;

  printf("%d\n", TOOL_SELECT_PORT);

  return;
}





// Wrong
  /* // the lowest 3 bits are the actual tool select value, should be set directly to the TOOL_SELECT_PORT */
  /* // the highest 5 bits are values of other modules, should be interfered with !! */
  /* state |= 0b11111000;  // setting the highest 5-bits and leaving the lowest 3-bits */


