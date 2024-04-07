.. image:: https://github.com/matthiaskoenig/spt-app/raw/main/docs/images/spt-app.png
   :align: left
   :alt: spt-app logo

spt-app: web application of SPT model
=====================================
This project provides the visualization of the simulation results at https://sptmodel.streamlit.app.

Simulation of zonation-function relationships in the liver using coupled multiscale models: Application to drug-induced liver injury
Steffen Gerhäusser, Lena Lambers, Luis Mandl, Julian Franquinet, Tim Ricken, Matthias König
bioRxiv 2024.03.26.586870; doi: https://doi.org/10.1101/2024.03.26.586870

Installation
============
To run the example applications install the requirements::

    cd spt-app
    mkvirtualenv spt_app --python=python3.11
    (protein_app) pip install -r requirements.txt

Run app
=======
To run the app use::

    streamlit run main/spt_app.py

License
=======

* Source Code: `LGPLv3 <http://opensource.org/licenses/LGPL-3.0>`__
* Documentation: `CC BY-SA 4.0 <http://creativecommons.org/licenses/by-sa/4.0/>`__

The spt-app source is released under both the GPL and LGPL licenses version 2 or
later. You may choose which license you choose to use the software under.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License or the GNU Lesser General Public
License as published by the Free Software Foundation, either version 2 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

Funding
=======
Matthias König is supported by the Federal Ministry of Education and Research (BMBF, Germany)
within the research network Systems Medicine of the Liver (**LiSyM**, grant number 031L0054)
and by the German Research Foundation (DFG) within the Research Unit Programme FOR 5151
"`QuaLiPerF <https://qualiperf.de>`__ (Quantifying Liver Perfusion-Function Relationship in Complex Resection -
A Systems Medicine Approach)" by grant number 436883643 and by grant number
465194077 (Priority Programme SPP 2311, Subproject SimLivA).

© 2024 Matthias König
