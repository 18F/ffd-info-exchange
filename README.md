# ffd-info-exchange

## Team practices

See our [team practices document](/docs/team-practices.md) for additional information.

## Local installation

This app is designed to run on Python 3.4+. `pyvenv` can manage the dependencies installed with `pip`. With that, you can prepare your development environment by running:

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

## Contributing

See [CONTRIBUTING](CONTRIBUTING.md) for additional information.

## Public domain

This project is in the worldwide [public domain](LICENSE.md). As stated in [CONTRIBUTING](CONTRIBUTING.md):

> This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
>
> All contributions to this project will be released under the CC0 dedication. By submitting a pull request, you are agreeing to comply with this waiver of copyright interest.
