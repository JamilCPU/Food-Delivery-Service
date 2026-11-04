# Food Delivery Service

An early object-oriented sketch of a grocery/food delivery backend in Python. It defines the core domain classes (users, accounts, authentication, stores, orders and drivers) with getters/setters and stubbed-out methods for the workflows that were planned. It was a design exercise and is a work in progress: most behaviour is placeholder `print("implement ...")` stubs.

## Stack

- Python 3 (standard library only, no dependencies)

## Running

```bash
python main.py
```

`main.py` is a small demo that creates a `User` with made-up data and exercises its getters and setters.

## Project layout

- `User.py` - user profile (username, name, phone, email) with accessors
- `Account.py` - account wrapper with stubs for tipping, order history, placing orders and store selection
- `Authentication.py` - credential-check and token-generation outline
- `Store.py`, `Order.py`, `Driver.py` - store, order and delivery-driver models
- `main.py` - demo script

## Status

Work in progress and not runnable beyond the demo. Several classes still have incomplete constructors and stub methods; there is no persistence, networking or real authentication. Passwords in the demo are placeholder strings, not a security design.
