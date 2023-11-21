# Basick


COMPILER DETAILS

Basick is a compiler designed as part of a college course on compiler design. This compiler focuses on simplicity and serves as an educational tool for understanding the fundamental concepts of language translation. The name "Basick" reflects its core design philosophy, emphasizing basic functionalities for calculations while allowing room for continuous expansion with additional features.
Key Features The Basick compiler includes essential components such as a lexer, parser, and basic abstract syntax tree (AST) nodes. It currently supports arithmetic expressions, including addition, subtraction, multiplication, and division. The compiler is extensible, enabling the constant addition of new functions and features to enhance its capabilities.
Compiler Components:
Lexer and Parser: The lexer tokenizes input source code, identifying numbers, operators, and other language elements. The parser generates an AST from the tokenized code, capturing the syntactic structure.
Abstract Syntax Tree (AST): Basick’s AST represents the parsed code structure, comprising nodes for numbers, binary operations, and variables.
Basic Functions: The compiler supports basic mathematical operations, making it suitable for simple calculations and mathematical expressions.
Educational Purpose: As a compiler designed for a college course, Basick aims to provide students with hands-on experience in building a compiler. It simplifies complex concepts, making them accessible for learners while fostering a deeper understanding of language translation and compiler construction.
Future Development: Given its extensible nature, Basick serves as a starting point for students to explore advanced compiler concepts. The intention is to continually enhance the compiler by incorporating more sophisticated features, optimization techniques, and support for a broader range of programming constructs.

In summary, Basick is a compiler crafted for educational purposes, offering a foundational understanding of compiler design principles. It provides a stepping stone for students to delve into the intricacies of language translation while allowing for ongoing development and expansion.


Table of Contents
COMPILER DETAILS	2
Compiler Basics	5
Problem Statement	5
Background	5
Motivation/Need for the Compiler	5
Objective:	5
Sub-Objectives	5
Methodology	5
Theoretical Framework	6
Standard Math Functions:	6
Trigonometric Functions (if applicable):	7
Additional Math Functions:	8
Schematic Flow Diagram:	9
Review of Literature	12
Key Bibliography:	12














List of Figures
Symbol table 
Process flow diagram 
List of functions
Lex functions  
Parse code 
Sematic Analysis
 


Compiler Basics
Problem Statement: Developing a Modular Compiler for College Course - Compiler Design
Background: In the realm of programming, compilers play a pivotal role by translating high-level source code into machine-readable instructions. Understanding the fundamentals of compiler design is crucial for software developers and computer science students.
Motivation/Need for the Compiler: The growing complexity of software applications necessitates efficient translation from human-readable code to machine-executable instructions. A compiler serves as a bridge between high-level programming languages and the low-level instructions executed by a computer.
Objective: To develop a comprehensive understanding of compiler basics, encompassing lexical analysis, syntax analysis, semantic analysis, and code generation, laying the foundation for creating efficient compilers.
Sub-Objectives:
1.	Explore the theoretical foundations of compiler design.
2.	Implement a basic compiler with modular components.
3.	Understand the importance of lexical, syntax, and semantic analysis.
4.	Grasp the principles of intermediate code generation and optimization.
Mode of Achieving Objective: Engage in a structured learning approach involving theoretical study, practical implementation, and hands-on exercises to reinforce concepts. Appled knowledge through the creation of a simple compiler to solidify comprehension.
Methodology: Combine theoretical study with practical implementation. Utilize educational resources, hands-on exercises, and a step-by-step approach to gradually build a basic compiler. Emphasize learning through application and experimentation.
 
Theoretical Framework: The theoretical framework revolves around foundational concepts in compiler design, including lexical analysis, parsing techniques, semantic analysis, intermediate code representation, and optimization strategies. Key theories include finite automata, context-free grammars, and compiler construction principles.
Sources of Data: Primarily rely on academic textbooks, research papers, and online educational materials. Combine theoretical knowledge with practical application to reinforce learning.
 
Around 50 functions consisting in lex code 
Standard Math Functions:
1.	add(x, y)
•	Description: Adds two numbers.
•	Parameters: x and y - the numbers to be added.
•	Return: The sum of x and y.
2.	subtract(x, y)
•	Description: Subtracts one number from another.
•	Parameters: x - the minuend, y - the subtrahend.
•	Return: The result of subtracting y from x.
3.	multiply(x, y)
•	Description: Multiplies two numbers.
•	Parameters: x and y - the numbers to be multiplied.
•	Return: The product of x and y.
4.	divide(x, y)
•	Description: Divides one number by another.
•	Parameters: x - the dividend, y - the divisor.
•	Return: The result of dividing x by y.
5.	power(base, exponent)
•	Description: Raises a number to a specified power.
•	Parameters: base - the base number, exponent - the power to which base is raised.
•	Return: The result of raising base to the power of exponent.
6.	sqrt(x)
•	Description: Calculates the square root of a number.
•	Parameters: x - the number for which the square root is calculated.
•	Return: The square root of x.
Trigonometric Functions (if applicable):
7.	sin(angle)
•	Description: Calculates the sine of an angle.
•	Parameters: angle - the angle in radians.
•	Return: The sine of the given angle.
8.	cos(angle)
•	Description: Calculates the cosine of an angle.
•	Parameters: angle - the angle in radians.
•	Return: The cosine of the given angle.
9.	tan(angle)
•	Description: Calculates the tangent of an angle.
•	Parameters: angle - the angle in radians.
•	Return: The tangent of the given angle.
Additional Math Functions:
10.	abs(x)
•	Description: Returns the absolute value of a number.
•	Parameter: x - the number.
•	Return: The absolute value of x.
11.	log(x)
•	Description: Returns the natural logarithm of a number.
•	Parameter: x - the number.
•	Return: The natural logarithm of x.
12.	exp(x)
•	Description: Calculates the exponential function e^x.
•	Parameter: x - the exponent.
•	Return: e raised to the power of x.
•	 

Schematic Flow Diagram:
1.	Theoretical Study: Understand compiler basics, including lexical and syntax analysis, semantic checks, and code generation.
2.	Practical Implementation: Apply theoretical knowledge to create a simple compiler, focusing on modularity and extensibility.
3.	Testing and Optimization: Develop test cases, perform debugging, and explore basic optimization techniques.
4.	Documentation: Prepare comprehensive documentation detailing the compiler's design, implementation, and usage.
 
Report on Provided Python Script

1. Imports:
•	The script imports a custom module named strings_with_arrows, suggesting potential functionality for displaying code with arrow annotations for error messages.
2. Constants:
•	The script defines the constant DIGITS to represent the digits '0' through '9'.
3. Errors:
•	The script includes a base Error class and specific error classes (IllegalCharError and InvalidSyntaxError) for handling different types of errors during parsing.
4. Position Class:
•	The Position class is responsible for tracking the current position (line, column, and index) in the source code. It also handles advancing the position based on the current character.
5. Tokens:
•	Token types (e.g., TT_INT, TT_PLUS) are defined.
•	The Token class represents a token with type, value, and position information.
•	Token instances are created during lexical analysis.
6. Lexer:
•	The Lexer class tokenizes the input text, identifying integers, floats, and basic arithmetic operators.
•	It skips whitespaces and handles parentheses.
•	Lexical errors are reported using the IllegalCharError class.
7. Nodes:
•	The script defines nodes for the Abstract Syntax Tree (AST).
•	Node classes include NumberNode, BinOpNode, UnaryOpNode, VarAccessNode, and VarAssignNode.
8. ParseResult Class:
•	The ParseResult class is responsible for tracking parsing results, including errors and AST nodes.
•	It includes methods for registering results, marking success, and marking failure.
9. Parser:
•	The Parser class handles the parsing of statements, expressions, and variable assignments.
•	Parsing methods include factor, term, expr, var_access, var_assign, statement, and statements.
•	Statements can include variable assignments (var x = 5) and arithmetic expressions.
10. Run Function:
•	The run function orchestrates the entire process, from lexing to parsing.
•	It returns the AST node and any encountered errors.
11. Enhancements:
•	The script has been enhanced to include variable assignments and accesses in addition to basic arithmetic expressions.
•	Support for multiple statements and variable declarations is evident.
12. Recommendations:
•	Consider expanding the language features and functionalities, such as adding support for control flow statements (if, else).
•	Enhance the error reporting mechanism for better debugging and user feedback.
•	 
Conclusion:
The provided script serves as a foundation for a simple expression language with variables. It includes a lexer and parser that can handle basic arithmetic expressions, variable assignments, and variable accesses. Further development can extend the language's capabilities and improve the overall user experience.
Please note that this report provides an overview based on the provided code snippets, and further details about the language's intended features and use cases would be beneficial for a more detailed analysis.

Semantic analysis involves checking the meaning of statements and expressions in a program. It ensures that the code adheres to the language's semantic rules beyond basic syntax. For the given script, we can perform semantic analysis by adding functionality to the existing nodes and parsing logic. Below is an extended version of the script with semantic analysis:
 
In this extension, semantic analysis is added to the parser. The Context class is introduced to maintain a symbol table for variable declarations. The parser now checks if a variable has already been declared before allowing a new declaration. Additional semantic analysis rules can be added based on the language's requirements.

Review of Literature
: Explore key works in compiler design, including:
1.	"Compilers: Principles, Techniques, and Tools" by Aho, Lam, Sethi, and Ullman.
2.	"Modern Compiler Implementation in Java" by Andrew W. Appel.
3.	Academic papers on lexical analysis, parsing algorithms, and code optimization.
Key Bibliography:
1.	Aho, Alfred V., et al. "Compilers: Principles, Techniques, and Tools."
2.	Appel, Andrew W. "Modern Compiler Implementation in Java."
3.	Cooper, Keith D., and Linda Torczon. "Engineering a Compiler."


