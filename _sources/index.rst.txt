.. aeon_docs documentation master file, created by
   sphinx-quickstart on Mon Apr 25 22:02:55 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Project Aeon's online docs!
======================================

.. include:: ../readme.md
   :parser: myst_parser.sphinx_
   :start-after: ## Project Aeon Organization Overview
   :end-before: ### [aeon_mecha]

.. grid:: 1 2 2 2
   :gutter: 3
   
   .. grid-item-card:: :fas:`database;sd-text-primary` aeon_mecha
      :link: https://github.com/SainsburyWellcomeCentre/aeon_mecha
      :link-type: url

      Project Aeon's main library for interfacing with acquired data

   .. grid-item-card:: :fas:`flask;sd-text-primary` aeon_experiments
      :link: https://github.com/SainsburyWellcomeCentre/aeon_experiments
      :link-type: url

      Aeon experiment workflows written in the Bonsai visual programming language
      
   .. grid-item-card:: :fas:`book;sd-text-primary` aeon_acquisition
      :link: https://github.com/SainsburyWellcomeCentre/aeon_acquisition
      :link-type: url
      
      Source code for the 'aeon_acquisition' Bonsai package used in Aeon experiment workflows
   
   .. grid-item-card:: :fas:`chart-simple;sd-text-primary` aeon_analysis
      :link: https://github.com/SainsburyWellcomeCentre/aeon_analysis
      :link-type: url

      Python modules for analysis of Aeon experiment data

   .. grid-item-card:: :fas:`gear;sd-text-primary` aeon_lineardrive
      :link: https://github.com/SainsburyWellcomeCentre/aeon_lineardrive
      :link-type: url

      Source code for actuating a linear drive motor used in Aeon experiments

   .. grid-item-card:: :fas:`cookie-bite;sd-text-primary` aeon_feeder
      :link: https://github.com/SainsburyWellcomeCentre/aeon_feeder
      :link-type: url

      Source code for pellet delivery via feeders used in Aeon experiments

.. note::
   .. include:: ../readme.md
      :parser: myst_parser.sphinx_
      :start-after: *Note*: 
      :end-before: ### [aeon_experiments]

.. include:: ../readme.md
   :parser: myst_parser.sphinx_
   :start-after: /code_of_conduct.md).

.. toctree::
   :maxdepth: 2
   :hidden:

   Home <self>
   data_contract
   design_considerations
   Developer API <api>
   dev_practices/dev_practices
