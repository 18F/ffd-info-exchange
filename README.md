# ffd-info-exchange

## About this project

Welcome to the ffd-info-exchange repository! The Federal Front Door: Information Exchange project is a twelve-week discovery engagement (ending 12/23/16) meant to uncover possibilities for information sharing between federal agencies as a way of providing better public access to government services. 

Our work is divided into three broad categories: research, prototyping (and testing), and synthesis. During the research phase, we familiarized ourselves with applicable legislation — namely, the Privacy Act of 1974 and the Computer Matching and Privacy Protection Act of 1988 — and determined how these laws apply to our work. We also identified current examples of information-sharing between agencies, conducted user interviews, and researched best practices for communicating privacy- and security-related concepts.

During the second phase, we’ll build a series of prototypes representing the interfaces users will encounter as they’re being asked to authorize information sharing between agencies from which they hope to acquire services. Using feedback from our prototype-test participants, we’ll refine our designs and modify our initial hypotheses to reflect our users’ preferences, feelings, and insights.

Finally, we’ll synthesize our findings and outline potential next steps in a research report.

## Resources

Throughout the project, we’ll post research findings, observations, and more in our [wiki](https://github.com/18F/ffd-info-exchange/wiki); check back often to learn more about our latest work. If you’re interested in contributing to the project, please visit [CONTRIBUTING](https://github.com/18F/ffd-info-exchange/blob/master/CONTRIBUTING.md) for more information on [18F’s Code of Conduct](https://github.com/18F/code-of-conduct/blob/master/code-of-conduct.md) and [open source policy](https://github.com/18f/open-source-policy).

## Team practices

See our [team practices document](/docs/team-practices.md) for additional information.

## Local installation

This app is designed to run on Python 3.4+. You'll also need to have [PostgreSQL](https://www.postgresql.org) running.

If you don't already have PostgreSQL installed and are running MacOS/OS X, you can install it using [Homebrew](http://brew.sh/):

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
3. To run functional tests, run the following command:
```
python functional_tests.py
```

4. To run unit tests, run the following command:
```
python manage.py test
```

## Contributing

See [CONTRIBUTING](CONTRIBUTING.md) for additional information.

## Public domain

This project is in the worldwide [public domain](LICENSE.md). As stated in [CONTRIBUTING](CONTRIBUTING.md):

> This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
>
> All contributions to this project will be released under the CC0 dedication. By submitting a pull request, you are agreeing to comply with this waiver of copyright interest.
