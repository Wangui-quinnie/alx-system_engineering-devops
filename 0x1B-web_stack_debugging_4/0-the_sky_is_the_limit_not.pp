# Increase the ULIMIT of the default file
file { '/etc/default/nginx':
  ensure  => present,
  content => "ULIMIT=4096\n",
}

# Restart Nginx when the configuration changes
service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/default/nginx'],
}
