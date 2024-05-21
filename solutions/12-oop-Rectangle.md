# Instructions  

  **create and work with a simple object**

  ## Rectangle
  1. Write the code for a Rectangle class in rectangles.py
      * attributes: width and height
      * methods (behaviour):
        * `area()` returns area
        * `perimiter()` returns perimiter
        * __str__ returns  the dimensions in an f string
        * `change()` two parameters, amount to add to width, amount to add to height (Note: could be -ve, validate to ensure it does not make width or height 0)<br>
        NOTE: area & perimiter methods do NOT need any parameters besides self, since a Rectangle object already knows its own dimensions
  3. In main.py `main()` function use the Rectangle class  (you will need an import statement.)
     * Instantiate 3 rectangles:  Consider that you have to mow the lawn of a 100 x 100 lot, where the house is 40 x 30, the dog house is 2x4 and the driveway is 5 x 8.
     * Use instances of the Rectangle object to calculate the area that you have to mow.
     * Then display the area you have to mow in a format string
  3. optional: create a Square class that inherits from  Rectangle, think of any changes you might need ex: __init__  needs only 1 side ; __str__ with text it's a square