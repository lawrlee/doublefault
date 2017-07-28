import pytest

FULL_QUERY = '''
{
  allQuestions {
    edges {
      node {
        id
        text
        created
        modified
        score
        views
        tags {
          id
        }
        owner {
          id
          username
        }
        upvotes {
          id
        }
        downvotes {
          id
        }
        acceptedAnswer {
          id
        }
        comments {
          id
          text
          owner {
            id
            username
          }
        }
        answers {
          edges {
            node {
              id
              text
              accepted {
                id
              }
              created
              modified
              owner {
                id
                username
              }
              comments {
                id
                text
                owner {
                  id
                  username
                }
              }
            }
          }
        }
      }
    }
  }
  __debug {
    sql {
      rawSql
    }
  }
}
'''


def _get_all_query(query):
    return '''
{{
  {query} {{
    edges {{
      node {{
        id
      }}
    }}
  }} 
}}
'''.format(query=query)


def _get_single_query(query, relay_id):
    return '''
{{ 
  {query}(id: "{relay_id}") {{
    id
    text
  }}
}}
    '''.format(query=query,
               relay_id=relay_id)


LIST_QUERIES = ['allQuestions',
                'allAnswers',
                'allComments',
                'allTags',
                'allUsers']

SINGLE_QUERIES = ['question',
                  'answer',
                  'comment',
                  'tag',
                  'user']

@pytest.mark.django_db(transaction=False)
@pytest.mark.parametrize('query', LIST_QUERIES)
def test_get_all(client, snapshot, query):
    result = client.execute(_get_all_query(query))
    snapshot.assert_match(result)


@pytest.mark.django_db(transaction=False)
@pytest.mark.parametrize('list_query,single_query', zip(LIST_QUERIES, SINGLE_QUERIES))
def test_get_single(client, snapshot, list_query, single_query):
    all_objects = client.execute(_get_all_query(list_query))
    relay_id = all_objects['data'][list_query]['edges'][0]['node']['id']
    result = client.execute(_get_single_query(single_query, relay_id))
    snapshot.assert_match(result)
