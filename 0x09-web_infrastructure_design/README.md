DevOps - SysAdmin - web infrastructure
	Learning objectives
At the end of this project we are expected we are expected to be able to;
Draw a diagram covering the web stack you built with the sysadmin/devops track projects
Explain what each component is doing
Explain system redundancy
Know all the mentioned acronyms: LAMP, SPOF, QPS
1. System Redundancy: refers to the duplication of critical components or systems within a larger system or infrastructure. The purpose of redundancy is to provide backup or failover capability in case of component or system failures. By having redundant components or systems, the overall system can continue to operate even if one or more components fail. Redundancy can be achieved through various techniques, such as using redundant hardware, software, network paths, or data storage.

2. LAMP: is an acronym that stands for Linux, Apache, MySQL, and PHP/Perl/Python. It is a popular open-source software stack used for developing and running dynamic websites and web applications. Linux is the operating system, Apache is the web server software, MySQL is the relational database management system, and PHP/Perl/Python is the scripting/programming language used for web development. The LAMP stack is widely used due to its flexibility, stability, and ease of use.

3. SPOF: stands for Single Point of Failure. It refers to a component or system that, if it fails, would cause the entire system or infrastructure to fail. SPOFs present a significant risk as they represent a potential single point of failure that can disrupt operations or services. To mitigate the risk of SPOFs, redundancy and fault-tolerant measures are implemented to ensure there are backup systems or components in place, minimizing the impact of a single failure.

4. QPS: stands for Queries Per Second. It is a measure of the number of queries or requests that a system, such as a database or an application server, can handle within a second. QPS is often used to benchmark and evaluate the performance and capacity of systems, especially those handling high traffic or critical applications. It helps determine the system's ability to handle a specific workload and can be used to identify potential bottlenecks or performance limitations.
To help achieve this objectives are some tasks:
	
	TASKS
0. Simple web stack
mandatory
A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a LAMP stack.

On a whiteboard, design a one server web infrastructure that hosts the website that is reachable via www.foobar.com. Start your explanation by having a user wanting to access your website.

Requirements:

You must use:
1 server
1 web server (Nginx)
1 application server
1 application files (your code base)
1 database (MySQL)
1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8
You must be able to explain some specifics about this infrastructure:
What is a server
What is the role of the domain name
What type of DNS record www is in www.foobar.com
What is the role of the web server
What is the role of the application server
What is the role of the database
What is the server using to communicate with the computer of the user requesting the website
You must be able to explain what the issues are with this infrastructure:
SPOF
Downtime when maintenance needed (like deploying new code web server needs to be restarted)
Cannot scale if too much incoming traffic


1. Distributed web infrastructure
mandatory
On a whiteboard, design a three server web infrastructure that hosts the website www.foobar.com.

Requirements:

You must add:
2 servers
1 web server (Nginx)
1 application server
1 load-balancer (HAproxy)
1 set of application files (your code base)
1 database (MySQL)
You must be able to explain some specifics about this infrastructure:
For every additional element, why you are adding it
What distribution algorithm your load balancer is configured with and how it works
Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
How a database Primary-Replica (Master-Slave) cluster works
What is the difference between the Primary node and the Replica node in regard to the application
You must be able to explain what the issues are with this infrastructure:
Where are SPOF
Security issues (no firewall, no HTTPS)
No monitoring


2. Secured and monitored web infrastructure
mandatory
On a whiteboard, design a three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.

Requirements:

You must add:
3 firewalls
1 SSL certificate to serve www.foobar.com over HTTPS
3 monitoring clients (data collector for Sumologic or other monitoring services)
You must be able to explain some specifics about this infrastructure:
For every additional element, why you are adding it
What are firewalls for
Why is the traffic served over HTTPS
What monitoring is used for
How the monitoring tool is collecting data
Explain what to do if you want to monitor your web server QPS
You must be able to explain what the issues are with this infrastructure:
Why terminating SSL at the load balancer level is an issue
Why having only one MySQL server capable of accepting writes is an issue
Why having servers with all the same components (database, web server and application server) might be a problem

3. Scale up
#advanced
Readme

Application server vs web server
Requirements:

You must add:
1 server
1 load-balancer (HAproxy) configured as cluster with the other one
Split components (web server, application server, database) with their own server
You must be able to explain some specifics about this infrastructure:
For every additional element, why you are adding it

