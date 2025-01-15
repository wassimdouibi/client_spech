# -*- coding: utf-8 -*-
{
    'name': "Client SpecH",

    'summary': """Gestion Clients Grossiste""",

    'description': """
        Gestion client grossiste module pour :
            - Gerer client et commandes 
            - Gerer assurances            
    """,

    'author': "G1_Equipe4",
    'website': "http://www.G1_Equipe4.com",

    # Categories can be used to filter modules in modules listing
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        # Pour trouver le sale_management il faut activer le mode développeur puis aller vers Apps et copier le id du module
        'sale_management'
    ],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        # Templates cpour le qweb view pour les rapports
        'templates.xml',
        'views/clientspec.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}