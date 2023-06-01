import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define a function to create a plot
def create_plot(data, x_col, y_col):
    """Creates a plot of the data.

    Args:
        data: A pandas DataFrame.
        x_col: The name of the column to use for the x-axis.
        y_col: The name of the column to use for the y-axis.

    Returns:
        A Streamlit plot.
    """

    # Create a figure
    fig, ax = plt.subplots()

    # Plot the data
    ax.plot(data[x_col], data[y_col])

    # Set the title
    ax.set_title('Plot')

    # Set the x-axis label
    ax.set_xlabel(x_col)

    # Set the y-axis label
    ax.set_ylabel(y_col)

    # Return the plot
    return fig

# Create a sidebar
st.sidebar.title('Plot Options')

# Add options for users to enter custom x and y values
x_values = st.sidebar.text_area('Enter x values (comma-separated)')
y_values = st.sidebar.text_area('Enter y values (comma-separated)')

# Process the user-provided x and y values
x_values = list(map(float, x_values.split(',')))
y_values = list(map(float, y_values.split(',')))

# Create a DataFrame from the user-provided x and y values
data = pd.DataFrame({
    'x': x_values,
    'y': y_values
})

# Create a plot of the data
fig = create_plot(data, 'x', 'y')

# Display the plot
st.pyplot(fig)
plt.show()  # Add this line to display the plot correctly
