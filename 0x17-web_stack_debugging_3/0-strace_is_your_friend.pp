# Debbugging Apache returning 500 error.

service { 'apache2':
  ensure => running
}

exec { 'mv /var/www/html/wp-includes/class-wp-locale.php':
  command => '/bin/mv /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp',
  notify  => Service['apache2']
}
