# chatgpt-environment-setup

1. ``npm -v`` to see if npm is installed
   1. if not, install here: [Download npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
2. ``conda --version`` to see if conda is installed. Install conda if not already installed
   1. Don't worry about the prerequisites. It's not necessary. [Link](https://docs.anaconda.com/anaconda/install/linux/)
3. run the following commands in a separate folder. The modules do not need to be in the project repo. When prompted, just press enter. The default options are fine.
    ```
    npm init playwright@latest
    playwright install firefox
    ```
4. run the following commands:
    ```
    conda env create -n chatgpt -f environment.yml
    conda activate chatgpt
    sudo apt install moreutils
    pip install git+https://github.com/mmabrouk/chatgpt-wrapper
    chatgpt install
    ```
5. login
6. try to run test.py ``python3 test.py``

