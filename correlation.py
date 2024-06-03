import json
from math import sqrt
from sys import argv
script, json_file = argv

def load_journal(json_file):
    file = open(json_file)
    file_content = file.read()
    data = json.loads(file_content)
    return data
 

def compute_phi(journal_file, event):
    n_11, n_00, n_10, n_01 = 0, 0, 0, 0
    
    for i in journal_file:
        # print("i of event is :",i["events"])
        if event in i['events'] and i['squirrel'] == True:
            n_11 += 1  # Both event and squirrel transformation happened
        elif event not in i['events'] and i['squirrel'] == False:
            n_00 += 1  # Neither event nor squirrel transformation happened
        elif event in i['events'] and i['squirrel'] == False:
            n_10 += 1  # Event happened but squirrel transformation didn't
        elif event not in i['events'] and i['squirrel'] == True:
            n_01 += 1  # Squirrel transformation happened but event didn't
    
    phi = (n_11 * n_00 - n_10 * n_01) / sqrt((n_11 + n_10) * (n_01 + n_00) * (n_11 + n_01) * (n_10 + n_00))
    
    return phi


def compute_correlations():
    journal_file = load_journal(json_file)
    events = set()
    correlations = {}
    for i in journal_file:                  # here i iterates through all keys and values in journal.json file
        # next we are adding all the events to "events" variable, which is a set datatype so all events will placed must be unique
        events.update(i["events"])         
        # now we get, all unique events, inside the journal.json file

    # now i'm iterates through all events and pass that event as a functional argument to compute_phi(....), 
    # after that each of the events will go to that function and check the condition and calculate its phi and returns the value
    # and that value will store in the dictionary which we created as empty "correlations"{correlations[i]} - store as key, phi - store as a value).
    for i in events:
        correlations[i] = compute_phi(journal_file, i)   

    return correlations


def diagnose():
    correlations = compute_correlations()

    print("correlations is ", correlations)
    most_positive_event = ""
    most_negative_event = ""
    max_correlation = -1  # Start with a minimum possible correlation
    min_correlation = 1   # Start with a maximum possible correlation

    for event, correlation in correlations.items():
        print(f"Correlation for event '{event}': correlation {correlation}")
        if correlation > max_correlation:
            max_correlation = correlation
            most_positive_event = event
        
        if correlation < min_correlation:
            min_correlation = correlation
            most_negative_event = event

    return most_positive_event, most_negative_event, max_correlation, min_correlation


if __name__ == "__main__":
    print("diagnose",diagnose())
    most_positive, most_negative, max_correlation, min_correlation = diagnose()
    print("Most positive event:", most_positive, "correlation:",max_correlation)
    print("Most negative event:", most_negative, "correlation:",min_correlation)