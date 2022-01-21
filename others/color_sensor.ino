#define S0 9//four output pins
#define S1 10
#define S2 11
#define S3 12
#define Read 8

int SavedArray[3];

void setup() 
{
  

Serial.begin(9600);
pinMode (S0 , OUTPUT);
pinMode (S1 , OUTPUT);
pinMode (S2 , OUTPUT);
pinMode (S3 , OUTPUT);
pinMode (Read, INPUT);
//setting frequency to 20%
digitalWrite(S0,HIGH);
digitalWrite(S1,LOW);
}

void loop() { 
   //RED
   digitalWrite(S2,LOW);
   digitalWrite(S3,LOW);
   int frequencyRed=pulseIn(Read , LOW);
  // frequencyRed = map(frequencyRed,25,72,0,255);
   delay(100);

   //BLUE
   digitalWrite(S2,LOW);
   digitalWrite(S3,HIGH);
    int frequencyBlue=pulseIn(Read , LOW);
  // frequencyBlue = map(frequencyBlue,30,90,0,255);
   delay(100);

  // frequencyBlue = map(frequencyBlue,30,90,0,255);
   delay(100);
   //GREEN
   digitalWrite(S2,HIGH);
   digitalWrite(S3,HIGH);
   int frequencyGreen=pulseIn(Read , LOW);
   //frequencyGreen = map(frequencyGreen,70,25,255,0);
   delay(100);  

   int Colors[3]= {frequencyRed,frequencyBlue,frequencyGreen};
   Serial.print("Color is ");
if(!(Colors[0]>=100&&Colors[1]>=100&&Colors[2]>=100)){
   
  if(frequencyGreen<frequencyBlue && frequencyGreen<frequencyRed)
  {
    Serial.println(frequencyGreen); Serial.println(frequencyRed); Serial.println(frequencyBlue);
   Serial.print("Green \n");
   }
   else if(frequencyRed<frequencyBlue && frequencyGreen>frequencyRed)
  {
   Serial.println(frequencyGreen); Serial.println(frequencyRed); Serial.println(frequencyBlue);
   Serial.print("Red \n");
   }else if(frequencyBlue<frequencyGreen && frequencyBlue<frequencyRed)
  {
    Serial.println(frequencyGreen); Serial.println(frequencyRed); Serial.println(frequencyBlue);
   Serial.print("Blue \n");
   }
}else{Serial.println("Color is Black");}
}
