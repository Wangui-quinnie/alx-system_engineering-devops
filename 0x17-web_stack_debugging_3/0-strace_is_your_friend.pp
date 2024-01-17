# Fix "phpp" extension to "php" in wordpress setting.

exec { 'fix wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/ :/bin/'
}
