# coding: utf-8
import re

def parse_story(story_text):
    return StoryParser(story_text)


class RegexInternationalized(object):
    _all_regexes = {
                'pt-br': {'story_regex': r'História: (.+)',
                          'as_a_regex': r'Como um (.+)',
                          'i_want_to_regex': r'Eu quero (.+)',
                          'scenario_regex': r'Cenário \d+: (.+)',
                          'given_regex': r'Dado que (.+)',
                          'when_regex': r'Quando (.+)',
                          'then_regex': r'Então (.+)',
                         },
                'en-us': {'story_regex': r'Story: (.+)',
                          'as_a_regex': r'As an? (.+)',
                          'i_want_to_regex': r'I want to (.+)',
                          'scenario_regex': r'Scenario \d+: (.+)',
                          'given_regex': r'Given (.+)',
                          'when_regex': r'When (.+)',
                          'then_regex': r'Then (.+)',
                         },
               }

    def __init__(self, language_code):
        self._regexes = self._all_regexes[language_code]

    def __getitem__(self, term):
        return self._regexes[term]

class StoryParser(object):
    _story_title = ''
    _story_role = ''
    _story_benefit = ''

    def __init__(self, story_text, language='en-us'):
        self._scenarios = []
        self._story_text = story_text
        self._lines = []
        self._remove_blank_lines()
        self._regexes = RegexInternationalized(language)
        self._parse()

    def _remove_blank_lines(self):
        lines = self._story_text.split('\n')
        self._lines = [line.strip() for line in lines if line.strip()]

    def _parse_header(self):
        story_title = re.match(self._regexes['story_regex'], self._lines[0])
        story_role = re.match(self._regexes['as_a_regex'], self._lines[1])
        story_benefit = re.match(self._regexes['i_want_to_regex'], self._lines[2])
        if story_title is None or\
           story_role is None or\
           story_benefit is None:
            raise InvalidHeaderException("Invalid Story title line")
        else:
            self._story_title = story_title.group(1)
            self._story_role = story_role.group(1)
            self._story_benefit = story_benefit.group(1)

    def _parse_scenarios(self):
        index = 3
        scenarios = []
        while index < len(self._lines):
            story_title = re.match(self._regexes['scenario_regex'], self._lines[index])
            if story_title:
                index += 1
                steps = {'given': [],
                         'when': [],
                         'then': []}
                while index < len(self._lines):
                    if re.match(self._regexes['scenario_regex'], self._lines[index]):
                        break
                    line = self._lines[index]
                    given_line = re.match(self._regexes['given_regex'], line)
                    when_line = re.match(self._regexes['when_regex'], line)
                    then_line = re.match(self._regexes['then_regex'], line)
                    if given_line:
                        steps['given'].append(given_line.group(1))
                    elif when_line:
                        steps['when'].append(when_line.group(1))
                    elif then_line:
                        steps['then'].append(then_line.group(1))
                    else:
                        raise InvalidScenarioException("Invalid step line!")
                    index += 1
                self._scenarios.append((story_title.group(1), steps))
            else:
                raise InvalidScenarioException("Invalid Scenario!")

    def _parse(self):
        self._parse_header()
        self._parse_scenarios()

    def get_story_title(self):
        return self._story_title

    def get_story_role(self):
        return self._story_role

    def get_story_benefit(self):
        return self._story_benefit

    def get_scenarios(self):
        return self._scenarios



class InvalidHeaderException(Exception):
    pass


class InvalidScenarioException(Exception):
    pass
