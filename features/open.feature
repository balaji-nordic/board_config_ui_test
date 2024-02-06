Feature: Board configurator

  Scenario: Open Board Configurator app
    When nRF Connect for Desktop is opened
	When Board Configurator Open button is clicked
    Then The Board Configurator is opened
	Then Close the Board Configurator
	Then Close nRF Connect for Desktop
