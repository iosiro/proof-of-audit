Description
===========

A website that verifies a PGP signed base64 string
containing information about work done for a company. This allows a company to cryptographically
prove that iosiro has conducted security work for them. Most often, this gives
assurance to the company's customers that the company takes security seriously, and customers
will thank them for it.

Query String
------------

The query string is a base64 encoded, PGP signed JSON string. The string contains the following
fields:

- Client Name - The name of the company
- Date Signed - Date of work done
- Nature of work done - e.g. Smart contract audit, penetration test, etc.
- Description - Further information about the scope, duration and links to relevant artifacts about the test.

```
{
  "client_name" : "Name",
  "date_signed" : "2018-03-16 14:49:05.624434",
  "nature_of_work" : "Smart Contract Audit"
  "description" : "A standard smart contract audit conducted against the smart contracts available on https://github.com/iosiro/ico/contracts/ with commit hash 38aef92"

}
```

Signing Tool
------------

Signing tool is an interactive tool that creates the message that is signed by our PGP key. Simply run:

```
python3 signing_tool.py
```

Settings
------------

A number of settings are available to customise in settings.py.

- dns

Dependencies
------------
