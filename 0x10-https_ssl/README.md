DevOps SysAdmin Security

1. Main Roles of HTTPS SSL:
Authentication: SSL establishes a secure connection between a user's web browser and the server. It verifies the identity of the server, ensuring that the user is connecting to the intended website.
Encryption: SSL encrypts the data transmitted between the user's browser and the server, preventing unauthorized parties from intercepting and understanding the information.
2. Purpose of Encrypting Traffic:

Confidentiality: Encrypting traffic ensures that the data exchanged between a user and a server remains confidential. Even if someone intercepts the communication, they won't be able to decipher the encrypted information without the proper decryption key.

Integrity: Encryption helps maintain the integrity of the data during transmission. It ensures that the information received is exactly the same as what was sent, without any unauthorized alterations.

Authentication: Encryption plays a role in authentication by ensuring that the server's identity can be verified. This prevents attackers from impersonating the server and tricking users into providing sensitive information to malicious entities.

Trust: Encryption builds trust between users and websites. Knowing that their data is protected during transmission, users are more likely to trust a website with sensitive information such as login credentials or payment details.

3. SSL Termination:

Definition: SSL termination refers to the process of decrypting encrypted traffic at a certain point within the network infrastructure, allowing the content to be processed in an unencrypted form.

In Detail: When SSL termination occurs, the encrypted data is decrypted at a load balancer, reverse proxy, or a similar device. After decryption, the data is forwarded to the backend servers in an unencrypted form. This is often done to offload the resource-intensive task of encryption from the backend servers, improving overall performance.

Advantages:

Reduces the computational load on backend servers.
Simplifies the management of SSL certificates, as they are typically handled at the termination point.
Allows for the inspection of unencrypted traffic for security purposes.
In summary, HTTPS and SSL play critical roles in securing online communication by providing authentication, encryption, and data integrity. Encrypting traffic ensures the confidentiality and integrity of data, and SSL termination involves decrypting encrypted traffic at a specific point in the network for various advantages.

	TASKS

0. World wide web
Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

Requirements:

Add the subdomain www to your domain, point it to your lb-01 IP (your domain name might be configured with default subdomains, feel free to remove them)
Add the subdomain lb-01 to your domain, point it to your lb-01 IP
Add the subdomain web-01 to your domain, point it to your web-01 IP
Add the subdomain web-02 to your domain, point it to your web-02 IP
Your Bash script must accept 2 arguments:
domain:
type: string
what: domain name to audit
mandatory: yes
subdomain:
type: string
what: specific subdomain to audit
mandatory: no
Output: The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]
When only the parameter domain is provided, display information for its subdomains www, lb-01, web-01 and web-02 - in this specific order
When passing domain and subdomain parameters, display information for the specified subdomain
Ignore shellcheck case SC2086
Must use:
awk
at least one Bash function
You do not need to handle edge cases such as:
Empty parameters
Nonexistent domain names
Nonexistent subdomains


1. HAproxy SSL termination
“Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.

Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www..

Requirements:

HAproxy must be listening on port TCP 443
HAproxy must be accepting SSL traffic
HAproxy must serve encrypted traffic that will return the / of your web server
When querying the root of your domain name, the page returned must contain Holberton School
Share your HAproxy config as an answer file (/etc/haproxy/haproxy.cfg)
The file 1-haproxy_ssl_termination must be your HAproxy configuration file

Make sure to install HAproxy 1.5 or higher, SSL termination is not available before v1.5.


2. No loophole in your website traffic
A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS.

Requirements:

This should be transparent to the user
HAproxy should return a 301
HAproxy should redirect HTTP traffic to HTTPS
Share your HAproxy config as an answer file (/etc/haproxy/haproxy.cfg)
The file 100-redirect_http_to_https must be your HAproxy configuration file






