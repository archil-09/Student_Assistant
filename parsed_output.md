## INTERNATIONAL INSTITUTE OF PROFESSIONAL STUDIES, DEVI AHILYA UNIVERSITY, INDORE

## M. Tech. (IT) 5 Years Batch - IT-2K23 Semester - IV

January-May 2025

Syllabus

<!-- image -->

## INTERNATIONAL INSTITUTE OF PROFESSIONAL STUDIES

## DEVI AHILYA UNIVERSITY, INDORE

## M. Tech. (IT) 5 Years

Batch - IT-2K23

## Semester - IV

January-May 2025

## Subject Credits

| Sub. Code   | Subject Name                    | L       | T       | P       |   C |
|-------------|---------------------------------|---------|---------|---------|-----|
| IT-401C     | Computer Architecture           | 3       | 1       | 0       |   4 |
| IT-402A     | Numerical Analysis & Design     | 3       | 1       | 0       |   4 |
| IT-403B     | Database Management Systems     | 3       | 1       | 0       |   4 |
| IT -404A    | System Programming              | 3       | 1       | 0       |   4 |
| IT-405B     | Python Programming              | 3       | 1       | 0       |   4 |
| IT-407B     | Database Management Systems Lab | 0       | 0       | 4       |   2 |
| IT-410      | Python Programming Lab          | 0       | 0       | 4       |   2 |
| IT-408      | Comprehensive Viva              | 0       | 0       | 0       |   4 |
| Total =     | Total =                         | Total = | Total = | Total = |  28 |

## Course Type: - Core Course Credits - 4 Theory

Course Objectives: to understanding historical developments, fundamental principles, and advanced concepts in computer architecture and organization. By exploring performance measurement metrics, memory hierarchy optimization, instruction sets, pipeline design, parallel computing, and emerging trends topics, students will develop the knowledge and skills necessary for careers in research, development, and innovation in computer systems design.. Course Outcomes - After completion of the course, student will; CO1: Differentiate between computer architecture and organization, and understand their interrelationship.. CO2: Able to analyze and evaluate the performance of computer systems using metrics such as throughput, latency, and scalability. Recognize the factors affecting system performance and strategies for optimization CO3: Able to design cost effective memory for a computer system with good performance. CO4:Explore emerging trends and challenges in computer architecture, also the advanced techniques for improving CPU performance, such as pipelining, superscalar execution, and out-of-order execution. . Acquire knowledge of instruction set architecture (ISA) design, including various instruction formats, addressing modes, and how

they impact CPU operations.

## Course Contents -

|   Unit No | Title                       | Contents                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |   Hr | Targeted Levels of Blooms T. (Q1)   | Content and Pedagogy (Q2)     | (Q3) Online Resource s   | (Q4) Assign./ Assessment/D iscussion                                      |
|-----------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|-------------------------------------|-------------------------------|--------------------------|---------------------------------------------------------------------------|
|         1 | Introduction and vocabulary | History of computer architecture, Overview of computer organization, Difference between Computer architecture & organization, von Neumann/Turing, IBM 360 series, Moore's law, Performance measurement: IPC, CPI, MIPS, Amdahl's law, CPU performance equation, Speeding it up, Performance Mismatch& Solutions, Instruction cycle, Interrupt cycle, Bus interconnections: Types, Arbitration, PCI. LO1: illustrate the historical development and evolution of computer architecture and organization.Explore the role of computer architecture and computer organization in designing/implementing computer system. LO2: Able to apply Amdahl's Law to analyze the potential speedup in a computer system and use the CPU performance equation to estimate overall performance. |    6 | 1,2,3                               | Book1,4 (Lecture, numerical ) |                          | Assign: practice questions for implementing laws and performance metrics. |

## Subject Name - Computer Architecture

|   2 | Processor organization         | CPU Structure, Registers, User Visible Registers, General Purpose Registers, accumulator organization, general register organization, stack organization of CPU, High level issues in CPU design LO1Evaluate the significance of user-visible registers and general-purpose registers in CPU design, recognizing their roles in executing instructions, managing data, and optimizing performance in various computing tasks.                                                                                                                                                                                                     |   4 | 1,2,3    | Book 2,3 (Lecture, numerical )   | Assign: practice questions                                        |
|-----|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|----------|----------------------------------|-------------------------------------------------------------------|
|   3 | Memory                         | Location, Capacity, Unit of transfer, Access method, Performance (Access, cycle, transfer rate), Physical type (semi conductor or magnetic), Physical characteristics (volatile, erasable etc.), Locality of references, Cache mapping techniques, Cache write policies, Cache initialization, External memory, RAID organization of hard disks. LO1: Analyze the characteristics of different memory types, LO2: Evaluate cache mapping techniques, write policies, and initialization methods, along with RAID organization principles, to design efficient memory hierarchies and improve system performance and reliability.. |   6 | 1, 2,3,4 | Book 1,2,3 (Lecture, numerical ) | Assign: practice and assignment questions on cache memory         |
|   4 | Input/Output:                  | Programmed I/O, Interrupt Driven I/O, Direct Memory Access. Representing information digitally, Byte Ordering: Big-Endian & Little-Endian. Instruction sets, Elements of an Instruction, Instruction Representation Instruction types, Number of Addresses, Design Decisions [CISC/RISC], Addressing Modes, Large Register File in RISC. Register and data flow design, data fetch and instruction fetch in indirect instruction cycle. .LO1:Differentiate between various techniques of I/O ; Analyze and compare the design decisions in CISC and RISC, and demonstrate various addressing modes with their applications.       |   6 | 1,2,3,4. | Book 1,3 (Lecture, numerical )   | Assign: practice and assignment questions on addressing modes     |
|   5 | CPU control unit               | CPU control unit, Functions of Control Unit, Micro-Operations, hardwired implementation, Micro Programmed Control unit, basic concepts, advantages-disadvantages of Micro Programmed and Hardwired control unit LO1: Compare the design considerations and trade-offs involved in selecting between micro programmed and hardwired control unit implementations along with the impact of the control unit design on CPU performance.                                                                                                                                                                                              |   5 | 1,2      | Book 1,2 (Lecture )              | Assignment:c ompare and contrast implementatio n techniques of CU |
|   6 | Instruction level parallelism: | Pipeline design, Synchronous & Asynchronous Pipeline conflicts: Resource conflict,Data dependency, and Branch difficulties. Solutions to deal with pipelining: Hardware interlocks, operand forwarding, Delayed load, Pre fetch target instruction, Branch target buffer, Loop buffer, Branch prediction, and Delayed branch. Super scalar design; Super pipelining, and VLIW processors. LO1: Identify the various types of pipeline conflicts and evaluate solutions to mitigate pipeline conflicts. LO2: Analyze advanced techniques like super scalar design, super                                                           |   7 | 1,2,4,5. | Book 2,3 (Lecture, numerical )   | Pipeline hazards and overcome techniques and numericals           |

|    |                      | pipelining, and VLIW processors, to enhance CPU performance and efficiency in modern computing systems.                                                                                                                                                                                                                                                                                                                                                                                                                      |    |      |                     |                                   |
|----|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|------|---------------------|-----------------------------------|
|  7 | Parallel Processing: | Flynn's classification SISD, SIMD, MISD, MIMD. Vector processor, Array Processor, Symmetric multi processing, NUMA, Cache coherence in parallel computing. LO1: Explain Flynn's classification of computer architectures and their implications for parallel computing. Comprehend specialized parallel computing architectures such as vector processors, array processors, SMP, NUMA, and cache coherence mechanisms to ensure consistency among multiple caches accessing the same memory location in parallel computing. |  8 | 1, 2 | Book 1,2 (Lecture ) | Comparing solutions of CC problem |

## * 1- Remember, 2- understand, 3- Apply, 4- Analyze, 5-Evaluate

## Books and Reading

1. William Stallings, Computer Organization and Architecture: Design for performance 10th Ed., Pearson Education.
2. Govindarajalu, Computer Architecture and organization Design Principles and Applications, 2nd Ed., Tata McGraw HILL.
3. M.Morris Mano, Computer system architecture,PHI
4. Rajkamal, Computer Architecture, ISP 2006, Tata McGraw HILL.

## CO-PO Mapping

|      | Program Specific Outcomes   | CO1   | CO2   | CO3   | CO4   |
|------|-----------------------------|-------|-------|-------|-------|
| PSO1 | Conceptual knowledge        |      |       |       |       |
| PSO1 | Practical skills            |       |       |       |       |
| PSO1 | Innovative skills           |       |       |      |       |
| PSO1 | Research skills             |       |       |       |       |
| PSO1 | Reflective thinking         |       |       |       |       |
| PSO2 | Disciplinary knowledge      |      |       |       |       |

|      | Critical thinking               |    |    |    |    |
|------|---------------------------------|----|-----|----|----|
|      | Programming skills              |    |     |    |    |
| PSO3 | Problem solving skills          |    |    |    |    |
| PSO3 | Analytical reasoning skills     |    |     |   |    |
| PSO3 | Research skills                 |    |     |    |   |
| PSO4 | Team work and cooperation       |    |     |    |    |
| PSO4 | Decision making skills          |    |    |   |   |
| PSO4 | Managerial competencies         |    |     |    |    |
| PSO4 | Communication skills            |    |     |    |    |
| PSO4 | Leadership qualities            |    |     |    |    |
| PSO5 | Ethical awareness               |    |     |    |   |
| PSO5 | Moral values                    |    |     |    |    |
| PSO5 | Technological ethical practices |    |    |    |    |
| PSO6 | Modern technologies             |    |     |    |   |
| PSO6 | Life long learning              |    |     |    |    |
| PSO6 | Technological knowledge         |   |    |   |   |

Course Type: - Core

Course Credits - 4 Theory

Course Objective - To teach basic numerical methods required for typical engineering and business applications.

Course Outcomes -After completion of this course, learners will be able to

-  CO1- To make learners aware of basic numerical methods and interpret the results for engineering problems.
-  CO2- To understand numerical approximations to the roots of an equation by basic methods.
-  CO3- Understand basics of finite differences and learn various interpolation methods.
-  CO4- Learner working with numerical integration and differentiation.

## Course Content -

|   Unit No | Name                              | Contents                                                                                                                                                                                                                                                            | Hours   |
|-----------|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
|         1 | Introduction of Numerical Methods | Error, Types of error, Introduction of Transcendental and Algebraic equation, Iterative method derivation and numerical, Bisection method derivation and numerical, False-Position method derivation and numerical, Newton Raphson method derivation and numerical. | 6 Hrs   |
|         2 | Interpolation                     | Finite Differences, Forward, Backward and Central differences, Differences of a polynomial, Newton's formula for interpolation, related numerical and derivation, Gauss's Central differences formula, related numerical and derivation.                            | 6 Hrs   |
|         3 | Interpolation Unevenly            | Interpolation with unevenly spaced points: LaGrange's interpolation derivation and numerical, Inverse interpolation derivation and numerical,                                                                                                                       | 6 Hrs   |

## Subject Name - Numerical Analysis and Design

|    |                                         | Divided differences and theirs properties, Newton's general interpolation formula, Method of successive approximations, Extrapolation.                                                                                                             |       |
|----|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
|  4 | Numerical Differentiation               | Introduction of Numerical Differential, Newton's Differential formula derivation and numerical, Differential equations and related applications.                                                                                                   | 4 Hrs |
|  5 | Numerical Integration                   | Introduction of Numerical Integration, General Quadrature formula of Integration derivation and numerical, Trapezoidal rule, Simpson's 1/3 rule, Simpson's 3/8 rule, Boole's rule and Weddle's rule derivation and numerical.                      | 6 Hrs |
|  6 | Solution of Differential Equations      | Solution of differential equation, Taylor's series method derivation and numerical, Picard's method of successive approximations derivation and numerical, Euler's method derivation and numerical, Runge-Kutta methods, derivation and numerical. | 6 Hrs |
|  7 | Ill-conditioned Equations and solutions | Introduction of Simultaneous Linear Equations, Solution of simultaneous linear equations, Gauss elimination and pivoting derivation and numerical, Gauss - Seidel iterative methods derivation and numerical.                                      | 6 Hrs |

## Books and Reading:

-  S. S. Shastri, Numerical Methods, PHI Publications.
-  Dr. Santosh Kumar, Computer Based Numerical and Statistical Techniques, S. Chand Publications.
-  E. Balagurusamy, Numerical Methods, McGraw Hill Education Publications.
-  Veda Murthi and iyenger, Numerical methods.

|      | Program Specific Outcomes       | CO1   | CO2   | CO3   | CO4   |
|------|---------------------------------|-------|-------|-------|-------|
| PSO1 | Conceptual knowledge            | √     | √     | √     | √     |
|      | Practical skills                |       |       |       |       |
|      | Innovative skills               |       | √     | √     | √     |
|      | Research skills                 | √     | √     | √     | √     |
|      | Reflective thinking             |       |       | √     | √     |
| PSO2 | Disciplinary knowledge          |       |       |       |       |
|      | Critical thinking               |       |       | √     | √     |
|      | Programming skills              |       |       |       |       |
| PSO3 | Problem solving skills          | √     | √     | √     | √     |
|      | Analytical reasoning skills     |       | √     | √     | √     |
|      | Research skills                 | √     | √     | √     | √     |
| PSO4 | Team work and cooperation       | √     | √     | √     | √     |
|      | Decision making skills          |       |       |       |       |
|      | Managerial competencies         |       |       |       |       |
|      | Communication skills            |       |       |       |       |
|      | Leadership qualities            |       |       |       |       |
| PSO5 | Ethical awareness               |       |       |       |       |
|      | Moral values                    |       |       |       |       |
|      | Technological ethical practices |       |       | √     | √     |
| PSO6 | Modern technologies             | √     | √     | √     | √     |
|      | Lifelong learning               |       | √     | √     | √     |
|      | Technological knowledge         | √     | √     | √     | √     |

Course Type: Core

## Subject Name: Database Management System

Course Credits: 4

Course Objectives: To understand concepts of DBMS and build capacity to implement and maintain an efficient database system using emerging trends.

Course Outcomes - After completion of the course, student will;

CO1:Acquire clarity of the fundamental concepts of DBMS and database models for database analysis and design.

CO2: Analyze the real world scenarios and design conceptualand logical database models.

CO3:Execute set of queries using SQL and Relational algebra.

- CO4: Acquire deep knowledge about DBMS to handle and create large database system to manipulate it efficiently

## Course Contents -

|   Unit No | Title                        | Contents                                                                                                                                                                                                                                                                                                                          |   Hr | Targeted Levels of Blooms T. (Q1)   | Content and Pedagogy (Q2)                | (Q3) Online Resources   | (Q4) Assign./ Assessment/Disc ussion                                          |
|-----------|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|-------------------------------------|------------------------------------------|-------------------------|-------------------------------------------------------------------------------|
|         1 | Introduction to DBMS         | Definition and Purpose of DBMS, Views of data,Three Level Architecture of DBMS, Data independence, Data models- Physical Model, Logical Model, Conceptual Model, Hierarchical Data Model, Network Data Model, Relational Data Model, Object Oriented Model and their comparison. LO1:Define DBMS and explain various data models. |    4 | 1 and 2*                            | Book 1 & Book 2 (Lecture)                |                         | Discussion regarding various DBMSs uses and their applications                |
|         2 | Database Languages and Users | Introduction to Database Languages (DDL, DML, DCL and TCL), Transaction Management, Storage Management, Database Administrator, Database Users, Overall System Structure of DBMS. LO1:Classify different database users and describe the types of database languages.                                                             |    4 | 1 and 2                             | Book 2 & Book 3 (Lecture)                |                         | demonstrate the database concepts studied till now                            |
|         3 | Entity-Relationship Model    | Basic Concepts- Entities, Attributes and Relationship, Mapping Constraint, Keys, Design Issues, Entity-Relationship Diagram, Reduction of an E-R Schema into Relational Models. LO1:Analyze and draw ER Diagrams for desired Scenarios to demonstrate the logical representation of database.                                     |    6 | 1, 2, 3 and 4*                      | Book 2 & Book 3 (Lecture &illustration)  |                         | Various exercises for implementing ER concepts                                |
|         4 | Relational Database Design   | Codd's 12 Rules, Pitfalls in Relational-Database Design, Decomposition, Functional Dependencies, Normalization up to 3NF. LO1:Normalize the relational database design and apply the integrity constraints.                                                                                                                       |    4 | 1, 2, 3 and 4                       | Book 2 & Book 3 (Lecture & illustration) |                         | Discussion regarding practical implementation of Codd's Rules & Normalization |

* 1- Remember, 2- Understand, 3- Apply, 4- Analyze, 5- Evaluate, 6- Create

|   5 | Relational Algebra                            | Introduction to relational Algebra, meaning of tuples, attributes, insertion, deletion, updating and retrieval in relational approach, various operations in relational approach like select, project, join, union. LO1:Discuss the significance of Relational Algebra(RA) and write RA queries.                                                                                                                   |   6 | 1, 2,3 and 4*   | Book 1, Book 2 & Book 3 (Lecture and discussion)   | Assignment of RA queries   |
|-----|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----------------|----------------------------------------------------|----------------------------|
|   6 | Structured Query Language                     | Table Fundamentals, data types, creating viewing table, inserting, deleting, updating and modifying data in table, Applying data constraints-adding primary key, foreign key, unique key in table. Basic Structure, Set Operations, , Data Definition Language, Data Control Language, Data Transaction Language LO1:Write and execute SQL queries for designing and manipulating the database.                    |  10 | 1 to 5*         | Book 4                                             | SQL queries exercises      |
|   7 | SQL Integrity Constraint, Joins and Functions | Integrity Constraint: - Entity Integrity, Referential Integrity and Domain Constraint. Oracle functions-string function,, numeric function, Aggregation Functions, Null Values, Nested Sub Queries, Joined Relation LO1:Write and execute complex SQL queries to impose various Integrity Constraints LO2: Write and execute complex SQL queries using Joins/Nested queries to retrieve data from multiple tables. |   6 | 1 to 6*         | Book 4 (Lecture)                                   | SQL practice exercises     |

## Books and Reading

## BOOKS:

1. A Silberschatz, H.F Korth, Sudersan 'Database System Concepts' , MGH Publication.
2. Modern Database Management (Latest Edition) by Fred R. McFadden, Jeffrey A. Hoffer, Mary B. Prescott
3. Elmasri&amp;Navathe 'Fundamentals of Database systems'
4. Ivan Bayross 'SQL, PL/SQL the Programming Language of Oracle'.

## CO-PO Mapping

|      | PROGRAM SPECIFIC OUTCOMES   | CO1   | CO2   | CO3   | CO4   |
|------|-----------------------------|-------|-------|-------|-------|
| PSO1 | Algorithm development       |       |       |       |       |
| PSO1 | Computer Based Solution     |       | √     | √     | √     |
| PSO1 | Application Development     |       | √     | √     | √     |

|      | Disciplinary Knowledge             | √   | √   | √   | √   |
|------|------------------------------------|-----|-----|-----|-----|
| PSO2 | Programming Skill                  |     | √   | √   |     |
| PSO2 | Problem Solving/ Critical thinking |     | √   | √   | √   |
| PSO2 | Mathematical Analysis              |     |     | √   |     |
| PSO3 | Financial Aspects                  |     |     |     |     |
| PSO3 | Modern Tools                       | √   | √   | √   | √   |
| PSO3 | Complex Problems solving           |     | √   | √   | √   |
| PSO3 | Time Frame Analysis                |     |     |     |     |
| PSO4 | Computer Architecture              |     |     |     |     |
| PSO4 | Cooperation/Teamwork               | √   | √   | √   | √   |
| PSO4 | Resource Management                | √   | √   | √   | √   |
| PSO5 | Modern Problem solving Technique   | √   | √   | √   | √   |
| PSO5 | Business Skills                    |     |     |     |     |
| PSO6 | Communication skills               | √   | √   | √   | √   |
| PSO6 | Decision making skills             | √   | √   | √   | √   |
| PSO6 | Managerial Skill                   | √   | √   | √   | √   |
| PSO6 | Environmental constraints          |     |     |     |     |
| PSO6 | Research Skills                    |     |     |     | √   |

Course Type: Core

## Subject Name: System Programming

Course Credits:4

Course Objectives: The course aims to make the students familiar with concepts of systems programming and design of system software.

Course Outcomes - After completion of the course, student will be able to:

-  CO1: Understand basic concepts of system software and system programming.
-  CO2: Learn the design of assemblers, compilers and preprocessors.
-  CO3: Understand the structure and design of assembler, compiler, linker and loader.
-  CO4: Understand the concept and theory behind the implementation of high level languages.

## Course Contents -

|   Unit No | Title                            | Contents                                                                                                                                                                                                                                                                  |   Hr | Targeted Levels of Blooms T. (Q1)   | Content and Pedagogy (Q2)                                           | (Q3) Online Resources   | (Q4) Assign./ Assessment/Discussion                                |
|-----------|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|-------------------------------------|---------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------|
|         1 | Introduction to System Software. | Basic concept of System Software and Application Software.System Programming, Components of Language Processing System, Fundamentals of Language processing systems. LO1: Describe the fundamental concepts of Software and Application Software.                         |    6 | 1 and 2*                            | B.No. 1 and related text from other referred readings. (Lecture)    |                         | Assign: Present a framework of system software and its components. |
|         2 | Assembler                        | Explain Assembler and Elements of Assembly Language programming, a simple Assembly Scheme, Pass Structures of Assemblers, Design of a Two-pass Assembler, and Algorithms for two pass assembler. LO1: Explain Assemble, its elements and type with algorithms.            |    6 | 1, 2 ,3and 4*                       | B.No. 1 and related text from other referred readings. (Lecture)    |                         | Assign: Assembler and different type of assembler with algorithms. |
|         3 | Macro Processors                 | Macros and Macro Processors: Macro definition and call, macro expansions, nested macro calls, Advance Macro facilities, Design of Macro Preprocessor and macro Assembler. LO1: Demonstrate Macro Processors and its call. LO2: Explain different type of Macro facilities |    6 | 1 and 2*                            | B.No. 1 and related text from other referred readings. (Lecture and |                         | Assign: How to call macro and design of macro.                     |

|    |                | and design of macro preprocessor.                                                                                                                                                                                                                                           |    |               | Numerical)                                                                      |                                                                         |
|----|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|---------------|---------------------------------------------------------------------------------|-------------------------------------------------------------------------|
|  4 | Compiler       | Compiler and Translators, cross compilers, phases in complier Design, design of Lexical analyzer. LO1:Describe the cross compilers and its phases. LO2: Explain design of Lexical analyzer.                                                                                 |  6 | 1, 2 ,3and 4* | B.No. 1 and related text from other referred readings. (Lecture and Numerical)  | Assign: Describe compiler and its type.                                 |
|  5 | Loaders        | General loader scheme, Absolute loading, Relocating loading, Dynamic Run Time Loading. LO1: Describe different type of Loaders.                                                                                                                                             |  5 | 1 and 2*      | B.No. 1 and related text from other referred readings. (Lecture and Numerical)  | Assign: explain loader and dynamic run time loading.                    |
|  6 | Linkers        | Linker, Dynamic Linker, Re-locatable and self- relocating programs. LO1: Illustrate Dynamic Linker LO2: Describe Re-locatable and self-relocating programs.                                                                                                                 |  5 | 1 ,2,3 and 4* | B.No. 1 And related text from other referred readings. (Lecture and discussion) | Assign: explain self-relocating program in loader                       |
|  7 | Software Tools | Software tools for program development, Editors, Debugger, Debug Monitors, Programming Environments, User Interfaces, Co-routines and reentrant programs LO1: Explain Editors, Debugger, Debug Monitors LO2: Describe User Interfaces, Co-routines and reentrant programs . |  6 | 1, 2, and 3 * | B.No. 1 And related text from other referred readings. (Lecture )               | Assign: Any two Case studies of software tools for program development. |

## * 1- Remember, 2- understand, 3- Apply, 4- Analyze

## Books and Reading

1. John. J. Donovan, System Programming, Tata McGraw Hill.
2. D. M. Dhamdhere, System Programming and Operating System, 5th edition
3. Aho and Ullman , Principles of Compiler Design, Pearson Education.
4. Leland L. Beck, 'System Software An Introduction to Systems Programming', Pearson Education 3rd Edition.
5. Dougles. V. Hall , 'Microprocessors and Interfacing', Tata McGraw Hill.
6. Assembly Language Techniques for IBM PC, BPB Publication, Alan R. Millar

## CO-PO Mapping

|      | Program Specific Outcomes   | CO1   | CO2   | CO3   | CO4   |
|------|-----------------------------|-------|-------|-------|-------|
| PSO1 | Conceptual knowledge        | ✔     | ✔     |       | ✔     |
| PSO1 | Practical skills            | ✔     | ✔     | ✔     | ✔     |
| PSO1 | Innovative skills           | ✔     | ✔     | ✔     | ✔     |
| PSO1 | Research skills             |       | ✔     | ✔     | ✔     |
| PSO1 | Reflective thinking         | ✔     |       | ✔     | ✔     |
| PSO2 | Disciplinary knowledge      | ✔     | ✔     | ✔     | ✔     |
| PSO2 | Critical thinking           |       | ✔     | ✔     |       |
| PSO2 | Programming skills          |       | ✔     | ✔     |       |
| PSO3 | Problem solving skills      |       | ✔     | ✔     | ✔     |
| PSO3 | Analytical reasoning skills |       | ✔     | ✔     |       |
| PSO3 | Research skills             |       | ✔     | ✔     | ✔     |

| PSO4   | Team work and cooperation       |    |    |    |
|--------|---------------------------------|----|----|----|
| PSO4   | Decision making skills          |    |    | ✔  |
| PSO4   | Managerial competencies         |    |    |    |
| PSO4   | Communication skills            |    |    |    |
| PSO4   | Leadership qualities            |    |    |    |
| PSO5   | Ethical awareness               |    |    |    |
| PSO5   | Moral values                    |    |    |    |
| PSO5   | Technological ethical practices |    |    |    |
| PSO6   | Modern technologies             | ✔  | ✔  |    |
| PSO6   | Life long learning              | ✔  | ✔  |    |
| PSO6   | Technological knowledge         | ✔  | ✔  |    |

Course Type: Core

Course Credits: 4

Course Objectives: To familiarize students with the concepts of Python programming language and to learn various modules of python programming, such as, list, tuple, class, etc.

Course Outcomes - After completion of the course, student will be able to;

- CO1:Able to understand basic concepts, and paradigm of Python Programming
- CO2: Able to interpret various data structures and programming constructs in the Python language.
- CO3: Able to identify the significance and implementation of selection, and iteration for solving business problems.
- CO4: Able to understand the need of object oriented programming concepts, accessing data from files and database, Numpy.

## Course Contents -

|   Unit No | Title                           | Contents                                                                                                                                                                                                                                                                                                                                                                                                      |   Hr | Targeted Levels of Blooms T. (Q1)   | Content and Pedagogy (Q2)                  | (Q3) Online Resources   | (Q4) Assign./ Assessment/Dis cussion   |
|-----------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|-------------------------------------|--------------------------------------------|-------------------------|----------------------------------------|
|         1 | Introduction to Python          | How to install Python, Packages, How to install packages, Python variants, How to use python (Command line mode, Scripting Mode), Print Statement, Variables :Values, Types(Boolean, String, Integer, Float ), Variables , benefits of using variables over values, Keywords: Integers, Floats, Booleans, Logical operators, LO1: Explain the concept of how to install python, various datatypes, operator.. |    4 | 1 and 2*                            | Book 1. (Lecture)                          |                         | Discussion about basics of language.   |
|         2 | Control Structure and functions | Control Statements: IF, indentation, IF-Else Statement, Loops: For, While), Continue, Break and Pass,Functions : Functions:def , body, return, Function calling, Nesting of functions, Global Keyword, Default arguments, Docstring, Lambda functions, LO1: Understood the various control & loop structures with the help of programming exercises.                                                          |    8 | 1, 2 and 3*                         | Book 1 and 2 (Lecture, and Program Design) |                         | Develop Program and scripts            |
|         3 | List, Tuple                     | Lists: Notion of list, accessing elements, Slicing and adding, Multiplying a list by integer, copying a list, Operations and functions over list (len, append, count, insert, sort, remove, pop, in), Map and Filter, ), Tuples, packing and unpacking, Functions with multiple return values LO1: Explain and develop script with the use of list, tuple and functions.                                      |    7 | 1, 2 and 3*                         | Book 1 and 2 (Lecture, and Program Design) |                         | Develop Program and scripts            |
|         4 | Dictionary ,Set,                | Dictionaries: Defining and accessing a dictionary Sets: Set definitions, Set operations, String: Definition, Formatting, Split, Upper and lowercase functions, Join, LO1: Explain and understood the concepts of set, dictionary                                                                                                                                                                              |    6 | 1, 2 and 3*                         | Book 1 and 2 (Lecture, and Program Design) |                         | Develop Program and scripts            |

## Subject Name: Python Programming

|   5 | Module, File I/O                | Modules: Importing a module, Writing user defined modules, overview of common Modules (math, string, random), File input and Output (I/O) :Opening, Reading from and writing to file simple file, reading and writing class object in file LO1: Explain and implement the module and file I/O                                                                    |   6 | 1, 2 and 3*    | Book 1 and 2 (Lecture, and Program Design)   | Develop Program and scripts   |
|-----|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|----------------|----------------------------------------------|-------------------------------|
|   6 | Class and Database Connectivity | Classes: Defining and initializing an object, self parameters, class attributes and class hierarchy, Operator Overloading Database Connectivity: connect python to MySQL database, execute insert, select, update and delete SQL command by python script. LO1: Explain and implement class and database operations by python script                             |   4 | 1, 2 and 3*    | Book 1 and 2 (Lecture, and Program Design)   | Develop Program and scripts   |
|   7 | Numpy and Matplotlib            | Introduction to Numpy: N-dimensional array object, Array broadcasting with scalars, vector operations, Matrix operations, Slicing arrays, Iterating over arrays, Reshaping, Linear Algebra operations Introduction to Matplotlib: Plotting library, Scator plot, Histogram, Boxplot, Imageplot, Wireplot LO1: Explain and understood Numpy and Matplotlib module |   5 | 1, 2, 3 and 4* | Book 1 and 2 (Lecture, and Program Design)   | Develop Program and scripts   |

## * 1- Remember, 2- understand, 3- Apply, 4- Analyze

## Books and Reading

## BOOKS:

1. Learning Python, 5th Edition by Mark Lutz Publisher(s): O'Reilly Media
2. Python Programming, by Anurag Gupta and G P Biswas, Publisher: McGraw Hill
3. [https://nptel.ac.in/courses/106106182](https://nptel.ac.in/courses/106106182)

## CO-PO Mapping

|      | Program Specific Outcomes   | CO1   | CO2   | CO3   | CO4   |
|------|-----------------------------|-------|-------|-------|-------|
| PSO1 | Conceptual knowledge        |      |      |      |      |
|      | Practical skills            |       |      |      |      |
|      | Innovative skills           |       |       |       |      |
|      | Research skills             |       |       |       |       |
|      | Reflective thinking         |       |       |       |       |
| PSO2 | Disciplinary knowledge      |      |      |      |      |
|      | Critical thinking           |       |       |       |      |
|      | Programming skills          |      |      |      |      |
| PSO3 | Problem solving skills      |      |      |      |      |

|      | Analytical reasoning skills     |    |    |    |    |
|------|---------------------------------|----|----|----|-----|
|      | Research skills                 |    |    |    |     |
| PSO4 | Team work and cooperation       |    |    |    |    |
|      | Decision making skills          |    |    |    |    |
|      | Managerial competencies         |    |    |    |     |
|      | Communication skills            |    |    |    |     |
|      | Leadership qualities            |    |    |    |     |
| PSO5 | Ethical awareness               |    |    |    |     |
|      | Moral values                    |    |    |    |     |
|      | Technological ethical practices |    |   |   |    |
| PSO6 | Modern technologies             |    |   |   |    |
|      | Life long learning              |    |    |    |     |
|      | Technological knowledge         |   |   |   |    |