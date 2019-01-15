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
            data1 = s.recv(1024)
            s.sendall(b'0')
            data = s.recv(1024)
            list_data = [x.decode("utf-8") for x in data.split()]
            result = []
            appliances = ["BULB", "PUMP", "INVERTER"]
            icons = ["fa fa-lightbulb", "fa fa-plug", "fa fa-calendar-alt"]
            for x in range(len(list_data)):
                if list_data[x] == "ON":
                    result.append(
                        {'colour': 'yellow', 'status': list_data[x], "icon": icons[x], "appliance": appliances[x],
                         "index": x + 1})
                else:
                    result.append(
                        {'colour': 'white', 'status': list_data[x], "icon": icons[x], "appliance": appliances[x],
                         "index": x + 1})
            s.close()
        except:
            result = []
            button = "disabled"
            htmlclass = "reddot"
            status = "Offline"
            data1 = bytes("Please check your TCP server/network",'utf-8')
        return render(request,"index.html",{'result':data1.decode("utf-8"),'sent':inp['message'][0],'htmlclass':htmlclass,'status':status, "button":button, "data":result })
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
            s.sendall(b'0')
            data = s.recv(1024)
            list_data = [x.decode("utf-8") for x in data.split()]
            result = []
            appliances = ["BULB","PUMP","INVERTER"]
            icons = ["fa fa-lightbulb","fa fa-plug","fa fa-calendar-alt"]
            for x in range(len(list_data)):
                if list_data[x] == "ON":
                    result.append({'colour':'yellow','status':list_data[x],"icon":icons[x],"appliance":appliances[x],"index":x+1})
                else:
                    result.append({'colour':'white','status': list_data[x],"icon":icons[x],"appliance":appliances[x],"index":x+1})
            s.close()
        except Exception as e:
            print(e)
            result = []
            button = "disabled"
            htmlclass = "reddot"
            status = "Offline"
        return render(request, "index.html", {'htmlclass':htmlclass,'status':status, "button":button, "data":result})