# log in with holberton user and open files without an error
exec { 'holb_user':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => 'sed -i -e "s/nofile 5/nofile 5000/g" /etc/security/limits.conf;
  sed -i -e "s/nofile 4/nofile 4000/g" /etc/security/limits.conf'
}
