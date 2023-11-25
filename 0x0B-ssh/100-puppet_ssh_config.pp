# Makes changes to our client SSH configuration file.

exec {'edit config':
  command => 'echo -e "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config'
}
