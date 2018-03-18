Description
===========

This project provides a website that can be queried by a PGP signed base64 string which
contains information about work done for a client. This allows a client to cryptographically
prove that iosiro has conducted security work for them. Most often, this gives
assurance to customers that the customer takes security seriously, and customers
will thank them for it.

Query String
===========

The query string is a base64'd JSON object. The object contains the following
fields:

- Client Name (The name of the Client or Customer)
- Date of work done
- Nature of work done (Smart contract audit, penetration test)
- Description (Further information about the scope, duration and links to relevant artifacts about the test.)

```
{
  "client_name" : "Name",
  "date_signed" : "2018-03-16 14:49:05.624434",
  "nature_of_work" : "Smart Contract Audit"
  "description" : "A standard smart contract audit conducted against the smart contracts available on https://github.com/iosiro/contracts/ with commit hash 38aef92"

}

```
