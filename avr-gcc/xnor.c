#include<avr/io.h>
#include<stdbool.h>
int main(void){

bool w,x,a=0;
DDRB = 0b00000011; //8&9 as inputs
PORTB= 0b11111100;
DDRD = 0b00000100; //2as output

//DDRB |= (1<<DDB5);


while(1)
   {
	   w = (PINB & (1<<PINB0)) == (1<<PINB0);	
	   x = (PINB & (1<<PINB1)) == (1<<PINB1);
	  
	   a = ((!w)&&(!x)) || ((w)&&(x)) ;
	   PORTD |= (a<<2);

   }

	return 0;
}
