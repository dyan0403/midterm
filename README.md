Check similarity tools

Classes in project:

    Class Preprocessor:
    Task: preprocess code, remove unwanted characters or lines.
    


    Class PythonPreprocessor: Inherit from class Preprocessor
    
    Task: Override method preprocess() to remove comments, blank lines and docstrings.
    


    Class JavaPreprocessor: Inherit from class Preprocessor
    
    Task: Override method preprocess() to remove comments, blank lines and Javadoc comments.
    
    

    Class CppPreprocessor: Inherit from class Preprocessor
    
    Task: Override method preprocess() to remove comments, blank lines and string literals.
    
    

    Class CodeComparator:
    
    Task: Compare 2 codes and calculate their similarity.
    
    Method compare() returns the similarity score as a float value between 0 and 100.
    
   

    Class ComparatorFactory:
    
    Task: Create CodeComparator object with appropriate Preprocessor based on the input programming language.
    
    Method create() returns a CodeComparator object.
    


Files in project:

preprocessor.py: Store class Preprocessor and its subclasses, namely PythonPreprocessor, JavaPreprocessor, and CppPreprocessor.

comparator.py: store class CodeComparator 

comparator_factory.py: store class ComparatorFactory

main.py: tool's command lines 

