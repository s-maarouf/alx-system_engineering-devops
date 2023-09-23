# Connects to a server using SSH

file { '~/.ssh/school':
  ensure  => present
  content => "Host *
              IdentityFile ~/.ssh/school
              PasswordAuthentication no"
}

