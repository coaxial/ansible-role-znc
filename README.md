znc
=========
  [![Build Status](https://travis-ci.org/coaxial/ansible-role-znc.svg?branch=master)](https://travis-ci.org/coaxial/ansible-role-znc)

Install and configure [ZNC](https://znc.in), an advanced IRC bouncer.

Role Variables
--------------

Name | Default | Possible values | Description
---|---|---|---
`znc__port` | `1888` | Any port above 1024 | Which port will ZNC be running on
`znc__ipv4` | `0.0.0.0` | Any valid IPv4 | Which IPv4 will ZNC listen on
`znc__ipv6` | `::/0` | Any valid IPv6 | Which IPv6 will ZNC listen on
`znc__admin_username` | unset, required | Any valid IRC nick | Used to log in to the webadmin interface
`znc__admin_password` | unset, required | Any string, will be hashed to SHA256 in the config file, **use an Ansible encrypted variable to store your plaintext password** | Used to log in to the webadmin interface
`znc__admin_nick` | `znc__admin_username` | Any valid IRC nick | Will be that user's nick on the IRC networks
`znc__admin_alt_nick` | `znc__admin_username`_ | Any valid IRC nick | Alternative nick if it's not available on the IRC networks
`znc__admin_ident` | `znc__admin_username` | Any valid [ident](https://wiki.swiftirc.net/wiki/Idents) string | What to answer [ident](https://wiki.swiftirc.net/wiki/Idents) requests with
`znc__admin_realname` | unset, mandatory | Any string | What to show as the Real Name on IRC
`znc__admin_salt` | unset, mandatory | A random 20 chars string | What to salt the password with, `pwgen -sy 20` generates such a string from the command line

Adding more users
-----------------

To add more users beyond the admin user, either use a `blockinfile` in a playbook, or do it as the admin user through the webadmin/by issuing commands over IRC.

There are too many specifics for configuring users, it would be convoluted and cumbersome to handle that in this role in my opinion.

Example Playbook
----------------

```yaml
- hosts: all
  vars:
    znc__admin_username: admin
    znc__admin_password: mypassword
    znc__admin_salt: "}T-GmTGu/ck`2B6Pu$g["
    znc__admin_nick: l33t
    znc__admin_realname: h4x0r
  roles:
    - znc
```

License
-------

MIT

Author Information
------------------

Coaxial ([64b.it](https://64b.it))
