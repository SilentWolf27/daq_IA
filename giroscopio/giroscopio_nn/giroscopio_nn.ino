//https://github.com/jarzebski/Arduino-MPU6050

#include <Wire.h> //Libreria para I2C
#include <MPU6050.h>

MPU6050 mpu;
double x[3];
double y0[2]; //Entradas de la segunda capa
double y[0];    //Salida de la red neuronal

//Acomodar los pesos y bias de cada neurona
const double w0[2][3] = {
    { 1.8250473, -0.03614833, 0.16480891 },
    { -0.78917944, -0.45210207, 0.6395318 }
  };
const double b0[2] = { 1.1012075, 0.57231617};

const double w1[1][2] = { {2.1686864, -0.9566574} };
const double b1[1] = { -1.3464559 };

//Valores para el preprocesamiento
const double mean[3] = { -327.381395, -902.432558, 266.604651 };
const double standard[3] = { 14457.436125, 5280.763678, 5691.1240 };
  
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
  Vector rawAccel = mpu.readRawAccel();
  double normData[3];
  normData[0] = normalize(rawAccel.XAxis, mean[0], standard[0]);
  normData[1] = normalize(rawAccel.YAxis, mean[1], standard[1]);
  normData[2] = normalize(rawAccel.ZAxis, mean[2], standard[2]);
  
  fordwardPropagation(normData[0], normData[1], normData[2]);
  Serial.println(y[0] > 0.8 ? "Arriba" : "Abajo");

  delay(100);
}

double normalize(double data, double mean, double dStd){
  return (data - mean) / dStd;
}

int fordwardPropagation(double x0, double x1, double x2){
  x[0] = x0;
  x[1] = x1;
  x[2] = x2;
  //Primer capa
  for (int j = 0; j < 2; j++){ //Para cada neurona
    double aux = 0.0;
    for (int i = 0; i < 3; i++){ //Para cada peso
      aux += w0[j][i] * x[i]; 
    }
    y0[j] = relu(aux + b0[j]);
  } 

  //Capa de salida
  for (int j = 0; j < 1; j++){ //Para cada neurona
    double aux = 0.0;
    for (int i = 0; i < 2; i++){ //Para cada peso
      aux += w1[j][i] * y0[i];  
    }
    y[j] = sigmoid(aux + b1[j]);
    y[j] = round(y[j]);
  } 
}

double relu(double x){
   return x > 0 ? x : 0.0;
}

double sigmoid(double x){
   return 1 / (1 + exp(-x));
}
