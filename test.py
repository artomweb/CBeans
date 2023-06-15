def partition_into_0_5_increments(number):
    partitions = []
    
    if number % 0.5 != 0:
        return partitions
    
    def partition_recursive(number, current_partition, partitions):
        if number == 0:
            partitions.append(current_partition.copy())
            return
        
        if number < 0 or number < 0.5:
            return
        
        # Case when the remaining number is a whole number
        if number % 0.5 == 0:
            current_partition.append(number)
            partition_recursive(0, current_partition, partitions)
            current_partition.pop()
        else:
            for i in range(1, int(number / 0.5) + 1):
                current_partition.append(0.5)
                partition_recursive(number - i * 0.5, current_partition, partitions)
                current_partition.pop()
    
    partition_recursive(number, [], partitions)
    return partitions


partitions = partition_into_0_5_increments(1)
print(partitions)
