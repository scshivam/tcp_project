from django.shortcuts import render
from django.views.generic import TemplateView
import socket

class HomePageView(TemplateView):
    def post(self,request, **kwargs):
        try:
            htmlclass = "greendot"
            status = "Online"
            button = ""
            host = '192.168.0.197'
            port = 80  # The same port as used by the server
            inp = request.POST
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            s.connect((host, port))
            s.sendall(bytes(inp['message'][0],'utf-8'))
            data = s.recv(1024)
            s.close()
        except:
            button = "disabled"
            htmlclass = "reddot"
            status = "Offline"
            data = bytes("Please check your TCP server/network",'utf-8')
        return render(request,"index.html",{'result':data.decode("utf-8"),'sent':inp['message'][0],'htmlclass':htmlclass,'status':status, "button":button })
    def get(self,request, **kwargs):
        try:
            button = ""
            htmlclass = "greendot"
            status = "Online"
            host = '192.168.0.197'
            port = 80  # The same port as used by the server
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            s.connect((host, port))
            s.close()
        except:
            button = "disabled"
            htmlclass = "reddot"
            status = "Offline"
        return render(request, "index.html", {'htmlclass':htmlclass,'status':status, "button":button})