#include <Arduino.h>
int W,X;
int A;
int B=0,C=0,D=0;
void disp_7447(int D,int C,int B,int A)
{
      digitalWrite(2,A);
}
void setup(){
        pinMode(5,INPUT);
        pinMode(6,INPUT);
        pinMode(2,OUTPUT);
}
void loop(){
        W=digitalRead(5);
        X=digitalRead(6);
        A=(!W&&!X)||(W&&X);
        digitalWrite(2,A);
        disp_7447(D,C,B,A);
}
