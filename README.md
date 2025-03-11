* Para que la app funcione es necesario
1) instalar dependencias pip install fastapi uvicorn
2) correr codigo python con python main.py
3) abrir otra terminal y ejecutar curl http://127.0.0.1:8000/nombres
4) visualizar la respuesta, en este caso:
StatusCode        : 200
StatusDescription : OK
Content           : ["Juan","MarÃ­a","Pedro"]
RawContent        : HTTP/1.1 200 OK
                    Content-Length: 25       
                    Content-Type: application/json
                    Date: Tue, 11 Mar 2025 18:27:15 GMT
                    Server: uvicorn

                    ["Juan","MarÃ­a","Pedro"]
Forms             : {}
Headers           : {[Content-Length, 25], [Content-Type, application/json], [Date, Tue, 11 Mar 2025 18:27:15 GMT], [Server, uvicorn]}
Images            : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 25
