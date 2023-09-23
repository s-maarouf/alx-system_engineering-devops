# Connects to a server using SSH

file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  content => "Host *\n    IdentityFile ~/.ssh/school\n    PasswordAuthentication no\n",
}

