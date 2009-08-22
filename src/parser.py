# coding: utf-8
import re


def get_regex_first_group(regex):
    """
    >>> get_regex_first_group(re.match('In order to (.+)', 'In order to avoid duplication'))
    'avoid duplication'
    """
    if regex:
        return regex.group(1)
    return None

def parse_text(story_text):
    return StoriesParser(story_text)


class RegexInternationalized(object):
    _all_regexes = {
                'pt-br': {'story_regex': r'História: (.+)',
                          'in_order_to_regex': r'Para que (.+)',
                          'as_a_regex': r'Como um (.+)',
                          'i_want_to_regex': r'Eu quero (.+)',
                          'so_that_regex': r'Para que (.+)',
                          'scenario_regex': r'Cenário \d+: (.+)',
                          'given_regex': r'Dado que (.+)',
                          'when_regex': r'Quando (.+)',
                          'then_regex': r'Então (.+)',
                         },
                'en-us': {'story_regex': r'Story: (.+)',
                          'in_order_to_regex': r'In order to (.+)',
                          'as_a_regex': r'As an? (.+)',
                          'i_want_to_regex': r'I want to (.+)',
                          'so_that_regex': r'So that (.+)',
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


class StoryParsed(object):
    def __init__(self, title, role, feature, business_value, scenarios):
        self._title = title
        self._role = role
        self._feature = feature
        self._business_value = business_value
        self._scenarios = scenarios

    @property
    def title(self):
        return self._title

    @property
    def role(self):
        return self._role

    @property
    def feature(self):
        return self._feature

    @property
    def business_value(self):
        return self._business_value

    @property
    def scenarios(self):
        return self._scenarios

class StoriesParser(object):
    _story_title = ''
    _story_role = ''
    _story_feature = ''
    _story_business_value = ''

    def __init__(self, story_text, language='en-us'):
        self._scenarios = []
        self._story_text = story_text
        self._stories = []
        self._lines = []
        self._remove_blank_lines()
        self._regexes = RegexInternationalized(language)
        self._parse_stories()

    def _remove_blank_lines(self):
        lines = self._story_text.split('\n')
        self._lines = [line.strip() for line in lines if line.strip()]

    def _parse_story_header_with_feature_injection(self, lines):
        """Story: ...
        In order to ...
        As a ...
        I want to ..."""
        return map(get_regex_first_group,
                        (re.match(self._regexes['story_regex'], lines[0]),
                         re.match(self._regexes['as_a_regex'], lines[2]),
                         re.match(self._regexes['i_want_to_regex'], lines[3]),
                         re.match(self._regexes['in_order_to_regex'], lines[1])))


    def _parse_story_header_with_basic_template(self, lines):
        """Story:
        As a ...
        I want to ...
        So that ..."""
        return map(get_regex_first_group,
                        (re.match(self._regexes['story_regex'], lines[0]),
                         re.match(self._regexes['as_a_regex'], lines[1]),
                         re.match(self._regexes['i_want_to_regex'], lines[2]),
                         re.match(self._regexes['so_that_regex'], lines[3])))

    def _parse_story_header(self, lines):
        if len(lines) < 4:
            raise InvalidHeaderException("Invalid Story Header!")
        header_with_basic_template = self._parse_story_header_with_basic_template(lines)
        header_with_feature_injection = self._parse_story_header_with_feature_injection(lines)
        if None not in header_with_basic_template:
            return header_with_basic_template
        elif None not in header_with_feature_injection:
            return header_with_feature_injection
        else:
           raise InvalidHeaderException("Invalid Story Header!")

    def _parse_scenarios(self, lines):
        index = 0
        scenarios = []
        while index < len(lines):
            story_title = re.match(self._regexes['scenario_regex'], lines[index])
            if story_title:
                index += 1
                steps = {'given': [],
                         'when': [],
                         'then': []}
                while index < len(lines):
                    if re.match(self._regexes['scenario_regex'], lines[index]):
                        break
                    given_line = re.match(self._regexes['given_regex'], lines[index])
                    when_line = re.match(self._regexes['when_regex'], lines[index])
                    then_line = re.match(self._regexes['then_regex'], lines[index])
                    if given_line:
                        steps['given'].append(given_line.group(1))
                    elif when_line:
                        steps['when'].append(when_line.group(1))
                    elif then_line:
                        steps['then'].append(then_line.group(1))
                    else:
                        raise InvalidScenarioException("Invalid Step!")
                    index += 1
                scenarios.append((story_title.group(1), steps))
            else:
                raise InvalidScenarioException("Invalid Scenario!")
        return scenarios

    def _parse_stories(self):
        index = 0
        while index < len(self._lines):
            line_regex = re.match(self._regexes['story_regex'], self._lines[index])
            if line_regex:
                story_block = [self._lines[index]]
                index += 1
                while index < len(self._lines) and\
                      re.match(self._regexes['story_regex'], self._lines[index]) is None:
                    story_block.append(self._lines[index])
                    index += 1
            else:
                raise InvalidHeaderException("Invalid Story Header!")
            title, role, feature, business_value = self._parse_story_header(story_block)
            scenarios = self._parse_scenarios(story_block[4:])
            self._stories.append(StoryParsed(title,
                                             role,
                                             feature,
                                             business_value,
                                             scenarios))

    def get_stories(self):
        return self._stories



class InvalidHeaderException(Exception):
    pass


class InvalidScenarioException(Exception):
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
