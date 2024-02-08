Feature: Board configurator

  Scenario: Open Board Configurator app
    When nRF Connect for Desktop is opened
	When Board Configurator Open button is clicked
    Then The Board Configurator is opened
	Then Close the Board Configurator
	Then Close nRF Connect for Desktop

  Scenario: Select nRF54L15 PDK
    When nRF Connect for Desktop is opened
	When Board Configurator Open button is clicked
    Then The Board Configurator is opened
  When the nRF54L15 DK is selected
    Then the nRF54L15 DK configuration is displayed
	Then Close the Board Configurator
	Then Close nRF Connect for Desktop
