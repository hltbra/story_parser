Story Parser
============

This project is a start towards writing text stories to pyhistorian, but it can be used out of it.
It parsers a string file like::

    Story: Writing a parser
    As a pyhistorian contributor
    I want to add support to stories written in text
    So that everyone can use it, even the stakeholders

    Scenario 1: Getting Title
      Given I have a story like this one
      When I try parse it and get the title
      Then I get "Writing a parser" title

Installing
==========
``$ python setup.py install``

Or you can run ``make`` in a UNIX box and it installs story_parser and run all it's tests
