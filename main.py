import math

def dB_to_linear(db_value, reference):
    """ Convert dB value to linear scale """
    return reference * (10 ** (db_value / 20.0))

def linear_to_dB(linear_value, reference):
    """ Convert linear scale value to dB """
    return 20 * math.log10(linear_value / reference)


def convert_values(input_value, input_type):
    """ Convert between different dB scales and SPL """
    # Reference values
    ref_dBV = 1.0  # 1 Volt
    ref_dBu = 0.775  # Volts (approx for 0 dBm under 600 ohm load)
    ref_dBW = 1.0  # 1 Watt
    ref_dBm = 0.001  # 1 milliwatt
    ref_SPL = 0.00002  # 20 micropascals

    # Initialize linear_value
    linear_value = None

    # Convert input dB to linear voltage or power
    if input_type == 'dBV':
        linear_value = dB_to_linear(input_value, ref_dBV)
    elif input_type == 'dBu':
        linear_value = dB_to_linear(input_value, ref_dBu)
    elif input_type == 'dBW':
        linear_value = dB_to_linear(input_value, ref_dBW)
    elif input_type == 'dBm':
        linear_value = dB_to_linear(input_value, ref_dBm)
    elif input_type == 'SPL':
        linear_value = dB_to_linear(input_value, ref_SPL)
    else:
        return f"Error: Unrecognized dB type '{input_type}'. Please choose from dBV, dBu, dBW, dBm, SPL."

    # If linear_value was not set due to unrecognized input_type, return an error message
    if linear_value is None:
        return f"Error: Unrecognized dB type '{input_type}'. Please choose from dBV, dBu, dBW, dBm, SPL."

    # Convert linear value to all dB types
    results = {
        'dBV': linear_to_dB(linear_value, ref_dBV),
        'dBu': linear_to_dB(linear_value, ref_dBu),
        'dBW': linear_to_dB(linear_value, ref_dBW),
        'dBm': linear_to_dB(linear_value, ref_dBm),
        'SPL': linear_to_dB(linear_value, ref_SPL)
    }

    return results


def main():
    print("Welcome to the dB converter. Please select the dB type and enter the value you want to convert:")
    print("Types: dBV, dBu, dBm, dBW, SPL")
    input_type = input("Enter dB type: ")
    input_value = float(input("Enter dB value: "))

    results = convert_values(input_value, input_type)
    print(f"Conversions from {input_value} {input_type}:")
    for key, value in results.items():
        print(f"{key}: {value:.2f}")

if __name__ == "__main__":
    main()
