# ffd-info-exchange

## About this project

Welcome to the ffd-info-exchange repository! The Federal Front Door: Information Exchange project was a three-month discovery engagement (ending 12/31/16) meant to uncover possibilities for information sharing between federal agencies as a way of providing better public access to government services. 

Our work was divided into three broad categories: research, prototyping (and testing), and synthesis. During the research phase, we familiarized ourselves with applicable legislation — namely, the Privacy Act of 1974 and the Computer Matching and Privacy Protection Act of 1988 — and determined how these laws apply to our work. We also identified current examples of information-sharing between agencies, conducted user interviews, and researched best practices for communicating privacy- and security-related concepts.

During the second phase, we built a series of prototypes representing the interfaces users could encounter as they’re being asked to authorize information sharing between agencies from which they hope to acquire services. Using feedback from our prototype-test participants, we refined our designs and modified our initial hypotheses to reflect our users’ preferences, feelings, and insights.

Finally, we synthesized our findings and outlined potential next steps in a research report. (Link to come.)

Please note: as this was a discovery sprint with simulated use cases, the prototypes were tailored to our two rounds of user research. In order to protect personally identifiable information that users might have shared during testing, they intentionally don't save any data. They don't include many of the capabilities and standards that we would implement for production software. They're explicitly not meant for any sort of production use.

## Resources

Throughout the project, we posted research findings, observations, and more in our [wiki](https://github.com/18F/ffd-info-exchange/wiki). The project isn't currently under active development, but if you’re interested in contributing, please visit [CONTRIBUTING](https://github.com/18F/ffd-info-exchange/blob/master/CONTRIBUTING.md) for more information on [18F’s Code of Conduct](https://github.com/18F/code-of-conduct/blob/master/code-of-conduct.md) and [open source policy](https://github.com/18f/open-source-policy).

## Team practices

See our [team practices document](/docs/team-practices.md) for additional information.

## Local installation

The prototypes are designed to run on Python 3.4+. You'll also need to have [PostgreSQL](https://www.postgresql.org) running.

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

The apps should now be running at http://localhost:8000/fafsa and http://localhost:8000/uscis, respectively.

## Testing

These prototypes were built for discovery and user testing with simulated use cases, not for production. Accordingly, though we started with test-driven development, we intentionally prioritized rapid iteration and deprioritized tests.

To manually run the tests that do exist:

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
