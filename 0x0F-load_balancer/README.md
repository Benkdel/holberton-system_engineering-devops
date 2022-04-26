*** Load Balancer ***


frontend MyFrontend
tbind *:80
tmode http
tdefault_backend MyServers_01

backend MyServers_01
tbalance roundrobin
tserver 3669-web-01 35.185.21.233:80 check
tserver 3669-web-02 35.172.200.220:80 check" >> /etc/haproxy/haproxy.cfg