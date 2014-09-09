ZODB-talk
=========

An introduction to persistency in python, ZODB (Zope Object DataBase) and ZEO (Zope Enterprize Objects)

Code Examples
----

* 01_pickle_write.py
* 02_pickle_read.py -- reading and writing pickle objects

* 03_zodb_write.py -- sample writing into ZODB
* 04_zodb_transaction.py -- comming transactions and reverting history
* 05_zodb_persistent.py -- Inheriting from persistent class
* 06_zodb_container.py -- more examples of persistency, using persistent containers aka Folderish types

* 07_zope_catalog.py -- using repose.catalog for indexing ZODB

* 08_zeo.py -- an example of accessing ZODB through ZEO service.
* zeo_command.sh -- bash command to start zeo
* runzeo.py -- zeo startup service script from zopefoundation/ZEO repo

* common.py -- comon ZODB instantiation functions used as shorthand in 04_zodb_write.py .. 07_zope_catalog.py


References
----


### Pickle Module

* https://docs.python.org/2/library/pickle.html

### ZODB

* http://zodb.readthedocs.org/en/latest/
* http://stackoverflow.com/questions/5704589/zodb-not-able-to-commit

### ZODB Indexing

* https://pypi.python.org/pypi/zc.catalog
* http://docs.repoze.org/catalog/
* http://mainlydata.kubadev.com/python/repoze-catalog-and-zodb-beginners-example-part-1/

### ZEO

* http://zodborg.readthedocs.org/en/latest/documentation/guide/zeo.html
* http://pyinsci.blogspot.ca/2007/09/zodb-vs-relational-database-simple.html

