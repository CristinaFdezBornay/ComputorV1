# WELCOME TO COMPUTOR V1


### SUMMARY
Computor V1 is a 42 project which aim is to develop a program able to solve equations (up to 2nd degree).

#### Displayed information
The information that will be displayed is:
* The equation in its reduced form.
* The degree of the equation.
* The discriminant and solution(s).

*Exceptions:*
* INPUT ERROR
* Unsolvable equations

#### Input format
The input should be formated as follows:
`a * X^0 + b * X^1 + c * X^2 + ... + Σ[ z * X^n ]ᵢ = Σ[ z * X^n ]ᵢ`

Being `a, b, c, ..., z` the coeficient and `0, 1, 2, ..., n` the exponent of each term.


### HOW TO
#### Basic usage
Using the program directly from the command line:

```bash
cd api
python3 -m venv venv
venv/bin/pip3 install -r requirements.txt
source venv/bin/activate
python api.py "[EQUATION]"
```

#### Advanced usage
To solve more than just one equation at a time:

1.  Include all the equations that you would like to solve in a file
    
    Ex. `api/equations_file.example.txt`

2.  Run the following command:
    ```bash
    cd api
    python3 -m venv venv
    venv/bin/pip3 install -r requirements.txt
    source venv/bin/activate
    ./run_api.sh equations_file.example.txt > output.example.txt
    open output.example.txt
    ```

#### ✨✨✨ Premium Usage ✨✨✨
A Web GUI has been implemented:

1.  Open a terminal and run `yarn star-api`
2.  In a new terminal window run `yarn start-front`
3.  Go to your browser `https://localhost:3000`


### INPUT FORMAT
Since the mandatory format is pretty annoying some improvements have been implemented.

Taking as a reference: `Σ[ z * X^n ]ᵢ`

1.  It is not required to introduce the terms by incrementing exponent order.
    
    Ex: `2 * X^0 + 4 * X^2 = 0` equals `4 * X^2 + 2 * X^0 = 0`

2.  If no `[ * X^n ]` is present, the coeficient will be admitted as `[ coef * X^0 ]`.
    
    Ex: `2 + 4 * X^2 = 0` equals `2 * X^0 + 4 * X^2 = 0`

3.  If no `[ ^n ]` is present, the coeficient will be admitted as `[ coef * X^1 ]`.
    
    Ex: `5 * X + 4 * X^2 = 0` equals `5 * X^1 + 4 * X^2 = 0`

4.  The caracter `*` is not mandatory.
    
    Ex: `5 X + 4 X^2 = 0` equals `5 * X^1 + 4 * X^2 = 0`

5.  The caracter `^` is not mandatory.
    
    Ex: `4 X2 = 0` equals `4 * X^2 = 0`

6.  Both `x` and `X` are admitted.
    
    Ex: `5 x + 4 x2 = 0` equals `5 * X^1 + 4 * X^2 = 0`

7.  Spaces are not required.
    
    Ex: `5x +4x2 = 0` equals `5 * X^1 + 4 * X^2 = 0`

8.  If the entire part of a float is 0 it can be formated as `[ .decimal_part ]`
    
    Ex: `.3x2 = 0` equals `0.3 * X^2 = 0`

9.  If the no character `=` appears the equation will be considered as equal to 0.
    
    Ex: `5x +4x2` equals `5 * X^1 + 4 * X^2 = 0`


### TESTING
Inside of the folder `api/test` there are many test that can be executed using the script:
```bash
cd api
python3 -m venv venv
venv/bin/pip3 install -r requirements.txt
source venv/bin/activate
./run_api.sh test/choose_the_file_you_want_to_test.txt > output_test.txt
open output.example.txt
```
