The ducks problem is given as: \
In a circle, randomly place 4 ducks, what is the probability that the 4 ducks end up in a semicircle? \
(The picture is a screenshot of the original problem) 

![photo_2022-10-15_20-13-02](https://user-images.githubusercontent.com/82872879/195979761-de372033-690c-4780-8d77-a75848d53822.jpg)

I provide here my Monte Carlo code as well as an analytical solution, assuming a certain way of randomly placing the ducks that is: 
1. Choose an angle from a reference line, the angle (radian) is uniformly distributed on $[0, 2\pi]$
2. Choose a length, it turns out that length does not matter in this setting

![Ducks P1](https://user-images.githubusercontent.com/82872879/195979739-a9f1ab25-fc29-46d5-9cb5-5131291ecf4b.png)
![Ducks P2](https://user-images.githubusercontent.com/82872879/195979867-b44126b4-1cf0-4eb9-8309-48a5625c947f.png)
![Ducks P3](https://user-images.githubusercontent.com/82872879/195979868-ac33c161-6152-46fd-90ba-ddafb12e3093.png)
