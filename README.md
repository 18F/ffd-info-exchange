# ffd-info-exchange

## Team practices

See our [team practices document](/docs/team-practices.md) for additional information.

## Local installation

This app is designed to run on Python 3.4+. You'll also need to have [PostgreSQL](https://www.postgresql.org) running.

If you don't already have PostgreSQL installed and are running MacOS/OS X you can install it using [Homebrew](http://brew.sh/):

```
brew update
brew install postgres
```

Follow the post-installation instructions for postgres. If you didn't see them, run `brew info postgres`. Lastly, make a default `postgres` user:

```
createuser -sdl postgres
```

If you're running an operating system other than MacOS, follow installation instructions on the [PostgreSQL website](https://www.postgresql.org).

`pyvenv` can manage the dependencies installed with `pip`. With that, you can prepare your development environment by running:

```
git clone https://github.com/18F/ffd-info-exchange.git
cd ffd-info-exchange
pyvenv ffd-env
source ffd-env/bin/activate
pip install -r requirements.txt
createdb ffd-info-exchange
cd ffd_info_exchange
python manage.py migrate
python manage.py runserver
```

The app should now be running at http://localhost:8000.

## Testing

To manually run the test suite:

1. Open a new tab or window in your command line terminal.
2. Navigate to the `ffd_info_exchange` directory specified above.
3. Run the following command:

```
python fafsa/functional_tests.py
```

## Contributing

See [CONTRIBUTING](CONTRIBUTING.md) for additional information.

## Public domain

This project is in the worldwide [public domain](LICENSE.md). As stated in [CONTRIBUTING](CONTRIBUTING.md):

> This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
>
> All contributions to this project will be released under the CC0 dedication. By submitting a pull request, you are agreeing to comply with this waiver of copyright interest.
