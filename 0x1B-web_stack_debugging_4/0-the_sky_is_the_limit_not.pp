# testing how well our web server setup featuring Nginx is doing
exec { 'http_requests':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => 'sed -i -e "s/15/4096/g" /etc/default/nginx; service nginx restart'
}
