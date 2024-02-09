Feature: Board configurator

Scenario: Open Board Configurator app
    When nRF Connect for Desktop is opened
	When Board Configurator Open button is clicked
    Then The Board Configurator is opened
	Then Close the Board Configurator
	Then Close nRF Connect for Desktop

  Scenario: Change voltages on nRF54L15 PDK
    When nRF Connect for Desktop is opened
	When Board Configurator Open button is clicked
    Then The Board Configurator is opened
  When the nRF54L15 DK is selected
    Then Wait "5" seconds
    Then select "1.8"v
    Then select "2.0"v
    Then Close the Board Configurator
    Then Close nRF Connect for Desktop
