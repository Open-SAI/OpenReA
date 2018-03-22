# coding=utf-8

import time
from telenium.tests import TeleniumTestCase


class TestTestCase(TeleniumTestCase):
    cmd_entrypoint = [u'/home/debianita86/Documentos/Autenticacion/main.py']
    
    def test_new_test(self):
        self.assertExists('//ActionView', timeout=5)
        self.assertExists('//ActionBar', timeout=5)
        self.assertExists('//ActionGroup', timeout=5)
        self.assertExists('//ActionPrevious', timeout=5)
        self.cli.wait_click('//ActionPrevious', timeout=5)
        self.cli.wait_click('//ActionGroup', timeout=5)
        self.assertExists('//TextInput', timeout=5)
        self.cli.wait_click('//TextInput', timeout=5)
        self.cli.setattr('//TextInput', 'text', "diego")
        self.assertExists('//ActionButton', timeout=5)
        self.cli.wait_click('//ActionGroup', timeout=5)
