# Python

- **Python For Beginners**
  - [Think Python](https://greenteapress.com/wp/think-python-2e/)
  - [The hitchhiker's guide to Python](https://docs.python-guide.org/intro/learning/)
  - [A byte of Python](https://python.swaroopch.com/)

- **Python Advanced Level**
  - [Problem-solving with algorithms ](https://runestone.academy/runestone/books/published/pythonds/index.html)

- **Python Package to Learn Math**
  - Numeric and Mathematical Modules - [Documentation](https://docs.python.org/3/library/numeric.html)
  - SymPy - [About](https://www.sympy.org/en/index.html) | [Tutorial](https://docs.sympy.org/latest/tutorial/intro.html#what-is-symbolic-computation) | [Documentation](https://docs.sympy.org/latest/index.html)
  - Sage - [About](https://www.sagemath.org/) | [Tutorial](https://doc.sagemath.org/pdf/en/thematic_tutorials/thematic_tutorials.pdf) | [Documentation](https://doc.sagemath.org/html/en/tutorial/introduction.html#installation)
    - [Sage web interface](https://sagecell.sagemath.org/)
    - [CoCalc interface](https://cocalc.com/?utm_source=sagemath.org&utm_medium=icon)

- **Making Pandas more efficient** [(here)](https://towardsdatascience.com/4-tricks-for-making-python-pandas-more-efficient-20237a045f09)
  - Utilize parameters provided in **read_csv** function. Like-
    - **parse_dates** converting dates to datetime data type 
    - **usecols** for columns subseting while reading a file
  - Use **normalization=True** in **value_counts** function for true representation of values
  - Use **bin** parameter for converting continuous variable to categorical and then check for the distribution. E.g. **df.Price.value_counts(normalize=True, bins=5)**
  - Use **query** function for filtering a dataframe, it's simple and similar to where clause in SQL
