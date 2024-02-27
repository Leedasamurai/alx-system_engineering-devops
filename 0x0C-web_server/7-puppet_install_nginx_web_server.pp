# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Create custom 404 page
file { '/usr/share/nginx/html/404.html':
  ensure  => present,
  content => "Ceci n'est pas une page\n",
  require => Package['nginx'],
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Enable redirection
nginx::resource::vhost { 'redirect_me':
  www_root     => '/usr/share/nginx/html',
  listen_port  => '80',
  server_name  => '_',
  ensure       => present,
  redirect_to  => 'https://twitter.com/Emmanue17280546',
  redirect_code => '301',
}
