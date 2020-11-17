# random_password

Simple CLI tool the generate password.

It could be used to set environment variables.

``export LEN=30``

``export PASS=`python random_pass.py -l $LEN` ``

The argument ``-l`` is the password lenght, by default length = `30`

You can save password into file
`` python random_pass.py -l $LEN >> mypass.txt ``


The tools contains list of checks for each step if generated password satisfy criterias:
- maximum number of entrence for each symbol in the whole password
- symbols should not repeat in sequence.
