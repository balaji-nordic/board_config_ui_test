# Experimental: Board Configurator GUI Testing Repository

## Overview

This repository contains automated tests for the Board Configurator GUI using Python with the `pyautogui` module. The tests interact with the GUI and verify its functionality by comparing screen areas with known snapshots.

## Requirements

- Python 3.x
- nRF Connect for Desktop 
- Board Configurator app installed
- nRF54L15 DK connected

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/balaji-nordic/board_config_ui_test.git
   ```

2. Install the required Python modules:

   ```bash
   pip install -r requirements.txt
   ```

## Test Scenarios

See https://github.com/balaji-nordic/board_config_ui_test/blob/8c6135344c368cf8de9f08c6063b410bfdbe0755/features/open.feature#L3-L19

## Limitations

- Tested only on Windows
- The tests are currently designed to work correctly on a PC with the monitor having the same resolution as where the snapshots were taken. This is the limitation of `pyautogui` framework.
-- Work in progress: Efforts are being made to use the scaling functionality of `pillows`  to ensure that the tests adapt to different screen resolutions. See [resizing branch](https://github.com/balaji-nordic/board_config_ui_test/tree/resizing_to_work_on_all_monitors) for more details.

## Usage

To run the tests, use the following command:

```bash
behave
```

## Demo

![](https://github.com/balaji-nordic/board_config_ui_test/blob/main/working_capture.gif)
