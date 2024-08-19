# Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at <https://github.com/jorenham/exports/issues>.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything unassigned tagged
with "enhancement" is open to whoever wants to implement it.

### Submit Feedback

The best way to send feedback is to file an issue at
<https://github.com/jorenham/exports/issues>.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

## Get Started

Ready to contribute? Here's how to set up `exports` for local development.

1. Fork the `exports` repo on GitHub.
2. Clone your fork locally:
   ```bash
    git clone git@github.com:jorenham/exports.git
    ```

3. Install your local copy using [poetry](https://python-poetry.org/).
   Assuming you have [poetry installed](https://python-poetry.org/docs/#installation),
   this is how you set up your fork for local development:
    ```bash
    poetry install
    ```

4. Install pre-commit:

    ```bash
    poetry run pre-commit install
    ```

## Pull Request Guidelines

Before you submit a [pull request](https://github.com/jorenham/exports/pulls), check
that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in `README.md`.
