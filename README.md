pyglassdoor
=========

Python API for Glassdoor.com

## Install

From source:
   
    $ clone https://github.com/ghanemar/pyglassdoor
    $ cd pyglassdoor
    $ sudo pip install .

From pip:

    $ sudo pip install pyglassdoor

## Use

    >>> import pyglassdoor
    >>> api = pyglassdoor.Api(partner_id= 'glassdoor parter id',
                             partner_ke= 'glassdoor partner key')

    >>> company = api.get_company('ibm')
   