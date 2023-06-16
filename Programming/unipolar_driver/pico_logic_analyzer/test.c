#include <stdio.h>
#include <stdint.h>

#define MAXDIGITS 3

uint8_t intToAscii(uint8_t num) {
  return '0' + num;
}

void intToAscii_s(int value) {
 
    uint8_t index = MAXDIGITS-1;
    uint8_t* nums[MAXDIGITS];
    /* while (value != 0) { */

    /*     printf("mod: %d, ascii: %d\n", value%10, intToAscii(value%10)); */
    /*     nums[index] = intToAscii(value%10); */
    /*     /1* nums[index] = value%10; *1/ */
    /*     index--; */
                
/* //        value = (int)(value*0.1); */
/* //        value = value*0.1; */
    /*     value *= 0.1; */
    /* } */

    nums[2] = (value!=0)?intToAscii(value%10):0;
    value *= 0.1;
    nums[1] = (value!=0)?intToAscii(value%10):0;
    value *= 0.1;
    nums[0] = (value!=0)?intToAscii(value%10):0;

    
    for(index=0; index<MAXDIGITS; index++) {
        printf("%d\n", nums[index]);
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
