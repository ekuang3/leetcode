import pandas as pd

class DataTransformer:
    def __init__(self, data):
        """
        Initializes the DataTransformer with a DataFrame.
        
        Parameters:
        - data (pd.DataFrame): The data to transform.
        """
        self.data = data

    def drop_missing(self, columns=None):
        """
        Drops rows with missing values in specified columns.
        
        Parameters:
        - columns (list): List of columns to check for missing values.
        
        Returns:
        - pd.DataFrame: DataFrame with missing values dropped.
        """
        self.data = self.data.dropna(subset=columns) if columns else self.data.dropna()
        return self.data

    def fill_missing(self, columns=None, fill_value=0):
        """
        Fills missing values in specified columns with a given value.
        
        Parameters:
        - columns (list): List of columns to fill missing values in.
        - fill_value (any): Value to replace missing values with.
        
        Returns:
        - pd.DataFrame: DataFrame with missing values filled.
        """
        self.data = self.data.fillna({col: fill_value for col in columns}) if columns else self.data.fillna(fill_value)
        return self.data

    def rename_columns(self, column_mapping):
        """
        Renames columns based on a given mapping.
        
        Parameters:
        - column_mapping (dict): A dictionary mapping old column names to new names.
        
        Returns:
        - pd.DataFrame: DataFrame with columns renamed.
        """
        self.data = self.data.rename(columns=column_mapping)
        return self.data

    def filter_rows(self, condition):
        """
        Filters rows based on a given condition.
        
        Parameters:
        - condition (pd.Series): Boolean condition to filter rows.
        
        Returns:
        - pd.DataFrame: Filtered DataFrame.
        """
        self.data = self.data[condition]
        return self.data

    def sort_data(self, columns, ascending=True):
        """
        Sorts data by specified columns.
        
        Parameters:
        - columns (list): List of columns to sort by.
        - ascending (bool or list): Sort order (True for ascending, False for descending).
        
        Returns:
        - pd.DataFrame: Sorted DataFrame.
        """
        self.data = self.data.sort_values(by=columns, ascending=ascending)
        return self.data

    def add_column(self, column_name, data):
        """
        Adds a new column with the specified data.
        
        Parameters:
        - column_name (str): Name of the new column.
        - data (pd.Series or list): Data for the new column.
        
        Returns:
        - pd.DataFrame: DataFrame with the new column added.
        """
        self.data[column_name] = data
        return self.data

    def get_summary_statistics(self):
        """
        Returns a summary of statistics for the numerical columns in the data.
        
        Returns:
        - pd.DataFrame: Summary statistics of numerical columns.
        """
        return self.data.describe()

    def get_data(self):
        """
        Returns the transformed DataFrame.
        
        Returns:
        - pd.DataFrame: Transformed DataFrame.
        """
        return self.data
    
    def get_size_of_data(self):
        """
        Returns size of DataFrame.
        
        Returns:
        - (row, column)
        """
        return self.data.shape
    
if __name__=='__main__':

    # Sample data
    data = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, 27, None, 22],
        'Salary': [50000, 54000, None, 45000]
    })

    # Initialize the transformer
    transformer = DataTransformer(data)

    # Fill missing values in 'Age' with the average age
    transformer.fill_missing(columns=['Age'], fill_value=data['Age'].mean())

    # Drop rows where 'Salary' is missing
    transformer.drop_missing(columns=['Salary'])

    # Rename 'Name' column to 'EmployeeName'
    transformer.rename_columns({'Name': 'EmployeeName'})

    # Filter rows where Age is greater than 23
    transformer.filter_rows(transformer.data['Age'] > 23)

    # Sort data by 'Salary'
    transformer.sort_data(columns=['Salary'])

    # Add a new column 'Department'
    transformer.add_column('Department', 'General') # add one
    transformer.add_column('Department', ['HR', 'Engineering']) # add multiple

    # Get summary statistics
    print(transformer.get_summary_statistics())

    # Get transformed data
    print(transformer.get_data())

    # Get size of data
    print(transformer.get_size_of_data())