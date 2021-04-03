# pkill a process called killmenow

exec { 'pkill':
    command => 'pkill -f killmenow',
    path    => '/usr/bin'
}
