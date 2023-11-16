# Increase the amount of traffic "ULIMIT" an Nginx server can handle
exec { 'upgrade-ULIMIT':
  path    => '/bin/',
  command => 'sed -i "/ULIMIT/s/15/4096/" /etc/default/nginx',
}

exec { 'restart-nginx':
  path    => '/bin/',
  command => 'service nginx restart',
}
