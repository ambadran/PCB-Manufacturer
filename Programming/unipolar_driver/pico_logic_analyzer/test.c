#include <stdio.h>
#include <stdint.h>

uint8_t intToAscii(uint8_t num) {
  return '0' + num;
}

void intToAscii_s(int num) {
  
  uint8_t mod;
  while (num != 0) {

   mod = num%10;
   printf("%d\n", intToAscii(mod));

   num /= 10;

  }

  /* printf('0' + num); */
}


int main() {

  int num = 8;

  int ascii = '0' + num;

  printf("%c\n", ascii);
  printf("%c\n", intToAscii(8));

  printf("%d\n", ascii);
  printf("%d\n", intToAscii(8));

  printf("\n\n");

  intToAscii_s(123);



}
