'''Change case of all characters in a .txt file using Python'''
with open('data.txt', 'r') as data_file:
    
    # open output.txt file in append mode
    with open('output.txt', 'a') as output_file:
        
        # read each line from data.txt
        for line in data_file:
            
            # change case for the line and write
            # it into output file
            output_file.write(line.upper())