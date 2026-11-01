# Kibo — smart pet feeder

**Kibo** = **kib**ble + ro**bo**t.

A LEGO Mindstorms EV3 robot that feeds a pet and gives it water on a schedule,
controlled from a web site.

## How it works

```
Browser  →  Python server on a PC  →  Bluetooth  →  EV3  →  motors
```

- Food is dispensed by a rotating roller; each compartment holds about 5 g.
- The schedule, food amount and water amount are set on the web site.

## Run

```
cd "RobotProgram - py"
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe Kibo\main.py
```

> Work in progress — school robotics project.
