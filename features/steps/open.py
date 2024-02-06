from behave import *
from nrfconnect_open import mytest

boardConfigTest = mytest()

@given('nRF Connect for Desktop is opened')
def step_impl(context):
	boardConfigTest.setUp()

@when('Board Configurator Open button is clicked')
def step_impl(context):
    boardConfigTest.openBoardConfigurator()

@then(u'the Board Configurator is opened')
def step_impl(context):
	assert boardConfigTest.checkBoardConfiguratorIsOpen()