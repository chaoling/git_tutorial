# SPIKE Prime with VS Code and Pybricks

This project accompanies the [SPIKE Prime introduction slides](https://docs.google.com/presentation/d/1NlBcVt-mRRwkiEH20NNqN8sVg2lf-drlXsCYM-t-bdk/edit).

## 1. Download the project and laptop tools

1. On [the repository page](https://github.com/chaoling/git_tutorial), choose **Code > Download ZIP**, then extract it. If Git is installed, you can instead run `git clone https://github.com/chaoling/git_tutorial.git` from a parent folder.
2. Download [Visual Studio Code](https://code.visualstudio.com/download) for Windows or macOS and run its installer. On macOS, move the app to Applications.
3. Install [Python 3.13](https://www.python.org/downloads/). This is the classroom version used by this lesson. The Python interpreter is a separate download from VS Code.
4. In VS Code, choose **File > Open Folder** and open **spike-prime** inside the downloaded project. Accept the workspace trust prompt if this is the copy you intended to open.
5. Install the recommended **Python**, **Pylance**, and **Python Debugger** extensions from Microsoft. VS Code lists them in the Extensions view.

## 2. Install firmware on the hub once

Use a charged Prime Hub, a micro-USB data cable, and Chrome or Edge. Open [Pybricks Code](https://code.pybricks.com/) and follow **Tools > Install Pybricks Firmware**. Select Prime Hub, give it a unique name such as `Team 01`, and follow its update-mode and connection instructions. The installer provides the firmware, so you do not need a separate firmware download.

After installation, disconnect the hub from Pybricks Code and the LEGO app before using VS Code. Leave Bluetooth enabled on the laptop and turn on the hub. Keep the robot still while its IMU starts. You can restore official LEGO firmware from the Pybricks Code Tools menu later.

## 3. Create a project virtual environment

In VS Code, open the Command Palette with **Ctrl+Shift+P** on Windows or **Cmd+Shift+P** on Mac. Choose **Python: Create Environment > Venv > Python 3.13**. If prompted for dependencies, choose `requirements.txt`. Select the `.venv` interpreter, then open **Python: Create Terminal**.

Alternatively, create and activate the environment in the project terminal:

Windows PowerShell:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS:

```sh
python3.13 -m venv .venv
source .venv/bin/activate
```

Then install the tools:

```sh
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -c "import sys; print(sys.executable)"
```

The printed path should contain `.venv`. `pybricks` supplies editor API hints. `pybricksdev` sends programs to the hub. The actual robot runs the Pybricks firmware installed on its hub. If completion does not update, choose **Python: Restart Language Server**.

If Windows blocks PowerShell activation, open a Command Prompt terminal and run `.venv\Scripts\activate.bat`, or skip activation and use `.venv\Scripts\python.exe -m pip install -r requirements.txt`. You can also send code without activation using `.venv\Scripts\python.exe -m pybricksdev run ble main.py`. On Mac, the corresponding interpreter is `.venv/bin/python`.

## 4. Upload the first program

Open and save `main.py`. It changes the light to green and prints a greeting without moving any motors. In the activated terminal:

```sh
pybricksdev run ble main.py
```

When several hubs are nearby, use the exact name assigned during installation:

```sh
pybricksdev run ble --name "Team 01" main.py
```

You should see a green hub light and `Hello, SPIKE Prime!` in the terminal.

For a menu-based launch, choose **Terminal > Run Task > Pybricks: run current file on hub**. Use the named-hub task in a classroom. You can also select **Pybricks: send current file to hub** in Run and Debug and press **Ctrl+F5**. These configurations send the active saved `.py` file through `pybricksdev`. They do not provide on-hub breakpoints. Use the hub's center button to stop a running program.

The ordinary **Run Python File** button executes Python on the laptop. Use the Pybricks task, launch configuration, or terminal command for robot programs.

## 5. Try the robot movement examples

The movement examples adapt the existing [course first-step samples](https://github.com/chaoling/pybricks_tut). Start with `01_drivebase_basics.py`, then `02_turn_types.py`, then `03_gyro_and_settings.py`.

Before moving, check these example settings against your build:

| Setting | Sample value |
| --- | --- |
| Left wheel motor | Port A, counterclockwise positive |
| Right wheel motor | Port B, clockwise positive |
| Wheel diameter | 56 mm |
| Axle track | 112 mm between wheel contact centers |

These are example measurements. Adjust the ports, motor directions, and dimensions in each file. Lift the wheels for the first direction test. For movement, put the robot on the floor with at least 1 meter of clear space. Keep fingers and cables away from wheels. Stay ready to press the hub center button.

```sh
pybricksdev run ble --name "Team 01" 01_drivebase_basics.py
```

Positive distance means forward. Positive turn angle means right, clockwise from above. These samples use sequential calls, so they do not need `async`, `await`, or `run_task`. The gyro sample waits for the IMU to be ready before enabling gyro control. Keep the robot flat and still while it waits.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| `pybricksdev` is missing | Select `.venv`, create a fresh terminal, and install `requirements.txt`. |
| The laptop cannot find a hub | Turn it on, enable Bluetooth, allow Bluetooth access to VS Code or its terminal if prompted, and close other hub connections. Check the exact hub name. |
| Nothing happens after the Run Python File button | Use the Pybricks task or `pybricksdev run ble ...`. |
| A straight command makes the robot spin | Check the two motor ports and positive directions. |
| Distance or turn angle is wrong | Check wheel diameter and axle track, then measure repeated runs. |
| The gyro program waits at G | Set the complete robot flat and still until its IMU is ready. |

## Reference guides

- [Official VS Code setup for Pybricks](https://pybricks.com/project/pybricks-other-editors/)
- [Pybricks firmware installation](https://pybricks.com/learn/getting-started/install-pybricks/)
- [VS Code Python environments](https://code.visualstudio.com/docs/python/environments)
- [pybricksdev commands](https://github.com/pybricks/pybricksdev)
- [DriveBase API](https://docs.pybricks.com/en/stable/robotics.html)

The setup instructions were checked against the official guides on November 10, 2026. The project pins `pybricks` 4.1.1 and `pybricksdev` 2.3.2. Laptop syntax and CLI checks do not replace a physical robot test. A coach should test the environment on classroom computers before class.
