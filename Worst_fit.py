def worst_fit(block_sizes, process_sizes):
    """
    Allocates memory to processes using the Worst Fit Algorithm.

    Parameters:
    block_sizes (list): A list of available block sizes.
    process_sizes (list): A list of process sizes to be allocated.

    Returns:
    list: Allocation status of each process, where -1 indicates no allocation.
    """
    # Initialize allocation list to store which block each process is allocated to
    allocation = [-1] * len(process_sizes)

    # Iterate over each process to allocate memory
    for i in range(len(process_sizes)):
        worst_index = -1

        # Find the index of the largest block that can fit the process
        for j in range(len(block_sizes)):
            if block_sizes[j] >= process_sizes[i]:
                if worst_index == -1 or block_sizes[j] > block_sizes[worst_index]:
                    worst_index = j

        # If a suitable block is found, allocate it to the process
        if worst_index != -1:
            allocation[i] = worst_index
            block_sizes[worst_index] -= process_sizes[i]

    return allocation

# Program to get inputs dynamically
if __name__ == "__main__":
    # Input number of blocks and their sizes
    num_blocks = int(input("Enter the number of memory blocks: "))
    block_sizes = []
    print("Enter the sizes of each block:")
    for _ in range(num_blocks):
        block_sizes.append(int(input()))

    # Input number of processes and their sizes
    num_processes = int(input("Enter the number of processes: "))
    process_sizes = []
    print("Enter the sizes of each process:")
    for _ in range(num_processes):
        process_sizes.append(int(input()))

    # Allocate processes using the Worst Fit Algorithm
    allocation = worst_fit(block_sizes, process_sizes)

    # Print the allocation result
    print("\nProcess No.  Process Size  Block No.")
    for i in range(len(process_sizes)):
        print(f"{i + 1}            {process_sizes[i]}            {allocation[i] + 1 if allocation[i] != -1 else 'Not Allocated'}")
