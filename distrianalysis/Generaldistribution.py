class Distribution:

    def __init__(self, mean = 0, sdev = 0):
        """Generic distribution class for calculating and
        visualizing a probability distribution.
        
        Attributes:
            mean (float) representing the mean value of the distribution
            stdev (float) representing the standard deviation of the distribution
            data_list (list of floats) a list of floats extracted from the data file
        """
        
        self.mean = mean
        self.stdev = sdev
        self.data = []
        
        
    def read_data_file(self, file_name):
    
        """Function to read in data from a text file. The text file should have
        one number (float) per line. The numbers are stored in the data attribute.
        
        Args:
            file_name (string): name of a file to read from
            
        Returns:
            None
        """
        
        with open(file_name) as file:
            data_list = []
            number = file.readline()
            while number:
                data_list.append(float(number))
                number = file.readline()
            file.close()
            
            self.data = data_list
