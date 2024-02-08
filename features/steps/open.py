from behave import *
from nrfconnect_open import mytest
import time

boardConfigTest = mytest()

@when('nRF Connect for Desktop is opened')
def step_impl(context):
	boardConfigTest.opennRFConnectForDesktop()

@when(u'Board Configurator Open button is clicked')
def step_impl(context):
    boardConfigTest.openBoardConfigurator()

@then(u'the Board Configurator is opened')
def step_impl(context):
	assert boardConfigTest.checkBoardConfiguratorIsOpen()

@then(u'Close the Board Configurator')
def step_impl(context):
	boardConfigTest.closeActiveBoardConfigurator()

@then(u'Close nRF Connect for Desktop')
def step_impl(context):
	boardConfigTest.closenRFConnectForDesktop()

@given('the Board Configurator is opened')
def step_impl(context):
	boardConfigTest.opennRFConnectForDesktop()
	boardConfigTest.openBoardConfigurator()

@when('the nRF54L15 DK is selected')
def step_impl(context):
	boardConfigTest.selectnrf54l15DK()

@then('the nRF54L15 DK configuration is displayed')
def step_impl(context):
	assert boardConfigTest.checknRF54L15ConfigurationIsShown()

@then(u'select "{voltage:f}"v')
def step_impl(context, voltage):
	boardConfigTest.selectVoltage(voltage)

@then(u'Wait "{seconds:d}" seconds')
def step_impl(context, seconds):
	time.sleep(seconds)
