from story_parser import parse_text,\
                         InvalidHeaderException,\
                         InvalidScenarioException
from should_dsl import should_be
import unittest


      
class StoryParserWithInvalidStoryHeaders(unittest.TestCase):
    def test_should_raise_InvalidHeaderException_with_invalid_story_title(self):
        InvalidHeaderException |should_be.thrown_by| (parse_text, """
                                                      Story title is invalid
                                                      As a <role>
                                                      I want to <feature>
                                                      So that <business value>""")

    def test_should_raise_InvalidHeaderException_with_invalid_story_header(self):
        InvalidHeaderException |should_be.thrown_by| (parse_text, """
                                                      Story: Title is OK""")

    def test_should_raise_InvalidHeaderException_with_invalid_story_role(self):
        InvalidHeaderException |should_be.thrown_by| (parse_text, """
                                                      Story: <Title>
                                                      As a_invalid
                                                      I want to <feature>
                                                      So that <business value>""")

    def test_should_raise_InvalidHeaderException_with_invalid_story_feature(self):
        InvalidHeaderException |should_be.thrown_by| (parse_text, """
                                                      Story: <Title>
                                                      As a <role>
                                                      I want to_be invalid
                                                      So that <business value>""")

    def test_should_raise_InvalidHeaderException_with_invalid_story_business_value(self):
        InvalidHeaderException |should_be.thrown_by| (parse_text, """
                                                      Story: <Title>
                                                      As a <role>
                                                      I want to <feature>
                                                      So that_business value_invalid""")


class StoryParserWithInvalidScenarios(unittest.TestCase):
    def test_should_raise_InvalidScenarioException_if_scenario_title_is_wrong(self):
        InvalidScenarioException |should_be.thrown_by| (parse_text,
                                                        """Story: <Title>
                                                           As a <role>
                                                           I want to <feature>
                                                           So that <business value>

                                                           Scenario Getting Money""") 

    def test_should_raise_InvalidScenarioException_if_step_line_is_not_valid(self):
        InvalidScenarioException |should_be.thrown_by| (parse_text,
                                                        """Story: <Title>
                                                           As a <role>
                                                           I want to <feature>
                                                           So that <business value>

                                                           Scenario 1: <scenario_title>
                                                           Foo Step
                                                        """)
        
class ScenarioWithInvalidAndStep(unittest.TestCase):
    def test_and_without_context(self):
        InvalidScenarioException |should_be.thrown_by| (parse_text,
                                                        """Story: 1
                                                        As a 2
                                                        I want to 3
                                                        So that 4

                                                        Scenario 1: 5
                                                        And aff""")
if __name__ == '__main__':
    unittest.main()
