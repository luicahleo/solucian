/*
    This sketch sends a string to a TCP server, and prints a one-line response.
    You must run a TCP server in your local network.
    For example, on Linux you can use this command: nc -v -l 3000
*/

#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>

#ifndef STASSID
#define STASSID "TP-LINK_51B440"
#define STAPSK  "telecomunicaciones"
//#define STASSID "libre"
//#define STAPSK  "10051982"
//#define STASSID "libre_plus"
//#define STAPSK  "10051982"
#endif

const char* ssid     = STASSID;
const char* password = STAPSK;

const char* host = "192.168.0.105";
const uint16_t port = 8266;
//const char* host = "10.3.141.1";
//const uint16_t port = 8267;

int contador = 0;

ESP8266WiFiMulti WiFiMulti;

void setup() {
  Serial.begin(115000);

  // We start by connecting to a WiFi network
  WiFi.mode(WIFI_STA);
  WiFiMulti.addAP(ssid, password);

  Serial.println();
  Serial.println();
  Serial.print("Wait for WiFi... ");

  while (WiFiMulti.run() != WL_CONNECTED) {
    Serial.print(".");
    delay(100);
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  delay(100);
}


void loop() {
  Serial.print("connecting to ");
  Serial.print(host);
  Serial.print(':');
  Serial.println(port);

  // Use WiFiClient class to create TCP connections
  WiFiClient client;

  if (!client.connect(host, port)) {
    Serial.println("connection failed");
    Serial.println((String)"wait: "+ contador + " seconds");
    delay(500);

    contador++;

    if (contador == 2){
      Serial.print("no hay servidor, mejor me duermo para no gastar energia.");
      ESP.deepSleep(0);
    }
    
    return;
  }

  // This will send the request to the server
  client.println("terraza 7");

  //read back one line from server
  Serial.println("receiving from remote server");
  Serial.println("............................");
  
  String line = client.readStringUntil('\r');
  Serial.println(line);

  Serial.println("closing connection");
  client.stop();

  //Serial.println("wait 1/10 sec...");
  //delay(100);

  Serial.println("entrando a deepSleep.... me voy a dormir");



  ESP.deepSleep(0);
}
