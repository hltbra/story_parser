from story_parser import parse_story,\
                         InvalidHeaderException
from should_dsl import should_be
import unittest


class StoryParserWithValidStorysHeaders(unittest.TestCase):
    def test_story_title_should_be_Title1(self):
        story_parsed = parse_story("""Story: Title1
        As a <role>
        I want to <feature>
        So that <businness value>""")
        story_parsed.get_story_title() |should_be.equal_to| 'Title1'

    def test_story_role_should_be_business_analyst(self):
        story_parsed = parse_story("""
        Story: <Title>
        As a businness analyst
        I want to <feature>
        So that <businness value>""")
        story_parsed.get_story_role() |should_be.equal_to| 'businness analyst'

    def test_story_feature_should_be_be_rich(self):
        story_parsed = parse_story("""
        Story: <Title>
        As a <role>
        I want to be rich
        So that <businness value>""")
        story_parsed.get_story_feature() |should_be.equal_to| 'be rich'

    def test_story_businness_value_should_be_i_rest_in_peace(self):
        story_parsed = parse_story("""
        Story: <Title>
        As a <role>
        I want to <feature>
        So that I rest in peace""")
        story_parsed.get_story_businness_value() |should_be.equal_to| 'I rest in peace'


class StoryParserWithValidScenarios(unittest.TestCase):
    def test_scenario_title_should_be_getting_money(self):
        story_parsed = parse_story("""Story: <Title>
                                      As a <role>
                                      I want to <feature>
                                      So that <businness value>

                                      Scenario 1: Getting Money""") 
        scenarios = story_parsed.get_scenarios()
        scenarios |should_be.equal_to| [('Getting Money', {'given':[],
                                                           'when':[],
                                                           'then':[]}), ]

    def test_steps_should_contain_just_a_given_with_it_works_text(self):
        story_parsed = parse_story("""Story: <Title>
                                      As a <role>
                                      I want to <feature>
                                      So that <businness value>
                                      
                                      Scenario 1: Getting Money
                                      Given it works""") 
        scenarios = story_parsed.get_scenarios()
        scenarios |should_be.equal_to| [('Getting Money', {'given': ['it works'],
                                              'when': [],
                                              'then': []})]

    def test_steps_should_contain_a_given_a_when_and_a_then_step(self):
        story_parsed = parse_story("""Story: <Title>
                                      As a <role>
                                      I want to <feature>
                                      So that <businness value>

                                      Scenario 1: Searching for pyhistorian at Google
                                        Given I go to http://www.google.com
                                        When I search for pyhistorian
                                        Then I see a github.com page""") 
        scenarios = story_parsed.get_scenarios()
        scenarios |should_be.equal_to| [('Searching for pyhistorian at Google',
                                         {'given': ['I go to http://www.google.com'],
                                          'when': ['I search for pyhistorian'],
                                          'then': ['I see a github.com page']})]


    def test_story_with_two_scenarios_each_one_with_three_steps(self):
        story_parsed = parse_story("""Story: <Title>
                                      As a <role>
                                      I want to <feature>
                                      So that <businness value>
                                      Scenario 1: Searching for pyhistorian at Google
                                        Given I go to http://www.google.com
                                        When I search for pyhistorian
                                        Then I see a github.com page
                                      
                                      Scenario 2: Searching for pyhistorian at Yahoo
                                        Given I go to http://www.yahoo.com
                                        When I search for pyhistorian
                                        Then I see the old code.google.com page""") 

        scenario = story_parsed.get_scenarios()
        scenario |should_be.equal_to| [('Searching for pyhistorian at Google',
                                        {'given': ['I go to http://www.google.com'],
                                         'when': ['I search for pyhistorian'],
                                         'then': ['I see a github.com page']}),

                                       ('Searching for pyhistorian at Yahoo',
                                        {'given': ['I go to http://www.yahoo.com'],
                                         'when': ['I search for pyhistorian'],
                                         'then': ['I see the old code.google.com page']}) ]


if __name__ == '__main__':
    unittest.main()
