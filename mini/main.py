import requests
import json

if __name__ == '__main__':
    
    
   # url = 'http://httpbin.org/get'
    #url = 'http://localhost:8080/bloc/index.jsp'
    #args = {'nombre':'Luis','curso':'python','nivel':'intermedio'}#diccionario
    #args = {'usuario':'admin','clave':'clave'}#diccionario
    url = 'http://localhost:8080/bloc/acceso'
    #args = {'usuario':'usuario', 'clave':'clave','mesa':'35'}
    payload = {'usuario':'maquina', 'clave':'clave','mesa':'35'}

    headers = {'Content-Type' : 'application/json'}
    
    #con json internamente se serializa
    #con data nosotros tenemos que serializarlo
    response = requests.post(url,data=payload)
    print(response.url)

    if response.status_code == 200:
        
        
        content = response.content
        print(content)
        
        file = open("archivo.txt", 'wb')
        file.write(content)
        file.close()
        
        
        #print(response.content)
       #cabecera_json = json.loads(response.text)
       # origin = cabecera_json['origin']
       # print(cabecera_json)
       
#        headers_response = response.headers#diccionario
#        print(headers_response)
#        set_cookie = headers_response['Set-Cookie']
#        print(set_cookie)