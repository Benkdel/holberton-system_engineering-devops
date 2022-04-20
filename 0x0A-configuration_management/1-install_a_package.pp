# Install a package - Using Puppet, install flask.

exec { 'Flask Install':
    command => 'pip3 install Flask',
    provider => 'shell',
}

