# Installs and configures Nginx web server.

$doc_root = '/var/www/html'
$server_block = '/etc/nginx/sites-available'

package { 'nginx':
  ensure   => 'installed',
  provider => 'apt',
  before   => Exec['allow nginx']
}

exec {'apt-get update':
  command => '/usr/bin/apt-get update',
  before  => Package['nginx']
}

service { 'ufw':
  ensure => 'running',
  enable => 'true'
}

exec {'allow nginx':
  command => '/usr/bin/sudo ufw allow "Nginx HTTP"',
  require => Service['/usr/sbin/ufw'],
  before  => file['$doc_root/index.html']
}

file {'$doc_root/index.html':
  ensure  => 'present',
  content => 'Hello World!',
  notify  => Service['nginx'],
  require => Package['nginx']
}

file {'$doc_root/custom_404':
  ensure  => 'present',
  content => 'Ceci n\'est pas une page',
  notify  => Service['nginx'],
  require => Package['nginx']
}

file {'$server_block/default':
  backup  => 'true';
  notify  => Service['nginx'],
  require => Package['nginx']
}

file_line {'name': 
  line      => '',
  path      => 'absolute path to the file',
  #after    => undef,
  #ensure   => 'present',
  #match    => undef, # /.*match/
  #multiple => undef, # 'true' or 'false'
  #name     => undef,
  #replace  => true, # 'true' or 'false'
}
