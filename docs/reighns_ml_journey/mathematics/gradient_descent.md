$$
\newcommand{\F}{\mathbb{F}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\u}{\mathbf{u}}
\newcommand{\v}{\mathbf{v}}
\newcommand{\x}{\mathbf{x}}
$$

## Gradient Descent

In mathematics, **gradient descent** (also often called steepest descent) is a **first-order iterative optimization algorithm** for finding a local minimum of a differentiable function. The idea is to take repeated steps in the opposite direction of the gradient (or approximate gradient) of the function at the current point, because this is the direction of steepest descent. Conversely, stepping in the direction of the gradient will lead to a local maximum of that function; the procedure is then known as gradient ascent.[^gradient_descent_intro] 

This blog answers two questions:

1. How does the gradient descent algorithm work?
2. Why does the gradient points in the direction of the steepest ascent? 

In many articles and courses, gradient descent is often used to find the minimum of a function, by way of the following procedure:
${\color{red} \textbf{To rewrite this pseudocode}}$

    1. Start at the initial point.
    2. Take a step in the opposite direction of the gradient.
    3. Repeat steps 2 and 3 until the function is no longer decreasing.
    4. The point where the function is no longer decreasing is the minimum.

Our second question is equivalent to answering the point 2, on why do we take a step in the opposite direction of the gradient.

### The Intuition

Quote wikipedia's example.

### The idea of neighbourhood

Let us start with an one-dimensional example to illustrate the idea of neighbourhood.

Define $f: \R \to \R$ to be $f(x) = x^2$, then the gradient of $f$ at a point $x = x_0$ is $\frac {\partial f(x)} {\partial x} \vert x_0 = 2x_0$.

A wrong interpretation is to treat the understanding of gradient as if it is a linear function. 

Let us fix a point $x = 2$, its output $f(x) = 4$ and the gradient at that point is $\frac {\partial f(x)} {\partial x} \vert_{x=2} = 4$.
It is wrong to say that for every $1$ unit increase of $x$, $f(x)$ will increase by $4$, where $4$ is the gradient at that point.
One can indeed verify that if $x$ is increased by $1$ unit from $x=2$ to $x = 3$, then $f(x) = 3^2 = 9$, where $f(x)$ is increased by $5$ units, and not by $4$.

Unlike the case of a linear function, the gradient of $f$ at a point $x = x_0$ is not fixed, but depends on the value of $x_0$. 
Consequently, the meaning of the gradient in such a function is only well defined in a small $\epsilon$-neighbourhood[^epsilon] around $x = 2$.
Within this small neighbourhood, we can "loosely" visualize the portion of the function to be a "linear function" with a slope of $2$, as illustrated in the following figure.
The enclosed green box is the neighborhood of $x = 2$, where if we zoom in, the portion of the function inside looks like a linear function with a slope of $2$.

<figure markdown>
  ![Image title](./../../assets/mathematics/gradient_descent/neighbourhood
.jpg){ width="300" }
  <figcaption>Neighbourhood around x = 2.</figcaption>
</figure>


Indeed, if we set $\epsilon = 0.001$, then if $x = 2$, we have $f(x) = 4$; moving $x$ by $\epsilon$ from $x = 2$ to $x = 2.001$ 
yields us $f(x) \approxeq 4.004$. We now see that $x$ increasing by $0.001$ unit indeed yields us an increase of $4.004 - 4 = 0.004$, 
a factor of $4$ increase to the output $f(x)$.

---

### Gradient Vector

!!! abstract "Definition: Gradient Vector"
    Let $f: \R^n \to \R$ be a function that maps $\x$ to $f(\x)$:

    $$
    \begin{align*}
    f \colon \R^n &\longrightarrow \R \\
    \x &\longmapsto f(\x) \\
    \end{align*}
    $$
    
    where $\x = [x_1, x_2, \ldots, x_n]^\top$ is a vector of $n$ variables. 
    
    Then the ***gradient*** of $f$ is the **vector** of first-order partial derivatives of $f$ with respect to each of the $n$ variables.

    $$
    \begin{equation}
    \nabla f(\x) = \bigg[\frac{\partial f(\x)}{\partial x_1}, \frac{\partial f(\x)}{\partial x_2}, \ldots, \frac{\partial f(\x)}{\partial x_n} \bigg]^\top
    \label{eq:grad_vec}
    \end{equation}
    $$

    We can also replace the notation $\frac{\partial f(\x)}{\partial x_i}$ in equation $\eqref{eq:grad_vec}$ with $f_{x_i}$.

---

### Directional Derivatives

!!! abstract "Definition: Directional Derivative"
    Let $f: \R^n \to \R$ be a function that maps $\x$ to $f(\x)$:

    $$
    \begin{align*}
    f \colon \R^n &\longrightarrow \R \\
    \x &\longmapsto f(\x) \\
    \end{align*}
    $$
    
    where $\x = [x_1, x_2, \ldots, x_n]^\top$ is a vector of $n$ variables. 
    
    Then the ***directional derivative*** of $f$ **at a point** $\x$ along a **direction vector**

    $$
    \v = [v_1, v_2, \ldots, v_n]^\top
    $$

    is the function $D_{\v}(f)$ defined by the limit:

    $$
    \begin{equation}
    D_{\v}(f) = \lim_{h \to 0} \frac{f(\x + h\v) - f(\x)}{h}
    \label{eq:directional_derivative_def}
    \end{equation}
    $$

To avoid notation confusion and also understand the definition better, we use a simple example in 2-dimensional to illustrate the definition of the directional derivative.

!!! example "Example: Directional Derivative"
    Let $f: \R^2 \to \R$ be defined as 

    $$
    f(\x) = f(x_1, x_2) = x_1^2 + x_2^2
    $$

    where $\x$ is a vector of scalar values $x_1$ and $x_2$, both corresponds to the x- and y-coordinates of a point in the plane respectively.
  
    Following closely the definition, we need to define a **direction vector** $\v$.
    Since the definition did not say what $\v$ was, we can define $\v$ to be the unit vector in the south-east direction.

    $$
    \v = \begin{bmatrix} 1 \\ -1 \end{bmatrix}
    $$

    We also note that we want to compute the **directional derivative** of $f$ at a point $(x_1, x_2)$, where we arbitrarily choose $(x_1, x_2) = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$.

    Then, we can define the directional derivative of $f$ at the point $\x = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$ along $\v = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$ as:

    $$
    \begin{equation*}
    \begin{split}
    D_{\v}(f(1, 1)) &= \lim_{h \to 0} \frac{f(\x + h\v) - f(\x)}{h} \\
              &= \lim_{h \to 0} \frac{f(x_1 + hv_1, x_2 + hv_2) - f(x_1, x_2)}{h} \\
              &= \lim_{h \to 0} \frac{f(1 + h, 1 - h) - f(1, 1)}{h} 
    \end{split}
    \end{equation*}
    $$

    which evaluates to how much $f$ changes when it moves a small unit distance $h$ from $\x$ to $\x + h$ along the direction $\v$.

---

#### Intuition of Directional Derivative

This section builds up to an important derivation of the idea of the directional derivative.

!!! warning
    In this section, we should constantly recall the idea of a [neighbourhood](gradient_descent.md#the-idea-of-neighbourhood) whenever we talk about per unit change, we should visualize that this unit is very small.

Let us restrict our focus to 2-variable mutlivariate function $f(x, y)$, bearing in mind that it can be scaled up to $n$ variables.
The components of $\nabla f$ are the partial derivatives of $f$ with respect to $x$ and $y$.

More concretely, given the partial derivative 

$$
\begin{equation}
\frac{\partial f(x, y)}{\partial x} 
\label{eq:partial_x}
\end{equation}
$$

equation $\eqref{eq:partial_x}$ answers the question: 
how much does the value of $f$ change when we hold $y$ constant and nudge $x$ by a small amount in the $x$ direction (i.e. in the direction pointed to by the vector $\begin{bmatrix} 1 & 0 \end{bmatrix}^\top$)?[^partial_x_intuition]

In a similar vein, given the partial derivative

$$
\begin{equation}
\frac{\partial f(x, y)}{\partial y}
\label{eq:partial_y}
\end{equation}
$$

equation $\eqref{eq:partial_y}$ answers the question:
how much does the value of $f$ change when we hold $x$ constant and nudge $y$ by a small amount in the $y$ direction (i.e. in the direction pointed to by the vector $\begin{bmatrix} 0 & 1 \end{bmatrix}^\top$)?[^partial_y_intuition]

Finally, it is often useful to note that $x$ and $y$ can move in tandem (i.e. we do not hold any of them constant), how do we then calculate how much $f$ changes when we nudge both $x$ and $y$ by a small amount. 
Note that moving $x$ and $y$ both by $a$ and $b$ respectively is synonymous with moving the point $(x, y)$ by the vector $\begin{bmatrix} a & b \end{bmatrix}^\top$. With vector in the playing field, we now attach the notion of a "direction".

We can use equation $\eqref{eq:directional_derivative_def}$ to compute how much $f$ changes when we nudge the points $x$ and $y$ by a small amount in the $x$ and $y$ directions respectively.
However, the calculation is cumbersome if we use the definition of the directional derivative. 
We will now use an example to derive an *alternate* formula by relating directional derivative to their partial derivatives composition. 

!!! example "Example"
    If we want to move $x$ and $y$ by $1$ and $-1$ respectively, then it simply means that $x$ is moved 1 unit along the $x$ axis
    and $y$ is moved -1 unit along the $y$ axis. 
    
    In vector terms, this means we moved $(x, y)$ in the direction $\begin{bmatrix} 1 & -1 \end{bmatrix}^\top$.

    More generically, let $x$ and $y$ move $a$ and $b$ units respectively, then we moved $(x, y)$ in the direction $\begin{bmatrix} a & b \end{bmatrix}^\top$.
    It turns out that the amount that $f$ changes when we move in the $\v = \begin{bmatrix} a & b \end{bmatrix}^\top$ direction is exactly how much 
    $f$ changes when we move $a$ units along the $x$ axis and $b$ units along the $y$ axis[^partial_xy_intuition]. 
    
    Recall that we **know** how much $f$ changes when we move $x$ by 1 unit: 

      - The partial derivative of $f$ with respect to $x$: $\frac{\partial f(x, y)}{\partial x}$

    Recall that we **know** how much $f$ changes when we move $y$ by 1 unit:

      - The partial derivative of $f$ with respect to $y$: $\frac{\partial f(x, y)}{\partial y}$

    It follows that if we move $x$ by $a$ units, then $f$ changes by
      
      - $a \cdot \frac{\partial f(x, y)}{\partial x}$

    and if we move $y$ by $b$ units, then $f$ changes by

      - $b \cdot \frac{\partial f(x, y)}{\partial y}$

    Therefore, the amount that $f$ changes when we move $x$ by $a$ units and $y$ by $b$ units is
      
      - $a \cdot \frac{\partial f(x, y)}{\partial x} + b \cdot \frac{\partial f(x, y)}{\partial y}$

    One might notice that for multivariate $f:\R^n \to \R$, the derivative $D_{\v}(f)$ at the point $x \in \R^n$ is defined to be a linear map $T: \R^n \to \R$.
    Therefore, the linearity rule applies.

    If the above is still not obvious, then we can approach it geometrically. 
    Recall that we are mapping from $\R^2$ to $\R$, the below diagram illustrates the mapping.

    <figure markdown>
    ![Image title](./../../assets/mathematics/gradient_descent/geometric_r2_r1
    .jpg){ width="300" }
    <figcaption>Geometric Intuition.</figcaption>
    </figure>

---

#### Theorem (The Direction Derivative)

The intuition [developed in the previous section](gradient_descent.md#intuition-of-directional-derivative) allows us to 
derive a new formula to calculate the directional derivative of $f$ at a point $\x$ when moved in the direction of $\v$.

Although the example used is in 2-dimensions, we can generalize to $n$ variables and we state it formally.

!!! abstract "Theorem: Directional Derivative"
    Let $f: \R^n \to \R$ be a function $f(\x)$ where $\x = [x_1, x_2, \ldots, x_n]^\top$ is a vector of $n$ variables. 
    
    If $f$ is **differentiable** at $\x$, then the directional derivative $D_{\v}(f)$ at $\x$ is defined as follows:

    $$
    \begin{equation}
    D_{\v}(f(\x)) = \nabla f(\x) \cdot \v
    \label{eq:directional_derivative_theorem}
    \end{equation}
    $$

    In most textbooks, we will **normalize** the direction vector $\v$ to the standard unit vector $\u$.
    However, the usage of unit vector simplifies the derivation and other applications[^unit_vector_1][^unit_vector_2] , it is not an universal rule.


!!! info "Important"
    It is extremely important to remember that the **gradient vector** of $f$ at $\x$ is already defined as $\nabla f(\x)$, to be the vector of partial derivatives of $f$ at $\x$.
    
    This has two consequences:
    
    1. Given the gradient vector of $f$ at $\x$ and any direction $\v$, we can recover the directional derivative $D_{\v}(f)$ at $\x$ by simply multiplying it by $\v$.
    2. Given the gradient vector of $f$ at $\x$ and a scalar value directional derivative $D_{\v}(f)$, we can recover the direction $\v$ by division.

One variant of the proof:


!!! info
    The 

---

#### Difference between Gradient and Directional Derivative[^gradient_directional_derivative_difference]

When I was learning multivariate calculus, I have had my fair share of trouble with the difference between the gradient and the directional derivative.
It is easy to confuse the two terms.

Let us go back to the definitions:

- The **gradient** of a mutlivariate function $f$ at a point $\x$ is the ***vector*** of partial derivatives of $f$ at $\x$, as defined in equation $\eqref{eq:grad_vec}$.
  
$$
\nabla f(\x) = \bigg[\frac{\partial f(\x)}{\partial x_1}, \frac{\partial f(\x)}{\partial x_2}, \ldots, \frac{\partial f(\x)}{\partial x_n} \bigg]^\top
$$

- The **directional derivative** of a mutlivariate function $f$ at a point $\x$ is the ***scalar*** value of the partial derivative of $f$ at $\x$ in the direction of $\v$,
  as defined in equation $\eqref{eq:directional_derivative_def}$ and $\eqref{eq:directional_derivative_theorem}$.

There are infinite directional derivatives around a point $\x$ since there are infinitely many directions $\v$. 
However, there is only one gradient vector around a point $\x$ and this is defined to be the vector that is the steepest ascent, which we will prove in the next section.

Consider the following example:

- We have a point $(x, y)$ in $f$, where $f$ is a function of two variables. 
  Since this function can be graphed in 3-dimensions, we can visualize that there are ***infinite*** number of directions around the point $(x, y)$.

- We can categorize the directions around the point as vectors $\v$. For simplicity, we restrict $\v$ to be unit vectors.

- Recall the definition of the directional derivative of $f$ at a point $\x$ to be a **scalar-valued** function $D_{\v}(f)$ parametrized by the direction vector $\v$.
    - We also note that $D_{\v}(f)$ is the instantaneous rate of change of $f$ when we move in the direction $\v$.
  
- There exists **infinite** number of such directional derivatives of $f$ at a point $\x$ since there are infinite number of directions $\v$. This can be seen by the orange arrows.

- However, there exists an **unique** direction $\v$ which gives rise to the fastest instantaneous rate of change of $f$ when moved in that direction.
   
- This unique direction points in the same direction as the gradient vector $\v$.


<figure markdown>
  ![Image title](./../../assets/mathematics/gradient_descent/infinite_directions
.jpg){ height="100" width="500"  }
  <figcaption>Infinite directions around a point in cross-sectional plane of 3d-figure.</figcaption>
</figure>


---


### Gradient Points to the Direction of Steepest Ascent

We finally have the necessary definitions and theorems to prove the following statement:

> The **direction** of steepest ascent of a function $f: \R^n \to \R$ is given by the **gradient vector** of $f$
  at a point $\x = \begin{bmatrix} x_1 & x_2 & \ldots & x_n \end{bmatrix}^\top$.
  In other words, $f$ increases the fastest when we move in the direction of the **gradient vector**.

Before we prove this, it is best for us to rephrase the question to:

> Given a function $f$ and a point $\x$, which direction vector $\v$ gives the fastest rate of change of $f$ when moved in that direction?

This can be then be found easily by following the theorem/definition in the [section on the alternative definition of the directional derivative](gradient_descent.md#theorem-the-direction-derivative).

The definition $\eqref{eq:directional_derivative_theorem}$ states that $D_{\v}(f(\x)) = \nabla f(\x) \cdot \v$.
We then seek to solve the optimization problem:

$$
\begin{align}
\v_{\max} &= \underset{\v, \lVert \v \rVert = 1}{\operatorname{argmax}}D_{\v}(f(\x)) \label{eq:steepest_ascent_1} \\ 
          &= \underset{\v, \lVert \v \rVert = 1}{\operatorname{argmax}}\nabla f(\x) \cdot \v \label{eq:steepest_ascent_2} \\
          &= \underset{\v, \lVert \v \rVert = 1}{\operatorname{argmax}} \lVert \nabla f(\x) \rVert \cdot \lVert \v \rVert \cos(\theta) \label{eq:steepest_ascent_3} \\
\end{align}
$$

where we want to find the **unique** $\v_{\max}$ such that $D_{\v}(f(\x))$ is the **maximum**.

In equation $\eqref{eq:steepest_ascent_3}$, we invoked the [geometric definition of the dot product](https://en.wikipedia.org/wiki/Dot_product#Geometric_definition) 
to represent the dot product as the **cosine of the angle between the two vectors**.

Since we are optimizing over $\v$ and the length of $\v$ is 1, we can simplify the expression to:

$$
\begin{align}
\v_{\max} &= \underset{\v, \lVert \v \rVert = 1}{\operatorname{argmax}} \lVert \nabla f(\x) \rVert \cdot \lVert \v \rVert \cos(\theta)  \\
          &= \underset{\v}{\operatorname{argmax}} \lVert \nabla f(\x) \rVert \cos(\theta) \label{eq:steepest_ascent_4} \\
\end{align}
$$


!!! success
    We finally convinced ourselves that subtracting the gradient vector indeed (local) minimizes the objective/loss function provided it's differentiable.

---

### References

Bibliography.

- https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/partial-derivative-and-gradient-articles/a/the-gradient

---

[^gradient_descent_intro]: **"Gradient Descent," Wikipedia (Wikimedia Foundation, June 28, 2022), https://en.wikipedia.org/wiki/Gradient_descent.**
[^epsilon]: $\epsilon$ is often denoted $h$ in the limit definition of derivatives.
[^partial_x_intuition]: [Proof That the Gradient Points in the Direction of Steepest Ascent](https://sootlasten.github.io/2017/gradient-steepest-ascent/): Sten Sootla's Blog, Sten Sootla, March 15, 2017.
[^partial_y_intuition]: [Proof That the Gradient Points in the Direction of Steepest Ascent](https://sootlasten.github.io/2017/gradient-steepest-ascent/): Sten Sootla's Blog, Sten Sootla, March 15, 2017. 
[^partial_xy_intuition]: [Proof That the Gradient Points in the Direction of Steepest Ascent](https://sootlasten.github.io/2017/gradient-steepest-ascent/): Sten Sootla's Blog, Sten Sootla, March 15, 2017. 
[^unit_vector_1]: [Why in a directional derivative it has to be a unit vector](https://math.stackexchange.com/questions/1486767/why-in-a-directional-derivative-it-has-to-be-a-unit-vector#:~:text=If%20you%20don't%20use,the%20magnitude%20of%20the%20vector.&text=That%20is%20a%20way%20to,to%20use%20a%20unit%20vector)
[^unit_vector_2]: [why normalize and the definition of directional derivative](https://math.stackexchange.com/questions/809376/why-normalize-and-the-definition-of-directional-derivative)
[^gradient_directional_derivative_difference]: [What is the difference between the gradient and the directional derivative?](https://math.stackexchange.com/questions/661195/what-is-the-difference-between-the-gradient-and-the-directional-derivative)