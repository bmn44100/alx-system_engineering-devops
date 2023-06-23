# Using Puppet, create a manifest that kills a process named killmenow
exec { 'killp_menow':
  command  => 'pkill -f killmenow',
  provider => 'shell',
  path     => ['/usr/bin', '/usr/sbin',]
}
