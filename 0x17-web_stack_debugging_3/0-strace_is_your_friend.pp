# fix Apache server
exec { 'fix_apache':
  path     => '/usr/bin:/usr/sbin:/bin',
  provider => 'shell',
  command  => 'sed -i -e "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php'
}
