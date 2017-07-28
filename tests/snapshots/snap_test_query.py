# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['test_get_all[allQuestions] 1'] = {
    'data': {
        'allQuestions': {
            'edges': [
                {
                    'node': {
                        'id': 'UXVlc3Rpb25Ob2RlOjE='
                    }
                },
                {
                    'node': {
                        'id': 'UXVlc3Rpb25Ob2RlOjI='
                    }
                }
            ]
        }
    }
}

snapshots['test_get_all[allAnswers] 1'] = {
    'data': {
        'allAnswers': {
            'edges': [
                {
                    'node': {
                        'id': 'QW5zd2VyTm9kZTox'
                    }
                },
                {
                    'node': {
                        'id': 'QW5zd2VyTm9kZToy'
                    }
                }
            ]
        }
    }
}

snapshots['test_get_all[allComments] 1'] = {
    'data': {
        'allComments': {
            'edges': [
                {
                    'node': {
                        'id': 'Q29tbWVudE5vZGU6Mg=='
                    }
                },
                {
                    'node': {
                        'id': 'Q29tbWVudE5vZGU6Mw=='
                    }
                },
                {
                    'node': {
                        'id': 'Q29tbWVudE5vZGU6NA=='
                    }
                },
                {
                    'node': {
                        'id': 'Q29tbWVudE5vZGU6NQ=='
                    }
                }
            ]
        }
    }
}

snapshots['test_get_all[allTags] 1'] = {
    'data': {
        'allTags': {
            'edges': [
                {
                    'node': {
                        'id': 'VGFnTm9kZTox'
                    }
                },
                {
                    'node': {
                        'id': 'VGFnTm9kZToy'
                    }
                }
            ]
        }
    }
}

snapshots['test_get_all[allUsers] 1'] = {
    'data': {
        'allUsers': {
            'edges': [
                {
                    'node': {
                        'id': 'VXNlck5vZGU6MQ=='
                    }
                },
                {
                    'node': {
                        'id': 'VXNlck5vZGU6Mg=='
                    }
                },
                {
                    'node': {
                        'id': 'VXNlck5vZGU6Mw=='
                    }
                }
            ]
        }
    }
}

snapshots['test_get_single[allQuestions-question] 1'] = {
    'data': {
        'question': {
            'id': 'UXVlc3Rpb25Ob2RlOjE=',
            'text': 'my first question'
        }
    }
}

snapshots['test_get_single[allAnswers-answer] 1'] = {
    'data': {
        'answer': {
            'id': 'QW5zd2VyTm9kZTox',
            'text': 'my first answer'
        }
    }
}

snapshots['test_get_single[allComments-comment] 1'] = {
    'data': {
        'comment': {
            'id': 'Q29tbWVudE5vZGU6Mg==',
            'text': 'this is a great question'
        }
    }
}

snapshots['test_get_single[allTags-tag] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 5,
                    'line': 5
                }
            ],
            'message': 'Cannot query field "text" on type "TagNode".'
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
