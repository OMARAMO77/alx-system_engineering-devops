# login with the holberton user and open a file without any error message.
# Increase "hard nofile" and "soft nofile" limit for Holberton user
exec { 'Increase hard nofile limit':
  path    => '/bin/',
  command => 'sed -i "/holberton hard/s/5/4096/" /etc/security/limits.conf',
}

exec { 'Increase soft nofile limit':
  path    => '/bin/',
  command => 'sed -i "/holberton soft/s/4/1024/" /etc/security/limits.conf',
}
