# Configuration dictionary for all tutorials
TUTORIAL_CONFIG = {
    # Data Science tutorials
    'data_science': {
        'custclust': {
            'template': 'data_science/custclust.html',
            'markdown': 'customer_clustering.md'
        },
        'decisiontreetut': {
            'template': 'data_science/custclust.html'
        },
        'knearest': {
            'template': 'data_science/k_nearest.html',
            'markdown': 'k_nearest.md'
        }
    },
    
    # Google Sheets tutorials
    'gsheets': {
        'gs_home': {
            'template': 'gsheets/gs_home.html'
        },
        'index_match_sumifs': {
            'template': 'gsheets/gs_index_match_sumifs.html',
            'markdown': 'index_match_sumif.md'
        },
        'test': {
            'template': 'gsheets/GS_test.html',
            'markdown': 'content.md'
        },
        'xlookup_vs': {
            'template': 'gsheets/gs_xlookup_vs.html',
            'markdown': 'xlookup.md'
        }
    },
    
    # Web Development tutorials
    'web_dev': {
        'sticky_nav': {
            'template': 'web_dev/stickyNav.html',
            'markdown': 'fixed_navbar.md'
        },
        'flask_markdown': {
            'template': 'web_dev/flaskMarkdown.html',
            'markdown': 'markdownFlaskFile.md'
        }
    },

    # R tutorials
    'r_tutorials': {
        'r_basics': {
            'template': 'Learn_R/r_basics.html'
        }
    },

    # Portfolio Website tutorials
    'portfolio_website': {
        'pw_setup': {
            'template': 'portfolio_website/pw_setup.html'
        },
        'python_setup': {
            'template': 'portfolio_website/pw_python_setup.html'
        },
        'flask_code': {
            'template': 'portfolio_website/pw_flask_code.html'
        },
        'css_code': {
            'template': 'portfolio_website/pw_css_code.html'
        },
        'run_locally': {
            'template': 'portfolio_website/pw_run_locally.html'
        },
        'hosting': {
            'template': 'portfolio_website/pw_hosting.html'
        }
    },

    # Old Projects
    'old_projects': {
        'covidanalysis': {
            'template': 'old_projects/covidtableaupublic.html'
        },
        'bankingchurn': {
            'template': 'old_projects/bankingchurn.html'
        },
        'shiny_dashboard': {
            'template': 'old_projects/shiny_dash.html'
        },
        'walmartanalysis': {
            'template': 'old_projects/walmart_analysis.html'
        }
    },

    # Regression Prediction
    'regression_prediction': {
        'regpredweb': {
            'template': 'home.html'
        }
    }
}