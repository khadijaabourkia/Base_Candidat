# -*- coding: utf-8 -*-

{
    'name': 'Base Candidat',
    'version': '1.0',
    'category': 'Human Resources',
    'sequence': 6,
    'summary': 'Candidat, Recruitment',
    'description': """
Gérer les candidats 
======================================

Ce module vous permet d'avoir une base de candidats.
    """
    'author': 'Khadija Abourkia',
    'website': '',
    'depends': [
        'decimal_precision',
        'hr',
		'hr_recruitment',
        'survey',
        'calendar',
        'fetchmail',
        'web_kanban_gauge',
    ],
    'data': [
        'hr_base_candidat_view.xml',
        'hr_recruitment_menu.xml',
        'views/hr_recruitment.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}


