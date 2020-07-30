import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Gaussian(Distribution):
    """ Gaussian distribution class for calculating and visualizing a
    Gaussian distribution.
    
    Attributes:
        mean (float) represnting the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from a data file
    """
    
    def __init__(self, mean=0, sdev=1):
        
        Distribution.__init__(self, mean, sdev)
        
    def calculate_mean(self):
        """ Function to calculate the mean of the data set.
        
        Args:
            None
        
        Returns:
            (float) mean of the data set
            
        """
        
        mean = (1.0*sum(self.data))/len(self.data)
        
        self.mean = mean
        
        return self.mean
        
    def calculate_stdev(self, sample=True):
        
        """ Function to calculate the standard deviation of the data set.
        
        Args:
            sample (bool): whether the data represents a sample or a population
            
        Returns:
            (float) standard devaition of the data set
        
        """
        
        n = len(self.data)
        
        if sample:
            n -= 1
        
        mean = self.mean
        
        sdev = 0
        
        for data in self.data:
            sdev += (data - mean) ** 2
        
        sdev = math.sqrt(sdev/n)
        
        self.stdev = sdev
        
        return self.stdev
        
    def read_data_file(self, file_name, sample = True):
        
        """Function to read in data from a text file. The text file should have one
        number (float) per line. The numbers are stored in the data attribute.
        After reading in the file, the mean and standard deviation are calculated for the given data.
        
        Args:
            file_name (string): name of a file to read from
            
        Returns:
            None
        """
        
        with open(file_name) as file:
            data_list = []
            number = file.readline()
            while number:
                data_list.append(float(line))
                line = file.readline()
        file.close()
        
        self.data = data_list # Could I have simply used Distribution.read_data_file for this part?
        
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample)
        
    def plot_histogram(self):
        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.
        
        Args:
            None
        
        Returns:
            None
        """
        plt.hist(self.data)
        plt.title('Histogram of data')
        plt.xlabel('Data')
        plt.ylable('Counts')
        
    def pdf(self, x):
        """Probability density function for the Gaussian distribution.
        
        Args:
            x (float): point for calculating the probability density function
            
        Returns:
            float: probability density function output
        """
        
        sdev = self.stdev
        mean = self.mean
        
        return (1/(math.sqrt(2*math.pi*(sdev**2))))*math.exp(-((x-mean)**2)/(2*(sdev**2)))
        
    def plot_histogram_pdf(self, n_spaces = 50):
        """Function to plot the normalized histogram of the data and a plot of the probability
        density function (pdf) along the same range.
        
        Args:
            n_spaces (int): number of data points (Default = 50)
            
        Returns:
            (list) x values for the pdf plot
            (list) y values for the pdf plot
        """
        
        mean = self.mean
        
        sdev = self.stdev
        
        min_range = min(self.data)
        max_range = max(self.data)
        
        # calculates the interval between x values
        interval  = 1.0 * (max_range - min_range) / n_spaces
        
        x = []
        y = []
        
        # calculate the x values to visualize
        for i in range(n_spaces):
            temp = min_range + interval*i
            x.append(temp)
            y.append(self.pdf(temp))
            
        # make the plots
        fig, axes = plt.subplots(2, sharex=True)
        fig.subplots_adjust(hspace=0.5)
        axes[0].hist(self.data, density = True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_label('Density')
        
        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[1].set_ylable('Density')
        plt.show()
        
        return x, y
        
    def __add__(self, other):
        """Function to add two Gaussian distributions.
        
        Args:
            other (Gaussian): Gaussian instance
        
        Returns:
            Gaussian: Gaussian Distribution
        
        """
        
        result = Gaussian()
        result.mean = self.mean + other.mean
        result.stdev = math.sqrt(self.stdev ** 2 + other.stdev ** 2)
        
        return result
        
    def __repr__(self):
        """Function to output the characteristics of the Gaussian instance.
        
        Args:
            None
            
        Returns:
            string: characteristics of the Gaussian
        
        """
        
        return "mean {}, standard deviation {}".format(self.mean, self.stdev)
