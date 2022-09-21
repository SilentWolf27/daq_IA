//https://github.com/jarzebski/Arduino-MPU6050

#include <Wire.h> //Libreria para I2C
#include <MPU6050.h>

MPU6050 mpu;
void setup() {
  Serial.begin(9600);

  // Initialize MPU6050
  //Serial.println("Inicializando MPU6050");
  while(!mpu.begin(MPU6050_SCALE_2000DPS, MPU6050_RANGE_2G))
  {
    //Serial.println("Buscando...");
    //delay(100);
  }
  
  mpu.calibrateGyro();
}

void loop() {
  
}

void printMPU6050Data(){
  Vector rawGyro = mpu.readRawGyro();
  Vector rawAccel = mpu.readRawAccel();
   
  Serial.println(
    String(rawGyro.XAxis) + " " + 
    String(rawGyro.YAxis) + " " + 
    String(rawGyro.ZAxis) + " " + 
    String(rawAccel.XAxis) + " " +
    String(rawAccel.YAxis) + " " +
    String(rawAccel.ZAxis)  
  );
}

void serialEvent() {
  String data = Serial.readStringUntil('\n');
 
   if(data == "G"){
     printMPU6050Data();  
   }
   else if(data == "test"){
     Serial.println("OK");
   }
}
