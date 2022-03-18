# Code-Summary-Audio-Python
Using Mantium AI writing a code summary package that explains the code pieces via audio while looking at another piece of a code project.

In general there are two types of summarization, abstractive and extractive summarization.

Abstractive Summarization: Abstractive methods select words based on semantic understanding, even those words did not appear in the source documents. It aims at producing important material in a new way. They interpret and examine the text using advanced natural language techniques in order to generate a new shorter text that conveys the most critical information from the original text.

In this case semantic understanding of code involved the a number of rules for now declaring n > 5

2. Extractive Summarization: Extractive methods attempt to summarize articles by selecting a subset of words that retain the most important points.

This means weighting classes in a package by importance: x usage times of Classname, consumption of threading, expected consumption of process.

Abstractive summarization methods cope with problems such as semantic representation

The other factors of semantic representation may include:

Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them.

Build a similarity matrix of modules, and then classes in a package

The equivalent to stop words in programming templating are declarations.

Building a similarity matrix, stop words are declarations, and when assessing block, line, and statement similarity the program must assess which products are precursors to steps in the program. Then order and display intelligently to assess where a program begins and ends.

You can also inject CRUD blocks into a program to assess where a program can be stopped and then continued to assess execution flow.

def build_similarity_matrix(sentences, stop_words):
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
 
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2: #ignore if both are same sentences
                continue 
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)return similarity_matrix

### To use OpenPrompt for this task.

Determine the classes and the InputExample of the task.

classes will be in this case Python reserved words.

``` # in abstract analysis tokens will be assigned to reserved word classes. There are a few more classes, for now count occurences
classes = [
"and" "exec" "not"
"assert" "finally" "or"
"break" "for" "pass"
"class" "from" "print"
"continue" 	"global" "raise"
"def" "if" "return"
"del" "import" "try"
"elif" "in" "while"
"else" "is" "with"
"except" "lambda" "yield"
]
```
[ ] Mantium AI count occurrences of class instantiations
[ ] Mantium AI chain entry point of program task call (method call) and output order of methods called
[ ] Mantium AI confirm that all method calls are counted
[ ] Mantium AI which reads python code in ordered fashion audio
