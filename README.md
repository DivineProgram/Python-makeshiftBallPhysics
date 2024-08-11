# Python-makeshiftBallPhysics
While messing with Python UIs using Turtle for the first time, I made a program that replicates simple physics on a ball; here's the result.

### All the files included work independently.
Each program is meant to replicate physics in a different way.
Most of the programs include the ball being able to bounce off the sides of you window, meaning adjusting the size of the window will give the ball more or less room to move about.

# Below is stated all the files' indicators and what they mean!

***Classic*** - Your standard ball physics

***Controllable*** - The ball's momentum is contrallable by the user, using keyboard inputs

***Customisable*** - Ball physics where you get to adjust the variables that the program uses to calculate the physics

***No walls*** - Standard ball physics except when it reaches the left or right side of the window, it teleports to the opposite side

***Seed-based*** - Standard ball physics where the initial trajectory, momentum and position can be set by using a specific seed

***Orbital*** - Rather than the ball falling downwards, it gravitates towards a single point on screen (indicated by a blue dot)
  
***Global*** - Orbital physics where the ball experiences the same gravitational force, no matter where they are on screen
	
***Proximity*** - Orbital physics where the ball experiences a higher gravitational force, the closer they are to the point of gravitational attraction
	
***Global Double Ball Gravity*** - Orbital physics where there is no single point of attraction, but there are two balls which gravitate towards each other (without collision), with the same gravitational force no matter how far away they are from each other
	
***Double Orbits*** - Orbital physics where there's one ball and two points of attraction, where the ball can be attracted towards both
