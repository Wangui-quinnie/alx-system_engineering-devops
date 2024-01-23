# Set file descriptor limits for holberton user
file { '/etc/security/limits.conf':
  ensure  => present,
  content => "holberton hard nofile 4096\nholberton soft nofile 4096\n",
}
