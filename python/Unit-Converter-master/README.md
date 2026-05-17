
# Unit Converter with NiceGUI

This project is a Unit Converter built with Python using the NiceGUI framework. The converter supports conversions for Length, Weight, and Temperature units. It provides an interactive UI for users to input values, select units, and perform conversions.

## Features

- **Length conversion**: Supports conversions between common units like meter, kilometer, foot, inch, yard, and mile.
- **Weight conversion**: Supports conversions between units like gram, kilogram, ton, and pound.
- **Temperature conversion**: Converts between Celsius, Fahrenheit, and Kelvin.
- **Reset function**: Clears inputs and hides results after each conversion.

## Project Structure

```
app.py            # Main application script with NiceGUI UI logic
Units/
   length.py      # Contains the logic for length conversions
   weight.py      # Contains the logic for weight conversions
   temperature.py # Contains the logic for temperature conversions
```

## Getting Started

### Prerequisites

- Python 3.x
- `nicegui` library

You can install the required dependencies using pip:

```bash
pip install nicegui
```

### Running the Application

1. Clone the repository:

```bash
git clone https://github.com/your-username/unit-converter.git
```

2. Navigate to the project directory:

```bash
cd unit-converter
```

3. Run the `app.py` script:

```bash
python app.py
```

This will start the NiceGUI application, and the UI will be accessible in your browser at `http://localhost:8080`.

### Usage

1. Select the type of unit conversion you want to perform (Length, Weight, or Temperature).
2. Enter the value you want to convert.
3. Choose the units to convert from and to.
4. Click "Convert" to get the result.
5. Click "Reset" to clear the input fields and start a new conversion.

![image](https://github.com/user-attachments/assets/ebfad5f3-72aa-4727-94fb-316934d6f58d)

![image](https://github.com/user-attachments/assets/9041d22e-9f2f-4a8c-aaa5-9f7651f03f8f)

![image](https://github.com/user-attachments/assets/56d39f35-b34a-417e-81c8-556dd4a55ac8)

## Units Supported

- **Length**: Centimeter, Meter, Kilometer, Foot, Inch, Yard, Mile
- **Weight**: Gram, Milligram, Kilogram, Ton, Pound
- **Temperature**: Celsius, Fahrenheit, Kelvin

## Customization

You can extend the converter by adding more units or modifying the UI by editing the corresponding files in the `Units/` directory.

## License

This project is licensed under the MIT License. Feel free to modify and use it as per your needs.

## Acknowledgements

- [NiceGUI](https://nicegui.io/) - A Python framework for building beautiful web-based user interfaces with minimal code.

## Project URL:
https://roadmap.sh/projects/unit-converter
