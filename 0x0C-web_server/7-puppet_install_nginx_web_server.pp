#!/usr/bin/env bash
# Install Nginx package
package { 'nginx':
  ensure => installed,
}
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
                listen 80 default_server;
                listen [::]:80 default_server;

                root /var/www/html;
                index index.html;

                location / {
                    return 200 'Hello World!';
                }

                location /redirect_me {
                    return 301 /;
                }
            }",
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
