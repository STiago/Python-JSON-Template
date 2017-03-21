#!env/bin/python
from hamcrest import *
import unittest
from module import *

# One unit test per function, several cases per unit test
class AddTemplateTest(unittest.TestCase):

    def setUp(self):
        queue = Queue.Queue()

    def tearDown(self):
        queue = None

    def testEmptyJsonDoesNotModifyTheQueue(self):
        add_template('')
        assert_that(queue.empty(), is_(True))

    def testMissingActionInJsonDoesNotModifyTheQueue(self):
        add_template('{"when": "2016-4-19 10:00:00"}')
        assert_that(queue.empty(), is_(True))

    def testActionDifferentThanApplyDoesNotModifyTheQueue(self):
        add_template('{"action": "1", "age": "black", "template": 2}')
        assert_that(queue.empty(), is_(True))

    def testMissingTemplateInJsonDoesNotModifyTheQueue(self):
        add_template('{"action": "apply", "when": "2016-4-19 10:00:00"}')
        assert_that(queue.empty(), is_(True))

    def testValidJsonAddsTemplateToTheQueue(self):
        add_template('{"action": "apply", "when": "2016-4-19 10:00:00", "template":"TEST TEMPLATE"}')
        assert_that(queue.empty(), is_(False))
        assert_that(queue.get(), equal_to("TEST TEMPLATE"))

if __name__ == '__main__':
    unittest.main()
