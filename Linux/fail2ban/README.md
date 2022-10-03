## Fail2Ban + Nginx
##### [Blog Post](https://blog.cyberjake.xyz/Fail2Ban-CloudFlare) to learn more

### How to use
1. Copy the filter file to /etc/fail2ban/filter.d/
2. Create a jail in jail.d  
   Should look like:  

        [nginx-blocked]
        enabled = true
        port = http.https
        filter = nginx-blocked
        logpath = /var/log/nginx/errorlog
              <include other error log paths you want to monitor. Seperate by line>
        maxretry = 1

3. Check the configeration is vaild
   - ```sudo fail2ban-client -t. ```  
4. If the check passes then reload
   - ```sudo systemctl reload fail2ban.service```
5. See the new jail
   - ```sudo fail2ban-client status nginx-blocked```  

Once IPs start connecting, they will appear in the jail.
