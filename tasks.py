import numpy as np

# Follow the tasks below to practice basic Python concepts.
# Write your code in between the dashed lines.
# Don't import additional packages. Numpy suffices.


# Task 1: Compute Output Size for 1D Convolution
# Instructions:
# Write a function that takes two one-dimensional numpy arrays (input_array, kernel_array) as arguments.
# The function should return the length of the convolution output (assuming no padding and a stride of one).
# The output length can be computed as follows:
# (input_length - kernel_length + 1)

# Your code here:
# -----------------------------------------------

def compute_output_size_1d(input_array, kernel_array):
    output = len(input_array) - len(kernel_array) + 1
    return output



# -----------------------------------------------
# Example:
input_array = np.array([1, 2, 3, 4, 5])
kernel_array = np.array([1, 0, -1])
print(compute_output_size_1d(input_array, kernel_array))


# Task 2: 1D Convolution
# Instructions:
# Write a function that takes a one-dimensional numpy array (input_array) and a one-dimensional kernel array (kernel_array)
# and returns their convolution (no padding, stride 1).

# Your code here:
# -----------------------------------------------

def convolve_1d(input_array, kernel_array):
    output_list = []
    output_length = compute_output_size_1d(input_array, kernel_array)
    kernel_length = len(kernel_array)
    for i in range(output_length):
      window = input_array[i : i + kernel_length]
      products = []
      for j in range(kernel_length):
        products.append(window[j] * kernel_array[j])
      total = sum(products)
      output_list.append(total)
    return output_list


# -----------------------------------------------
# Another tip: write test cases like this, so you can easily test your function.
input_array = np.array([1, 2, 3, 4, 5])
kernel_array = np.array([1, 0, -1])
print(convolve_1d(input_array, kernel_array))

# Task 3: Compute Output Size for 2D Convolution
# Instructions:
# Write a function that takes two two-dimensional numpy matrices (input_matrix, kernel_matrix) as arguments.
# The function should return a tuple with the dimensions of the convolution of both matrices.
# The dimensions of the output (assuming no padding and a stride of one) can be computed as follows:
# (input_height - kernel_height + 1, input_width - kernel_width + 1)

# Your code here:
# -----------------------------------------------

def compute_output_size_2d(input_matrix, kernel_matrix):
    height_output = compute_output_size_1d(
        input_array = input_matrix[:, 0],
        kernel_array = kernel_matrix[:, 0]
    )

    width_output = compute_output_size_1d(
        input_array = input_matrix[0, :],
        kernel_array = kernel_matrix[0, :]
    )

    return (height_output, width_output)

## test
inp  = np.zeros((5, 7))
kern = np.zeros((3, 4))
print(compute_output_size_2d(inp, kern))


# -----------------------------------------------


# Task 4: 2D Convolution
# Instructions:
# Write a function that computes the convolution (no padding, stride 1) of two matrices (input_matrix, kernel_matrix).
# Your function will likely use lots of looping and you can reuse the functions you made above.

# Your code here:
# -----------------------------------------------

def convolute_2d(input_matrix, kernel_matrix):
    out_h, out_w = compute_output_size_2d(input_matrix, kernel_matrix)
    output_matrix = np.zeros((out_h, out_w))

    kernel_h, kernel_w = kernel_matrix.shape

    for i in range(out_h):
        for j in range(out_w):
            window = input_matrix[i : i + kernel_h, j : j + kernel_w]

            # compute total manually
            total = 0
            for m in range(kernel_h):
                for n in range(kernel_w):
                    total += window[m, n] * kernel_matrix[m, n]

            output_matrix[i, j] = total

    return output_matrix




# -----------------------------------------------
