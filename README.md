# Scope of this project
**CamCatch** is part of a bigger project. A project made for my University final exam for the `"Intelligent Robotics"` Class.

The aim of the final project is to build a laser-pointer robot (points at black circles for the sake of simplicity). This part of the project is responsible of:

1. Capturing frames from the built-in camera

2. Processing those frames to acquire an `Inverted-Binary` image

3. Using the `Inverted-Binary` image to calculate center of mass (in pixels) of a singular black circle on the camera

4. Converting center of mass values to generate a `Transformation Matrix` indicating the transformation of the black circle in real world (relative to camera position)

5. Converting the Obtained `Transformation Matrix` (relative to camera) to another `Transformation Matrix` that is relative to the pointer robot.

6. Calculating `Inverse Kinematics` for the robot using the `Transformation Matrix`

7. Sending the obtained angle values to the robot through `Serial Communication`

# Running CamCatch `(venv)`

**Linux/MacOS**
```bash
python -m venv venv  # Create the virtual environment
source venv/bin/activate  # Activate virtual environment
pip install -r requirements.txt  # Install dependencies
python src/main.py # Run the application
```

**Windows**
```bash
python -m venv venv  # Create the virtual environment
venv\Scripts\activate # Activate virtual environment
pip install -r requirements.txt  # Install dependencies
python src/main.py # Run the application
```
