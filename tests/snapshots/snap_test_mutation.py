# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['test_create_question 1'] = {
    'data': {
        'createQuestion': {
            'question': {
                'downvotes': [
                ],
                'id': 'UXVlc3Rpb25Ob2RlOjM=',
                'owner': {
                    'id': 'VXNlck5vZGU6MQ=='
                },
                'score': '0',
                'text': 'creating a question',
                'upvotes': [
                ]
            }
        }
    }
}

snapshots['test_create_answer 1'] = {
    'data': {
        'createAnswer': {
            'answer': {
                'downvotes': [
                ],
                'id': 'QW5zd2VyTm9kZToz',
                'owner': {
                    'id': 'VXNlck5vZGU6MQ=='
                },
                'score': '0',
                'text': 'creating an answer',
                'upvotes': [
                ]
            }
        }
    }
}

snapshots['test_create_comment_for_answer 1'] = {
    'data': {
        'createComment': {
            'comment': {
                'downvotes': [
                ],
                'id': 'Q29tbWVudE5vZGU6Ng==',
                'owner': {
                    'id': 'VXNlck5vZGU6MQ=='
                },
                'score': '0',
                'text': 'creating a comment',
                'upvotes': [
                ]
            }
        }
    }
}

snapshots['test_create_comment_for_question 1'] = {
    'data': {
        'createComment': {
            'comment': {
                'downvotes': [
                ],
                'id': 'Q29tbWVudE5vZGU6Ng==',
                'owner': {
                    'id': 'VXNlck5vZGU6MQ=='
                },
                'score': '0',
                'text': 'creating a comment',
                'upvotes': [
                ]
            }
        }
    }
}

snapshots['test_voting[{}Question-question-allQuestions-downvote] 1'] = {
    'data': {
        'downvoteQuestion': {
            'question': {
                'downvotes': [
                    {
                        'id': 'VXNlck5vZGU6MQ=='
                    }
                ],
                'id': 'UXVlc3Rpb25Ob2RlOjE=',
                'owner': {
                    'id': 'VXNlck5vZGU6MQ=='
                },
                'score': '2',
                'text': 'my first question',
                'upvotes': [
                    {
                        'id': 'VXNlck5vZGU6MQ=='
                    },
                    {
                        'id': 'VXNlck5vZGU6Mg=='
                    },
                    {
                        'id': 'VXNlck5vZGU6Mw=='
                    }
                ]
            }
        }
    }
}

snapshots['test_voting[{}Question-question-allQuestions-upvote] 1'] = {
    'data': {
        'upvoteQuestion': {
            'question': {
                'downvotes': [
                ],
                'id': 'UXVlc3Rpb25Ob2RlOjE=',
                'owner': {
                    'id': 'VXNlck5vZGU6MQ=='
                },
                'score': '3',
                'text': 'my first question',
                'upvotes': [
                    {
                        'id': 'VXNlck5vZGU6MQ=='
                    },
                    {
                        'id': 'VXNlck5vZGU6Mg=='
                    },
                    {
                        'id': 'VXNlck5vZGU6Mw=='
                    }
                ]
            }
        }
    }
}

snapshots['test_voting[{}Answer-answer-allAnswers-downvote] 1'] = {
    'data': {
        'downvoteAnswer': {
            'answer': {
                'downvotes': [
                    {
                        'id': 'VXNlck5vZGU6MQ=='
                    },
                    {
                        'id': 'VXNlck5vZGU6Mw=='
                    }
                ],
                'id': 'QW5zd2VyTm9kZTox',
                'owner': {
                    'id': 'VXNlck5vZGU6Mg=='
                },
                'score': '0',
                'text': 'my first answer',
                'upvotes': [
                    {
                        'id': 'VXNlck5vZGU6MQ=='
                    },
                    {
                        'id': 'VXNlck5vZGU6Mg=='
                    }
                ]
            }
        }
    }
}

snapshots['test_voting[{}Answer-answer-allAnswers-upvote] 1'] = {
    'data': {
        'upvoteAnswer': {
            'answer': {
                'downvotes': [
                    {
                        'id': 'VXNlck5vZGU6Mw=='
                    }
                ],
                'id': 'QW5zd2VyTm9kZTox',
                'owner': {
                    'id': 'VXNlck5vZGU6Mg=='
                },
                'score': '1',
                'text': 'my first answer',
                'upvotes': [
                    {
                        'id': 'VXNlck5vZGU6MQ=='
                    },
                    {
                        'id': 'VXNlck5vZGU6Mg=='
                    }
                ]
            }
        }
    }
}

snapshots['test_voting[{}Comment-comment-allComments-downvote] 1'] = {
    'data': {
        'downvoteComment': {
            'comment': {
                'downvotes': [
                    {
                        'id': 'VXNlck5vZGU6MQ=='
                    }
                ],
                'id': 'Q29tbWVudE5vZGU6Mg==',
                'owner': {
                    'id': 'VXNlck5vZGU6Mw=='
                },
                'score': '-1',
                'text': 'this is a great question',
                'upvotes': [
                ]
            }
        }
    }
}

snapshots['test_voting[{}Comment-comment-allComments-upvote] 1'] = {
    'data': {
        'upvoteComment': {
            'comment': {
                'downvotes': [
                ],
                'id': 'Q29tbWVudE5vZGU6Mg==',
                'owner': {
                    'id': 'VXNlck5vZGU6Mw=='
                },
                'score': '1',
                'text': 'this is a great question',
                'upvotes': [
                    {
                        'id': 'VXNlck5vZGU6MQ=='
                    }
                ]
            }
        }
    }
}

snapshots['test_edit[True-editQuestion-question-allQuestions] 1'] = {
    'data': {
        'editQuestion': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 3
                }
            ],
            'message': 'User=2 cannot edit Question=1 owned by user=1.'
        }
    ]
}

snapshots['test_edit[True-editAnswer-answer-allAnswers] 1'] = {
    'data': {
        'editAnswer': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 3
                }
            ],
            'message': 'User=1 cannot edit Answer=1 owned by user=2.'
        }
    ]
}

snapshots['test_edit[True-editComment-comment-allComments] 1'] = {
    'data': {
        'editComment': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 3
                }
            ],
            'message': 'User=1 cannot edit Comment=2 owned by user=3.'
        }
    ]
}

snapshots['test_edit[False-editQuestion-question-allQuestions] 1'] = {
    'data': {
        'editQuestion': {
            'question': {
                'downvotes': [
                ],
                'id': 'UXVlc3Rpb25Ob2RlOjE=',
                'owner': {
                    'id': 'VXNlck5vZGU6MQ=='
                },
                'score': '3',
                'text': 'made an edit',
                'upvotes': [
                    {
                        'id': 'VXNlck5vZGU6MQ=='
                    },
                    {
                        'id': 'VXNlck5vZGU6Mg=='
                    },
                    {
                        'id': 'VXNlck5vZGU6Mw=='
                    }
                ]
            }
        }
    }
}

snapshots['test_edit[False-editAnswer-answer-allAnswers] 1'] = {
    'data': {
        'editAnswer': {
            'answer': {
                'downvotes': [
                    {
                        'id': 'VXNlck5vZGU6Mw=='
                    }
                ],
                'id': 'QW5zd2VyTm9kZTox',
                'owner': {
                    'id': 'VXNlck5vZGU6Mg=='
                },
                'score': '1',
                'text': 'made an edit',
                'upvotes': [
                    {
                        'id': 'VXNlck5vZGU6MQ=='
                    },
                    {
                        'id': 'VXNlck5vZGU6Mg=='
                    }
                ]
            }
        }
    }
}

snapshots['test_edit[False-editComment-comment-allComments] 1'] = {
    'data': {
        'editComment': {
            'comment': {
                'downvotes': [
                ],
                'id': 'Q29tbWVudE5vZGU6Mg==',
                'owner': {
                    'id': 'VXNlck5vZGU6Mw=='
                },
                'score': '0',
                'text': 'made an edit',
                'upvotes': [
                ]
            }
        }
    }
}
