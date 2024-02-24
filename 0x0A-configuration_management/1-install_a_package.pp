# 1-install_a_package.pp

exec { 'install_flask':
  command => '/usr/bin/apt-get -y install flask= -v 2.1.0',
}

