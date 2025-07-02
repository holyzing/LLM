* netsh interface portproxy add v4tov4 listenport=8118 listenaddress=172.25.144.1 connectport=8118 connectaddress=10.0.2.158
* netsh interface portproxy delete v4tov4 listenport=8118 listenaddress=
* netsh interface portproxy show all
* netsh interface portproxy reset
* netstat -ano | findstr "8118"
* pip install httpx[socks]
* 172.25.148.106:8080
* watch -n 3 nvidia-smi
* nvidia-smi -l 1
* nvidia-smi --query-gpu=utilization.gpu,utilization.memory --format=csv -l 1
