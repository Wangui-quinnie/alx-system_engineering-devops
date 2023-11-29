# Changes our configuration file with puppet
file { '/etc/ssh/ssh_config':
  ensure  => file,
  mode    => '0600',
  content => "
    Host 18.209.179.13
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
