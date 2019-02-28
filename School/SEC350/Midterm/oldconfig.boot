firewall {
    all-ping enable
    broadcast-ping disable
    config-trap disable
    ipv6-receive-redirects disable
    ipv6-src-route disable
    ip-src-route disable
    log-martians enable
    name DMZ-LAN {
        default-action drop
        enable-default-log
        rule 1 {
            action accept
            state {
                established enable
            }
        }
        rule 10 {
            action accept
            destination {
                address 172.16.200.10
                port 514
            }
            protocol udp
        }
        rule 15 {
            action accept
            description DNS
            destination {
                address 172.16.200.11
                port 53
            }
            protocol tcp_udp
        }
    }
    name DMZ-WAN {
        default-action drop
        enable-default-log
        rule 1 {
            action accept
            state {
                established enable
            }
        }
        rule 15 {
            action accept
            description "proxy outbound"
            protocol tcp
            source {
                address 172.16.50.4
            }
        }
        rule 20 {
            action accept
            description NTP
            destination {
                port 123
            }
            protocol udp
        }
    }
    name LAN-DMZ {
        default-action drop
        enable-default-log
        rule 10 {
            action accept
            description "LAN to Proxy"
            destination {
                address 172.16.50.4
                port 3128
            }
            protocol tcp
        }
        rule 11 {
            action accept
            description "DNS back"
            protocol udp
            source {
                port 53
            }
        }
        rule 15 {
            action accept
            description SSH
            destination {
                address 172.16.50.0/29
                port 22
            }
            protocol tcp
        }
    }
    name LAN-WAN {
        default-action drop
        enable-default-log
    }
    name WAN-DMZ {
        default-action drop
        enable-default-log
        rule 10 {
            action accept
            description "Allow WAN access to Web01 HTTP"
            destination {
                address 172.16.50.3
                port 80
            }
            protocol tcp
        }
        rule 15 {
            action accept
            state {
                established enable
            }
        }
    }
    name WAN-LAN {
        default-action drop
        enable-default-log
        rule 1 {
            action accept
        }
    }
    receive-redirects disable
    send-redirects enable
    source-validation disable
    syn-cookies enable
    twa-hazards-protection disable
}
interfaces {
    ethernet eth0 {
        address 10.0.17.125/24
        description SEC350-WAN
        duplex auto
        hw-id 00:50:56:a1:0c:8c
        smp_affinity auto
        speed auto
    }
    ethernet eth1 {
        address 172.16.50.2/29
        description Jake-DMZ
        duplex auto
        hw-id 00:50:56:a1:6c:5e
        smp_affinity auto
        speed auto
    }
    ethernet eth2 {
        address 172.16.150.2/24
        description Jake-LAN
        duplex auto
        hw-id 00:50:56:a1:82:7e
        smp_affinity auto
        speed auto
    }
    loopback lo {
    }
}
nat {
    destination {
        rule 10 {
            description "Web 01 HTTP"
            destination {
                port 80
            }
            inbound-interface eth0
            protocol tcp
            translation {
                address 172.16.50.3
            }
        }
    }
    source {
        rule 10 {
            description "NAT FROM DMZ to WAN"
            outbound-interface eth0
            source {
                address 172.16.50.0/29
            }
            translation {
                address masquerade
            }
        }
        rule 15 {
            description "NAT FROM LAN to WAN"
            outbound-interface eth0
            source {
                address 172.16.150.0/24
            }
            translation {
                address masquerade
            }
        }
    }
}
protocols {
    static {
        route 172.16.200.0/28 {
            next-hop 172.16.150.3 {
            }
        }
    }
}
service {
    dns {
        forwarding {
            cache-size 150
            domain sec350.local {
                server 172.16.200.11
            }
            listen-on eth1
            listen-on eth2
        }
    }
    ssh {
        listen-address 10.0.17.125
        port 22
    }
}
system {
    config-management {
        commit-revisions 100
    }
    console {
    }
    gateway-address 10.0.17.2
    host-name fw1-jake
    login {
        user vyos {
            authentication {
                encrypted-password $6$2wD9S5Df$BTrutaChW9wInqMsH8rLR6BKuzZHly9qKzEz0sfm/QuEmmogKiSUlFfyTM5OFyoNa9PyuH1M3a8Vo9zZg8lgN1
                plaintext-password ""
            }
            level admin
        }
    }
    name-server 10.0.17.2
    ntp {
        server 0.pool.ntp.org {
        }
        server 1.pool.ntp.org {
        }
        server 2.pool.ntp.org {
        }
    }
    package {
        auto-sync 1
        repository community {
            components main
            distribution helium
            password ""
            url http://packages.vyos.net/vyos
            username ""
        }
    }
    syslog {
        global {
            facility all {
                level notice
            }
            facility protocols {
                level debug
            }
        }
        host 172.16.200.10 {
            facility authpriv {
                level info
            }
            facility kern {
                level debug
            }
        }
    }
    time-zone UTC
}
zone-policy {
    zone DMZ {
        default-action drop
        from LAN {
            firewall {
                name LAN-DMZ
            }
        }
        from WAN {
            firewall {
                name WAN-DMZ
            }
        }
        interface eth1
    }
    zone LAN {
        default-action drop
        from DMZ {
            firewall {
                name DMZ-LAN
            }
        }
        from WAN {
            firewall {
                name WAN-LAN
            }
        }
        interface eth2
    }
    zone WAN {
        default-action drop
        from DMZ {
            firewall {
                name DMZ-WAN
            }
        }
        from LAN {
            firewall {
                name LAN-WAN
            }
        }
        interface eth0
    }
}


/* Warning: Do not remove the following line. */
/* === vyatta-config-version: "cluster@1:config-management@1:conntrack-sync@1:conntrack@1:cron@1:dhcp-relay@1:dhcp-server@4:firewall@5:ipsec@4:nat@4:qos@1:quagga@2:system@6:vrrp@1:wanloadbalance@3:webgui@1:webproxy@1:zone-policy@1" === */
/* Release version: VyOS 1.1.8 */
