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

	>>> re.match(english['i_want_to_regex'], 'I want to <feature>') is not None
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

    >>> parsed_stories = parse_text("""História: Jogando Par ou Ímpar
    ...   Como um professor do ensino fundamental
    ...   Eu quero mostrar o jogo de par ou ímpar
    ...   Para que os alunos possam se divertir jogando par ou ímpar
    ...
    ...   Cenário 1: Cada jogador coloca números pares
    ...     Dado que duas crianças estão jogando par ou ímpar
    ...     Quando cada uma coloca um número par
    ...     Então o jogador que pediu par ganha
    ...
    ...   Cenário 2: Um jogador coloca número par e o outro, ímpar
    ...     Dado que duas crianças estão jogando par ou ímpar
    ...     Quando a primeira coloca um número par e a segunda um número ímpar
    ...     Então quem pediu ímpar vence""", language='pt-br').get_stories()
    >>> first_story = parsed_stories[0]
    >>> print first_story.title
    Jogando Par ou Ímpar
    >>> print first_story.role
    professor do ensino fundamental
    >>> print first_story.business_value
    os alunos possam se divertir jogando par ou ímpar
    >>> print first_story.feature
    mostrar o jogo de par ou ímpar

    >>> first_scenario = first_story.scenarios[0]
    >>> second_scenario = first_story.scenarios[1]

    >>> print first_scenario[0]
    Cada jogador coloca números pares
    >>> print first_scenario[1]['given'][0]
    duas crianças estão jogando par ou ímpar
    >>> print first_scenario[1]['when'][0]
    cada uma coloca um número par
    >>> print first_scenario[1]['then'][0]
    o jogador que pediu par ganha


    >>> print second_scenario[1]['given'][0]
    duas crianças estão jogando par ou ímpar
    >>> print second_scenario[1]['when'][0]
    a primeira coloca um número par e a segunda um número ímpar
    >>> print second_scenario[1]['then'][0]
    quem pediu ímpar vence


    >>> print second_scenario[0]
    Um jogador coloca número par e o outro, ímpar
'''
from story_parser import RegexInternationalized, parse_text
import re

if __name__ == '__main__':
	import doctest
	doctest.testmod()
