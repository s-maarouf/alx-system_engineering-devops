# Kills a process using pkill

  exec { 'kill process':
    command  => 'pkill killmenow',
    provider => 'shell',
}
