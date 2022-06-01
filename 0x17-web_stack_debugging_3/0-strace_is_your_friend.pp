# fix 500 error
exec { 'typo':
  command => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
  path    => '/usr/bin:/bin',
}
