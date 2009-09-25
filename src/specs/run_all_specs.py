from parsing_invalid_stories import *
from parsing_valid_stories import *
from story_parser import parser
import regex_with_i18n
import doctest

MODULES_WITH_DOCTESTS = (regex_with_i18n, parser, )

if __name__ == '__main__':
    suite = unittest.TestSuite()
    for obj in globals().values():
        if unittest.TestCase in getattr(obj, '__bases__', []):
            suite.addTest(unittest.makeSuite(obj))
    for module in MODULES_WITH_DOCTESTS:
        suite.addTest(doctest.DocTestSuite(module))
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)
