# coding: utf-8
'''
	>>> portuguese = RegexInternationalized('pt-br')
	>>> english = RegexInternationalized('en-us')

	>>> re.match(english['story_regex'], 'Story: Title') is not None
	True
	>>> re.match(portuguese['story_regex'], 'História: Título') is not None
	True

	>>> re.match(english['as_a_regex'], 'As a <role>') is not None
	True
	>>> re.match(portuguese['as_a_regex'], 'Como um <papel>') is not None
	True

	>>> re.match(english['i_want_to_regex'], 'I want to <benefit>') is not None
	True
	>>> re.match(portuguese['i_want_to_regex'], 'Eu quero <benefício>') is not None
	True
	
	>>> re.match(english['scenario_regex'], 'Scenario 666: <title>') is not None
	True
	>>> re.match(portuguese['scenario_regex'], 'Cenário 666: <título>') is not None
	True

	>>> re.match(english['given_regex'], 'Given <stuff>') is not None
	True
	>>> re.match(portuguese['given_regex'], 'Dado que <alguma coisa>') is not None
	True

	>>> re.match(english['when_regex'], 'When <stuff>') is not None
	True
	>>> re.match(portuguese['when_regex'], 'Quando <alguma coisa>') is not None
	True

	>>> re.match(english['then_regex'], 'Then <stuff>') is not None
	True
	>>> re.match(portuguese['then_regex'], 'Então <alguma coisa>') is not None
	True

'''
from story_parser import RegexInternationalized
import re

if __name__ == '__main__':
	import doctest
	doctest.testmod()
