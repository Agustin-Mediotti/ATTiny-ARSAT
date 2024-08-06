#include <Arduino.h>
#include <avr/pgmspace.h>

#include "../utils/frequencies.h" // Include frequencies file
#include "../utils/durations.h"   // Include durations file

int speakerPin = 0; // Pin PB0

void setup()
{
  // Iterate over the audio peaks:
  for (uint8_t thisPeak = 0; thisPeak < sizeof(frequencies) / sizeof(frequencies[0]); thisPeak++)
  {
    uint8_t dur = pgm_read_byte(&durations[thisPeak]);
    uint16_t freq = pgm_read_word(&frequencies[thisPeak]);

    tone(speakerPin, freq, dur);

    // To set a minimum time between frequencies.
    int pauseBetweenFreq = dur * 1;
    delay(pauseBetweenFreq);

    // Stop the tone playing:
    noTone(speakerPin);
  }
}

void loop()
{
  // The setup() is enough to play it once.
}