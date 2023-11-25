# Makes changes to our client SSH configuration file.

command {'edit config':
  command => 'echo -e "PasswordAuthentication no\nIdentityFile ~/.ssh/school">> /etc/ssh/ssh_config'
}
