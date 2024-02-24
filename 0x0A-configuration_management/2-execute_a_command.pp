# 2-execute_a_command.pp

exec { 'killmenow':
  command     => '/usr/bin/pkill -f killmenow',
  refreshonly => true,
}
