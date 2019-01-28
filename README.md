# Blink- Smart-Doorbell
Security, connection, convenience.  A doorbell add-on that upon sensing movement, captures a picture and takes an audio recording till the motion ceases. Additionally, it permits communication between the visitor and the home-owner by allowing visitors to send texts in case they arrive in the absence of the home-owner. The home-owner also has a secure button-operated command on their phone to open a compartment in the doorbell body that they can use to store things in.


Problem: Living in Berkeley, it isn't a surprise that my neighbourhood is plagued with robberies and break-ins. Being a college student, I couldn't afford to buy a security system, so I decided to make my own using items I had lying around. I demo-ed this project for my EE49 class. 



This project made the use of both an ESP32 and an Arduino Uno - however, the entire project could be made with just an Arduino Uno. The reason I chose not to do so is because my Uno board is very old and unstable while handling too many tasks. Since I did not want to invest in another and had an ESP32 lying around, I decide to split this project up into two different components - one that handles security (Arduino) and the other that handles communication. 
