$server_block = '/etc/nginx/sites-available'
$another_string = '\n\terror_page 404 /custom_404;\n\tlocation = /custom_404 {\n\t\troot /var/www/html;\n\t\tinternal;\n\t}'
$new_string = "server_name _;\n\trewrite ^/redirect_me https://pinterest.com permanent;${another_string}"

file {'default':
  ensure => 'present',
  path   => "${server_block}/default"
}

exec {'sed':
  command => '/usr/bin/sed -i "s%server_name _;%server_name _;\n\trewrite ^/redirect_me https://pinterest.com permanent;\n\terror_page 404 /custom_404;\n\tlocation = /custom_404 {\n\t\troot /var/www/html;\n\t\tinternal;\n\t}%" /etc/nginx/sites-available/default',
  require => File['default']
}
