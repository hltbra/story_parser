from story_parser import parse_story,\
                         InvalidHeaderException,\
                         InvalidScenarioException
from should_dsl import should_be
import unittest


      
class StoryParserWithInvalidStoryHeaders(unittest.TestCase):
    def test_should_raise_InvalidHeaderException_with_invalid_story_title(self):
        InvalidHeaderException |should_be.thrown_by| (parse_story, """
                                                      Story title is invalid
                                                      As a <role>
                                                      I want to <feature>
                                                      So that <businness value>""")

    def test_should_raise_InvalidHeaderException_with_invalid_story_role(self):
        InvalidHeaderException |should_be.thrown_by| (parse_story, """
                                                      Story: <Title>
                                                      As a_invalid
                                                      I want to <feature>
                                                      So that <businness value>""")

    def test_should_raise_InvalidHeaderException_with_invalid_story_feature(self):
        InvalidHeaderException |should_be.thrown_by| (parse_story, """
                                                      Story: <Title>
                                                      As a <role>
                                                      I want to_be invalid
                                                      So that <businness value>""")

    def test_should_raise_InvalidHeaderException_with_invalid_story_businness_value(self):
        InvalidHeaderException |should_be.thrown_by| (parse_story, """
                                                      Story: <Title>
                                                      As a <role>
                                                      I want to <feature>
                                                      So that_businness value_invalid""")


class StoryParserWithInvalidScenarios(unittest.TestCase):
    def test_should_raise_InvalidScenarioException_if_scenario_title_is_wrong(self):
        InvalidScenarioException |should_be.thrown_by| (parse_story,
                                                        """Story: <Title>
                                                           As a <role>
                                                           I want to <feature>
                                                           So that <businness value>

                                                           Scenario Getting Money""") 

    def test_should_raise_InvalidScenarioException_if_step_line_is_not_valid(self):
        InvalidScenarioException |should_be.thrown_by| (parse_story,
                                                        """Story: <Title>
                                                           As a <role>
                                                           I want to <feature>
                                                           So that <businness value>

                                                           Scenario 1: <scenario_title>
                                                           Foo Step
                                                        """)
        
if __name__ == '__main__':
    unittest.main()
