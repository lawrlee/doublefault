# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_get_all[allQuestions] 1'] = {
    'data': {
        'allQuestions': [
            {
                'id': '1'
            },
            {
                'id': '2'
            }
        ]
    }
}

snapshots['test_get_all[allAnswers] 1'] = {
    'data': {
        'allAnswers': [
            {
                'id': '1'
            },
            {
                'id': '2'
            }
        ]
    }
}

snapshots['test_get_all[allComments] 1'] = {
    'data': {
        'allComments': [
            {
                'id': '2'
            },
            {
                'id': '3'
            },
            {
                'id': '4'
            },
            {
                'id': '5'
            }
        ]
    }
}

snapshots['test_get_all[allTags] 1'] = {
    'data': {
        'allTags': [
            {
                'id': '1'
            },
            {
                'id': '2'
            }
        ]
    }
}

snapshots['test_get_all[allUsers] 1'] = {
    'data': {
        'allUsers': [
            {
                'id': '1'
            },
            {
                'id': '2'
            },
            {
                'id': '3'
            }
        ]
    }
}

snapshots['test_get_single[allQuestions-question] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 16,
                    'line': 3
                }
            ],
            'message': '''Argument "id" has invalid value "1".
Expected type "Int", found "1".'''
        }
    ]
}

snapshots['test_get_single[allAnswers-answer] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 14,
                    'line': 3
                }
            ],
            'message': '''Argument "id" has invalid value "1".
Expected type "Int", found "1".'''
        }
    ]
}

snapshots['test_get_single[allComments-comment] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 15,
                    'line': 3
                }
            ],
            'message': '''Argument "id" has invalid value "2".
Expected type "Int", found "2".'''
        }
    ]
}

snapshots['test_get_single[allTags-tag] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 11,
                    'line': 3
                }
            ],
            'message': '''Argument "id" has invalid value "1".
Expected type "Int", found "1".'''
        },
        {
            'locations': [
                {
                    'column': 5,
                    'line': 5
                }
            ],
            'message': 'Cannot query field "text" on type "TagType".'
        }
    ]
}

snapshots['test_get_single[allUsers-user] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 3
                }
            ],
            'message': 'Cannot query field "user" on type "Query". Did you mean "answer"?'
        }
    ]
}
