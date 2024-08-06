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
    uint16_t freq = pgm_read_word(&frequencies[thisPeak]);
    uint8_t dur = pgm_read_byte(&durations[thisPeak]);

    // Play the tone with the specified frequency and duration
    tone(speakerPin, freq, dur);

    // Wait for the duration of the tone plus a small pause
    delay(dur + 10); // Adding 10 ms pause to ensure the tone completes

    // Stop the tone playing:
    noTone(speakerPin);
  }
}

void loop()
{
  // The setup() is enough to play it once.
}
