#include <SPI.h>

const int BUFFER_SIZE = 32;
char receivedBuffer[BUFFER_SIZE];
volatile boolean receivedMessage = false;

void setup() {
  Serial.begin(9600);
  SPCR |= _BV(SPE);
  SPI.attachInterrupt();
}

ISR (SPI_STC_vect) {
  static int bufferIndex = 0;
  
  if (bufferIndex < BUFFER_SIZE - 1) {
    receivedBuffer[bufferIndex] = SPDR;
    bufferIndex++;
    
    if (SPDR == '\0') {
      receivedMessage = true;
      bufferIndex = 0;
    }
  }
}

void loop() {
  if (receivedMessage) {
    Serial.println(receivedBuffer);
    receivedMessage = false;
  }
}