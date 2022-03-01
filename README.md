# Scraping Promart Prices

This is a crawler for Promart cables prices made in Python.
Version Python:
- _Python 3.9.x_

Libraries:
- beautifulsoup4==4.10.0
- certifi==2021.10.8
- charset-normalizer==2.0.12
- idna==3.3
- requests==2.27.1
- soupsieve==2.3.1
- urllib3==1.26.8

Installation:

1. Create a virtual enviroment:
   - <code>python3 -m venv venv</code>
2. Activate the virtual enviroment:

   if you are using Linux:
   - <code>source venv/bin/activate</code>
   if you are using Windows(CMD):
   - <code>venv\Scripts\activate.bat</code>
   if you are using Windows(PowerShell):
   - <code>venv\Scripts\activate.ps1</code>
   if you are using MacOS:
   - <code>source venv/bin/activate</code>
3. Install the dependencies:

   ~~~
   requirements.txt:
      beautifulsoup4==4.10.0
      certifi==2021.10.8
      charset-normalizer==2.0.12
      idna==3.3
      requests==2.27.1
      soupsieve==2.3.1
      urllib3==1.26.8 
   ~~~
   - <code>pip install -r requirements.txt</code>
4. Run the program:
   - <code>python3 main.py</code>