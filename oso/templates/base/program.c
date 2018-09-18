#include <avr/io.h>
#include <delay.h>
#include <stdio.h>


//declare global arrays for two patterns
unsigned char p1[7] = { 0b10000001,
                        0b01000010,    
                        0b00100100,
                        0b00011000,
                        0b00100100,
                        0b01000010,
                        0b10000001 };

unsigned char p2[15] = {0b10000000,
                        0b01000000,    
                        0b00100000,
                        0b00010000,
                        0b00001000,
                        0b00000100,
                        0b00000010,
                        0b00000001,
                        0b00000010,
                        0b00000100,
                        0b00001000,  
                        0b00010000,
                        0b00100000,
                        0b01000000,
                        0b10000000 };
// Voltage Reference: AVCC pin
#define ADC_VREF_TYPE ((0<<REFS1) | (1<<REFS0) | (0<<ADLAR))

// Read the AD conversion result
unsigned int read_adc(unsigned char adc_input)
{
    ADMUX=adc_input | ADC_VREF_TYPE;
    // Delay needed for the stabilization of the ADC input voltage
    delay_us(10);
    // Start the AD conversion
    ADCSRA|=(1<<ADSC);
    // Wait for the AD conversion to complete
    while ((ADCSRA & (1<<ADIF))==0);
    ADCSRA|=(1<<ADIF);
    return ADCW;
}

                    
void delayKitt()
{
    delay_ms(read_adc(4));
}                         


unsigned char i=0;
unsigned char j=0;                //loop counter

int main(void)
{

    // ADC initialization
    // ADC Voltage Reference: AVCC pin
    // ADC Auto Trigger Source: ADC Stopped
    // Digital input buffers on ADC0: On, ADC1: On, ADC2: On, ADC3: On
    // ADC4: Off, ADC5: On
    DIDR0=(0<<ADC5D) | (1<<ADC4D) | (0<<ADC3D) | (0<<ADC2D) | (0<<ADC1D) | (0<<ADC0D);
    ADMUX=ADC_VREF_TYPE;
    ADCSRA=(1<<ADEN) | (0<<ADSC) | (0<<ADATE) | (0<<ADIF) | (0<<ADIE) | (1<<ADPS2) | (1<<ADPS1) | (1<<ADPS0);
    ADCSRB=(0<<ADTS2) | (0<<ADTS1) | (0<<ADTS0);   

    
    DDRD = 0xFF;                //PB as output
    //PORTD= 0x00;             //keep all LEDs off 

    while(1)
    {
        //# if SW0 is pressed show pattern 1
        if(PINC.0==0)                                           
        {
            PORTD=p1[i];  //output data
            i++;
            if(i>=6) i=0; //restarts counter 
            delayKitt();  //wait for some time
        }
        
        if(PINC.0==1)           
        {
            PORTD=p2[j];  //output data
            j++;
            if(j>=13) j=0; //restarts counter 
            delayKitt();  //wait for some time
        }
    }        
} 