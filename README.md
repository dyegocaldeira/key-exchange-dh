# key-exchange-dh
Algorithm created to exemplify the exchange of keys using the Diffie Hellman algorithm.

Requirements:

`Ubuntu`

`Python 2.7`

`simple-crypt`

### Rules
- Randomly choose two public keys that should / can be shared between clients
- Both randomly choose the private key
- Both exchange their partial keys
- Final key will be the same for both

### How to use

```bash
$ git clone https://github.com/dyegocaldeira/key-exchange-dh.git
$ cd key-exchange-dh
$ python -m pip install -r requirements.txt
$ python runDH.py
```
