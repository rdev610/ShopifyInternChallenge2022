# Shopify Backend Summer Internship Challenge 2022
## ABOUT 
This is a web application that tracks the inventory for a logistics company.

To use the application the user must sign-up/login first. 

Once logged in the user can add, delete, read, and  update the products in the application. The user can also press a button that will export the product data into a CSV file.  

## To run the app locally
1). Download and install [Visual Studio Code](https://code.visualstudio.com/) if you do not already have Visual Studio Code. 

2). Install the Python extension on Visual Studio Code. You can either go to the [link or](https://marketplace.visualstudio.com/items?itemName=ms-python.python) directly add in VS code by clikcing on extnesions in the toolbar and searhcing for Python

3). Install a version of [Python 3](https://www.python.org/downloads/) specific to your computer's operating system. 

4). Dowload this repository by clicking on code and then download ZIP. Once the folder is downlaoded, unzip the file.  

5). Open the folder in Visual Studio Code by clicking on File (on the top left), and then click on open folder and select the folder

6). Open a new terminal by clicking on Terminal (top left) and then on New Terminal.  

7). Open up command prompt and the cnage the dreictory until you are in the correct folder. 

8). Create a [virtual envrionment](https://docs.python.org/3/library/venv.html) by running the following command prompts. 

### Windows

py -3 -m venv .venv

.venv\scripts\activate

### macOS

python3 -m venv .venv

source .venv/bin/activate

### Linux

sudo apt-get install python3-venv # If needed

python3 -m venv .venv

source .venv/bin/activate


9). Update pip in the virtual environment by running the following command prompt: 
python -m pip install --upgrade pip

10). Install all the required packages for the application by running the following command prompt:
pip install -r requirements.txt

11). Go back to Visual Studio Code and open up the main.py file

12). click on the run button (looks like the play button)

13). In the Visual Code terminal a link will be shown. Click on the link to open up the web application and start exploring!

<img width="269" alt="Screenshot 2022-01-19 183412" src="https://user-images.githubusercontent.com/97998450/150235289-2eead31c-3c4b-4d25-a62e-554a0ee2988f.png">


