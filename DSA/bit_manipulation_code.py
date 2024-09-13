def bitManipulation(num, i):
    # Convert 1-based index to 0-based index
    index = i - 1
    
    # Get the ith bit (0-based index)
    bit_value = (num >> index) & 1
    
    # Set the ith bit
    num_set = num | (1 << index)
    
    # Clear the ith bit
    num_clear = num & ~(1 << index)
    
    # Print the results
    print(bit_value, num_set, num_clear)
    
bitManipulation(8, 1)