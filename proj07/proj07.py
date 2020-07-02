#!/usr/bin/env python3
# -*- coding: utf-8 -*-

    ###########################################################
    #  Project #7
    #
    #     Searches news documents based on search terms provided
    #     by user and returns relevant documents. 
    #     News documents are in given files 
    #
    ###########################################################

# imports
import string

# constants


def file_separator(file):
    '''
    Reads a file with news documents strung together and returns a list of
    those documents separated and with their respective texts.

    Parameters
    ----------
    file : string
        Name of the news documents file

    Returns
    -------
    docs_list : list
        List with documents separated, numbered, and with associated text

    '''
    
    # Open the file 
    try:
        fp = open(file, "r" )    
        
    except IOError:
        print( "Unable to find documents. Please check file location" )
     
    
    # Separates the documents file
    # Beginning arguments
    docs_list = doc = []
    doc_counter = 0
    doc_text = ""    
    
    # For each line in file
    for line in fp:
        line = line.strip()
        
        # If start of a new document, initialize new set, append old one
        if line == "<NEW DOCUMENT>":
            if doc_counter != 0:
                doc.append(doc_text)
                docs_list.append(doc)
            
            doc_text = ""
            doc_counter += 1
            doc = [doc_counter]
        
        # Otherwise, add the new line to the document's text
        else:
            if doc_text == "":
                doc_text += "{}".format(line)  
            else:
                doc_text += "\n{}".format(line)
    
    # At the end of the file, add in the last document
    doc.append(doc_text)
    docs_list.append(doc)
    
    return docs_list


def make_searchdict(docs_list):
    '''
    Reads the text of docs in the list and indexes the words they contain
    based on which number doc they are in.

    Parameters
    ----------
    docs_list : list
        List of documents to be scanned for words and indexed

    Returns
    -------
    search_dict : dictionary
        List of words and which documents they are in

    '''
    search_dict = dict()
    
    # For each document in the document list
    for doc in docs_list:
        
        # Get the document number and split the words in the text
        doc_number = doc[0]
        doc_words = doc[1].split()
        
        # Then, for every word in the text
        for word in doc_words:
            
            # Remove carriage returns, punctuation, and capitals
            if "\n" in word:
                word.replace("\n","")
            
            word = word.translate(str.maketrans('', '', string.punctuation))
            word = word.lower()
            
            # Add the word with doc number in dictionary if not present,
            # if present in dictionary, just add the doc number to entry
            if word in search_dict:
                search_dict[word].add(doc_number)
            else:
                search_dict[word] = {doc_number}
                
    return search_dict



def match_docs(search_terms, search_dict):
    '''
    Uses the search dictionary and looks up matches between provided 
    search terms and documents in file. Gives back the document numbers

    Parameters
    ----------
    search_terms : string
        String of search terms inputted by user.
        
    search_dict : dictionary
        Dictionary where terms are looked for and sets taken from

    Returns
    -------
    matching_docs : set
        Set of docs that match the search terms

    '''
    matching_docs = set()
    
    # Isolate individual search terms
    terms = search_terms.split()
    
    # For each search term
    for term in terms:
        
        # Remove punctuation and lowercase 
        term = term.translate(str.maketrans('', '', string.punctuation))
        term = term.lower()

        
        # If term is in the dictionary, get the set of documents it's in
        if term in search_dict:
            found_set = search_dict[term]
            
            # If it's the first search term, the set of docs is the found set
            if matching_docs == set():
                for doc in found_set:
                    matching_docs.add(doc)
                    
            # Otherwise, find the intersection between the old and new sets
            else:
                matching_docs = matching_docs & found_set
               
    
    return matching_docs



def main():
    
    # Initialize files and search dictionary
    docs_list = file_separator("ap_docs.txt")
    search_dict = make_searchdict(docs_list)

        
    # Program user options 
    end = False
    while end == False:
        
        # User menu decision
        user_decision = input("""
What would you like to do? 

1. Search for documents
2. Read document
3. Quit program
> """)
        
        # Option 1: Search for documents
        if user_decision == "1":
            
            # Ask for search terms and find them
            user_search = input("Enter search terms: ")
            matching_docs = match_docs(user_search, search_dict)
            
            # Display documents if available
            if matching_docs != set():
                print("Documents fitting search: ")
                for number in matching_docs:
                    print("{} ".format(number))
            else:
                print("No documents match your search")
          
                
        # Option 2: Read document        
        elif user_decision == "2":
            
            # Ask for which document to read
            doc_read = input("Enter document number: ")
            
            # Print to terminal
            for doc in docs_list:
                if doc[0] == int(doc_read):
                    print("\n")
                    print("---------------------------------------")
                    print(doc[1])
                    print("---------------------------------------")
                    print("\n")
        
        # Option 3: Quit
        elif user_decision == "3":
            end = True
        
        # Bad decision
        else:
            print("Please enter a valid input (1, 2, or 3)!")
    
    
    


if __name__ == "__main__":
    main()