# Connects to a server using SSH

file { '~/.ssh/school':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  content => "Host *\n    IdentityFile ~/.ssh/school\n    PasswordAuthentication no\n",
}

