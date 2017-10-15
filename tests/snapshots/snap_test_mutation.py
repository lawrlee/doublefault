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
                'id': '3',
                'owner': {
                    'id': '1'
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
                'id': '3',
                'owner': {
                    'id': '1'
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
                'id': '6',
                'owner': {
                    'id': '1'
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
                'id': '6',
                'owner': {
                    'id': '1'
                },
                'score': '0',
                'text': 'creating a comment',
                'upvotes': [
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
                'id': '1',
                'owner': {
                    'id': '1'
                },
                'score': '3',
                'text': 'made an edit',
                'upvotes': [
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
    }
}

snapshots['test_edit[False-editAnswer-answer-allAnswers] 1'] = {
    'data': {
        'editAnswer': {
            'answer': {
                'downvotes': [
                    {
                        'id': '3'
                    }
                ],
                'id': '1',
                'owner': {
                    'id': '2'
                },
                'score': '1',
                'text': 'made an edit',
                'upvotes': [
                    {
                        'id': '1'
                    },
                    {
                        'id': '2'
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
                'id': '2',
                'owner': {
                    'id': '3'
                },
                'score': '0',
                'text': 'made an edit',
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
                ],
                'id': '1',
                'owner': {
                    'id': '1'
                },
                'score': '2',
                'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eu gravida libero. Pellentesque convallis tortor a orci rhoncus placerat. Phasellus varius, justo quis interdum suscipit, ante massa egestas ex, non elementum leo sem quis mi. Nulla pellentesque, neque a cursus placerat, turpis tortor elementum orci, non eleifend diam odio sed erat. Etiam dignissim pretium ante, eu feugiat turpis convallis id. Integer dictum ex tellus, a ullamcorper arcu elementum in. Proin fermentum nisi et mi feugiat hendrerit. Ut a arcu scelerisque, fringilla nibh vel, lobortis dolor. Quisque dictum luctus sapien non efficitur. Maecenas nunc ex, vestibulum non euismod eu, pellentesque vitae sem. Proin elementum magna felis, vel rutrum orci tincidunt a. Cras enim augue, consequat sed leo in, bibendum rhoncus magna.',
                'upvotes': [
                    {
                        'id': '2'
                    },
                    {
                        'id': '3'
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
                'id': '1',
                'owner': {
                    'id': '1'
                },
                'score': '3',
                'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eu gravida libero. Pellentesque convallis tortor a orci rhoncus placerat. Phasellus varius, justo quis interdum suscipit, ante massa egestas ex, non elementum leo sem quis mi. Nulla pellentesque, neque a cursus placerat, turpis tortor elementum orci, non eleifend diam odio sed erat. Etiam dignissim pretium ante, eu feugiat turpis convallis id. Integer dictum ex tellus, a ullamcorper arcu elementum in. Proin fermentum nisi et mi feugiat hendrerit. Ut a arcu scelerisque, fringilla nibh vel, lobortis dolor. Quisque dictum luctus sapien non efficitur. Maecenas nunc ex, vestibulum non euismod eu, pellentesque vitae sem. Proin elementum magna felis, vel rutrum orci tincidunt a. Cras enim augue, consequat sed leo in, bibendum rhoncus magna.',
                'upvotes': [
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
    }
}

snapshots['test_voting[{}Answer-answer-allAnswers-downvote] 1'] = {
    'data': {
        'downvoteAnswer': {
            'answer': {
                'downvotes': [
                    {
                        'id': '3'
                    }
                ],
                'id': '1',
                'owner': {
                    'id': '2'
                },
                'score': '0',
                'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque a neque sed purus tristique aliquet ac nec magna. Curabitur quis lorem elit. Donec non tellus nec purus eleifend laoreet. In nulla ante, gravida et mattis feugiat, finibus nec turpis. Etiam molestie est a orci condimentum maximus. Nunc porttitor, metus at.',
                'upvotes': [
                    {
                        'id': '2'
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
                        'id': '3'
                    }
                ],
                'id': '1',
                'owner': {
                    'id': '2'
                },
                'score': '1',
                'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque a neque sed purus tristique aliquet ac nec magna. Curabitur quis lorem elit. Donec non tellus nec purus eleifend laoreet. In nulla ante, gravida et mattis feugiat, finibus nec turpis. Etiam molestie est a orci condimentum maximus. Nunc porttitor, metus at.',
                'upvotes': [
                    {
                        'id': '1'
                    },
                    {
                        'id': '2'
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
                        'id': '1'
                    }
                ],
                'id': '2',
                'owner': {
                    'id': '3'
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
                'id': '2',
                'owner': {
                    'id': '3'
                },
                'score': '1',
                'text': 'this is a great question',
                'upvotes': [
                    {
                        'id': '1'
                    }
                ]
            }
        }
    }
}
