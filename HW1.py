import json
import math
from sys import argv

def load_journal(filename):
    """
    Load journal data from a JSON file.
    
    Args:
        filename (str): The name of the file to load the data from.
        
    Returns:
        list: A list of journal entries.
    """
    open_file = open(filename)
    data = json.load(open_file)
    open_file.close()
    return data

def compute_phi(journal, event):
    """
    Compute the phi correlation for a given event in the journal.
    
    Args:
        journal (list): A list of journal entries.
        event (str): The event to compute the correlation for.
        
    Returns:
        float: The phi correlation value.
    """
    n11 = n00 = n10 = n01 = 0  # Initialize counts
    for entry in journal:
        event_happened = event in entry['events']
        squirrel_happened = entry['squirrel']
        if event_happened and squirrel_happened:
            n11 += 1
        elif not event_happened and not squirrel_happened:
            n00 += 1
        elif event_happened and not squirrel_happened:
            n10 += 1
        elif not event_happened and squirrel_happened:
            n01 += 1

    # Calculate intermediate sums
    n1_plus = n11 + n10
    n0_plus = n00 + n01
    n_plus_1 = n11 + n01
    n_plus_0 = n00 + n10

    # Compute phi coefficient
    return ((n11 * n00) - (n10 * n01)) / (math.sqrt(n1_plus * n0_plus * n_plus_1 * n_plus_0))

def compute_correlations(filename):
    """
    Compute the phi correlations for all events in the journal.
    
    Args:
        filename (str): The name of the file to load the data from.
        
    Returns:
        dict: A dictionary with events as keys and their phi correlation as values.
    """
    journal = load_journal(filename)
    event_correlations = {}
    for dictionary in journal:
        items = list(dictionary.items())
        if items:  
            first_value = items[0][1]  # Extract the first value from the dictionary items
            for event in first_value: 
               event_correlations[event] = compute_phi(journal, event)
    
    return event_correlations

def diagnose(filename):
    """
    Diagnose the most and least correlated events in the journal.
    
    Args:
        filename (str): The name of the file to load the data from.
        
    Returns:
        tuple: A tuple containing the most positively correlated event, 
               its correlation value, the most negatively correlated event,
               and its correlation value.
    """
    correlations = compute_correlations(filename)
    print(correlations)
    my_values = []
    for value in correlations:
        my_values.append(correlations[value])

    # Find maximum and minimum correlation values
    max_value = max(my_values)
    min_value = min(my_values)
    max_key = None
    min_key = None
    for key, value in correlations.items():
      if value == max_value:
         max_key = key
         break
    for key, value in correlations.items():
      if value == min_value:
         min_key = key
         break  
    return max_key, max_value, min_key, min_value

if __name__ == "__main__":
    # Extract the filename from command line arguments
    script, filename = argv
    # Run the diagnosis and print the results
    most_positive, pos_corr, most_negative, neg_corr = diagnose(filename)
    print(f"Most positively correlated event: {most_positive} with correlation {pos_corr}")
    print(f"Most negatively correlated event: {most_negative} with correlation {neg_corr}")
