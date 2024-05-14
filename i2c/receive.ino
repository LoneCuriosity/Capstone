#include <SPI.h>
char rxMsg[20] = "";
int i = 0;
char ch;
volatile bool flag = false;

void setup()
{
  Serial.begin(115200);
  pinMode(SS, INPUT_PULLUP);
  pinMode(MISO, OUTPUT);
  SPCR |= _BV(SPE);
  SPCR |= !(_BV(MSTR));
  SPI.attachInterrupt();
}

void loop()
{
  if (flag == true)
  {
    rxMsg[i] = '\0';
    Serial.println(rxMsg);
    i = 0;
    memset(rxMsg, 0, sizeof rxMsg);
    flag = false;
  }
}

ISR(SPI_STC_vect)
{
  ch = SPDR;
  if (ch != '\n')
  {
    rxMsg[i] = ch;
    i++;
  }
  else
  {
    flag = true;
  }
}