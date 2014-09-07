smtprouted
======

smtprouted is a performant (500+ messages/second) Python script which can
forward email to different endpoints based on regular expression matching.  
It also provides address rewriting functionality and message de-duplication
(i.e. it will only forward a message to the first MAIL TO: recipient that it
receives, regardless of how many addresses are on the recipient list).  This
script is particularly useful when acting as the frontend for a catchall/
mailsink mail server used when testing large email campaigns.

## Installation

This is a single file script, so clone the git repo to a directory of your
choosing...

```git clone https://github.com/eschwim/smtprouted.git```

...and then copy the 'smtprouted' binary to your /usr/sbin directory, and the
'extras/smtprouted.initd' script to your /etc/init.d directory (assuming
you are running a Redhat variant; other Linux distros will likely need to
tweak the init script to get it working).

There is also a .spec file included in the extras directory, in the event
that anyone would like to convert this into an RPM.

## Configuration

smtrouted will look for a config file at /etc/smtprouted.conf, by default
(although this path can be overridden by using the -c flag from the command
line).  The config file included in the smtprouted git repo specifies the 
default config values which will take affect if the respective config 
variable are missing from the config file, or smtprouted cannot read the 
config file (for whatever reason).

Some alternative configuration options:

*Rewrite the domain of all incoming recpients to 'testmail.com'*

    [global]
    # Rewrite expressions are regular expressions that should be in the 
    # format <match from>/<rewrite to>
    rewriteExpr=@.*/@testmail.com

*All incoming mail forwarded to the default route will be de-duplicated
(i.e. the message will only be forwarded to the first address specified 
by the RCPT TO: SMTP command; all others will be ignored. The To: MIME 
header will be maintained, however)*

    [global]
    dedupeMail=True

*Define a custom route by creating a new section (denoted by the name
of the route encased in square brackets).  The name of the route is 
purely for identification purposes and is inconsequential.  The
route below will match all addresses whose username or domain start 
with '_custom.'.  So both '_custom.bob@myserver.com' and
'bob@_custom.myserver.com' will match this route.  Messages will be
forwarded to port 25 on myserver.com, will be deduplicated, and will 
have the '_prefix.' portion of the recipient address removed.*

    [my-custom-route]
    toExpr=(^|@)_custom\.
    routeAddr=myserver.com
    routePort=25
    rewriteExpr=_prefix\./

## Debugging

smtprouted supports two command line flags, '-f' and '-d', which enable
running in the foreground (i.e. not daemonizing) and sending debug
output, respectively.
