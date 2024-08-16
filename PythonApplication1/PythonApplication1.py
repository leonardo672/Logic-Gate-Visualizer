import numpy as np
import matplotlib.pyplot as plt

def NOR(x1, x2):
    inputs = np.array([x1, x2])
    weights = np.array([-1, -1])
    bias = 0.5

    net = np.sum(inputs * weights) + bias
    if net <= 0:
        return 0
    else:
        return 1

def AND(x1, x2):
    inputs = np.array([x1, x2])
    weights = np.array([1, 1])
    bias = -1.5

    net = np.sum(inputs * weights) + bias
    if net <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    inputs = np.array([x1, x2])
    weights = np.array([-1, -1])
    bias = 1.5

    net = np.sum(inputs * weights) + bias
    if net <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    inputs = np.array([x1, x2])
    weights = np.array([1, 1])
    bias = -0.5

    net = np.sum(inputs * weights) + bias
    if net <= 0:
        return 0
    else:
        return 1

def plot_logic_gates():
    # Get input values from the user
    x1 = int(input("Enter the value for input A (0 or 1): "))
    x2 = int(input("Enter the value for input B (0 or 1): "))

    # Compute the output for each gate
    nor_output = NOR(x1, x2)
    print("The NOR gate output for inputs A={} and B={} is {}".format(x1, x2, nor_output))
    and_output = AND(x1, x2)
    print("The AND gate output for inputs A={} and B={} is {}".format(x1, x2, and_output))
    nand_output = NAND(x1, x2)
    print("The NAND gate output for inputs A={} and B={} is {}".format(x1, x2, nand_output))
    or_output = OR(x1, x2)
    print("The OR gate output for inputs A={} and B={} is {}".format(x1, x2, or_output))

    # Clear the current plot
    plt.clf()

    # Create subplots for each gate
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))

    # Plot NOR gate
    axs[0, 0].axhline(y=0.2, color='red' if nor_output == 0 else 'green', linestyle='-', linewidth=2, label='Output')
    axs[0, 0].axhline(y=0, color='red' if x2 == 0 else 'green', linestyle='--', linewidth=2, label='Input B')
    axs[0, 0].axhline(y=-0.2, color='red' if x1 == 0 else 'green', linestyle=':', linewidth=2, label='Input A')
    axs[0, 0].set_ylim(-0.3, 0.3)
    axs[0, 0].set_yticks([])
    axs[0, 0].set_xlabel('Input')
    axs[0, 0].set_title('NOR Gate')
    axs[0, 0].legend(loc='upper right')

    # Plot AND gate
    axs[0, 1].axhline(y=0.2, color='red' if and_output == 0 else 'green', linestyle='-', linewidth=2, label='Output')
    axs[0, 1].axhline(y=0, color='red' if x2 == 0 else 'green', linestyle='--', linewidth=2, label='Input B')
    axs[0, 1].axhline(y=-0.2, color='red' if x1 == 0 else 'green', linestyle=':', linewidth=2, label='Input A')
    axs[0, 1].set_ylim(-0.3, 0.3)
    axs[0, 1].set_yticks([])
    axs[0, 1].set_xlabel('Input')
    axs[0, 1].set_title('AND Gate')
    axs[0, 1].legend(loc='upper right')

    # Plot NAND gate
    axs[1, 0].axhline(y=0.2, color='red' if nand_output == 0 else 'green', linestyle='-', linewidth=2, label='Output')
    axs[1, 0].axhline(y=0, color='red' if x2 == 0 else 'green', linestyle='--', linewidth=2, label='Input B')
    axs[1, 0].axhline(y=-0.2, color='red' if x1 == 0 else 'green', linestyle=':', linewidth=2, label='Input A')
    axs[1, 0].set_ylim(-0.3, 0.3)
    axs[1, 0].set_yticks([])
    axs[1, 0].set_xlabel('Input')
    axs[1, 0].set_title('NAND Gate')
    axs[1, 0].legend(loc='upper right')

    # Plot OR gate
    axs[1, 1].axhline(y=0.2, color='red' if or_output == 0 else 'green', linestyle='-', linewidth=2, label='Output')
    axs[1, 1].axhline(y=0, color='red' if x2 == 0 else 'green', linestyle='--', linewidth=2, label='Input B')
    axs[1, 1].axhline(y=-0.2, color='red' if x1 == 0 else 'green', linestyle=':', linewidth=2, label='Input A')
    axs[1, 1].set_ylim(-0.3, 0.3)
    axs[1, 1].set_yticks([])
    axs[1, 1].set_xlabel('Input')
    axs[1, 1].set_title('OR Gate')
    axs[1, 1].legend(loc='upper right')

    # Adjust spacing between subplots
    fig.tight_layout()

    # Show the plot
    plt.show()

# Call the function to plot the logic gates
plot_logic_gates()
