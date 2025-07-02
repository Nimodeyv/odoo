# nimodeyv

# Pour lancer odoo

conda activate odoo
python odoo-bin -r odoo -w odoo --addons-path addons,odoo/custom_addons -d PostgreSQL_17

Pour créer un module perso:

- Créer un répertoire par exemple custom_addons et l'ajouter dans le fichier de config ou dans le lancement de Odoo
  (cf. ci dessus custom_addons dans la ligne de commande)
- Créer un répertoire spécifique dans custom_addons qui contiendra le module spécifique (ici TriBois)
- créer **init**.py et **manifest**.py dans ce répertoire, ici TriBois
- créer les répertoires model, static, views et security dans le répertoire, ici TriBois
- insérer **init**.py dans chaque sous-répertoire et créer models.py, déclarer la nouvelle classe inhéritant de la classe model.model
- créer une vue spécifique dans le répertoire views

Pour visualiser dans odoo les nouveaux modules

- Dans le rectangle à gauche "damier", cliquer sur "Activate the developper moode"
- Cliquer sur la petite roue crantée dans le bandeau violet et cliquer sur "Devenez un superutilisateur"
- Le module Tribois devrait désormais apparaitre dans le rectangle à gauche "damier"

# Odoo

[![Build Status](https://runbot.odoo.com/runbot/badge/flat/1/master.svg)](https://runbot.odoo.com/runbot)
[![Tech Doc](https://img.shields.io/badge/master-docs-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/documentation/master)
[![Help](https://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/forum/help-1)
[![Nightly Builds](https://img.shields.io/badge/master-nightly-875A7B.svg?style=flat&colorA=8F8F8F)](https://nightly.odoo.com/)

Odoo is a suite of web based open source business apps.

The main Odoo Apps include an [Open Source CRM](https://www.odoo.com/page/crm),
[Website Builder](https://www.odoo.com/app/website),
[eCommerce](https://www.odoo.com/app/ecommerce),
[Warehouse Management](https://www.odoo.com/app/inventory),
[Project Management](https://www.odoo.com/app/project),
[Billing &amp; Accounting](https://www.odoo.com/app/accounting),
[Point of Sale](https://www.odoo.com/app/point-of-sale-shop),
[Human Resources](https://www.odoo.com/app/employees),
[Marketing](https://www.odoo.com/app/social-marketing),
[Manufacturing](https://www.odoo.com/app/manufacturing),
[...](https://www.odoo.com/)

Odoo Apps can be used as stand-alone applications, but they also integrate seamlessly so you get
a full-featured [Open Source ERP](https://www.odoo.com) when you install several Apps.

## Getting started with Odoo

For a standard installation please follow the [Setup instructions](https://www.odoo.com/documentation/master/administration/install/install.html)
from the documentation.

To learn the software, we recommend the [Odoo eLearning](https://www.odoo.com/slides),
or [Scale-up, the business game](https://www.odoo.com/page/scale-up-business-game).
Developers can start with [the developer tutorials](https://www.odoo.com/documentation/master/developer/howtos.html).

## Security

If you believe you have found a security issue, check our [Responsible Disclosure page](https://www.odoo.com/security-report)
for details and get in touch with us via email.
