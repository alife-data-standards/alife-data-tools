# Recommended Good Practices for Maintaining Software Tools

We advocate the use of a number of software development best practices.
All repositories maintained by the Artificial Life Data Standards Organization use continuous integration to ensure that all code is automatically tested when a change is made.
Test coverage is measured to ensure that these test suites are comprehensive.
Lastly, static analysis is automatically performed to identify error-prone code.

## Continuous Integration

From [Travis-CI's docs](https://docs.travis-ci.com/user/for-beginners/):
> Continuous Integration is the practice of merging in small code changes frequently - rather than merging in a large change at the end of a development cycle. The goal is to build healthier software by developing and testing in smaller increments.

In all of the Artificial Life Data Standards Organization repositories we use Travis CI (a continuous integration platform) to automatically build and test code changes.
On each of our code-based repositories, we report whether or not the current build of our 'master' branch passes testing or not.

Getting started with Travis CI is quick and easy, as it integrates with GitHub. Find a Travis CI tutorial [here](https://docs.travis-ci.com/user/tutorial/).

## Code Coverage and Static Analysis

Reporting whether or not a code base passes a set of tests is great, but if our tests don't adequately _test_ our code base, we can't put much confidence in whether or not our build passes!
To help us ensure that we are adequately testing our code base, we have setup code coverage tracking via [Codacy](codacy.com).
We also have static code analysis (via Codacy) to identify error-prone/problematic/bad-style code.

A Codacy getting started guide can be found [here](https://support.codacy.com/hc/en-us/categories/360001313954-Getting-Started).

For Python projects, we use [pytest](https://docs.pytest.org/en/latest/) for testing.
