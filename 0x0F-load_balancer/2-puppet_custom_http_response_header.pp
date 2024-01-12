# Installs Nginx and adds a custom HTTP header

# Ensure the system is updated before installing Nginx
exec { 'update':
  command => 'sudo apt-get -y update',
}

# Install Nginx package
package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

# Add custom HTTP header to Nginx configuration
file { '/etc/nginx/conf.d/custom_header.conf':
  content => "add_header X-Served-By '${hostname}';",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Restart Nginx service when configuration changes
service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/nginx/conf.d/custom_header.conf'],
}
